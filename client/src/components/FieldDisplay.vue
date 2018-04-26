
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
    // ===================================
    //            Field Set Up
    // ===================================
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

// Creating Hash markers
const masterShapeHolder = []
let HashMachine = () => {
  var cnt = 0
  for(var i =0; i < 101; i++){
    masterShapeHolder.push({
      type: 'rect',
      layer: 'below',
      xref: 'x',
      x0: -26.4,
      x1: -26,
      yref: 'y',
      y0: -50 + cnt,
      y1: -50.05 + cnt,
      fillcolor: '#ffffff',
      line: {
        color: "#ffffff"
      }
    },
    {
      type: 'rect',
      xref: 'x',
      layer: 'below',
      x0: 26.4,
      x1: 26,
      yref: 'y',
      y0: -50 + cnt,
      y1: -50.05 + cnt,
      fillcolor: '#ffffff',
      line: {
        color: "#ffffff"
      }
    },
    {
      type: 'rect',
      xref: 'x',
      layer: 'below',
      x0: 2.4,
      x1: 2,
      yref: 'y',
      y0: -50 + cnt,
      y1: -50.05 + cnt,
      fillcolor: '#ffffff',
      line: {
        color: "#ffffff"
      }
    },
    {
      type: 'rect',
      xref: 'x',
      x0: -2.4,
      x1: -2,
      layer: 'below',
      yref: 'y',
      y0: -50 + cnt,
      y1: -50.05 + cnt,
      fillcolor: '#ffffff',
      line: {
        color: "#ffffff"
      }
    }
    )
    cnt += 1
  }
}
  masterShapeHolder.push({
        type: 'rect',
        xref: 'x',
        x0: 0,
        x1: 0.2,
        yref: 'y',
        layer: 'below',
        y0: 48,
        y1: 47.95,
        fillcolor: '#ffffff',
        line: {
          color: "#ffffff"
        }},{
        type: 'rect',
        xref: 'x',
        x0: 0.2,
        layer: 'below',
        x1: 0,
        yref: 'y',
        y0: -48,
        y1: -47.95,
        fillcolor: '#ffffff',
        line: {
          color: "#ffffff"
        }})
  HashMachine()

  //yardLines
let YardMachine = () => {
  var cnt = 0
  for(var i = 0; i <= 20; i++){
  console.log("does this even run?")
    masterShapeHolder.push({
      type: 'rect',
      layer: 'below',
      xref: 'x',
      x0: -26.6,
      x1: 26.6,
      yref: 'y',
      y0: -50 + cnt,
      y1: -50.05 + cnt,
      fillcolor: '#ffffff',
      line: {
        color: "#ffffff"
      }
    },
    {
      type: 'rect',
      layer: 'below',
      xref: 'x',
      x0: 2,
      x1: 2.05,
      yref: 'y',
      y0: -44.7 + cnt,
      y1: -45.3 + cnt,
      fillcolor: '#ffffff',
      line: {
        color: "#ffffff"
      }
      },
      {
      type: 'rect',
      layer: 'below',
      xref: 'x',
      x0: -2,
      x1: -2.05,
      yref: 'y',
      y0: -44.7 + cnt,
      y1: -45.3 + cnt,
      fillcolor: '#ffffff',
      line: {
        color: "#ffffff"
      }
    })
    cnt += 5
  }
}
YardMachine()

const masterNumHolder = []
let NumMachine = () => {
  var cnt = 0
  var cnt1 = 0
  var fieldNumsR = ["http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/1_left.png", "http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/2_left.png", "http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/3_left.png", "http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/4_left.png", "http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/5_left.png"]
  var fieldNumsL = ["http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/1_right.png","http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/2_right.png","http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/3_right.png","http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/4_right.png","http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/5_right.png"]
  for(var i = 0; i < 9; i++){
  console.log("does this even run?")
    masterNumHolder.push({
        layer: 'above',
        x: 12,
        y: -37.6 + cnt,
        sizex: 2,
        sizey: 2,
        source : "http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/0_left.png",
        sizing: 'stretch',
        xref: 'x',
        yref: 'y'
      },
      {
        layer: 'above',
        x: -14,
        y: -40.4 + cnt,
        sizex: 2,
        sizey: 2,
        source : "http://ec2-13-58-111-5.us-east-2.compute.amazonaws.com:3838/vts-formations/0_left.png",
        sizing: 'stretch',
        xref: 'x',
        yref: 'y'
      },{
        layer: 'below',
        x: 12,
        y: -40.4 + cnt,
        sizex: 2,
        sizey: 2,
        source : fieldNumsR[cnt1],
        sizing: 'stretch',
        xref: 'x',
        yref: 'y'
      },
      {
        layer: 'below',
        x: -14,
        y: -37.6 + cnt,
        sizex: 2,
        sizey: 2,
        source : fieldNumsL[cnt1],
        sizing: 'stretch',
        xref: 'x',
        yref: 'y'
      })
    cnt += 10
    cnt1++
    if(cnt1 > 4){
      fieldNumsL.reverse()
      fieldNumsR.reverse()
      cnt1 = 1
    }
  }
}
NumMachine()
  // Layout
  var layout = {
  paper_bgcolor: '#005b24',
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
      showgrid: false,
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
    images: masterNumHolder,
    shapes: masterShapeHolder
  }
  var data = [ 
  outerfieldlines,
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
  margin-top: 80px;
  padding: 0px;
  width: 100%;
}
</style>
