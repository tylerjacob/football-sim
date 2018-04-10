<template>
  <div>
    
  </div>
</template>

<script>
export default {
  data () {
    return {
      drawer: null,
        items: [
          { title: 'Home', icon: 'dashboard' },
          { title: 'About', icon: 'question_answer' }
        ],
      component: Menu
    }
  },
  methods: {
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .play-btn {
    margin-left: 10px;
    font-family:  monospace
  }
</style>
