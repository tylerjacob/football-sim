<template>
    <v-data-table :headers="headers" :items="stats" hide-actions class="elevation-2">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.statistic }}</td>
        <td class="text-xs-left">{{ props.item.val }}</td>

      </template>
    </v-data-table>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  data () {
    return {
      headers: [
        {
          text: 'Statistic',
          align: 'center',
          sortable: false,
          value: 'statistic'
        },
        { text: 'Value', value: 'val', sortable: false, align: 'left' }
      ],
      stats: [
        {statistic: 'Completion Percentage', val: null},
        {statistic: 'Yards Per Attempt', val: null},
        {statistic: 'Avg. Air Yards', val: null},
        {statistic: 'Avg. Air Distance', val: null},
        {statistic: 'Avg. Time To Throw', val: null},
        {statistic: 'Sacks', val: null},
        {statistic: 'Intentional Grounding', val: null},
        {statistic: 'Thrown Away', val: null}
      ]
    }
  },
  computed: {
    ...mapGetters({
      trackingData: 'trackingData',
      sessionStats: 'sessionStats'
    })
  },
  methods: {
    fill () {
      this.stats[0].val = this.sessionStats['Completion Percentage'].toFixed(1) + ' %'
      this.stats[1].val = this.sessionStats['Yards Per Attempt'].toFixed(1) + ' yrds'
      this.stats[2].val = this.sessionStats['Average Air Yards'].toFixed(1) + ' yrds'
      this.stats[3].val = this.sessionStats['Average Air Distance'].toFixed(1) + ' yrds'
      this.stats[4].val = this.sessionStats['Average Time to Throw'].toFixed(1) + ' sec'
      this.stats[5].val = this.sessionStats.Sacks
      this.stats[6].val = this.sessionStats['Intentional Grounding']
      this.stats[7].val = this.sessionStats['Thrown Away']
    }
  },
  mounted () {
    this.fill()
  }
}
</script>
