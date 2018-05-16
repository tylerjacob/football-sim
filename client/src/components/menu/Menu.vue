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
         <v-list-tile class="menu-item" @click="setPlayAnimation">
           <form enctype="multiple/form-data">
                <input class="inputfile" type="file" webkitdirectory multiple @change="loadFiles" id="selectFiles">
                Choose Folder
                <br>
                Select File
          </form>
        </v-list-tile>
        <v-divider></v-divider>
        <v-list-tile class="menu-item" @click="setPlayInformation">
          Play Information
        </v-list-tile>
        <v-divider></v-divider>
        <v-list-tile class="menu-item" @click="setQBPerformance">
          QB Performance
        </v-list-tile>
        <v-divider></v-divider>
        <v-list-tile class="menu-item" @click="setSessionStatistics">
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
      items: [
        {title: 'Play Animation'},
        {title: 'Play Information'},
        {title: 'QB Performance'},
        {title: 'Session Statistics'}
      ],
      fileinput: '',
      parsedJsonArray: [],
      stringJSON: ''
    }
  },
  computed: mapGetters({
    sliderTime: 'sliderTime',
    btnState: 'btnState',
    trackingData: 'trackingData',
    maxTime: 'maxTime',
    currentPage: 'currentPage'
  }),
  methods: {
    orientation (xl, yl, xr, yr) {
    // determine angle
      let angle = Math.atan2(yr - yl, xr - xl)
      // shift towards player face
      angle += Math.PI / 2
      // return value of interest
      return angle
    },
    XYDirection (raw) {
      let parsed = JSON.parse(raw)
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
      console.log("this works!")
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
      console.log("MARKER")
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
      // return jsons
      this.$store.commit('settingJson', parsed)
      this.$store.commit('setMaxTime', parsed.balltrackingdata.length - 1)
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
          }
        }
      }
      this.orderedFiles = orderedFiles
      return orderedFiles
    },

    async jsonLoop (files) {
      for (let file of files) {
        let self = this
        let fr = new FileReader()
        fr.onload = (e) => {
          let jsonResult = e.target.result
          // add unparsed json string to our data
          self.stringJSON += jsonResult
          // adding parsed json to our jsonData as an array of objects
          self.parsedJsonArray = [...self.parsedJsonArray, JSON.parse(jsonResult)]
          // running the animation function
          self.XYDirection(jsonResult)
        }
        fr.readAsText(file)
      }
    },
    loadFiles (e) {
      if (window.File && window.FileReader && window.FileList && window.Blob) {
        let files = Array.from(e.target.files)
        // sort files
        this.orderFiles(files)
        this.jsonLoop(files)
      } else {
        alert('The File APIs are not fully supported in this browser. Please use a different browser')
      }
    }
  },
  drawer: null,
  mounted () {
    var inputs = document.querySelectorAll('.inputfile')
    Array.prototype.forEach.call(inputs, function (input) {
      let label	= input.nextElementSibling,
        labelVal = label.innerHTML

      input.addEventListener('change', function (e) {
        var fileName = ''
        if (this.files && this.files.length > 1) { fileName = (this.getAttribute('data-multiple-caption') || '').replace('{count}', this.files.length) } else { fileName = e.target.value.split('\\').pop() }

        if (fileName) { label.querySelector('span').innerHTML = fileName } else { label.innerHTML = labelVal }
      })
    })
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
