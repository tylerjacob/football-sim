
<template>
    <div class="plot" ref="scat"></div>
</template>

<script>
import Plotly from 'plotly.js'
export default {
  created () {
  },
  mounted () {
    var qb = {
      mode: 'markers+text',
      type: 'scatter',
      name: 'QB',
      x: [-0.1361191491688539],
      y: [-16.88973067585302],
      marker: {
          color: 'orange',
          size: 24
      }
    }
    var ball = {
      mode: 'markers+text',
      type: 'scatter',
      name: 'Ball',
      x: [-0.05291853674540683],
      y: [-16.86309654418198],
      marker: {
        color: 'brown',
        size: 16
      }
    }
    var offense = {
      mode: 'markers+text',
      type: 'scatter',
      name: 'Offense',
      x: [-16.48365286891222, -8.476765285068534, 6.025499336541266, 8.021701381598135, 16.473670352143483, -3.977517089530475, -1.9387129192184311, 0.02955567585301838, 1.9969091353164188, 4.006258705161855],
      y: [-15.80208739063867, -16.70911716243803, -16.02683391294838, -16.777435061242343, -15.796637569262174, -15.790363178040245, -15.790842435841354, -15.445097145669292, -15.80274775809274, -15.783139169582967],
      marker: {
        color: 'red',
        size: 24
      }
    }
    var defense = {
      mode: 'markers+text',
      type: 'scatter',
      name: 'Defense',
      x: [-16.516536027267424, -8.486742680081656,16.483841546369202, 2.0343309930008746, 10.02027278725576, 4.993783592155148, -4.950831477836104, -1.9301856408573927, -0.0295557487605716, 2.00503976013415, 3.0055593175853024],
      y: [-13.993418493000876, -9.128881831437738, -14.004081846019247, -0.06866352070574509, -9.138397769028872, -11.0695517133275, -14.058875539515894, -14.315508876494604, -13.224703484981044, -14.38542341426072, -14.01040696631671],
      marker: {
        color: 'blue',
        size: 24
      }
    }
    var layout = {
      xaxis: {
        range: [-26, 26]
      },
      yaxis: {
        range: [-50, 50]
      }
    }
    var data = [offense, defense, qb, ball]
    Plotly.plot(
      this.$refs.scat, data,layout
    )
    window.onresize = function() {
        Plotly.Plots.resize(gd);
    }
  },
  data () {
    return {
    }
  },
  methods: {
    }
  }
</script>

<style scoped>
.svg-container {
  height: 100%;
  width: 100%;
}
.js-plotly-plot {
  max-width: 100%;
}
.plot {
  width: 100%;
  height: 100%;
}
</style>
