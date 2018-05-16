import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    currentPage: null,
    trackingData: false,
    sliderTime: 0,
    btnState: false,
    maxTime: 0
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
    maxTime (state) {
      return state.maxTime
    },
    currentPage(state){
      return state.currentPage
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
    settingJson (state, jsonData) {
      state.trackingData = jsonData
    },
    setMaxTime (state, framesLength) {
      state.maxTime = framesLength
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
    resetTime(state){
      state.sliderTime = 0
    },
    adjustSlider(state, adjusted){
      state.sliderTime = adjusted
    }
    
  }
})
