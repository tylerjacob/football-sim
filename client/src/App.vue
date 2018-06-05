<template>
<div id="app">
  <v-app>
    <Menu id="menu"></Menu>
      <FieldDisplay
      v-if="show & currentPage === 'playAnimation'"/>
      <PlayInformation v-if="show & currentPage === 'playInformation'"/>
      <QBPerformance v-if="show & currentPage === 'QBPerformance'"/>
      <SessionStatistics v-if="show & currentPage === 'SessionStatistics'"/>
      <Splash v-if="trackingData === false"/>
      <!-- <router-view/> -->
  </v-app>
</div>
</template>

<script>
// random comment! 
import FieldDisplay from '@/components/FieldDisplay.vue'
import {mapGetters} from 'vuex'
import Menu from '@/components/menu/Menu.vue'
import PlayInformation from '@/components/menu/PlayInformation.vue'
import QBPerformance from '@/components/menu/QBPerformance.vue'
import SessionStatistics from '@/components/menu/SessionStatistics.vue'
import Splash from '@/components/Splash.vue'

export default {
  name: 'App',
  data () {
    return {
      show: true
    }
  },
  watch: {
    trackingData: {
      handler (val) {
        var self = this
        self.show = false

        this.$nextTick(function () {
          console.log('re-render')
          self.show = true
        })

        console.log('test')
      }
    }
  },
  components: {
    'FieldDisplay': FieldDisplay,
    'Menu': Menu,
    'PlayInformation': PlayInformation,
    'QBPerformance': QBPerformance,
    'SessionStatistics': SessionStatistics,
    'Splash': Splash
  },
  computed: {
    ...mapGetters({
      sliderTime: 'sliderTime',
      btnState: 'btnState',
      trackingData: 'trackingData',
      maxTime: 'maxTime',
      currentPage: 'currentPage'
    })
  },
  methods: {
  }
}
</script>

<style>
#menu {
  position: absolute;
  z-index: 1000000;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  padding: 0px;
  background-color: whitesmoke;
  color: #2c3e50;
}

div.cotainer.fluid {
  padding: 0px;
}

h1.page-title {
  color: white;
  background-color:#2c3e50;
  border-radius:0px 0px 10px 10px;
  margin:0 200px;
}
</style>
