<template>
  <div
   id="main-menu">
    <v-layout>
      <v-flex xs-1>
        <v-menu
        :nudge-bottom="50"
        :nudge-width="100"
        v-model="menu"
        offsex-x
        color="grey darken-4">
          <v-btn slot="activator" color="blue-grey darken-3" dark><i class="material-icons">scatter_plot</i></v-btn>
          <v-card>
            <v-list @hover="hoverMachine">
              <v-list-tile  class="menu-item">
                <form enctype="multiple/form-data">
                      <input class="inputfile" type="file" webkitdirectory multiple @change="loadFiles" id="selectFiles">
                      Choose Folder
                </form>
                <br>
                <br>
              </v-list-tile>
              <v-list-tile v-if="filesLoaded === true" class="menu-item" >
                <v-select v-if="filesLoaded === true" label="Select Play" :items="plays" item-text="name" @change="changePlay"></v-select>
              </v-list-tile>
              <v-divider></v-divider>
              <v-list-tile v-if="filesLoaded === true" class="menu-item" @click="setPlayAnimation">
                Play Animation
              </v-list-tile>
              <v-divider></v-divider>
              <v-list-tile v-if="filesLoaded === true" class="menu-item" @click="setPlayInformation">
                Play Information
              </v-list-tile>
              <v-divider></v-divider>
              <v-list-tile v-if="filesLoaded === true" class="menu-item" @click="setQBPerformance">
                QB Performance
              </v-list-tile>
              <v-divider></v-divider>
              <v-list-tile v-if="filesLoaded === true" class="menu-item" @click="setSessionStatistics">
                Session Statistics
              </v-list-tile>
            </v-list>
          </v-card>
        </v-menu>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  data () {
    return {
      a1: null,
      bool: false,
      files: [],
      fileNames: [],
      filesLoaded: false,
      items: [
        {title: 'Play Animation'},
        {title: 'Play Information'},
        {title: 'QB Performance'},
        {title: 'Session Statistics'}
      ],
      dirtyFiles: [],
      fileinput: '',
      parsedJsonArray: [],
      stringJSON: '',
      plays: [],
      cnt: 0
    }
  },
  computed: mapGetters({
    sliderTime: 'sliderTime',
    btnState: 'btnState',
    trackingData: 'trackingData',
    maxTime: 'maxTime',
    currentPage: 'currentPage',
    jsonData: 'jsonData'
  }),
  methods: {
    setPlayAnimation () {
      let val = 'playAnimation'
      console.log('Current play set to play Animation')
      this.$store.commit('changeCurrentPage', val)
    },
    setPlayInformation () {
      let val = 'playInformation'
      this.$store.commit('changeCurrentPage', val)
    },
    setQBPerformance () {
      let val = 'QBPerformance'
      this.$store.commit('changeCurrentPage', val)
    },
    setSessionStatistics () {
      let val = 'SessionStatistics'
      this.$store.commit('changeCurrentPage', val)
    },
    orientation (xl, yl, xr, yr) {
    // determine angle
      let angle = Math.atan2(yr - yl, xr - xl)
      // shift towards player face
      angle += Math.PI / 2
      // return value of interest
      return angle
    },
    XYDirection (raw, filename) {
      let parsed = JSON.parse(raw)
      if (parsed.balltrackingdata['0'].simulated_ball.x != undefined) {
        let times = []
        let plist = []
        // add sim times
        for (let i of parsed['balltrackingdata']) {
          times.push(i['sim_time'])
        }
        // calculate minimum sim time
        let mint = Math.min(times)
        // player tracking data
        for (let i of parsed['playertrackingdata']) {
        // initialize players
          let player = {}
          player['playerid'] = i['playerid']
          // initialize tracking
          let tracking = []
          for (let m of i['playertracking']) {
          // # initialize point
            let loc = {}
            // calculate locations
            loc['x'] = -(m['leftshoulder'].x + m['rightshoulder'].x + m['back'].x) / 3 / 91.44
            loc['y'] = (m['leftshoulder'].y + m['rightshoulder'].y + m['back'].y) / 3 / 91.44
            loc['dir'] = this.orientation(m['leftshoulder'].x, m['leftshoulder'].y,
              m['rightshoulder'].x, m['leftshoulder'].y)
            loc['time'] = m['sim_time'] - mint
            tracking.push(loc)
          }
          // add tracking data
          player['playertracking'] = tracking
          plist.push(player)
        }

        // amend large data section
        parsed['playertrackingdata'] = plist

        // ball tracking data
        let balltrack = []
        for (let j of parsed['balltrackingdata']) {
          let ball = {}
          ball.sim_time = j['sim_time'] - mint
          ball.simulated_ball = {}
          ball.simulated_ball.x = -j.simulated_ball.x / 91.44
          ball.simulated_ball.y = j.simulated_ball.y / 91.44
          ball.simulated_ball.z = j.simulated_ball.z / 91.44
          // add to time stamp
          balltrack.push(ball)
        }
        // amend data section
        parsed['balltrackingdata'] = balltrack

        // qb tracking data
        let qbTrack = []
        for (let j of parsed['qbtrackingdata']) {
          let qb = {}
          qb['x'] = -j['hmd_location'].x / 91.44
          qb['y'] = j['hmd_location'].y / 91.44
          if (j['hmd_direction'].x < 0) {
            qb['dir'] = Math.PI + Math.atan(j['hmd_direction'].y / j['hmd_direction'].x)
          } else {
            qb['dir'] = Math.atan(j['hmd_direction'].y / j['hmd_direction'].x)
          }
          qbTrack.push(qb)
        }
        parsed['qbtrackingdata'] = qbTrack
        parsed.name = filename
        console.log(parsed.name)
        console.log(parsed)
        this.$store.commit('updatePlay', parsed)
        // return jsons
      }
    },

    orderFiles (files) {
      let fileHolder = []
      let orderedDates = []
      let orderedFiles = []
      let cnt = 0
      // loop through files
      for (let file of files) {
        // push files to array
        if (cnt !== files.length) {
          // make sure file is a json file
          if (file['name'].endsWith('.json')) {
            orderedDates.push(file['lastModified'])
            fileHolder.push(file)
          }
        }
        cnt++
      }
      // sort files by date modified
      orderedDates.sort(function (a, b) { return b - a })
      for (var i = 0; i < orderedDates.length; i++) {
        for (var j = 0; j < fileHolder.length; j++) {
          if (fileHolder[j]['lastModified'] === orderedDates[i]) {
            orderedFiles.push(fileHolder[j])
            this.dirtyFiles.push(fileHolder[j].name)
          }
        }
      }
      this.orderedFiles = orderedFiles
      return orderedFiles
    },

    async jsonLoop (files, clickedPlay) {
      let count = 0
      console.log(clickedPlay, 'clickedPlay')
      for (let file of files) {
        let self = this
        let fr = new FileReader()
        self.cnt++
        if (clickedPlay === file.name) {
          fr.onload = (e) => {
            let jsonResult = e.target.result
            this.$store.commit('settingJson', JSON.parse(jsonResult))
            self.getRouteDetail()
              .then(jsonData => {
                let routeData = jsonData
                self.$store.commit('setRouteData', routeData)
                console.log(routeData, 'ROUTE')
              })
            self.XYDirection(jsonResult, file.name)
            self.getRelease()
              .then(jsonData => {
                let releaseData = jsonData
                self.$store.commit('setReleaseData', releaseData)
                console.log(releaseData, 'RELEASE')
              })
          }
        }

        // }
        this.fileNames.push(file.webkitRelativePath.toString())
        this.plays.push(file.name)
        self.filesLoaded = true
        fr.readAsText(file)
      }
    },
    getSessionStats () {
      let self = this
      let sessionStats = ''
      let host = '/totalstats'
      let data = {json: this.fileNames}
      console.log('JSON SENT', JSON.stringify({filename: this.plays[0]}))
      return fetch(host, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        url: host,
        body: JSON.stringify({filename: this.plays[0]}),
        dataType: 'json'
      })
        .catch(error => console.error('ERROR:', error))
        .then(res => res.json())
    },
    getRouteDetail () {
      let routeDetail = '/receivercalcs'
      let routeData = ''
      let data = JSON.stringify(this.jsonData)
      console.log('THIS IS WHAT IS BEING SENT ROUTE --->', this.jsonData)
      return fetch(routeDetail, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        url: routeDetail,
        body: data,
        dataType: 'json'
      })
        .catch(error => console.error('ERROR:', error))
        .then(res => res.json())
    },
    getRelease () {
      let release = '/release'
      let releaseData = ''
      let data = JSON.stringify(this.jsonData)
      console.log('THIS IS WHAT IS BEING SENT RELEASE--->', this.jsonData)
      return fetch(release, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        url: release,
        body: data,
        dataType: 'json'
      })
        .catch(error => console.error('ERROR:', error))
        .then(res => res.json())
    },
    loadFiles (e) {
      if (window.File && window.FileReader && window.FileList && window.Blob) {
        this.files = Array.from(e.target.files)
        // sort files
        // this.files = this.orderFiles(files)
        this.jsonLoop(this.files, this.files[0].name)
        this.setPlayAnimation()
        this.getSessionStats()
          .then(jsonData => {
            let sessionStats = jsonData
            this.$store.commit('setSessionStats', sessionStats)
            console.log('SESSION STATS', sessionStats)
          })
      } else {
        alert('The File APIs are not fully supported in this browser. Please use a different browser')
      }
    },

    changePlay (e) {
      this.jsonLoop(this.files, e)
    }
  },
  drawer: null,
  mounted () {
    console.log(self.stringJSON)
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.inputfile {
  opacity: 0;
	position: absolute;
}

.inputfile + label {
	cursor: pointer;
}
.menu-item {
  padding: 0;
}
.menu-item:hover {
  background-color: #57606f;
  color: white;
}

.navigation-drawer__border {
  width: 0px;
}

.play-btn {
    margin-left: 10px;
    font-family:  monospace
  }

</style>
