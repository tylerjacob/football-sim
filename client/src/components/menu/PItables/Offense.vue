<template>
    <v-data-table
      :headers="headers"
      :items="offense"
      hide-actions
      class="elevation-2"
    >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.position }}</td>
        <td class="text-xs">{{ props.item.number }}</td>
        <td class="text-xs">{{ props.item.name }}</td>
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
          align: 'center',
          value: 'position'
        },
        { text: '#', value: 'number', align: 'center' },
        { text: 'Name', value: 'name', align: 'center' }
      ],
      offense: [{
        position: 'QB',
        number: '00',
        name: 'Andy McCarthy'
      }]
    }
  },
  methods: {
    setPlayers () {
      for (let i = 0; i < this.trackingData.teamroster.offense.length; i++) {
        this.offense.push({
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
