<template>
<div id="timeline">
  <div id="top-bar" width="100px">
    <v-toolbar
    class="timelineBar"
    absolute
    height="80px;"
     color="blue-grey darken-3">
    <v-btn
    @click.stop="drawer = !drawer"
    color="blue-grey lighten-5">
      <i class="material-icons">menu</i>
    </v-btn>
    <v-btn
    class="menu-btn"
    color="blue-grey lighten-5"
    @click="clickMaster"
    >
     <i class="material-icons">{{btnState ? 'pause' : 'play_arrow'}}</i>
    </v-btn>
    <v-slider
      v-on:click="sliderClick"
      v-model="sliderDisplay"
      @input="changeCurrentValue"
      :max="maxTime"
      dark
      id="slider-bar"
      class="px-4 pt-4"
      color="blue-grey lighten-5">
    </v-slider>
    <v-flex xs1>
      <v-text-field
      :max="maxTime"
      @input='changeCurrentValue'
      color='blue-grey lighten-5'
      :value='sliderDisplay'
      type='number'
      :suffix='maxTime.toString()'></v-text-field>
    </v-flex>
  </v-toolbar>
  </div>
  <div>
    <v-navigation-drawer
    id= 'nav-bar'
    v-model="drawer"
    max-height=700
    dark
    absolute
    xs-2>
      <Menu pt-5 id='menu-options'></Menu>
    </v-navigation-drawer>
  </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
import Menu from '@/components/Menu.vue'

export default {
  watch: {
    btnState: {
      handler (val) {
        if (val === true) {
          if(this.sliderDisplay === this.maxTime){
            this.sliderDisplay = 0
            this.slideTimer = null
          }
          if(this.maxTime !== 0){
            this.displayRunner()
          }
        } else if (val === false) {
          clearInterval(this.slideTimer)
          // if(this.sliderDisplay === this.maxTime){
          //   this.sliderDisplay = 0
          // }
        }
      },
      deep: true
    },
    sliderDisplay: {
      handler(val){
        if(val === this.maxTime){
          // this.sliderDisplay = 0
          clearInterval(this.slideTimer)
          this.$store.commit('endPlay')
        }
      }
    }
  },
  computed: {
    ...mapGetters({
      sliderTime: 'sliderTime',
      btnState: 'btnState',
      trackingData: 'trackingData',
      maxTime: 'maxTime'
    })
  },
  components: {
    Menu: Menu
  },
  data () {
    return {
      drawer: null,
      playBtn: false,
      pauseBtn: true,
      sliderDisplay: 0,
      slideTimer: 0
    }
  },
  methods: {
    sliderClick(){
      this.$store.commit("endPlay")
    },
    displayRunner () {
      this.slideTimer = setInterval(() => this.sliderDisplay+=2, 85)
    },
    clickMaster () {
      this.playBtn = !this.playBtn
      this.pauseBtn = !this.pauseBtn
      this.$store.commit('clickHandler')
    },
    changeCurrentValue (e) {
      this.sliderDisplay = e
      this.$store.commit('sliderValFromInput', e)
    },
    labelMaker () {
      return this.maxTime.toString()
    }
  },
  compClasses () {
    return {
      playClass: this.playBtn,
      pauseClass: this.PauseBtn
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  opacity: 10%;
}
.menu-btn {
  font-family: monospace;
}
div.btn__content {
  padding: 0;
}

.navigation-drawer--absolute {
  z-index: -3;
  padding-top: 6em;
}

.navigation-drawer__border {
  width: 0px;
}

.timelineBar {
  top: 98%;
  width: 95%;
}


#timeline {
  z-index: 10;
  width: 0px;
  height: 0px;
}

#nav-bar {
  background-color: rgba(0, 0, 0, 0);
  width: 600px;
  outline: none;
}
#top-bar {
  z-index: 1000;
}
#menu-options{
  background-color: rgba(20, 21, 22, 0.0);
}

</style>
