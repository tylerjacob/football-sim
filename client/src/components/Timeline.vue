<template>
<div id="timeline">
  <div id="top-bar" width="100px">
    <v-toolbar fixed height="80px;" color="blue-grey darken-3">
    <v-btn
    @click.stop="drawer = !drawer"
    color="blue-grey lighten-5">
      <i class="fas fa-align-justify"></i>
    </v-btn>
    <v-btn
    class="menu-btn"
    color="blue-grey lighten-5"
    v-on:click="playClicked = !playClicked">
     <i :class="[ 'fas', {'fa-play': playClicked}, {'fa-pause': playClicked}]"></i>
    </v-btn>
    <v-slider
      dark
      label= "0:02.12  / 0:14.75"
      class="px-4 pt-4"
      color="blue-grey lighten-5"
      v-model="value1"
      step="0">
    </v-slider>
  </v-toolbar>
  </div>
  <div id="nav-bar">
    <v-navigation-drawer
    v-model="drawer"
    dark
    absolute
    height="700px">
      <h1>-</h1>
      <h1></h1>
      <Menu class="pt-5" id="menu-options"></Menu>
    </v-navigation-drawer>
  </div>
  </div>
</template>
<script>
import Menu from '@/components/Menu.vue'

export default {
  props: {currentTime: 0.03,
    totalTime: 0.14},
    components: {
    'Menu': Menu
  },
  data () {
    return {
      drawer: null,
      value1: 12,
      playClicked: true,
      name: 'Menu'
    }
  },
  methods: {
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  opacity: 10%;
}
.menu-btn {
  font-family:  monospace
}
div.btn__content {
  padding: 0;
}

#menu-options {
  position: relative;
  z-index: 100000;
  height: 300px;
  width: 300px;
}
#timeline {
  z-index: 2000;
  width: 0px;
  height: 0px;
}
#nav-bar {
  opacity: .7;
  width: 600px;
}
#top-bar {
  z-index: 1000;
}
</style>
