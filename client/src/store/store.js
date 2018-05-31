import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    currentPage: 'Splash',
    playChanger: false,
    jsonData: null,
    trackingData: false,
    sliderTime: 0,
    btnState: false,
    maxTime: 0,
    sessionStats: null,
    routeData: null,
    releaseData: null,
    displayOptions: null
  },

  getters: {
    sliderTime (state) {
      return state.sliderTime
    },
    btnState (state) {
      return state.btnState
    },
    trackingData (state) {
      return state.trackingData
    },
    jsonData (state) {
      return state.jsonData
    },
    maxTime (state) {
      return state.maxTime
    },
    currentPage (state) {
      return state.currentPage
    },
    playChanger (state) {
      return state.playChanger
    },
    sessionStats (state) {
      return state.sessionStats
    },
    routeData (state) {
      return state.routeData
    },
    releaseData (state) {
      return state.releaseData
    },
    displayOptions (state) {
      return state.displayOptions
    }
  },
  mutations: {
    // From Timeline
    clickHandler (state) {
      state.btnState = !state.btnState
    },
    sliderValFromInput (state, input) {
      state.sliderTime = input
    },
    // From Menu
    settingJson (state, data) {
      state.jsonData = data
    },
    setMaxTime (state, framesLength) {
      state.maxTime = framesLength
    },
    setSessionStats (state, stats) {
      state.sessionStats = stats
    },
    setRouteData (state, val) {
      state.routeData = val
    },
    setReleaseData (state, val) {
      state.releaseData = val
    },
    // From Field
    fieldStart (state) {
      state.btnState = false
    },
    endPlay (state) {
      state.btnState = false
    },
    playFunc (state, Timer) {
      state.sliderTime++
    },
    resetTime (state) {
      state.sliderTime = 0
    },
    adjustSlider (state, adjusted) {
      state.sliderTime = adjusted
    },
    updatePlay (state, val) {
      state.trackingData = val
    },
    changeCurrentPage (state, val) {
      state.currentPage = val
    },
    setDisplayOptions (state, val) {
      state.displayOptions = val
    },
    allPlayersOff (state) {
      state.displayOptions.player.off = false
      state.displayOptions.player.def = false
    },
    allPlayersOn (state) {
      state.displayOptions.player.off = true
      state.displayOptions.player.def = true
    }
  }
})
