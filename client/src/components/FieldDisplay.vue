<template>
  <div id="fieldDisplay">
    <v-content fill-height="true" fluid color="blue">
      <h1>FDSGDFGFDSGFSDGFDSDF</h1>
    </v-content>
  </div>
</template>

<script>
export default {
  name: 'FieldDisplay',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      component: FieldDisplay
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

#fieldDisplay {
  z-index: -2000;
}
</style>
