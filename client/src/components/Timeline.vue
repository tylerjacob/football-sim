<template>
  <div id="top-bar" width="100px">
    <v-toolbar fixed height="80px;" color="blue-grey darken-3">
    <v-btn
    menu
    @click.stop="drawer = !drawer"
    class="play-btn"
    color="blue-grey lighten-5">
      <i class="fas fa-align-justify"></i>
    </v-btn>
    <v-btn
    class="play-btn"
    color="blue-grey lighten-5"
    @click.stop="hasClick">
      <i 
      id="play-button"
      class="fas"
      v-bind:class="{'fa-play': hasClick, 'fa-pause': !hasClick}">
      </i>
    </v-btn>
    <v-slider
      dark
      class="px-4 pt-4"
      color="blue-grey lighten-5"
      v-model="value1"
      step="0">
    </v-slider>
  </v-toolbar>
  <v-navigation-drawer
  id="nav-drawer"
  v-model="drawer"
  dark>
    <v-list>
      
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
      <h1>-</h1>
       <OptionsMenu></OptionsMenu>
    </v-list>
  </v-navigation-drawer>
  </div>
</template>

<script>
import OptionsMenu from '@/components/Menu.vue'
export default {
  data () {
    return {
      drawer: null,
      value1: 0,
      hasClick: true,
      components: {
        'OptionsMenu': OptionsMenu
      } 
    }
  },
  methods: {
    hasClick: (click) => {
      this.isLoading = !this.isLoading
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  opacity: 10%;
}
.play-btn {
  font-family:  monospace
}
div.btn__content {
  padding: 0;
}

#timeline {
  padding-left: 0px;
}

#nav-drawer {
  opacity: 70%;
}

#top-bar {
  z-index: 1000;
}

</style>
