<template>
    <v-data-table
      :headers="headers"
      :items="defense"
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
      defense: []
    }
  },
  methods: {
    setPlayers () {
      for (let i = 0; i < this.trackingData.teamroster.defense.length; i++) {
        this.defense.push({
          value: false,
          position: this.trackingData.teamroster.defense[i].position.name,
          number: this.trackingData.teamroster.defense[i].jersey,
          name: this.trackingData.teamroster.defense[i].firstname + ' ' + this.trackingData.teamroster.defense[i].lastname
        })
      }
    }
  },
  mounted () {
    this.setPlayers()
  }
}
</script>
