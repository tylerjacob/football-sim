<template>
    <v-data-table
      :headers="headers"
      :items="offense"
      hide-actions
      class="elevation-1"
    >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.position }}</td>
        <td class="text-xs-center">{{ props.item.number }}</td>
        <td class="text-xs-center">{{ props.item.name }}</td>
      </template>
    </v-data-table>
</template>

<script>
import { mapGetters } from 'vuex'

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
          text: 'Pos',
          align: 'left',
          sortable: false,
          value: 'position'
        },
        { text: '#', value: 'number', sortable: false, align: 'center' },
        { text: 'Name', value: 'name', sortable: false, align: 'center' }
      ],
      offense: []
    }
  },
  methods: {
    setPlayers () {
      this.offense = []
      for (let i = 0; i < this.trackingData.teamroster.offense.length; i++) {
        this.offense.push({
          value: false,
          position: this.trackingData.teamroster.offense[i].position.name,
          number: this.trackingData.teamroster.offense[i].jersey,
          name: this.trackingData.teamroster.offense[i].firstname + ' ' + this.trackingData.teamroster.offense[i].lastname
        })
      }
    }
  },
  mounted () {
    this.setPlayers()
  }
}
</script>
