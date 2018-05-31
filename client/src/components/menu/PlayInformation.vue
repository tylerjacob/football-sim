<template>
  <v-container pt-0 mt-0>
    <h1 class="page-title">PLAY INFORMATION</h1>
            <h1>{{trackingData.playsituation.qbteam.abbr + ' ' + trackingData.playsituation.qbteamscore + '  ' + trackingData.playsituation.opponent.abbr + ' ' + trackingData.playsituation.opponentscore + ' | Q' + trackingData.playsituation.quarter +  ' | '+down+' & '+ trackingData.playsituation.distance+ ' | ' + timeRemaining  }}</h1>
    <v-layout row wrap>
      <v-flex xs-4 pa-4>
        <h1>Offense</h1>
        <Offense></Offense>
      </v-flex>
      <v-flex xs-4 pa-4>
        <h1>Defense</h1>
      <Defense></Defense>
    </v-flex>
      <v-flex xs-4 pa-4>
      <h1>Play Detail</h1>
        <Formation></Formation>
      </v-flex>
      <v-flex xs-4 pa-4>
      <h1>Route Detail</h1>
        <routeDetail></routeDetail>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
import Offense from './PItables/Offense.vue'
import Defense from './PItables/Defense.vue'
import Formation from './PItables/Formation.vue'
import RouteDetail from './PItables/routeDetail.vue'

export default {
  data () {
    return {
      down: 1,
      timeRemaining: null
    }
  },
  components: {
    Offense: Offense,
    Defense: Defense,
    Formation: Formation,
    RouteDetail: RouteDetail
  },
  computed: {
    ...mapGetters({
      trackingData: 'trackingData',
      routeData: 'routeData',
      releaseData: 'releaseData'
    })
  },
  methods: {
    minTommss (minutes) {
      var sign = minutes < 0 ? '-' : ''
      var min = Math.floor(Math.abs(minutes))
      var sec = Math.floor((Math.abs(minutes) * 60) % 60)
      return sign + (min < 10 ? '0' : '') + min + ':' + (sec < 10 ? '0' : '') + sec
    }
  },
  mounted () {
    this.timeRemaining = this.minTommss(this.trackingData.playsituation.clock / 60)
    console.log(this.trackingData.playsituation.clock, 'CLOCK')
    if (this.trackingData.playsituation.down === 1) {
      this.down = '1st'
    }
    if (this.trackingData.playsituation.down === 2) {
      this.down = '2nd'
    }
    if (this.trackingData.playsituation.down === 3) {
      this.down = '3rd'
    }
    if (this.trackingData.playsituation.down === 4) {
      this.down = '4th'
    }
    console.log(this.routeData, this.releaseData, 'FROM PLAYINFO')
  }
}
</script>

<style scoped>

</style>
