#%% load necessary libraries

import json
import os
import numpy as np
from io import BytesIO
from urllib.parse import quote
from base64 import b64encode
# graphics packages
import matplotlib.pyplot as plt
import matplotlib.patches as ptc

# load cherrypy
import cherrypy


class VTSassessment(object):

    @cherrypy.expose
    def index(self):
        return open('index.html')

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET','POST'])
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def release(self):
        raw = cherrypy.request.json
        # initialize whether the ball has been thrown
        thrown = False
        # establish release distance threshold (yards)
        dt = 1.25
        # initialize dropback depth
        dd = 0
        # initialize left and right
        maxl,maxr = 0,0
        # loop through ball-tracking data
        for i,j in enumerate(raw['balltrackingdata']):
            if thrown == False:
                # calculate distance between HMD and ball
                dx = (j['simulated_ball']['x']-raw['qbtrackingdata'][i]['hmd_location']['x'])/91.44
                dy = (j['simulated_ball']['y']-raw['qbtrackingdata'][i]['hmd_location']['y'])/91.44
                dz = (j['simulated_ball']['z']-raw['qbtrackingdata'][i]['hmd_location']['z'])/91.44
                dist = (dx**2.0 + dy**2.0)**0.5
                # check dropback depth
                if raw['playsituation']['los'] - raw['qbtrackingdata'][i]['hmd_location']['y']/91.44 > dd:
                    dd = raw['playsituation']['los'] - raw['qbtrackingdata'][i]['hmd_location']['y']/91.44
                # Determine drop type
                if raw['qbtrackingdata'][i]['hmd_location']['x'] > maxl:
                    maxl = raw['qbtrackingdata'][i]['hmd_location']['x']/91.44
                elif -raw['qbtrackingdata'][i]['hmd_location']['x'] > maxr:
                    maxr = -raw['qbtrackingdata'][i]['hmd_location']['x']/91.44
                # if the ball is "far enough" away from the headset in the X-Y plane, it has been released
                if dist > dt:
                    # release frame
                    rf = i
                    # time to throw
                    ttt = raw['qbtrackingdata'][i]['sim_time']-raw['qbtrackingdata'][0]['sim_time']
                    rh = j['simulated_ball']['z']/91.44*36.0     # convert to inches
                    # calculate total distance
                    tdis = (dx**2.0 + dy**2.0 + dz**2.0)**0.5
                    ra = np.arcsin(dz/tdis) * (180.0/np.pi)
                    thrown = True
            else:
                if i == rf+10 or i == len(raw['balltrackingdata'])-1:
                    # calculate distance traveled
                    dx = (j['simulated_ball']['x'] - raw['balltrackingdata'][rf]['simulated_ball']['x'])/91.44
                    dy = (j['simulated_ball']['y'] - raw['balltrackingdata'][rf]['simulated_ball']['y'])/91.44
                    dz = (j['simulated_ball']['z'] - raw['balltrackingdata'][rf]['simulated_ball']['z'])/91.44
                    # calculate time elapsed
                    dt = j['sim_time'] - raw['balltrackingdata'][rf]['sim_time']
                    # calculate speed
                    vel = ((dx**2.0+dy**2.0+dz**2.0)**0.5)/dt
                    # convert to miles per hour
                    vel = vel * (3600.0/1760.0)
                    break
        # determine dropback type
        if maxl < -3.5:
            dtype = 'Rollout Left'
        elif maxr > 3.5:
            dtype = 'Rollout Right'
        else:
            dtype = 'Straight'
        # initialize sack statistics
        issack = False
        sy = 0
        # if the ball was not thrown, it was a sack
        if thrown == False:
            rf = None
            vel = None
            ttt = raw['qbtrackingdata'][len(raw['qbtrackingdata'])-1]['sim_time']-raw['qbtrackingdata'][0]['sim_time']
            rh = None
            ra = None
            # sack statistics
            issack = True
            sy = round(raw['qbtrackingdata'][len(raw['qbtrackingdata'])-1]['hmd_location']['y']/91.44-raw['playsituation']['los'])
        # save in a json (dictionary) format
        metrics = {}
        metrics['Velocity'] = vel
        metrics['Time to Throw'] = ttt
        metrics['Release Height'] = rh
        metrics['Release Angle'] = ra
        metrics['Dropback Depth'] = dd
        metrics['Dropback Type'] = dtype
        metrics['Sack'] = issack
        metrics['Sack Yardage'] = sy
        # return value
        return metrics

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET','POST'])
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def receivercalcs(self):
        raw = cherrypy.request.json
        # establish release distance threshold (yards)
        dt = 1.25
        # initialize release frame
        rf = None
        # loop through ball-tracking data
        for i,j in enumerate(raw['balltrackingdata']):
                # calculate distance between HMD and ball
                dx = (j['simulated_ball']['x']-raw['qbtrackingdata'][i]['hmd_location']['x'])/91.44
                dy = (j['simulated_ball']['y']-raw['qbtrackingdata'][i]['hmd_location']['y'])/91.44
                dz = (j['simulated_ball']['z']-raw['qbtrackingdata'][i]['hmd_location']['z'])/91.44
                dist = (dx**2.0 + dy**2.0)**0.5
                # if the ball is "far enough" away from the headset in the X-Y plane, it has been released
                if dist > dt:
                    # release frame
                    rf = i
                    break
        # function for calculating orientation         
        def orientation(xl,yl,xr,yr):
            # determine angle
            angle = np.arctan2(yr-yl,xr-xl)
            # shift towards player face
            angle += np.pi/2
            # return value of interest
            return angle
        # identify who is running routes
        trackelig = []
        for i,j in enumerate(raw['playerroles']['offense']):
            if j['route'] is not None:
                for m,n in enumerate(raw['playertrackingdata']):
                    if n['playerid'] == j['playerid']:
                        trackelig.append(n)
        # identify which players are on defense
        dnum = []
        for k in raw['playerroles']['defense']:
            dnum.append(k['playerid'])
        # concentrate defensive tracking metrics
        trackd = []
        for i,j in enumerate(raw['playertrackingdata']):
            if j['playerid'] in dnum:
                trackd.append(j['playertracking'])
        # initialize minimum distance for non-thrown away (yards)
        mind = 5
        # set aim point distance in front of shoulders (in yards)
        apd = 0.5
        # initialize the intended receiver
        ir = None
        # calculate aim point and separation for each time step
        sep = []
        for k in trackelig:
            # for each time step
            # initialize separation
            recsep = []
            for i,j in enumerate(k['playertracking']):
                # condense receiver location to single point
                recloc = {}
                recloc['x'] = -(j['leftshoulder']['x']+j['rightshoulder']['x']+j['back']['x'])/3
                recloc['y'] = (j['leftshoulder']['y']+j['rightshoulder']['y']+j['back']['y'])/3
                # for aim point purposes only
                recloc['z'] = (j['leftshoulder']['z']+j['rightshoulder']['z'])/2
                recloc['dir'] = orientation(-j['leftshoulder']['x'],j['leftshoulder']['y'],
                      -j['rightshoulder']['x'],j['rightshoulder']['y'])
                # calculate separation by looping through defenders
                separ = []
                for m in trackd:
                    # defender location
                    dloc = {}
                    dloc['x'] = -(m[i]['leftshoulder']['x']+m[i]['rightshoulder']['x']+m[i]['back']['x'])/3
                    dloc['y'] = (m[i]['leftshoulder']['y']+m[i]['rightshoulder']['y']+m[i]['back']['y'])/3
                    # calculate separation
                    separ.append((((recloc['x']-dloc['x'])**2.0+(recloc['y']-dloc['y'])**2.0)**0.5)/91.44)
                recsep.append(min(separ))
                # after ball is thrown, start tracking aim point, find intended receiver,
                # and create ball placement graphic
                if rf is not None:
                    if i > rf:
                        aimpt = {}
                        aimpt['x'] = (recloc['x'] + apd*np.cos(recloc['dir']))/91.44
                        aimpt['y'] = (recloc['y'] + apd*np.sin(recloc['dir']))/91.44
                        aimpt['z'] = recloc['z']/91.44
                        aimpt['dir'] = recloc['dir']
                        # calculate distance between ball and aim point
                        dx = -raw['balltrackingdata'][i]['simulated_ball']['x']/91.44-aimpt['x']
                        dy = raw['balltrackingdata'][i]['simulated_ball']['y']/91.44-aimpt['y']
                        dz = raw['balltrackingdata'][i]['simulated_ball']['z']/91.44-aimpt['z']
                        dba = (dx**2.0+dy**2.0+dz**2.0)**0.5
                        # identify intended receiver
                        if dba < mind:
                            mind = dba
                            ir = k['playerid']
                            # coordinates of aim point
                            mark = aimpt
                            # target frame
                            ballmark = {}
                            ballmark['x'] = -raw['balltrackingdata'][i]['simulated_ball']['x']/91.44
                            ballmark['y'] = raw['balltrackingdata'][i]['simulated_ball']['y']/91.44
                            ballmark['z'] = raw['balltrackingdata'][i]['simulated_ball']['z']/91.44
            sep.append(recsep)
        # if not a sack and not thrown away
        if rf is not None and mind < 5:
            # determine relative angle
            tangle = orientation(ballmark['x'],ballmark['y'],mark['x'],mark['y'])-np.pi/2
            # construct accuracy image
            fig,ax = plt.subplots()
            recimg = plt.imread(os.getcwd()+'\\Moving.png')
            # determine if the receiver is moving from left to right or right to left
            if abs(aimpt['dir']) < np.pi/2:
                # running left
                plt.imshow(recimg, extent = [mark['x']*np.cos(tangle)+mark['y']*np.sin(tangle)-1.25,
                                              mark['x']*np.cos(tangle)+mark['y']*np.sin(tangle)+0.4,0,1.95])
                plt.gca().invert_xaxis()
            else:
                # running right
                plt.imshow(recimg, extent = [mark['x']*np.cos(tangle)+mark['y']*np.sin(tangle)-1.25,
                                              mark['x']*np.cos(tangle)+mark['y']*np.sin(tangle)+0.4,0,1.95])
            plt.plot(mark['x']*np.cos(tangle)+mark['y']*np.sin(tangle),mark['z'],'go')
            plt.plot(ballmark['x']*np.cos(tangle)+ballmark['y']*np.sin(tangle),mark['z'],'ko')
            gc = [[],[]]
            yc = [[],[]]
            rc = [[],[]]
            for ang in range(0,361,5):
                gc[0].append(mark['x']*np.cos(tangle)+mark['y']*np.sin(tangle)+0.5*np.cos(ang*np.pi/180))
                gc[1].append(mark['z']+0.5*np.sin(ang*np.pi/180))
                yc[0].append(mark['x']*np.cos(tangle)+mark['y']*np.sin(tangle)+1*np.cos(ang*np.pi/180))
                yc[1].append(mark['z']+1*np.sin(ang*np.pi/180))
                rc[0].append(mark['x']*np.cos(tangle)+mark['y']*np.sin(tangle)+1.5*np.cos(ang*np.pi/180))
                rc[1].append(mark['z']+1.5*np.sin(ang*np.pi/180))
            plt.plot(gc[0],gc[1],'g-')
            plt.plot(yc[0],yc[1],'y-')
            plt.plot(rc[0],rc[1],'r-')
            plt.axis('equal')
            # convert to a base64 image string
            imgdata = BytesIO()
            fig.savefig(imgdata, format='png',transparent=True,frameon=False,bbox_inches='tight')
            imgdata.seek(0)
            targetimage = 'data:image/png;base64,' + quote(b64encode(imgdata.read()))
            plt.close()
        else:
            targetimage = None
        # calculate air yards and air distance
        if rf is None:
            # sack (or scramble)
            ay = None
            ad = None
            targetimage = None
            zone = None
        elif ir is None:
            # air yards
            ay = round(raw['balltrackingdata'][len(raw['balltrackingdata'])-1]['simulated_ball']['y']/91.44)-raw['playsituation']['los']
            # air distance
            dx = raw['balltrackingdata'][len(raw['balltrackingdata'])-1]['simulated_ball']['x']-raw['qbtrackingdata'][rf]['hmd_location']['x']
            dy = raw['balltrackingdata'][len(raw['balltrackingdata'])-1]['simulated_ball']['y']-raw['qbtrackingdata'][rf]['hmd_location']['y']
            ad = (dx**2.0+dy**2.0)**0.5/91.44
            # placeholders for mark and ballmark
            targetimage = None
        else:
            # calculate air yards
            ay = round(ballmark['y'])-raw['playsituation']['los']
            # calculate air distance
            dx = ballmark['x']-raw['qbtrackingdata'][rf]['hmd_location']['x']
            dy = ballmark['y']-raw['qbtrackingdata'][rf]['hmd_location']['y']
            ad = ((dx**2.0+dy**2.0)**0.5)/91.44
        # check for intentional grounding
        ig = False
        if ir is None:
            if rf is not None:
                if abs(raw['qbtrackingdata'][rf]['hmd_direction']['x']-raw['qbtrackingdata'][0]['hmd_direction']['x'])/91.44 < 3.5:
                    ig = True
        # zone targeted (if not thrown away)
        zone = None
        if ay is not None and mind < 5:
            if ay > 15:
                zone = 'Deep '
                if ballmark['x'] < -(53+1/3)/6:
                    zone += 'Left'
                elif ballmark['x'] > (53+1/3)/6:
                    zone += 'Right'
                else:
                    zone += 'Middle'
            else:
                if ballmark['x'] < -(53+1/3)/4:
                    zone = 'Left '
                    if ay < 5:
                        zone += 'Flat'
                    else:
                        zone += 'Out'
                elif ballmark['x'] > (53+1/3)/4:
                    zone = 'Right '
                    if ay < 5:
                        zone += 'Flat'
                    else:
                        zone += 'Out'
                elif ballmark['x'] < 0:
                    zone = 'Left Hook'
                else:
                    zone = 'Right Hook'
        # convert to json (dictionary) format
        stats = {}
        stats['Intended Receiver'] = ir
        stats['Air Yards'] = ay
        stats['Air Distance'] = ad
        stats['Targeted Zone'] = zone
        stats['Intentional Grounding'] = ig
        stats['Ball Placement Image'] = targetimage
        stats['Separation'] = sep
        # return values of interest
        return stats

    # Streamlined function to be used to calculate stats necessary to construct
    # summary page without any unnecessary calculation
    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET','POST'])
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def sumcalcs(self):
        raw = cherrypy.request.json
        # function to calculate receiver orientation       
        def orientation(xl,yl,xr,yr):
            # determine angle
            angle = np.arctan2(yr-yl,xr-xl)
            # shift towards player face
            angle += np.pi/2
            # return value of interest
            return angle
        # function to calculate zone targeted
        def passzone(x,y):
            # deep zones
            if y > 15:
                    zone = 'Deep '
                    # determine third
                    if x < -(53+1/3)/6:
                        zone += 'Left'
                    elif x > (53+1/3)/6:
                        zone += 'Right'
                    else:
                        zone += 'Middle'
            else:
                # short zones
                if x < -(53+1/3)/4:
                    zone = 'Left '
                    if y < 5:
                        zone += 'Flat'
                    else:
                        zone += 'Out'
                elif x > (53+1/3)/4:
                    zone = 'Right '
                    if y < 5:
                        zone += 'Flat'
                    else:
                        zone += 'Out'
                elif x > 0:
                    zone = 'Left Hook'
                else:
                    zone = 'Right Hook'
            # return zone targeted
            return zone
        # initialize results
        results = {}
        # initialize the ball as not thrown
        thrown = False
        # release threshold (yards)
        dt = 1.25
        # aim point distance
        apd = 0.5
        # identify who is running routes
        trackelig = []
        for i,j in enumerate(raw['playerroles']['offense']):
            if j['route'] is not None:
                for m,n in enumerate(raw['playertrackingdata']):
                    if n['playerid'] == j['playerid']:
                        trackelig.append(n)
        # initialize minimum distance
        mind = 5
        # initialize release frame
        rf = None
        # initialize intended receiver
        results['ir'] = None
        # intialize relative ball placement
        rel = {}
        # loop through ball-tracking data
        for i,j in enumerate(raw['balltrackingdata']):
            if thrown == False:
                # calculate distance between HMD and ball
                dx = (j['simulated_ball']['x']-raw['qbtrackingdata'][i]['hmd_location']['x'])/91.44
                dy = (j['simulated_ball']['y']-raw['qbtrackingdata'][i]['hmd_location']['y'])/91.44
                dz = (j['simulated_ball']['z']-raw['qbtrackingdata'][i]['hmd_location']['z'])/91.44
                dist = (dx**2.0 + dy**2.0)**0.5
                # if the ball is "far enough" away from the headset in the X-Y plane, it has been released
                if dist > dt:
                    # release frame
                    rf = i
                    # time to throw
                    results['ttt'] = raw['qbtrackingdata'][i]['sim_time']-raw['qbtrackingdata'][0]['sim_time']
                    results['rh'] = j['simulated_ball']['z']/91.44*36.0     # convert to inches
                    # update thrown status
                    thrown = True
                elif i == len(raw['balltrackingdata'])-1:
                    results['ttt'] = raw['qbtrackingdata'][i]['sim_time']-raw['qbtrackingdata'][0]['sim_time']
            else:
                # after the ball has been thrown, start working towards identifying intended receiver
                for k in trackelig:
                    # condense receiver location to single point
                    orient = orientation(-k['playertracking'][i]['leftshoulder']['x'],k['playertracking'][i]['leftshoulder']['y'],
                      -k['playertracking'][i]['rightshoulder']['x'],k['playertracking'][i]['rightshoulder']['y'])
                    # calculate aimpoint
                    aimpt = {}
                    aimpt['x'] = -(k['playertracking'][i]['leftshoulder']['x']+k['playertracking'][i]['rightshoulder']['x']+k['playertracking'][i]['back']['x'])/3/91.44 + apd*np.cos(orient)
                    aimpt['y'] = (k['playertracking'][i]['leftshoulder']['y']+k['playertracking'][i]['rightshoulder']['y']+k['playertracking'][i]['back']['y'])/3/91.44 + apd*np.sin(orient)
                    aimpt['z'] = (k['playertracking'][i]['leftshoulder']['z']+k['playertracking'][i]['rightshoulder']['z'])/2/91.44
                    # calculate distance between ball and aim point
                    dx = -raw['balltrackingdata'][i]['simulated_ball']['x']/91.44-aimpt['x']
                    dy = raw['balltrackingdata'][i]['simulated_ball']['y']/91.44-aimpt['y']
                    dz = raw['balltrackingdata'][i]['simulated_ball']['z']/91.44-aimpt['z']
                    dba = (dx**2.0+dy**2.0+dz**2.0)**0.5
                    # identify intended receiver
                    if dba < mind:
                        mind = dba
                        results['ir'] = k['playerid']
                        # target frame
                        ballmark = {}
                        ballmark['x'] = -raw['balltrackingdata'][i]['simulated_ball']['x']/91.44
                        ballmark['y'] = raw['balltrackingdata'][i]['simulated_ball']['y']/91.44
                        ballmark['z'] = raw['balltrackingdata'][i]['simulated_ball']['z']/91.44
                        # coordinates of ball relative to aim point
                        rel['x'] = ballmark['x'] - aimpt['x']
                        rel['y'] = ballmark['y'] - aimpt['y']
                        rel['z'] = ballmark['z'] - aimpt['z']
        # calculate ball placement for figure
        results['relbp'] = {}
        if len(rel) > 0:
            rangle = np.arctan2(rel['x'],rel['y'])
            results['relbp']['width'] = rel['x']*np.cos(rangle) + rel['y']*np.sin(rangle)
            results['relbp']['height'] = rel['z']
        # calculate air yards and air distance
        if rf is None:
            # sack (or scramble)
            results['ay'] = None
            results['ad'] = None
            results['zone'] = None
        elif results['ir'] is None:
            # air yards
            results['ay'] = round(raw['balltrackingdata'][len(raw['balltrackingdata'])-1]['simulated_ball']['y']/91.44)-raw['playsituation']['los']
            # air distance
            dx = raw['balltrackingdata'][len(raw['balltrackingdata'])-1]['simulated_ball']['x']/91.44-raw['qbtrackingdata'][rf]['hmd_location']['x']/91.44
            dy = raw['balltrackingdata'][len(raw['balltrackingdata'])-1]['simulated_ball']['y']/91.44-raw['qbtrackingdata'][rf]['hmd_location']['y']/91.44
            results['ad'] = (dx**2.0+dy**2.0)**0.5
        else:
            # calculate air yards
            results['ay'] = round(ballmark['y'])-raw['playsituation']['los']
            # calculate air distance
            dx = ballmark['x']-raw['qbtrackingdata'][rf]['hmd_location']['x']/91.44
            dy = ballmark['y']-raw['qbtrackingdata'][rf]['hmd_location']['y']/91.44
            results['ad'] = (dx**2.0+dy**2.0)**0.5
        # check for intentional grounding
        results['ig'] = False
        if results['ir'] is None:
            if rf is not None:
                if abs(raw['qbtrackingdata'][rf]['hmd_direction']['x']-raw['qbtrackingdata'][0]['hmd_direction']['x'])/91.44 < 3.5:
                    results['ig'] = True
        # zone targeted (if not thrown away)
        results['zone'] = None
        if results['ay'] is not None and mind < 5:
            results['zone'] = passzone(ballmark['x'],results['ay'])
        # return values of interest
        return results

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET','POST'])
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def totalstats(self):
        folder = cherrypy.request.json
        # add relative folder path to more complete path
        folder = 'C:\\Users\\andrew.mccarthy\\Documents\\Assessment\\'+folder
        # function to calculate passer rating
        def pr(com,att,yds,td,inter):
            # initialize rating
            rating = None
            # calculate passer rating
            if att > 0:
                a = min(2.375,max(0.0,(com/att - 0.3)*5.0))
                b = min(2.375,max(0.0,(yds/att-3.0)*0.25))
                c = min(2.375,max(0.0,(td/att)*20.0))
                d = min(2.375,max(0.0,2.375-(inter/att*25.0)))
                rating = ((a+b+c+d)*100.0)/6.0
            # construct rating string
            string = str(com)+'/'+str(att)+' '+str(yds)+' yds'
            if td > 0:
                string += ' '+str(td)+' TD'
            if inter > 0:
                string += ' '+str(inter)+' INT'
            # determine how good the rating is
            if rating is None:
                color = 'gray'
            elif rating > 85:
                color = 'green'
            elif rating < 50:
                color = 'red'
            else:
                color = 'yellow'
            # return values of interest
            return rating,string,color
        # list plays in the session
        plist = []
        for file in os.listdir(folder):
            if file.endswith('.json'):
                plist.append(file)
        # initialize stats of interest
        totals = {}
        totals['Sacks'],totals['Intentional Grounding'],totals['Thrown Away'] = 0,0,0
        totals['Completions'],totals['Passing Yards'],totals['Passing Touchdowns'] = 0,0,0
        totals['Attempts'],totals['Interceptions'] = 0,0
        totals['Average Air Yards'],totals['Average Air Distance'],totals['Average Time to Throw'] = 0,0,0
        # what unique routes were run
        uroutes = []
        # overall route data
        totals['Route Data'] = [['Route','Run','Targets','Completions','Touchdowns','Yards']]
        # initialize ball placement data
        bp = {'rl': [], 'hilo': []}
        # initialize zone data
        byzone = {'Deep Left': {'Targets': 0,
                                'Completions': 0,
                                'Touchdowns': 0,
                                'Interceptions': 0,
                                'Yards': 0,
                                'Position': (-80/3,-35),
                                'Height': 15,
                                'Width': 160/9},
                  'Deep Middle': {'Targets': 0,
                                'Completions': 0,
                                'Touchdowns': 0,
                                'Interceptions': 0,
                                'Yards': 0,
                                'Position': (-80/9,-35),
                                'Height': 15,
                                'Width': 160/9},
                  'Deep Right': {'Targets': 0,
                                'Completions': 0,
                                'Touchdowns': 0,
                                'Interceptions': 0,
                                'Yards': 0,
                                'Position': (80/9,-35),
                                'Height': 15,
                                'Width': 160/9},
                  'Left Out': {'Targets': 0,
                                'Completions': 0,
                                'Touchdowns': 0,
                                'Interceptions': 0,
                                'Yards': 0,
                                'Position': (-80/3,-45),
                                'Height': 10,
                                'Width': 40/3},
                  'Left Hook': {'Targets': 0,
                                'Completions': 0,
                                'Touchdowns': 0,
                                'Interceptions': 0,
                                'Yards': 0,
                                'Position': (-40/3,-50),
                                'Height': 15,
                                'Width': 40/3},
                  'Right Hook': {'Targets': 0,
                                'Completions': 0,
                                'Touchdowns': 0,
                                'Interceptions': 0,
                                'Yards': 0,
                                'Position': (0,-50),
                                'Height': 15,
                                'Width': 40/3},
                  'Right Out': {'Targets': 0,
                                'Completions': 0,
                                'Touchdowns': 0,
                                'Interceptions': 0,
                                'Yards': 0,
                                'Position': (40/3,-45),
                                'Height': 10,
                                'Width': 40/3},
                  'Left Flat': {'Targets': 0,
                                'Completions': 0,
                                'Touchdowns': 0,
                                'Interceptions': 0,
                                'Yards': 0,
                                'Position': (-80/3,-50),
                                'Height': 5,
                                'Width': 40/3},
                  'Right Flat': {'Targets': 0,
                                'Completions': 0,
                                'Touchdowns': 0,
                                'Interceptions': 0,
                                'Yards': 0,
                                'Position': (40/3,-50),
                                'Height': 5,
                                'Width': 40/3}}
        for i,raw in enumerate(plist):
            ## read in json file
            with open(folder+'\\'+i) as file:
                raw = json.load(file)
            # perform calculations
            mets = sumcalcs(raw)
            # relative ball placement
            if len(mets['relbp']) > 0:
                bp['rl'].append(mets['relbp']['width'])
                bp['hilo'].append(mets['relbp']['height'])
            # determine which routes were run
            routes = [j['route']['name'] for j in raw['playerroles']['offense'] if j['route'] is not None]
            for j in routes:
                # accumulate routes run
                for k in totals['Route Data']:
                    if j == k[0]:
                        k[1] += 1
                if j not in uroutes:
                    uroutes.append(j)
                    totals['Route Data'].append([j,1,0,0,0,0])
            # what was the targeted route?
            if mets['ir'] is not None:
                byzone[mets['zone']]['Targets'] += 1
                troute = [j['route']['name'] for j in raw['playerroles']['offense'] if j['route'] is not None if j['playerid'] == mets['ir']][0]
                for j,k in enumerate(totals['Route Data']):
                    if k[0] == troute:
                        update = k
                        update[2] += 1
                        entry = j
                # determine if complete
                if raw['playresult']['result'] == 'Complete':
                    totals['Completions'] += 1
                    totals['Passing Yards'] += mets['ay'] + round(raw['playresult']['yac'])
                    update[3] += 1
                    update[5] += mets['ay'] + round(raw['playresult']['yac'])
                    # update zone
                    byzone[mets['zone']]['Completions'] += 1
                    byzone[mets['zone']]['Yards'] += mets['ay'] + round(raw['playresult']['yac'])
                    # determine if touchdown
                    if mets['ay'] + raw['playresult']['yac'] > 50-raw['playsituation']['los']:
                        totals['Passing Touchdowns'] += 1
                        byzone[mets['zone']]['Touchdowns'] += 1
                # update routes
                totals['Route Data'][entry] = update
            # accumulate time to throw (even on sacks)
            totals['Average Time to Throw'] += mets['ttt']
            # accumulate attempts, air yards, and air distance (on non-sacks)
            if mets['ay'] is not None:
                totals['Attempts'] += 1
                totals['Average Air Yards'] += mets['ay']
                totals['Average Air Distance'] += mets['ad']
            else:
                totals['Sacks'] += 1
            # accumulate intentional grounding
            if mets['ig']:
                totals['Intentional Grounding'] += 1
            # accumulate thrown away
            if mets['ay'] is not None and mets['ir'] is None:
                totals['Thrown Away'] += 1
        # calculate averages
        totals['Completion Percentage'] = totals['Completions']/totals['Attempts']
        totals['Yards Per Attempt'] = totals['Passing Yards']/totals['Attempts']
        totals['Average Air Yards'] = totals['Average Air Yards']/totals['Attempts']
        totals['Average Air Distance'] = totals['Average Air Distance']/totals['Attempts']
        totals['Average Time to Throw'] = totals['Average Time to Throw']/len(plist)
        # calculate passer rating
        totals['Passer Rating'] = pr(totals['Completions'],totals['Attempts'],totals['Passing Yards'],
              totals['Passing Touchdowns'],totals['Interceptions'])[0]
        # construct cumulative ball placement image
        fig,ax = plt.subplots()
        plt.plot(0,0,'go')
        gc = [[],[]]
        yc = [[],[]]
        rc = [[],[]]
        for ang in range(0,361,5):
            gc[0].append(0.5*np.cos(ang*np.pi/180))
            gc[1].append(0.5*np.sin(ang*np.pi/180))
            yc[0].append(1*np.cos(ang*np.pi/180))
            yc[1].append(1*np.sin(ang*np.pi/180))
            rc[0].append(1.5*np.cos(ang*np.pi/180))
            rc[1].append(1.5*np.sin(ang*np.pi/180))
        plt.plot(gc[0],gc[1],'g-')
        plt.plot(yc[0],yc[1],'y-')
        plt.plot(rc[0],rc[1],'r-')
        plt.plot(bp['rl'],bp['hilo'],'ko')
        plt.axis('equal')
        # convert to a base64 image string
        imgdata = BytesIO()
        fig.savefig(imgdata, format='png',transparent=True,frameon=False,bbox_inches='tight')
        imgdata.seek(0)
        totals['targetimage'] = 'data:image/png;base64,' + quote(b64encode(imgdata.read()))
        plt.close()
        # construct cumulative zone-by-zone image
        # field background
        fig,ax = plt.subplots(figsize=(160/3/10,30/10))
        fieldimg = plt.imread(os.getcwd()+'\\bwField.png')
        plt.imshow(fieldimg,origin = 'upper',extent = [-80/3, 80/3, -60, 60])
        # zones
        for i in byzone:
            # calculate passer rating and stats for each zone
            rat,zstr,zcol = pr(byzone[i]['Completions'],byzone[i]['Targets'],byzone[i]['Yards'],byzone[i]['Touchdowns'],byzone[i]['Interceptions'])
            ax.add_patch(ptc.Rectangle(byzone[i]['Position'],byzone[i]['Width'],byzone[i]['Height'],ec='black',fc = zcol,alpha = 0.7))
            ax.annotate(i,xy=(byzone[i]['Position'][0]+byzone[i]['Width']/2,byzone[i]['Position'][1]+byzone[i]['Height']/2+1),fontsize = 10,ha='center',va='center')
            ax.annotate(zstr,xy=(byzone[i]['Position'][0]+byzone[i]['Width']/2,byzone[i]['Position'][1]+byzone[i]['Height']/2-1),fontsize = 8,ha='center',va='center')
        # plot aesthetics
        ax.set_xlim(-80/3,80/3)
        ax.set_ylim(-50,-20)
        plt.axis('off')
        # convert to a base64 image string
        imgdata = BytesIO()
        fig.savefig(imgdata, format='png',transparent=True,frameon=False,bbox_inches='tight')
        imgdata.seek(0)
        totals['zoneimage'] = 'data:image/png;base64,' + quote(b64encode(imgdata.read()))
        plt.close()
        # return values of interest
        return totals

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET','POST'])
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def data(self):
        filename = cherrypy.request.json
        return filename
        with open("C:/Users/andrew.mccarthy/Desktop/"+filename['relpath']+filename['filename']) as file:
            raw = json.load(file)
        return raw


if __name__ == '__main__':
    # not having to restart the server
    cherrypy.config.update({"engine.autoreload.on": True,
                            "server.socket_host": "0.0.0.0",
                            })
    # finding static directory
    app_conf = {'/static': {"tools.staticdir.on": True,
                            "tools.staticdir.dir":
                                os.path.join(os.getcwd(), "static")}}
    # important
    cherrypy.tree.mount(VTSassessment(), '/', config=app_conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
