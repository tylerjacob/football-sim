<template>
<div id="app">
  <v-app>
      <Timeline></Timeline>
      <FieldDisplay/>
      <router-view/>
  </v-app>
</div>
</template>

<script>
import Timeline from '@/components/Timeline.vue'
import FieldDisplay from '@/components/FieldDisplay.vue'
// import Register from '@/components/Register.vue'

export default {
  name: 'App',
  components: {
    'Timeline': Timeline,
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
