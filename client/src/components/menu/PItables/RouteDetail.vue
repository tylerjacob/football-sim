<template>
    <v-data-table
      :headers="headers"
      :items="routes"
      hide-actions
      class="elevation-1"
    >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.num }}</td>
        <td class="text-xs-left">{{ props.item.rec }}</td>
        <td class="text-xs-left">{{ props.item.rte }}</td>
        <td class="text-xs-center">{{ props.item.depth }}</td>
        <td class="text-xs-center">{{ props.item.maxsep }}</td>
        <td class="text-xs-center">{{ props.item.avgsep }}</td>
        <td class="text-xs-center">{{ props.item.targeted }}</td>
      </template>
    </v-data-table>
</template>

<script>
export default {
  data () {
    return {
      headers: [
        {
          text: '#',
          align: 'left',
          sortable: false,
          value: 'num'
        },
        { text: 'Receiver', value: 'rec', sortable: false, align: 'left' },
        { text: 'Route', value: 'rte', sortable: false, align: 'left' },
        { text: 'Depth', value: 'depth', sortable: false, align: 'center' },
        { text: 'Max Separation', value: 'maxsep', sortable: false, align: 'center' },
        { text: 'Avg Separation', value: 'avgsep', sortable: false, align: 'center' },
        { text: 'Targeted', value: 'targeted', sortable: false, align: 'center' }
      ],
      routes: [
        {
          value: false,
          num: 15,
          rec: 'Chris Hogan',
          rte: 'Hitch',
          depth: 10,
          maxsep: 5.35,
          avgsep: 3.02,
          targeted: 0
        },
        {
          value: false,
          num: 28,
          rec: 'James White',
          rte: 'Corner',
          depth: 10,
          maxsep: 5.35,
          avgsep: 3.02,
          targeted: 1
        }
      ]
    }
  }
}
