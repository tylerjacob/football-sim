<template>
<div id="app">
  <v-app>
    <Menu id="menu"></Menu>
      <FieldDisplay
      v-if="trackingData !== false"/>
      <!-- <router-view/> -->
  </v-app>
</div>
</template>

<script>
import FieldDisplay from '@/components/FieldDisplay.vue'
import {mapGetters} from 'vuex'
import Menu from '@/components/menu/Menu.vue'
// import Register from '@/components/Register.vue'

export default {
  name: 'App',
  components: {
    'FieldDisplay': FieldDisplay,
    'Menu': Menu
  },
  computed: {
    ...mapGetters({
      sliderTime: 'sliderTime',
      btnState: 'btnState',
      trackingData: 'trackingData',
      maxTime: 'maxTime'
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
