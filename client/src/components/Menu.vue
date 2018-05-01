<template>
  <div>
    <v-list id="menu">
      <input type="file" class="pl-4 pt-3" @change="loadTextFromFile" id="selectFiles"/>
      <br>
      <v-btn id="import">Import</v-btn>
      <textarea id="result"></textarea>
      <v-card>
        <template slot="items">
        </template>
      </v-card>
      </v-list>
  </div>
</template>

<script>
export default {
  data: {
  },
  methods: {
    loadTextFromFile: () => {
	  var files = document.getElementById('selectFiles').files;
    if (files.length <= 0) {
      return false;
    }
    var fr = new FileReader()
    fr.readAsText(files.item(0))
    document.getElementById('import').addEventListener('click', function(){
      var jsonFile = JSON.parse(fr.result)
      console.log(jsonFile)
      return jsonFile
    })
    return jsonFile
  }
  
},
  drawer: null
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
