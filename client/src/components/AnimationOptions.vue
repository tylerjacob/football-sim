<template>
    <v-container
    height="400px"
     fluid>
     <h1>General Controls</h1>
     <v-flex offset-xs1>
         <v-flex offset-xs2>
             <v-switch  color='green' label="All Players" v-model="allPlayers"></v-switch>
         </v-flex>
    <v-layout row>
            <v-switch color='green' label="Offense" v-model="showOffense"></v-switch>
            <v-switch color='green' label="Defense" v-model="showDefense"></v-switch>
     </v-layout>
     </v-flex>
     <v-divider></v-divider>
     <p>Player Labels</p>
     <v-flex offset-xs1>
     <v-layout row>
      <v-switch color='green' label="Jersey #" v-model="jerseyNum" ></v-switch>
      <v-switch color='green' label="Position" v-model="position" ></v-switch>
     </v-layout>
     </v-flex>
    <v-divider></v-divider>
    <p>Display Options</p>
    <v-flex offset-xs1>
    <v-layout row>
      <v-switch color='green' label="QB View" v-model="QBView"></v-switch>
      <v-switch color='green' label="Ball Track" v-model="ballTrack" ></v-switch>
     </v-layout>
     <v-layout row>
      <v-switch color='green' label="Off Play" v-model="offPlay" ></v-switch>
      <v-switch color='green' label="Def Play" v-model="defPlay" ></v-switch>
     </v-layout>
     </v-flex>
     <v-divider></v-divider>
     <p>Single Player Selection</p>
        <v-layout row>
        <v-flex offset-xs1 xs7
        align-start>
            <p class="player-toggle-title" justify-left>{{headers[0].text}}</p>
    <v-switch hide-details color='red' :label="offense[0].position + ' #' + offense[0].jersey" v-model="offense[0].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[1].position + ' #' + offense[1].jersey " v-model="offense[1].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[2].position + ' #' + offense[2].jersey" v-model="offense[2].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[3].position + ' #' + offense[3].jersey" v-model="offense[3].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[4].position + ' #' + offense[4].jersey" v-model="offense[4].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[5].position + ' #' + offense[5].jersey" v-model="offense[5].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[6].position + ' #' + offense[6].jersey" v-model="offense[6].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[7].position + ' #' + offense[7].jersey" v-model="offense[7].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[8].position + ' #' + offense[8].jersey" v-model="offense[8].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[9].position + ' #' + offense[9].jersey" v-model="offense[9].playing"></v-switch>
    <v-switch hide-details color='red' :label="offense[10].position+' #' + offense[10].jersey" v-model="offense[10].playing"></v-switch>
        </v-flex>
        <v-flex xs6
        align-end>
            <p class="player-toggle-title">{{headers[1].text}}</p>
    <v-switch hide-details color='blue' :label="defense[0].position+ ' #' + defense[0].jersey" v-model="defense[0].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[1].position+ ' #' + defense[1].jersey" v-model="defense[1].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[2].position+ ' #' + defense[2].jersey" v-model="defense[2].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[3].position+ ' #' + defense[3].jersey" v-model="defense[3].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[4].position+ ' #' + defense[4].jersey" v-model="defense[4].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[5].position+ ' #' + defense[5].jersey" v-model="defense[5].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[6].position+ ' #' + defense[6].jersey" v-model="defense[6].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[7].position+ ' #' + defense[7].jersey" v-model="defense[7].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[8].position+ ' #' + defense[8].jersey" v-model="defense[8].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[9].position+ ' #' + defense[9].jersey" v-model="defense[9].playing"></v-switch>
    <v-switch hide-details color='blue' :label="defense[10].position+' #' + defense[10].jersey" v-model="defense[10].playing"></v-switch>
        </v-flex>
    </v-layout>
    <br>
  </v-container>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  computed: {
    ...mapGetters({
      sliderTime: 'sliderTime',
      btnState: 'btnState',
      trackingData: 'trackingData',
      maxTime: 'maxTime'
    })
  },
  data () {
    return {
      allPlayers: true,
      showOffense: true,
      showDefense: true,
      headers: [
        {
          text: 'Offense',
          align: 'left',
          sortable: false,
          value: 'name'
        },
        {
          text: 'Defense',
          align: 'right',
          sortable: false,
          value: 'name'
        }
      ],
      offense: [
        {position: 'QB', playing: true, jersey: 15},
        {position: 'WR', playing: true, jersey: 12},
        {position: 'RB', playing: true, jersey: 12},
        {position: 'TE', playing: true, jersey: 12},
        {position: 'TE', playing: true, jersey: 12},
        {position: 'WR', playing: true, jersey: 12},
        {position: 'OT', playing: true, jersey: 12},
        {position: 'G', playing: true, jersey: 12},
        {position: 'C', playing: true, jersey: 12},
        {position: 'G', playing: true, jersey: 12},
        {position: 'OT', playing: true, jersey: 12}
      ],
      defense: [
        {position: 'CB1', playing: true, jersey: 15},
        {position: 'CB2', playing: true, jersey: 12},
        {position: 'CB3', playing: true, jersey: 12},
        {position: 'S', playing: true, jersey: 12},
        {position: 'S', playing: true, jersey: 12},
        {position: 'LB', playing: true, jersey: 12},
        {position: 'LB', playing: true, jersey: 12},
        {position: 'DE', playing: true, jersey: 12},
        {position: 'DT', playing: true, jersey: 12},
        {position: 'DE', playing: true, jersey: 12},
        {position: 'LB', playing: true, jersey: 12}
      ],
      jerseyNum: true,
      position: true,
      QBView: true,
      ballTrack: true,
      offPlay: true,
      defPlay: true
    }
  },
  watch: {
    showDefense: {
      handler (val) {
        this.$store.commit('defenseHandler', val)
        if (val === false) {
          this.defenseOff()
        } else {
          this.defenseOn()
        }
      },
      deep: true
    },
    showOffense: {
      handler (val) {
        this.$store.commit('offenseHandler', val)
        if (val === false) {
          this.offenseOff()
        } else {
          this.offenseOn()
        }
      },
      deep: true
    },
    jerseyNum: {
      handler (val) {

      },
      deep: true
    }
  },
  methods: {
    defenseOff () {
      console.log(this.trackingData.teamroster.offense[0].jersey)
      for (let i of this.defense) {
        i.playing = false
      }
    },
    defenseOn () {
      for (let i of this.defense) {
        i.playing = true
      }
    },
    offenseOff () {
      for (let i of this.offense) {
        i.playing = false
      }
    },
    offenseOn () {
      for (let i of this.offense) {
        i.playing = true
      }
    }
  }
}
</script>

<style scoped>

table.table tbody td:first-child, table.table tbody td:not(:first-child), table.table tbody th:first-child, table.table tbody th:not(:first-child), table.table thead td:first-child, table.table thead td:not(:first-child), table.table thead th:first-child, table.table thead th:not(:first-child){
    padding: 0;
    width: 30%;
}

div .input-group__details {
    min-height: 0px;
}

.player-toggle-title {
    font-size: 1.2em;
    padding-right: 3em;
}

</style>
