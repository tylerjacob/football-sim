
<template>
<v-container
  id='contain'
  fluid>
</v-container>
</template>

<script>
import Plotly from 'plotly.js'
export default {
  created () {
  },
  mounted () {

  var d3 = Plotly.d3;
  var WIDTH_IN_PERCENT_OF_PARENT = 100
  var HEIGHT_IN_PERCET_OF_PARENT = 100
  var gd3 = d3.select('#contain')
  .append('div')
  .style({
    width: WIDTH_IN_PERCENT_OF_PARENT + '%',
    'margin':0,
    height: HEIGHT_IN_PERCET_OF_PARENT + 'vh',
    'padding': 0
  })

  var gd = gd3.node();

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

    // Field Set Up
    var outerfieldlines =  {
      x: [-26.6, -26.6,26.6, 26.6, -26.6],
      y: [60,-60, -60, 60, 60],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 5
  },
      name: 'outer field line',
      size: 24
    }

    var yd0 = {
      x: [-26.6, 26.6],
      y: [50, 50],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 5
  },
      name: '0 yd',
      size: 14
    }

    var yd10 = {
      x: [-26.6, 26.6, 26.6, -26.6],
      y: [45, 45, 40, 40],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 2.5
  },
      name: ' 10yd',
      size: 14
    }

    var yd20 = {
      x: [-26.6, 26.6, 26.6, -26.6],
      y: [35, 35, 30, 30],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 2.5
  },
      name: '20yd',
      size: 14
    }

    var yd30 = {
      x: [-26.6, 26.6, 26.6, -26.6],
      y: [25, 25, 20, 20],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 2.5
  },
      name: '30yd',
      size: 14
    }

    var yd40 = {
      x: [-26.6, 26.6, 26.6, -26.6],
      y: [15, 15, 10, 10],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 2.5
  },
      name: '40yd',
      size: 14
    }

    var yd50 = {
      x: [-26.6, 26.6, 26.6, -26.6, -26.6, 26.6],
      y: [5, 5, 0, 0, -5, -5],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 2.5
  },
      name: '50yd',
      size: 14
    }

    var ydneg40 = {
      x: [-26.6, 26.6, 26.6, -26.6],
      y: [-15, -15, -10, -10],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 2.5
  },
      name: '-40yd',
      size: 14
    }

    var ydneg30 = {
      x: [-26.6, 26.6, 26.6, -26.6],
      y: [-25, -25, -20, -20],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 2.5
  },
      name: '-30yd',
      size: 14
    }

    var ydneg20 = {
      x: [-26.6, 26.6, 26.6, -26.6],
      y: [-35, -35, -30, -30],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 2.5
  },
      name: '-20yd',
      size: 14
    }

    var ydneg10 = {
      x: [-26.6, 26.6, 26.6, -26.6],
      y: [-45, -45, -40, -40],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 2.5
  },
      name: '-10yd',
      size: 14
    }

    var ydneg0 = {
      x: [26.6, -26.6],
      y: [-50, -50],
      mode: 'lines',
      type: 'scatter',
      line: {
    color: '#ffffff',
    width: 5
  },
      name: '0yd',
      size: 14
    }

    var offense = {
      mode: 'markers+text',
      type: 'scatter',
      name: 'Offense',
      x: [-16.48365286891222, -8.476765285068534, 6.025499336541266, 8.021701381598135, 16.473670352143483, -3.977517089530475, -1.9387129192184311, 0.02955567585301838, 1.9969091353164188, 4.006258705161855],
      y: [-15.80208739063867, -16.70911716243803, -16.02683391294838, -16.777435061242343, -15.796637569262174, -15.790363178040245, -15.790842435841354, -15.445097145669292, -15.80274775809274, -15.783139169582967],
      marker: {
        color: 'red',
        size: 20
      }
    }
    var defense = {
      mode: 'markers+text',
      type: 'scatter',
      name: 'Defense',
      x: [-16.516536027267424, -8.486742680081656, 16.483841546369202, 2.0343309930008746, 10.02027278725576, 4.993783592155148, -4.950831477836104, -1.9301856408573927, -0.0295557487605716, 2.00503976013415, 3.0055593175853024],
      y: [-13.993418493000876, -9.128881831437738, -14.004081846019247, -0.06866352070574509, -9.138397769028872, -11.0695517133275, -14.058875539515894, -14.315508876494604, -13.224703484981044, -14.38542341426072, -14.01040696631671],
      marker: {
        color: 'blue',
        size: 20
      }
    }

    // far left hash function
    const masterShapeHolder = []
    let HashMachine = () => {
    var cnt = 0
    for(var i =0; i < 101; i++){
      console.log("does this even run?")
        masterShapeHolder.push({
          type: 'rect',
          xref: 'x',
          x0: -26.5,
          x1: -26,
          yref: 'y',
          y0: -50 + cnt,
          y1: -50.1 + cnt,
          fillcolor: '#ffffff',
          line: {
            color: "#ffffff"
          }
        },
        {
          type: 'rect',
          xref: 'x',
          x0: 26.5,
          x1: 26,
          yref: 'y',
          y0: -50 + cnt,
          y1: -50.1 + cnt,
          fillcolor: '#ffffff',
          line: {
            color: "#ffffff"
          }
        },
        {
          type: 'rect',
          xref: 'x',
          x0: 2.5,
          x1: 2,
          yref: 'y',
          y0: -50 + cnt,
          y1: -50.1 + cnt,
          fillcolor: '#ffffff',
          line: {
            color: "#ffffff"
          }
        },
        {
          type: 'rect',
          xref: 'x',
          x0: -2.5,
          x1: -2,
          yref: 'y',
          y0: -50 + cnt,
          y1: -50.1 + cnt,
          fillcolor: '#ffffff',
          line: {
            color: "#ffffff"
          }
        }
        )
        cnt += 1
      }
    }

    HashMachine()
    var layout = {
    shapes: masterShapeHolder,
    paper_bgcolor: 'rgb(33, 132, 39)',
    plot_bgcolor: 'rgba(0,0,0,0)',
      xaxis: {
        range: [-26.6, 26.6],
        showgrid: false,
        zeroline: false,
        ticks: '',
        showline: true,
        autotick: true,
        showticklabels: false
      },
      yaxis: {
        range: [-60, 60],
        showgrid: true,
        zeroline: false,
        ticks: '',
        showline: true,
        autotick: true,
        showticklabels: false,
        scaleanchor: 'x',
        scaleratio: .5
      },
      margin: {
          t: 0, //top margin
          l: 0, //left margin
          r: 0, //right margin
          b: 0 //bottom margin
      },
      showlegend: false,
      images: 
        [{
          x: -26.6,
          y: 60,
          sizex: 53.33,
          sizey: 120,
          source : "",
          sizing: 'stretch',
          xref: 'x',
          yref: 'y',
          layer: 'below'
        }]
    }
    var data = [ 
    outerfieldlines,
    yd0, yd10, yd20, yd30, yd40, yd50, ydneg40, ydneg30, ydneg20, ydneg10, ydneg0,
    offense, defense, qb, ball
    ]
    Plotly.plot(
      gd, data, layout
    )
    window.onresize = function () {
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
svg.main-svg {
  background-image: url('field-v.png')
}
.plot {
  height: 100%;
}

#contain {
  padding-top: 200px;
  margin: 0px;
}
</style>
