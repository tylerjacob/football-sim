<template>
<div id="app">
  <v-app>
    <Menu id="menu"></Menu>
      <FieldDisplay
      v-if="show & currentPage === 'playAnimation'"/>
      <PlayInformation v-if=" currentPage === 'playInformation'"/>
      <!-- <router-view/> -->
  </v-app>
</div>
</template>

<script>
import FieldDisplay from '@/components/FieldDisplay.vue'
import {mapGetters} from 'vuex'
import Menu from '@/components/menu/Menu.vue'
import PlayInformation from '@/components/menu/PlayInformation.vue'

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
    'PlayInformation': PlayInformation
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
  color: #2c3e50;
}
div.cotainer.fluid {
  padding: 0px;
}
</style>
