<template>
  <v-container pt-0 dark id="container">
    <h1 class="page-title">QB PERFORMANCE</h1>
    <v-layout row wrap>
      <v-flex xs-3 pa-3>
        <h2>Throwing Metrics</h2>
        <v-data-table :headers="throwingMetricHead" :items="qbmetrics" hide-actions class="elevation-2">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.metric }}</td>
            <td class="text-xs-left">{{ props.item.val }}</td>
          </template>
        </v-data-table>
      </v-flex>
      <v-flex xs-3 pa-3>
        <h2>Ball Placement</h2>
        <v-alert class="elevation-2" :value="!ballPlacement" type="info">No image available for this play</v-alert>
        <img v-if="ballPlacement !== null" :src="ballPlacement" alt="ball placement" />
      </v-flex>
      <v-flex xs-3 pa-3>
        <h2>Dropback Detail</h2>
        <v-data-table :headers="dropbackHead" :items="dropbackDetail" hide-actions class="elevation-2">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.metric }}</td>
            <td class="text-xs-left">{{ props.item.val }}</td>
          </template>
        </v-data-table>
      </v-flex>
      <!-- <v-flex>
         <h2>Throwing Motion</h2>
        <img :src="throwingMotion" alt="throwing Motion" />
      </v-flex> -->
    </v-layout>
  </v-container>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  data () {
    return {
      throwingMetricHead: [
        {
          text: 'Metric',
          align: 'center',
          sortable: false,
          value: 'metric'
        },
        { text: 'Value', value: 'val', sortable: false, align: 'left' }
      ],
      qbmetrics: [
        {metric: 'Velocity', val: null},
        {metric: 'Air Yards', val: null},
        {metric: 'Air Distance', val: null},
        {metric: 'Release Height', val: null},
        {metric: 'Release Angle', val: null}
        // { metric: 'Timing', val: null},
        // { metric: 'Ideal Velocity', val: null}
      ],
      dropbackHead: [
        {
          text: 'Metric',
          align: 'center',
          sortable: false,
          value: 'metric'
        },
        { text: 'Value', value: 'val', sortable: false, align: 'left' }
      ],
      dropbackDetail: [
        {metric: 'Dropback', val: null},
        {metric: 'Depth', val: null},
        {metric: 'Time to Throw', val: null},
        {metric: 'Sacked', val: null},
        {metric: 'Sacked Yardage', val: null},
        {metric: 'Intentional Grounding', val: null}
      ],
      ballPlacement: null,
      throwingMotion: null
    }
  },
  computed: {
    ...mapGetters({
      trackingData: 'trackingData',
      currentPage: 'currentPage',
      releaseData: 'releaseData',
      routeData: 'routeData'
    })
  },
  methods: {
    fill () {
      console.log(this.routeData, 'ROUTE DATA')
      console.log(this.releaseData, 'RELEASE DATA')
      // fill qb metrics
      this.qbmetrics[0].val = this.releaseData.Velocity.toFixed(1) + ' yds'
      this.qbmetrics[1].val = this.routeData['Air Yards'].toFixed(1) + ' yds'
      this.qbmetrics[2].val = this.routeData['Air Distance'].toFixed(1) + ' yds'
      this.qbmetrics[3].val = this.releaseData['Release Height'].toFixed(1) + ' in'
      this.qbmetrics[4].val = this.releaseData['Release Angle'].toFixed(1) + ' deg'
      // this.qbmetrics[6].val = null
      // this.qbmetrics[7].val = null
      // fill ball placement image
      this.ballPlacement = this.routeData['Ball Placement Image']

      // fill dropback detail
      let sackVal = 'no'
      let intGround = 'no'
      if (this.releaseData.Sack === true) {
        sackVal = 'yes'
      }
      if (this.routeData['Intentional Grounding'] === true) {
        intGround = 'yes'
      }
      this.dropbackDetail[0].val = this.releaseData['Dropback Type']
      this.dropbackDetail[1].val = this.releaseData['Dropback Depth'].toFixed(1)
      this.dropbackDetail[2].val = this.releaseData['Time to Throw'].toFixed(1)
      this.dropbackDetail[3].val = sackVal
      this.dropbackDetail[4].val = this.releaseData['Sack Yardage']
      this.dropbackDetail[5].val = intGround
    },
    getPic () {

    }
  },
  mounted () {
    this.fill()
  }
}
</script>

<style scoped>

</style>
