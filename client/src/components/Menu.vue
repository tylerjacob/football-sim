<template>
  <div>
    <v-list class="menu">
    <input type="file" @change="loadFile" class="pl-4 pt-3" id="selectFiles"/>
    <br>
    <v-btn id="import">Import</v-btn>
    <textarea id="result"></textarea>
    <v-card>
      <template slot="items">
      </template>
    </v-card>
    </v-list>
  </div>
</template>

<script>
export default {
  data() {
    return {
      file: {}
    }
  },
  methods: {
    XYDirection (raw) {
    let plist = []
    for(var i of raw['playertrackingdata'].entries()){
        //initialize players
        player = {}
        player['playerid'] = j['playerid']
        //calculate minimum sim time
        let mint = () => {
            for(p of j['playertracking'].entries()){
                Math.min(q['sim_time'])
        }}
        //initialize tracking
        let tracking = []
        for(var m of j['playertracking'].entries()){
            //# initialize point
            let loc = {}
            //  calculate locations
            loc['x'] = -(n['leftshoulder_x']+n['rightshoulder_x']+n['back_x'])/3/91.44
            loc['y'] = (n['leftshoulder_x']+n['rightshoulder_x']+n['back_x'])/3/91.44
            loc['dir'] = Orientation(n['leftshoulder_x'],n['leftshoulder_y'],
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

    //return json
    console.log(raw)
    return raw
    },

    loadFile (e) {
    let file = e.target.files[0]
    console.log(e)
    console.log(file)
    var reader = new window.FileReader()
    reader.onload = (e) => {
      console.log(e)
      console.log(reader)
      reader.readAsText(file)
    }
  }
},
  drawer: null
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .play-btn {
    margin-left: 10px;
    font-family:  monospace
  }
  .menu {
    position: relative;
    z-index: 25;
  }

  .text-reader {
  position: relative;
  overflow: hidden;
  display: inline-block;
  z-index: 26;

  /* Fancy button style 😎 */
  border: 2px solid black;
  border-radius: 5px;
  padding: 8px 12px;
  cursor: pointer;
}
.text-reader input {
  position: absolute;
  top: 0;
  left: 0;
  z-index: -100;
  opacity: 0;
}
</style>
