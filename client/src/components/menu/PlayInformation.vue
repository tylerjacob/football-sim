<template>
<div>
  <v-container>
    <v-layout>
      <v-flex xs-2 justify>
        <h1>{{trackingData.playsituation.qbteam.abbr + ' ' + trackingData.playsituation.qbteamscore + '  ' + trackingData.playsituation.opponent.abbr + ' ' + trackingData.playsituation.opponentscore + ' QTR ' + trackingData.playsituation.quarter + ' 0:00  '  + 'down:'+trackingData.playsituation.down+' & '+ trackingData.playsituation.distance}}</h1>
      </v-flex>
      <v-spacer></v-spacer>
    </v-layout>
    <v-divider></v-divider>
    <v-layout>
      <v-layout>
      <v-flex xs-4 offset-xs2>
        <h1>Offense</h1>
        <Offense></Offense>
      </v-flex>
      <v-flex xs-4 offset-xs2>
        <h1>Defense</h1>
      <Defense></Defense>
    </v-flex>
    </v-layout>
    </v-layout>
    <v-layout mt-5>
      <v-flex xs-4 offset-xs2>
      <h1>Formation/Play Detail</h1>
        <Formation></Formation>
      </v-flex>
    </v-layout>
    <v-layout mt-5>
      <v-flex xs-4 offset-xs2>
      <h1>Route Detail</h1>
        <!-- <routeDetail></routeDetail> -->
      </v-flex>

    </v-layout>

  </v-container>

</div>
</template>

<script>
import { mapGetters } from 'vuex'
import Offense from './PItables/Offense.vue'
import Defense from './PItables/Defense.vue'
import Formation from './PItables/Formation.vue'
import RouteDetail from './PItables/routeDetail.vue'

export default {
  data () {
    return {}
  },
  components: {
    Offense: Offense,
    Defense: Defense,
    Formation: Formation,
    RouteDetail: RouteDetail
  },
  computed: {
    ...mapGetters({
      sliderTime: 'sliderTime',
      btnState: 'btnState',
      trackingData: 'trackingData',
      maxTime: 'maxTime'
    })
  },
  methods: {}
}
</script>

<style scoped>

</style>
