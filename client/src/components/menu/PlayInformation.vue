<template>
<div>

</div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  components: {

  },
  computed: {
    ...mapGetters({
      sliderTime: 'sliderTime',
      btnState: 'btnState',
      trackingData: 'trackingData',
      maxTime: 'maxTime'
    })
  },
  methods: {
  }
}
</script>

<style>

</style>
