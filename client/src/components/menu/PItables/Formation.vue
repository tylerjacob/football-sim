<template>
<div>
  <v-data-table
    :headers="headers"
    :items="offplay"
    hide-actions
    class="elevation-1"
  >
    <template slot="items" slot-scope="props">
      <td>{{ props.item.detail }}</td>
      <td class="text-xs-left">{{ props.item.val }}</td>
    </template>
  </v-data-table>
</div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
  computed: {
    ...mapGetters({
      trackingData: 'trackingData',
      currentPage: 'currentPage'
    })
  },
  data () {
    return {
		  headers: [
        {
			  text: 'Off Detail',
			  align: 'left',
			  sortable: false,
			  value: 'detail'
        },
        { text: 'Off Value', value: 'val', sortable: false, align: 'left' },
        {
			  text: 'Def Detail',
			  align: 'left',
			  sortable: false,
			  value: 'detail'
        },
        { text: 'Off Value', value: 'val', sortable: false, align: 'left' }
		  ],
		  offplay: [
        {
			  value: false,
			  detail: 'Formation',
			  val: null
        },
        {
			  value: false,
			  detail: 'Play',
			  val: null
        },
        {
			  value: false,
			  detail: 'Play Type',
			  val: null
        },
        {
			  value: false,
			  detail: 'Offensive Personnel',
			  val: null
        },
        {
			  value: false,
			  detail: 'Offensive Basic',
			  val: null
        }
		  ]
    }
  },
  methods: {
    fill () {
      this.offplay[0].val = this.trackingData.playsituation.offplaycall.formation.name
      this.offplay[1].val = this.trackingData.playsituation.offplaycall.play.name
      this.offplay[2].val = this.trackingData.playresult.playtype
      this.offplay[3].val = this.trackingData.playsituation.offplaycall.personnel.name
    }
  },
  mounted () {
    this.fill()
  }
}
</script>
