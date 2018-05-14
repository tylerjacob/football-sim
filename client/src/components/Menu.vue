<template>
  <div>
    <v-layout>
      <v-expansion-panel expand>
    <v-expansion-panel-content>
      <div slot="header">Upload Play Folder</div>
      <v-card>
        <form enctype="multiple/form-data">
            <input class="inputfile pl-4 pt-5" type="file" webkitdirectory multiple @change="loadFiles" id="selectFiles"/>
            <br>
        </form>
      </v-card>
      <br>
    </v-expansion-panel-content>
    <v-expansion-panel-content>
      <div slot="header">Animation Options</div>
      <v-card>
        
      </v-card>
    </v-expansion-panel-content>
    <v-expansion-panel-content>
      <div slot="header">Play Assessment</div>
      <v-card>
        
      </v-card>
    </v-expansion-panel-content>
    <v-expansion-panel-content>
      <div slot="header">other features</div>
      <v-card>
        
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>
    </v-layout>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
  data () {
    return {
      fileinput: '',
      parsedJsonArray: [],
      stringJSON: ''
    }
  },
  computed: mapGetters({
    sliderTime: 'sliderTime',
    btnState: 'btnState',
    trackingData: 'trackingData',
    maxTime: 'maxTime'
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
          loc['x'] = -(m['leftshoulder_x'] + m['rightshoulder_x'] + m['back_x']) / 3 / 91.44
          loc['y'] = (m['leftshoulder_y'] + m['rightshoulder_y'] + m['back_y']) / 3 / 91.44
          loc['dir'] = this.orientation(m['leftshoulder_x'], m['leftshoulder_y'],
            m['rightshoulder_x'], m['leftshoulder_y'])
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
        ball['sim_time'] = j['sim_time'] - mint
        ball['simulated_ball_x'] = -j['simulated_ball_x'] / 91.44
        ball['simulated_ball_y'] = j['simulated_ball_y'] / 91.44
        ball['simulated_ball_z'] = j['simulated_ball_z'] / 91.44
        // add to time stamp
        balltrack.push(ball)
      }
      // amend data section
      parsed['balltrackingdata'] = balltrack

      // qb tracking data
      let qbTrack = []
      for (let j of parsed['qbtrackingdata']) {
        let qb = {}
        qb['x'] = -j['hmd_location_x'] / 91.44
        qb['y'] = j['hmd_location_y'] / 91.44
        if (j['hmd_direction_x'] < 0) {
          qb['dir'] = Math.PI + Math.atan(j['hmd_direction_y'] / j['hmd_direction_x'])
        } else {
          qb['dir'] = Math.atan(j['hmd_direction_y'] / j['hmd_direction_x'])
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
  mounted(){
  var inputs = document.querySelectorAll( '.inputfile' );
Array.prototype.forEach.call( inputs, function( input )
{
	var label	 = input.nextElementSibling,
		labelVal = label.innerHTML;

	input.addEventListener( 'change', function( e )
	{
		var fileName = '';
		if( this.files && this.files.length > 1 )
			fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
		else
			fileName = e.target.value.split( '\\' ).pop();

		if( fileName )
			label.querySelector( 'span' ).innerHTML = fileName;
		else
			label.innerHTML = labelVal;
	});
});
}
}


</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#menu-options[data-v-8eeda45e] {
    background-color: rgba(0, 0, 0, 0.5);
    opacity: .9;
}

/* .inputfile {
	width: 0.1px;
	height: 0.1px;
	opacity: 0;
	overflow: hidden;
	position: absolute;
	z-index: -1;
}

.inputfile + label {
    font-size: 1.25em;
    font-weight: 700;
    color: white;
    background-color: black;
    display: inline-block;
}

.inputfile:focus + label,
.inputfile + label:hover {
    background-color: red;
}

.inputfile + label {
	cursor: pointer; /* "hand" cursor } */


.navigation-drawer__border {
  width: 0px;
}

.play-btn {
    margin-left: 10px;
    font-family:  monospace
  }

</style>
