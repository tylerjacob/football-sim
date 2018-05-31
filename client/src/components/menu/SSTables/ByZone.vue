<template>
    <v-data-table :headers="headers" :items="zones" hide-actions class="elevation-2">
      <template slot="items" slot-scope="props">
        <td class="text-xs-left">{{ props.item.name }}</td>
        <td class="text-xs-center">{{ props.item.run }}</td>
        <td class="text-xs-center">{{ props.item.targeted }}</td>
        <td class="text-xs-center">{{ props.item.complete }}</td>
        <td class="text-xs-center">{{ props.item.td }}</td>
        <td class="text-xs-center">{{ props.item.int }}</td>
        <td class="text-xs-center">{{ props.item.firstdown }}</td>
        <td class="text-xs-center">{{ props.item.yds }}</td>
      </template>
    </v-data-table>
</template>

<script>
export default {
  data () {
    return {
      headers: [
        { text: 'Zone', value: 'name', sortable: false, align: 'left' },
        { text: 'Run', value: 'run', sortable: false, align: 'center' },
        { text: 'Targeted', value: 'targeted', sortable: false, align: 'center' },
        { text: 'Complete', value: 'complete', sortable: false, align: 'center' },
        { text: 'TD', value: 'td', sortable: false, align: 'center' },
        { text: 'INT', value: 'int', sortable: false, align: 'center' },
        { text: '1D', value: 'firstdown', sortable: false, align: 'center' },
        { text: 'Yards', value: 'yds', sortable: false, align: 'center' }
      ],
      zones: [
        {
          value: false,
          name: 'Deep Left',
          run: 6,
          targeted: 1,
          complete: 0,
          td: 0,
          int: 0,
          firstdown: 0,
          yds: 0
        }
      ]
    }
  }
}
</script>
