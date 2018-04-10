<template>
<div id="app">
  <v-app>
    <h1>MAIN CONTENT</h1>
    <v-container class="ml-0 pl-0">
      <Timeline></Timeline>
      <FieldDisplay></FieldDisplay>
      <!-- <router-view/> -->
    </v-container>
  </v-app>
</div>
</template>

<script>
import Timeline from '@/components/Timeline.vue'
import OptionsMenu from '@/components/Menu.vue'
import FieldDisplay from '@/components/FieldDisplay.vue'
// import Register from '@/components/Register.vue'
// import Menu from '@/components/Menu.vue'

export default {
  name: 'App',
  components: {
    'Timeline': Timeline,
    'OptionsMenu': OptionsMenu,
    'FieldDisplay': FieldDisplay
  }
}
</script>

<style>
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
