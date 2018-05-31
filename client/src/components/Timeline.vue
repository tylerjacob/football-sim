<template>
<div>
  <v-container id="top-bar"
  :style="{'margin-top':90 + 'vh'}">
    <v-layout>
      <v-toolbar
          id="timeline-bar"
          width="85%"
          height="50%"
          color="blue-grey darken-3">
        <v-btn class="menu-btn" color="blue-grey lighten-5" @click.stop="drawer = !drawer">
          <i class="material-icons">menu</i>
        </v-btn>
        <v-btn class="menu-btn" color="blue-grey lighten-5" @click="clickMaster">
          <i class="material-icons">{{btnState ? 'pause' : 'play_arrow'}}</i>
        </v-btn>
        <v-flex xs-10>
        <vueSlider
        id="slider"
        :realTime='true'
        :tooltip='false'
        :max="maxTime"
        @input='changeCurrentValue'
        v-model="sliderDisplay">
        </vueSlider>
        </v-flex>
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
    </v-layout>
  </v-container>
  <div id="nav-bar">
    <v-navigation-drawer
    :style="[{'margin-top':25 + '%'},{'opacity':.75}]"
    v-model="drawer"
    dark
    id="play-options"
    absolute
    height="14vh">
    <AnimationOptions/>
    </v-navigation-drawer>
  </div>
  </div>

</template>
<script>
import { mapGetters } from 'vuex'
import vueSlider from 'vue-slider-component'
import AnimationOptions from '../components/AnimationOptions'

export default {
  components: {
    'vueSlider': vueSlider,
    'AnimationOptions': AnimationOptions
  },
  watch: {
    btnState: {
      handler (val) {
        if (val === true) {
          if (this.sliderDisplay === this.maxTime) {
            this.sliderDisplay = 0
            this.slideTimer = null
          }
          if (this.maxTime !== 0) {
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
      handler (val) {
        if (val === this.maxTime) {
          // this.sliderDisplay = 0
          clearInterval(this.slideTimer)
          this.$store.commit('endPlay')
        }
      },
      deep: true
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
  data () {
    return {
      drawer: false,
      playBtn: false,
      pauseBtn: true,
      sliderDisplay: 0,
      slideTimer: 0
    }
  },
  methods: {
    sliderClick () {
      this.$store.commit('endPlay')
    },
    displayRunner () {
      this.slideTimer = setInterval(() => { this.sliderDisplay += 1 }, 15)
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

#top-bar {
  height: 0;
  padding: 0;
}

#play-options {
  position: absolute;
  padding: 0;
}

#nav-bar {
  background-color: rgba(0, 0, 0, 0);
  outline: none;
}

#menu-options{
  background-color: rgba(20, 21, 22, 0.0);
}

</style>
