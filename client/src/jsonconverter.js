//function for calculating player orientation
const orientation = (xl,yl,xr,yr) => {
    // determine angle
    let angle = Math.atan2(yr - yl, xr - xl)
    //shift towards player face
    angle += Math.PI/2
    // return value of interest
    return angle
}


const xydirection = (raw) => {
    //function for calculating player orientation
    orientaion(n['leftshoulder_x'],n['leftshoulder_y'],
    n['rightshoulder_x'],n['leftshoulder_y'])

    let plist = []

    for(i,j in raw['playertrackingdata'].entries()){
        //initialize players
        player = {}
        player['playerid'] = j['playerid']
        //calculate minimum sim time
        let mint = () => {
            for(p,q in j['playertracking'].entries()){
                Math.min(q['sim_time'])
        }}
        //initialize tracking
        let tracking = []
        for(m,n in j['playertracking'].entries()){
            //# initialize point
            let loc = {}
            //  calculate locations
            loc['x'] = -(n['leftshoulder_x']+n['rightshoulder_x']+n['back_x'])/3/91.44
            loc['y'] = (n['leftshoulder_x']+n['rightshoulder_x']+n['back_x'])/3/91.44
            loc['dir'] = orientation(n['leftshoulder_x'],n['leftshoulder_y'],
               n['rightshoulder_x'],n['leftshoulder_y'])
            loc['time'] = n['sim_time']-mint
            tracking.push(loc)
        }
        // add tracking data
        player['playertracking'] = tracking
    }
    plist.push(player)
    // amend large data section
    raw['playertrackingdata'] = plist

    //reurn json
    return raw
}

xydirection(jsonFile)