<template>
    <v-container width="50px">
     <v-flex offset-xs1 >
    <v-layout row>
            <v-switch color='green' label="Offense" v-model="displayOptions.player.off"></v-switch>
            <v-switch color='green' label="Defense" v-model="displayOptions.player.def"></v-switch>
     </v-layout>
     </v-flex>
     <v-divider></v-divider>
     <v-flex offset-xs1>
     <v-layout row>
       <v-radio-group row v-model="displayOptions.player.jersOrPos" :mandatory="true">
         <v-radio
        label="Jersey"
        value="jersey"
        color="green"
      ></v-radio>
      <v-radio
        label="Position"
        color="green"
        value="position"
      ></v-radio>
       </v-radio-group>
      </v-layout>
     </v-flex>
    <!-- <v-divider></v-divider>
    <v-flex offset-xs1 pt-3>
    <v-layout row>
      <v-switch color='green' label="QB View" v-model="displayOptions.field.qbView"></v-switch>
      <v-switch color='green' label="Ball Track" v-model="displayOptions.field.ballTrack" ></v-switch>
     </v-layout>
     <v-layout row pb-1>
      <v-switch color='green' label="Off Play" v-model="displayOptions.field.offPlay" ></v-switch>
      <v-switch color='green' label="Def Play" v-model="displayOptions.field.defPlay" ></v-switch>
     </v-layout>
     </v-flex> -->
  </v-container>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  computed: {
    ...mapGetters({
      trackingData: 'trackingData'
    })
  },
  data () {
    return {
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
      displayOptions: {
        player: {
          off: true,
          def: true,
          jersOrPos: null
        },
        field: {
          qbView: false,
          ballTrack: false,
          offPlay: false,
          defPlay: false
        }
      }
    }
  },
  watch: {
    displayOptions: {
      handler (val) {
        this.$store.commit('setDisplayOptions', val)
      },
      deep: true
    }
  },
  methods: {

  },
  mounted () {
    let val = this.displayOptions
    this.$store.commit('setDisplayOptions', val)
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

.input-group.input-group--selection-controls .input-group__input {
  padding-bottom: 50px;
}

</style>
