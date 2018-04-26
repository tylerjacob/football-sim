<template>
  <div>
    <v-list id="menu">
      <input type="file" class="pl-4 pt-4" @change="loadTextFromFile" id="selectFiles"/>
      <br>
      <v-btn id="import">Import</v-btn>
      <v-card>
        <template slot="items">
        </template>
      </v-card>
      </v-list>
  </div>
</template>

<script>
export default {
  data: {},
  methods: {
    loadTextFromFile (ev) {
      const file = ev.target.files[0]
      const reader = new FileReader()
      reader.onload = e => this.$emit('load', e.target.result)
      console.log(reader.readAsText(file))
    }
  },
  drawer: null,
  items: [
    { title: 'Home', icon: 'dashboard' },
    { title: 'About', icon: 'question_answer' }
  ]
}


</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .play-btn {
    margin-left: 10px;
    font-family:  monospace
  }

  #menu {
    position: relative;
    z-index: 25;
  }
</style>
