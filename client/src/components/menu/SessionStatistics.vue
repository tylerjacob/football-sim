<template>
<v-container mt-0 pt-0>
  <h1 class="page-title">SESSION STATISTICS</h1>
  <v-layout offset-xs3 v-if="zoneImg === null">
    <v-flex pa-3 xs-9>
      <h1 pt-5>Computing Session Stats</h1>
      <v-progress-linear :indeterminate="true"></v-progress-linear>
    </v-flex>
  </v-layout>
  <v-layout v-if="zoneImg !== null" row wrap>
    <v-flex pa-3 xs-3>
      <h2>Overall</h2>
      <Overall/>
    </v-flex>
    <v-flex pa-3 xs-3>
      <h2>By Route</h2>
      <ByRoute/>
    </v-flex>
    <!-- <v-flex pa-3 xs-3>
      <h2>By Zone</h2>
      <ByZone/>
    </v-flex> -->
    <v-flex pa-3 xs-3>
      <h2>Zone Summary</h2>
      <img :src="zoneImg" alt="">
    </v-flex>
     <v-flex pa-3 xs-3>
      <h2>Target Summary</h2>
      <img :src="targetImg" alt="">
    </v-flex>
  </v-layout>
</v-container>

</template>

<script>
import {mapGetters} from 'vuex'
import ByRoute from './SSTables/ByRoute.vue'
import ByZone from './SSTables/ByZone.vue'
import Overall from './SSTables/Overall.vue'

export default {
  data () {
    return {
      zoneImg: null,
      targetImg: null
    }
  },
  components: {
    'ByRoute': ByRoute,
    'ByZone': ByZone,
    'Overall': Overall
  },
  computed: {
    ...mapGetters({
      sessionStats: 'sessionStats'
    })
  },
  methods: {
    fill () {
      this.zoneImg = this.sessionStats.zoneimage
      this.targetImg = this.sessionStats.targetimage
    }
  },
  mounted () {
    this.fill()
  }
}
</script>

<style scoped>
  #h1 {
    background-color: blue
  }
</style>
