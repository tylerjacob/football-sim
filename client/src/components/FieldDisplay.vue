
<template>
  <v-container
  id='contain'
  fluid>
    <Timeline v-if="trackingData"
    id="timeline"
    ></Timeline>
    <div id="plotter"></div>
  </v-container>
</template>
<script>

/* eslint-disable */
 import {mapGetters} from 'vuex'
import Plotly from 'plotly.js'
import Timeline from '@/components/Timeline.vue'

export default { 
  components: {
    'Timeline': Timeline
  },
  computed: mapGetters({
    sliderTime: 'sliderTime',
    btnState: 'btnState',
    trackingData: 'trackingData',
    maxTime: 'maxTime',
    displayOptions: 'displayOptions',
    routeData: 'routeData'
  }),
  watch: {
    sliderTime:{
      handler (val) {
        // this.sliderState = this.sliderTime
        if(val === this.maxTime){
          clearInterval(this.playLooper)
          this.$store.commit('resetTime')
        } else {
          this.sliderAnimator(val)
        } 
      },
      deep: true
    },
    btnState:{
      handler (val) {
        // check if button is resting(play state is showing)
        if (val === true) {
        //if slider is at end, reset slider when play is pressed
        if(this.sliderState === this.maxTime){
          this.sliderState = 0
        }
        // this.playFunc()
        } 
        else {
        clearInterval(this.playLooper)
        // Plotly.animate('plotter', [], {mode: 'immediate'})
        }
      },
      deep: true
    },
    displayOptions: {
      handler(val){
        this.displayHandler(val)
      },
      deep: true
    }
    },
  data () {
    return {
      masterShapeHolder: [],
      masterNumHolder: [],
      hashWidth: .667,
      hashDistance: 3.08,
      hashHeight: .111,
      traces: [],
      aframes: [1],
      gd: {},
      layout: {},
      playLooper: '',
      sliderState: 0,
      offensePlayersx: [],
      offensePlayersy: [],
      defensePlayersx: [],
      defensePlayersy: [],
      offJersey: [],
      defJersey: []
    }
  },
  methods: {
    playFunc () {
      let self = this
      // this.playLooper = window.setInterval(()=>this.sliderState++, 600)
      },
    sliderAnimator(sliderVal){
      Plotly.animate('plotter', [this.aframes[sliderVal].name],{
        frame: 
            {
              duration: 1,
              redraw: false
              }
        ,
        transition: 
          {
            duration: 1,
          }
        ,
        mode: 'immediate'
      })
      },
    populatePlayers (i, offensePlayersx, offensePlayersy, defensePlayersx, defensePlayersy, offPos, defPos){
      //push vals to aframes
      this.aframes.push({
      data: [
        {mode: 'markers+text',
        name: 'QB',
        x: [this.trackingData['qbtrackingdata'][i]['x']],
        y: [this.trackingData['qbtrackingdata'][i]['y']],
        text: 'QB',
        marker: {
          color: 'cyan',
          label: 'QB',
          size: 24
        }
      },
      {
        mode: 'markers+text',
          name: 'Offense',
          x: offensePlayersx,
          y: offensePlayersy,
          hoverinfo: 'none',
          textfont: {
          color: '#ffffff'
        },
          visible: this.offenseVisible,
          marker: {
            color: 'red',
            size: 24
          }
      },{
        mode: 'markers+text',
        name: 'Defense',
        hoverinfo: 'none',
        x: defensePlayersx,
        y: defensePlayersy,
        textfont: {
          color: '#ffffff'
        },
        visible: this.defenseVisible,
        marker: {
          color: 'blue',
          size: 24,
      }
      },
      {
        mode: 'markers+text',
          name: 'Ball',
          x: [this.trackingData['balltrackingdata'][i]['simulated_ball'].x],
          y: [this.trackingData['balltrackingdata'][i]['simulated_ball'].y],
          marker: {
            color: 'yellow',
            size: 14
          }
      }
      ],
      name: i.toString()
      })
      },
    YardMachine(){
        let yardline = this.trackingData.balltrackingdata["0"].simulated_ball.y
        let firstDown = this.trackingData.balltrackingdata["0"].simulated_ball.y + this.trackingData.playsituation.distance
        this.masterShapeHolder.push({
        // sides
              type: 'rect',
              layer: 'below',
              xref: 'x',
              x0: -26.6,
              x1: -27.6,
              yref: 'y',
              y0: -60,
              y1: 60,
              fillcolor: '#ffffff',
              line: {
                color: "#ffffff"
              }
            },
            {
              type: 'rect',
              layer: 'below',
              xref: 'x',
              x0: 26.6,
              x1: 27.6,
              yref: 'y',
              y0: -60,
              y1: 60,
              fillcolor: '#ffffff',
              line: {
                color: "#ffffff"
              }
            },
            //top&bottom
            {
              type: 'rect',
              layer: 'below',
              xref: 'x',
              x0: -27.6,
              x1: 27.6,
              yref: 'y',
              y0: -60,
              y1: -61,
              fillcolor: '#ffffff',
              line: {
                color: "#ffffff"
              }
            },
            {
              type: 'rect',
              layer: 'below',
              xref: 'x',
              x0: -27.6,
              x1: 27.6,
              yref: 'y',
              y0: 60,
              y1: 61,
              fillcolor: '#ffffff',
              line: {
                color: "#ffffff"
              }
            },
            // first down markers
            {
              type: 'rect',
              layer: 'below',
              xref: 'x',
              x0: -26.6,
              x1: 26.6,
              yref: 'y',
              y0: yardline,
              y1: yardline + this.hashHeight,
              fillcolor: 'rgba(0,40,133,.5)',
              line: {
                color: "rgba(0,40,133,.7)"
              }
            },
            {
              type: 'rect',
              layer: 'below',
              xref: 'x',
              x0: -26.6,
              x1: 26.6,
              yref: 'y',
              y0: firstDown,
              y1: firstDown + this.hashHeight,
              fillcolor: 'rgba(245,236,0,.5)',
              line: {
                color: 'rgba(245,236,0,.5)'
              }
            }
            )
      let cnt = 0
      for(let i = 0; i <= 20; i++){
      console.log("does this even run?")
      this.masterShapeHolder.push({
        type: 'rect',
        layer: 'below',
        xref: 'x',
        x0: -26.6,
        x1: 26.6,
        yref: 'y',
        y0: -50 + cnt,
        y1: -50 - this.hashHeight + cnt,
        fillcolor: '#ffffff',
        line: {
          color: "#ffffff"
        }
      })
      if(i < 18){
        //inner hashes
        this.masterShapeHolder.push({
        type: 'rect',
        layer: 'below',
        xref: 'x',
        x0: this.hashDistance,
        x1: this.hashDistance + .05,
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
        x0: -this.hashDistance,
        x1: -this.hashDistance - .05,
        yref: 'y',
        y0: -44.7 + cnt,
        y1: -45.3 + cnt,
        fillcolor: '#ffffff',
        line: {
          color: "#ffffff"
        }}
        )
      }
      cnt += 5
      }
      },
    HashMachine(){
      let cnt = 0
      let self = this
      for(let i =0; i < 101; i++){
          //side hashes
          //left
          this.masterShapeHolder.push({
            type: 'rect',
            layer: 'below',
            xref: 'x',
            x0: -26 - self.hashWidth,
            x1: -26,
            yref: 'y',
            y0: -50 + cnt,
            y1: -50 - self.hashHeight + cnt,
            fillcolor: '#ffffff',
            line: {
              color: "#ffffff"
            }
          },
            //right
          {
            type: 'rect',
            xref: 'x',
            layer: 'below',
            x0: 26 + self.hashWidth,
            x1: 26,
            yref: 'y',
            y0: -50 + cnt,
            y1: -50 - self.hashHeight + cnt,
            fillcolor: '#ffffff',
            line: {
              color: "#ffffff"
            }
          },
          //middle hashes
          {
            type: 'rect',
            xref: 'x',
            layer: 'below',
            x0: self.hashDistance,
            x1: self.hashDistance + self.hashWidth,
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
            x0:  -self.hashDistance,
            x1: -self.hashDistance - self.hashWidth,
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
        // bottom and top mid hash
      this.masterShapeHolder.push({
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
        layer: 'below',
        x0: 0.2,
        x1: 0,
        yref: 'y',
        y0: -48,
        y1: -47.95,
        fillcolor: '#ffffff',
        line: {
          color: "#ffffff"
            }})
      },
    NumMachine(){
      let cnt = 0
      let cnt1 = 0
      const numberSize = 1.5
      const zero = "data:image/png;base64,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"
      const left1 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAABlCAYAAAARUUIIAAAABHNCSVQICAgIfAhkiAAAAAFzUkdCAK7OHOkAAAAEZ0FNQQAAsY8L/GEFAAAACXBIWXMAAGUBAABlAQGvsJ7JAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAA+ZJREFUeF7t3c+LjVEcx/F5jFmQ32poFhIxfoSEGfKjlCSJshT/BMXCzn9BStmxtbOUjV9pZKFhZyPjR5EiY8b33PONcN17znke957z9X7Vt+/3qXnuncXHcZ773HtnAOi12TCH9Mdrm6MdyM067bURcuSKkMO89dprq2Tvs03njqqqmtARqMVtuHXsZFIyN6pzLS7kIU/oQl7pCNQSmLmvUvMldtP+MB3bFeRqSGq1H+sh5MhZIxefhBw5a+Tik5AjZ4Qc5m3SXgshR86CXt7uhpAjZ0tnZ2dHdE5GyJG72lsWQo7cbdaejJAjdzu0JyPkyF3tkPPeFfRcaObUjNQSid9HfxiPlRy5cxnd4sc0hBwlGNeehJCjBPu0J2FPjp6L3JM7ryV+K3SOxkqOEgzLv4s1Okcj5ChF8paFkKMUe7VHI+QoRfJKzoUnei7hwtNx54xIDF/5w3DBK7n8XvN0BPrBLbKH/RgnZruyRDvQL8e0RyHkKMlh2VEM6hwsJuS1P6EBSEjrLJaLpfb4MVxMyMe0A3Us154qestCyNFrG7SnOq49WEzID8p/NQt1BlLt155qo+Rwo85BYkLu9kNn/AjEk3C6vJ30R7Wc0h5GnjjGcyleL0cSyc6JVorqeykVvkD7c6Jc1lOBYJKbBVKTrQQ1I/xvCukJsc7q6UBXkhf39pHrreQ056Y+fHd6QoqrUgv0YYC2JCODUldcYBr2RWpYn6Yz//PJpqTOSy3ThwN+kFyMST2U+lfO6VN1FPwuxC6+ST2Suivl3iU2JfVJCv8fd7NnldRRqUa+sLODF1KjVVW5r634q6ZCDvTLcQn5LZ3bIuQo3T0J+W6d24q5GQTkaFzW6Y6fGiLksOCC9rbYrsCKMdm2PND5F6zksOKS9j8QclhxRDYlbW/1s12BJU+ktv/+ujkrOSzZKnXajz+xksMad8fd3QX94A9ZyWHPSqmLfvRYyWHRtNROWc0n3AErOSyaK3VN1u8hd0DIYdV2qdaHe9iuwLKvUrsIOax7TMhhHntymEfIYR4hh3mEHOY1deH5WeqNlLvTBOTFhTzRW6kLUmv1oYA8teIa745U2LcXAf3mMxvlqdQiPR3In89tsBmpA3oqUAaf3WA39DSgHBreUMl/+hnoGw1viGd6ClCUmJtBt7UDRYkJ+X3tQFFiQt76vBxQmpiQv9MOFCUm5O+1A0UJfoNWJXQEihKzkgNFIuQwj5DDPEIO8wg5zCPkMI+QwzxCDvMIOcwj5DCPkMM8Qg7zCDnMI+Qwj5DDPEIO8wg5zCPkMI+QwzxCDvMIOcwj5DCPkMM8Qg7zCDmMGxj4DmncF54tWb4WAAAAAElFTkSuQmCC'
      const left2 = 'data:image/png;base64,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'
      const left3 = 'data:image/png;base64,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'
      const left4 = 'data:image/png;base64,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'
      const left5 = 'data:image/png;base64,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'
      const right1 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALkAAABlCAYAAAARUUIIAAAABHNCSVQICAgIfAhkiAAAAAFzUkdCAK7OHOkAAAAEZ0FNQQAAsY8L/GEFAAAACXBIWXMAAGUBAABlAQGvsJ7JAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABDdJREFUeF7t3c2rVVUYx/F7bgpaJigqzRObJRHWRBpJU/8G/4AmCTpy6KCJjYsGUdCgQYOUiAgCUzQ1IujFdCAURBGGFhQRufs9ez1XvNk9+22d41qP3w8899nrcPa5k99ZZ+2Xe+5sBahUI74516p3ICxCjvAIOcIj5AiPkCM8Qo7wCDnCI+QIj5AjPEKO8Ag5wiPkCI+QIzxCjvAIOcIj5AiPkCM8Qo7wCDnCI+QIj5AjPEKO8Ag5wiPkCI+QIzxCjio1TfOob3Yi5KjVDu+dCDlqtdN7J0KOWu333omQo1bPee9EyFGrF713IuSoTtM0B9WeSqNuhBw1esk7EI9m8RdUd1S9+a5A+ZTX7aqv2uQO4LsDZVNW96jOtqkdyF8CKJMy+qTquOqmBXaMmeqGvx5Qkk2qXaot7WgCCznTOULjFCLCI+QIj5AjPEKO8CzkX6RNICYL+RHV3+0ICGh1Npt9qX4iDYF4ZvajaZrNap+pnrExEEkbcqOg258TXVHZlSYgjLtnV3zZciqNgDjuzuRGs/l2te9UT7QPAAGsO0+u2fw3teNpBMSwbiY3ms3Xzp0/3T4AVG7dTG40m99RO5pGQP3uC7lR0D9W+zCNgLrdt1xZo2XLAbVLaQTU639ncqPZ/LLamTQC6rVhyN0r3oFqbbhcWaNly0W159MIqE/XTG5Oegeq1GcmtzeCXQXd2z6wOHZbwQeq71U37QE8dB5T7VbZFXf7vsNnVY+oFk9BP6palCuq3l/Di4eHcrFTdUz1i2o0f7n59Dz79qK/2j3yel21nHcqqqWMbFO9YYEZw1+mm577btolm7dUncslYI3y8nKbnIF892567qG0SxbXVNv8pYHelJvX2gQN4Lt203NXVT+0e0132F8WGETZ2aq63qaopz6nEFt+49abaTTJddXptAkMoxz+qfZqGvXTO+TuHe9TvOdvGGCst1W302a3QSFXOL9Vs5riU+/AKMrh72qfpFG3oTO5ed/7WFe9A1P0vkN2TMin3pnI1UzksNCQX1D1Xg/9lz5qbvkmMMWP3jsNDrlC+o/aR2kEPDC9J8sxM7nhjynwoPUO+ajL6k3T2F1i9nExeH99EnApH1nYhR7fnGvUTK6c/qQ29VQisBRjlyvmnHegaFNCft47UDRmcoQ36SBQ6/6f1fakUT8ceCKXhR543oPZHMUj5AhvasjtX7AARZu6Jn9cza489X6zsCZHLktZkyuvdl8vt86iaFOXK+Zz70CRCDnCyxHyr70DRcoR8m+8A0XKcqZDB7m/qu1Io/k4u4JclnJ25R72jbRAkXKFnCULipUr5Ne8A8Uh5AgvV8jt+w2BIuU6u7JJ7Q/V5vaBOTi7glz6nl3JFjj9Pvu/QvvSaGOEHLkoc/t9czn0C8/YO6uLPx1YmlxrcsPBJ4qUM+QcfKJIhBzBraz8C0fQgAkAsXdPAAAAAElFTkSuQmCC'
      const right2 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAL0AAAB8CAYAAAA8Y7EhAAAABHNCSVQICAgIfAhkiAAAAAFzUkdCAK7OHOkAAAAEZ0FNQQAAsY8L/GEFAAAACXBIWXMAAGUBAABlAQGvsJ7JAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAEgdJREFUeF7tnQnQHEUZhv25T0HBAxAlxSUE8EJMUA6VWy5FKVICQkDAFBLBQLAEUiggWCIaBRUoOQ0oIEdQDgmHEECOCoSA3OEWSEi4Q0IOn7enN9k/+f9sz0z3HDv9VL3VM727c/R8M9vT/fXXPR+IRBZi3rx5p5AcjF5DU206xaatvJamIX32ek9Pz1zSylNLo+eirEDycbQi0vJyaDZ6u01vchFmkEZSQvmeSjIyWXNmDtIN0LoZ2m+YhW+Q1vL0Mm6UShs9hb82ySC0idWn0ZpoVdSJeehl9BR60qaT0J0U9KukkX7IaPRZaN0o7TfGwsutf5hWnv5RdG0zUymjp7BXJvkG2hlthQYg36jAdBOMt7qBQnyeNGIp0OizoH/0vv5RWssttf5RtNzrRind6CngZUn2QPuh7ZCqKkWiwrgHXSlROI8rs8lU3OizoBuldTNMLc3oKdhPkhyODkSrK68iTERno4u4Ad40OQ2jC42+F0vYtDAo0HXROSw+gY5GVTJ4sRn6PXqB4zwLbWpyI11DYUaP8ayOzmTxUaTmsGWUX2H0fvEDNJHjvhHphTrSBQQ3eoxlSfQjFlVXHoaWUn7N2B7dxXmMRZ9NsiJ1JWidHgPZiOQ89CWT0R3oxfdyNJI6/2ST02Vw3VTl/DraBm2L1FRc6ebtNAQ5EQpN2z0SnYyKbo0pinfR8Wg0xq/Wga6F6/kxEhm/bgJJD7Pa3gTeD5wCUl34fPQtk9H9TEDDMPy7k9Xuh2v8UZKvIt0AamZeH9UGr0ZPYWxAcjXS32GTUFf6aWgUxv++yWkQXHdd713RbmhLVOn3Nm9Gz4kPJpHBf8RkNJP/oH0w/GeS1eaBHXyYRD3qugl2RB9ClcKL0XOi+ouTwcv5q+lMR0Mx/KuS1eaCXeiJL3eS76K9kIvPVHByGz0nphecf6LlTUZEqIXndHQsxi+nqsaDnahBQ9WfQ9HXkPf3SVdy7ZgT2YLkJqSX18iiXIeGYPhvJKsRgd2o9eeHaCiS71WhZDZ6DnxDkjuR6nCR/nkE7YbhP52sRlpgQ/K/OgHJ/6ow74BMRs/Bqm6mJjoZfqQzcnHdHcO/K1mNtIM9qelTzdzrmIzApL67OMAlSS5B0eDdUQ/nzZTdvslqpB0eBreRqKnzYZMRmCx/KeqF3ClZjKRAL3IXYvgnotJe4qoKhv8/kh2Q0qCkKnwulu5G3ZV1dBqrEmOQmjVnJquRFtiYWnbGJWthcDZ6DuaDJA+gEEP4mohavfbE8N9JViMtsLW/kuydrPknTfVG3ezR4P2hDr1xXODY+rUoP0fzx7T6xulJz4WRa7CaJwtrVmoQennbmSd+HJzeBjZ3C4k6Pr3T0YjZuervf0TR4MMwEI2nnGNrWG+usKl3XAz5EBRHC4VF8X1ux/A/l6xGQL3ZQVhs9YaLsBKJYsRoEEEkPK+jnajqyFuz8WB/Ctnh/Z2nk9GrTf5nyVqhvIIUjUz1XOkFpAJQmD6NWFKqY1eLkvx+WqlC/cmnX1oP1dEJToa/A4Z/b7LaXLA/tXBp2KJX+jV6drgaifxFZFCheQjJU1OuDfdxwWXkueD4VXWTb4ecm9S/8GWkF/I6uD/LPVmGf1+y2ky4hhpffUCyVgDscBQKyQR0OJJhFgL7WgYNQiPQ9WgmqirTUKNj7nD+6r32jt18b8hfEU0x3/DLLHQR0iir0uE4VkFD0KXoDVQ1XkEKXNtIOPeRphQ8YzffG/KHJx97Yy66AqmuXUk4tmXRLkg35QxUFV5GTRtzbOC8h5kS8Izd/ALI60FPmk/9MAmpTl0bON7V0FHoMVQFnkNq1mwUnPMh5uw901c7vd6W100Wc6E7ajTanBcy9ebWBo73NfRrFvWElbvAZajMKAcy+Ou4Xqskq5E89GX06ozKi2YC2QPDGY7eS7LqB8c+D41Dcn5S1UzRjGfpsxJQz+2VGH7hw+u6jV5GT4FqsINixedB/tDbYihjk9XugPN5BmlQc5nGrwBL5/XzD92NBDnPhTeqqGR5ogk/hwZjHPcnq90H5/asNX5F9foTKtr4h6AzksWuJ0h1bmGj/7ZNs/AS2l5Gkax2N5znc+gwFjdG15rM4jiCp/0RdjmSkvlGTyGqB1Z/n1nQjB3qQWzc1DWc81NI8Vw0V9ZjJrMYzuCa5a2KNpL2J/0uKOswwMO48IUM6q0qnL/cKDSLyU+QXuRDo2t3MYb/hWQ14kq70atpLgvncsEVHaHxUA6zkOZrUlPnpSYzLPKCvRrDl6NdxJF2o8/izaZApcOTxUgLDP9FpBdOVT/kMRqStdBVGH6MI+qIMXoKTE8mFV5aRnBx5eob6QPK5hoS+c6ocysk8h49n+vY/hCL9EOrkLK4CdzCRQ02pKtboIymInVu6ckfcqby76BTksWuwWkMd1paRp/lZeg4m0YcwPBVx5ersCZpDsUxPO27KYpakNDeLaPf3Kau3MNFrJU/TRWgzF5F6gDUpNEhOrX0ZDwXw1dM+Eg/LEEBLU36mWTVmd/YNJIBDF/z6Sq8hTr0fCPfnL9zXQsJhlpH9KT/FErjxKShbLEunxMMXxGMVa283WT4RT5U12D40SuzD2T0GkCdhmu5YGV5GnYVlOPLJGoqlg+Pb/T+oBFhijIdaUNGn9Z3PuSLWOPA8N9H8uHZH/l2w1Z0aY0LqCtBJmlL+6TXQIobksWITzD8i0gUsdd3Z5ac075vlyMgo08zBeaDXJzYGRUIylb1fA2aV8wfn5yJ4euGqhsr2tQrMnrN/uzKPTaNBALDn0yiGD0+Y7Srhe5yDL9uA8zzjO3oFxl9mpB90egLAMOXq7YmINYILV+ofjwWw6/T5NZBJv+Q0aeJFVikv3ijwfD1gqsRWpp9z1esdr2/qQ1fT/46EGSqVhl9mnpTI0ZFVQkMXxMUaMZtXy07X0F/SBabiYzelZlcgOCTYEUWhXLXeAWNd/DlsHYQT/uRdrnKBBsj6xqg9UWbRkoAwx9PMgj5GpJ5Moa/u12uKmkeys5oo649dnI/iJQIhq+WHbmB32Ey8qHr/hcM//PJaiXRNKTekdG7Ru4qM8JXxILhK06/5lu9ymTkQ8MN5aNT1eGGQeYXkNG7DmIuYrBzxAEMX5NSKFzL70xGPjRiTpHTqjiBRbDqjSu+ms0iHsDw5yDFvvHRpKl3hQsw/CAjlXIQ7EVWHSEuVK1AIoDhq0lTzmqzTUZ2NNzwF8liZQhm9NOSxY7EqfErCoZ/MYkiL+StglZmuCHHof6jYNUb+XS7EKR3LOIHDF/BphShLo+XZmu44RbJaqkEm+tMRj81WYzUHQxfE7PJWS1PW75G0SmAlEbUlUlQo3d90qfxxoyUBIb/FIlcDTRTY1bUhCnntCJmluyPoEavQnIhTqBcEzD8KSQahni9ychGa7hhkHq1A8HG9+qENCO4C5qOUgOOIzUAw9dgH7kZaC7WrMi9uaxY+EFi3ggZ/RPJohPxaV8jMHz1oh+EFFQ2KxpuqG0UTbCGExm9pqF3beoqbKLjiB8wfM2bpfDhCjA112Sm5ywMP+vcBVkJV6dXoZBOSFY70tiJfOsO11kBptQGP9NkpEPD9ooebhj0RVbca9NObGTTSA3B8OWXrxlTsnRiaYSdWnSChOXog2Dvj2mNPj7paw6GrwHnatnJMiBFww0vw/CLGG64hk290zJ6hZ5wYSAnHGSEeqQ4MHwN8Fdbfpbhn7phzsYOQvtirWlT7xijpxB08i6tOJrtogpd1JGccM11vdV7+4jJSMcBaFSyGIzgT3pxk007oWi7kS4Aw9cQ0K2RhiKm5QSe9vvZ5RBEo4+EAcNvjcS6zmS403JO824PbFMdU+EHtbCjldEM1Al9p0yfjEgAuKZLI03Bn5ZpyGurHtvb2Gw5EPOf9Nzxb5G4+GposG6ctLfL4Pqr93YoOt1kuKMmzH9gS1km6uuPoGN2e72Bc+CaDGxMsrZYFKNes2TXAs5LLU6abUXuspoZXRdqDnoDaVrQSZxPiFlBagnlpZg4GkWVpoVGL8TbUI65XdXZvzrRFMU5POxsJfQu6sRMlCYcYOFwfMujg9HNyOWcnkCnog3tJhoN5bAfeh+l4V6Uu+rLNkaZrQXC7mYB5Gk+UhcqGSGL41oSHY2m6CAzMAddghrvZ0QZ7IbeRmm4FeV6CeX3Y8yWAmF3swDyBicfdeR5VKlAoBzPOugOHZwH3kIhm+RqAWUwCE1XgaRA7gqZbYPf3me2Egi7m96QPzH5uCP72J+UDseyHnrRHJVfTkOhex8rDee/CXpWhZECRU9rbxJ3Qr9BeuAEw+6qN+QfmnzckYdQ6RN5cQxro2d0QIGo87xNXqAM1kQTTGm4o1g6qeyD729kfhkQu6vekL8cesl8ozMH25+VAvvvQXpZDY2a8xoNZaC+nBtNabijIYfOVR2+u6/5VUDsrhaFz0YkX+mIbo4gcwO5wL4PM0cRHr3QDbC7bSyUQZZOLIUNdJqrmO9pwEpQ7K4Whc90V79mvtWZX9qfFQr7XRWpR7Ao/mZ33WgoB/27nmhKxJ0bUMcoxHxHTcdBsbvqGz4/NvlaR2ajbezPCoN9jjR7L465qG6TlQWDshiKZqlgHFE1tN9BKHy2gflWYOzu+obPV0CuLSKTkUI/FwL7Unu89lk0jX+pbYfy2BG9bkrGjUfR+vbnvSD/FPONwNjd9Q/fSVNnLqbrGNjXVskuC0duC5E2KJNNkfptXFG1WS7N82FdVdVX9GFo7C77h+/oxeUR8203fmx/GhT2o/bzsig75F3loEzWQg+a0nFDriya+0rvB0uhi1Eh2ENePHxvW6T6rAuq38s/OyjsI82N6Js97WFE2qBcPoj+ZUrIHXWEqspTGE49Zj09PbeSKBy0C+qM0ODhLyar/mHbajosMzJDjOvZB9iJ5jrYBaWp5ip8YKFOfmm6iUcgjbJxQZ5212OcmyWr3lG4uTKJRt8PGL788r+HTjMZFcTZ6DkZhYzQDNauyPVYf3Wa2sU3u9q0LCrtVl022Iqiqh3L4iFI4xYqRSqHIE7kCpILkjUn9EQch+ErwJAX2JYGDAd/Z+jALJtGFgP2cg7JN1GlJulL7QUHmtzLNby3UNgQBfn/KfLhnKZgomU7ublW8xoPhj+WRIPH88yQ4pXURs9J6GVFrRdp7l4Z6UnoNgx/XZOTAX6r3rxCmkQ7kCbSc+PBZu4nGYweMxklk+VJr5OYRKKXFbc2zwUouNDDGO/pSGNVneH7OlbFWg8WtzwFD9g04gg2o9nOdf19zHZeHhjicSgrb6JzkJ4Ai4XvrIE0s3UVyBIRLGKh/OS2ribt0sg9Ioht/JZE9fw8qGVIcyTpb1B1v+lIU3gqFISeDnoRdnJNLYCTeGodb5cjGcBm9K/9K3SkySgYH0avbahFpwnjSdVqMwCjj+FCPIDtDCeRA1+manZWcu8MA1C9/kB0rsnobv4cDd4flKVqCZqpfIbJKIjcT/oW9omvv6yjTEb3oWbKDblQsbnSM9jOliRXo0Im8vP2t6InPlJzoox+tsnsLoZFgw8D5Xonid7d0vT/ZMbbk74d7tztSC5FqZolK8xoLozqn5GAYDfqwVdnVtA5EIIYveAE5Al5IdKMF3XmMjQEo6+cD0k3gt2oB1/xVIMFCQ721oyRqDNC3c8K//ee8mrINWjfaPDFQVlr0ue9kGZDrC/cvQrgo9HwdULzKqmvIFISlP8xSLFFvWI3Xwzsbw/0uNlzdVGE4zQu1JGAcC32Ru/pwvjCbro42KfGQyoM9H91ABXj32igPdRIReCabI28xTeymy0e9q1AnXsijbDy/heWEsXB3B8Fe7GP5INroyryZJQbu8ly4TgGIAXiTzOa3gcKCa3YiZUKOR7pG66THA/vRrmo3JONY9Ks1HIwU8S0rZDPXrq5SG7BmklvTE9PT/SYrBnYh5o0Nd3/7iYjA5X+O7c3pUbKa3p+1bU3Rp9Amk1awwb787xUE6M8N+Un8zR6CE1E4zH03HMiRcoFu9CgpNFomMlISW3rsPaGUEDQltS8qP6Ameid2Lbe/WADcvE+EdXWjiOR1GD4Q1CqJk3700ikvmDHisDnPC+W/VkkUm+w5YHIaV4s+5NIpP5gz5oX6wFj2YvBfj0S6Q6waQWRvclYd5/Mm/d/8iRSpumxbTwAAAAASUVORK5CYII='
      const right3 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMEAAAB5CAYAAACA20WEAAAABHNCSVQICAgIfAhkiAAAAAFzUkdCAK7OHOkAAAAEZ0FNQQAAsY8L/GEFAAAACXBIWXMAAGUBAABlAQGvsJ7JAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAEuhJREFUeF7tnQm0bmMZxx0UyViGQikZIxRlaDAkDYuiFpK4FGmwLs1iRd1Cq2hVuLFSZLpd1xCyiLhcqcwiQ8vsJnHdzG4ynH7//b7nds495/v28+5v7+/b+/ue31r/8+69z7en593Pfof9DkMLOQPP8PDwKwnWRasvoBXRq9GSMZSG0TNRz6Kno+5Hd6G7Y3jP0NCQ/l973AkGEB76pQnePUrvQkugMpGz3I5mRs3CKR4jrB3uBAMCD/4yBDugXdF2SG//bvIyuhWdi07BIe7TRsepHB7+rdDZaB6qCy+jK9DeaKl4qY5THjxYi6Cd0bWo7jyNjkCviZfvOJ3Bw7QLuhs1jSfRd5CybY6TDg/PBmgmajr/RpPRwvHWKqf2BWOMoZqMtdCqSPlHVdeNVNnJUP9BzyFVx/0TzZYoeD1O2PdgH9niCPRFtIi29Ql/QpOIR1W5VkqtnIAIfR3B1uh9SPXWevhfj4rwCLoR3YT+jGY2pd7aCvZ6O8E0tHa2of/Qy+1gdAxxp9qlSuipE8Qkb0u0I9oGrYequqbn0R/RBWg6Rv2XNjYR7CYbfQkdhRbTtj7nErQrcfZEWC2XnjgBkbgawSS0F3qztnWZF9Hv0C/QRRhXH3YaAbZTNvDX6BPZhsHhDrQ9cXVvWG0oRODG6AL0EqoLNyPVqNQ+P801roiuQYPKo2iraI7S6EpKwIWvTzAFKdvT0yxYG/Q1czJvmivCar3Ahko9/4DWyDYMLv9FuxNPZ4XVzqn0gSTiViD4EdoDda3Kq0NU0PwKRq5NmQE7vpVA+eJVsg3OC2gX4ui3YbUzKnMCIm4nghOQHKFpzEH7YOTzw2rvwI5681+JVs42OCOookNlBKWOHVG6ExBpyxMci9RQq+kcjw7E0DJ418GWqh6+GvWi8qAJqMr7g8SPbFSYUp2ASNuIQEmU8q/9gqpVd8TQc8Nqd8CWaj4wC22QbXBa8STagvhRs+1ClJZPJ9JUZacHpp8cQLwH/YX7WzOsVg/n0svpVOQOkI9eFudhs8IN8Dp2AkUYOpTFGUh12P2I8uVq+tstR/gGUtt/x4biZzrxU6iau6PskByAQPnmz2Ub+p9/oK1Ieu8Jq+WDTdVs5FLUT+2AusUU4uawuGymsBNEB/gJmpxtGBweQJtj7IfDanlgUzUQvAW9KdvgpPIS2o64uTys2ugkOzQVDZoDCJV5zuGBXTyslspxyB2gOEo9TyVulgurNgo5ASdR093Ph7WBZDOkdkelgU23JdBHRacz9D1FORQzydkhImt3gtPC2sDzZZLeJINPBDZ9BYGabfRrk+heoA9pF8bltiQ5AZH1TgJ9vXxVtsHRR7TNMPbNYbUY2PUAgo6dyRmDRrNYj7iZF1ZbY84OEVHq8HIOcgf4P2rLfwa2KTxmD/uqfltVzE656Cv7QWGxPaaUgIiSs2gAJfX4csYzlTeOOrkkg22PJvhKWKsFaqWpr+P/RnqLan201BdDzq+KgdGhnFntxBZFdUFdb5UatO2DYHWC/QmOCWvOBKjr33sxtvrFmsGuamel4Qu79ZFRnYfUB1v9dvWtY0Sq9tXocHO5h6cICxFflrqnlZByDnobq7egWsFKvWgEOIN72iUuT0iuE3BjqhL8G1KHbqc1KthujMHVzNcEtv0+wSFhrRLUrkaOeW3UNVxfV9tAjYb7VdXlFkgfBNU5Rm3Nqv4oqBfU+ty3eqZNSFsn4KL1/4uRhu1z8vkGxlb/iVywrUbR0Bt42WxDeegtr1oR9aXW+J9mp+w22ED3/iH0aaRnTLVkVXA6dtA5JiTPCVRvfUpYcwyoae9aGFxDv7QF236NwOQwBpR3/w36Oee+LtvSMLCHyhNqfr8fUk/EMlE5Zm1sM2HZoKUTcFEasPXvqK5fMJXM6S2nasqRQpvyvCqojagX7W9OxNj7xuUJwbayu2zbaYM89X5TwfpXnFMF2cYTbaNuuBpqZRNtKwm9IDQ20zjaOcEXCNQ0otvoYVZhUQW2kQKcIlsFt6zwJnFDufW/0ZE1xr46p0gqmK2DNkQqsFXR603tVzbk+m4Lq+PhujS8zGVhrRC6d31XOJLzaG6AvgQ7bU+g+3xLtqEzlEqvgr1UTsqHky+O/oGqRqNO3IJORPuiDVHXqtg416poD3Qymo3KQsO5tIT/q9lvUS5Bb4yH6nu41yXQj9CLqFPsbd348YFhn0p4Dp2P9kF6S9cGrmdTNBVpPMxOUWeccbD9tej57Bdp6CE4FHXS6LGxcN+boHtRJ9h6n/FDDev9YLZLudyE9ODXvuMN17gYmoTuQkW5KB5uDGz/bPh3EhqxWVmogQYbrIA6HXR403i41vCjj4TfloYG21LdcOPguhdFe6EHUBHGFezYdnH4l5nHkNpsOYAtXolOk2EK8rN4qNbwI7WVLwO9+fVRpPFwH0uj45FmWElBUxPNh/XXoP9m/7EhB3hb3N2JYJOF0TQZqAAaxa51rSH/fB1KiaSJeAEdhPou78o9bYvmICtymvl13ix/JttqQ/HQFy+RKsA2ShEuk6EK0Dpnwj+/GX5TGNWwTFgg7Be4vzXQnbpZI/M737A8I2wyMSj9tguDjZRC355ZKw0NCTox/PO68JtC/A0VnUugUXCfytZcr5s2oNow1QipwsFa63RmPJWTA7Z6B0qtbVM7qvHwD414XHS0aOX/mzjcYmG435WQdW4wZQ83C4u5PIEG4mVSFtjr4MxydvScj39e2bhn9u907kCvjYcZKLhvZY1UeM1DVc5TwmIu+lLvJIDNlMqmDlmvbsJjYWOR0ram31QzhIGF+98ps0Q+z8SwHSpr+HhDBcBumq85hbENQ9kgT5qb/SuNT8ZDDDTY4ZfBHB2zZzykUwDs9/tgRhNjJwRkw0ZhexIadtEBbKFaioczqxRH+6vBn1MQ7KemFdZvOfpdNmfySF2+ZkFMQbMKHhgWnaHQJTF5+L8FOIXjqAWtUxDsdz3BVWEtF7WgVs+2wk5wNCd8KC47gZOQhvkoileLlsOJMbSQOUEGycJVWQJhQ/XeA1UdagW77J9ZKJ3KJ6weFLDlq9DjmVXzOVn7qA2GUgN1MrFyMqmApjNyxqM5BZRVTKXn00L1Czyb6nCkeecsZDkgOcDqSKMhW+lFb7NGQASo19L0sJZER9MNOeNo26lpFOuSCCwqJ0jppXQnEa3hV5zWnBHDFP4SQ6ccNA2vZZ45jW6xkpxg1WzVRmlzx/Yxqp1Qf1Yrs72SoVywp7Kk1lqi1eQEbwjLJjSWjdMGIkBvoJRO9IUnnHPaotl+LKwsJ7BOEK0Cx01h0ckhZW5djazhlM8NMcxjlZTs0I285Wo7mlnNsEaA0Ch0TvlYh8t/o5xAA6dauCaGTj6ad0yDg1l4MIZOifDC1vhUmmgxjyw7ZJ1v4K4YOjkQAc8QWO3VFyPH1RS9jPJYUU5gnWDCk+00rE7gWczqsMTBMnICjdlpwZ0gDUtSLB6PoVM+uQMjwyIp2aHS5+3tc6z2spYdnHQscbC02QnI5/obKw3NCGNBceBUg+Uj5Cus2SGN7+6kocKxBU3W4VSDJSVYUk5g+cTft8N/V4jVCXwarOqwtOhdTE7gvZmqwVrrk9KC10nDMgnhEnKCwrMVOm2xpp7uBNVhqnSQE2hmlTzqNDdtU7BOQucDbVXEkG1WmiflBJZaH39bpWP9/qK5fp3e8bI1Jcj6bsZFx4Z1alb17HN6iJzgkbCYi6btd+wsFsM8PCWoCF7clnGcnpATWJtDDOR4ox1gnZZqZSLL6jBOGpY4eFxOYG3KW6tJ9hqAtRylQaDqOld007FUTmQpgdUJPKLSsNYOCc8SVYPlQ2RSSuARlYa1YCz8BVMNljLBnJQyQRmzig8SKd9W3AmqwdJr8iE5gRoZWT4qbBBDx0bKtxV3gmqw9J9/cOGhoaFhFq4L621Za7gBE3HXiJQaH89qVsPKMWzHbKUEYuKJzMaiGVRSxiwddKzdVoXXvFWDZTihB1KcQGwVQyefFCdIKUQ7dvKcQE2t7x9xAkt2SLw/hk4+KdmhZclq6nuBUy558+lpbN2s7ZBa26lDsqVj+BZeLjCT2k/DnaBEeE6VEuc5wR36M5ISiIti2A61jPxYWHRysPYsE8/qjRSXnXJQbWbeTKB/1Z/RTnBODPPYNYZOe1LGGPXhbMrHMgVZNiT+aCe4HFm+F3yIpMY7guRzWwwt+EDH5bNxDFuhwSOyMWPH5EN5uE8n+FRYa8v3Sb6/HZe7Bten0r5ubi20HFI/XjUFV3lmFtdkceKuwLWuRKCy1ugXTSt25tp97ocSwf5qDtRu2oEbsPkmcfn/sOMnkIVHUVd6m3Ee1Zx8Hd2A2vE80mTOO8Rdew7Xco4uLId7kDelLhHs+fbMsu05Kv58LPwjZea/H8TdKoHjL4GmoKd1skQuRUotegrXsDp6TBfUgnlom/hzpySw6aGZddvzgfjz8fDPn4bf5PIMUpJfOhx3G/SATtIBc9H74iF7BtewEbpFF7QAd6OeX18/gl2vyyzcmmfR/D7g4+qm+edbCTQ5n6Xeegb5ql3icsdwbuWfv4sORpa8dB6aOmknrtFS/VsZ3JdsuSlaD6l5751IZRhT/+66wH2oQZrKZepqq56GqovX0DJPoL+j+7gntUXrGVyjmvbkTdBxIde5fVyeGA50AbLyubhbR3AcZcVmZEcsF6UI3kqzANhtObQvOh3NRnk8hVQO2g31pJzDeU9BeUyKP28NP9KXYSsqQ1ha67WE/eUAysdXxbWojJRlIMBW6vc8FT2HiiKn2Q917Us451oFqYKkHSqHLRN3aQ8/VE2LlQtRoZtlPxWAq3SAEXaOp3TagJ32QU9mFisH5Sq60kCQ8/wwO2N7zo0/z4cfq0D3UrabDeXlk2AfJbezsr2r5ybUtbdS08A2i6DjZagKkO31XacyOP6bkd7yeaQ1+2GHk8J+Jl5G+8Rdc+G3K6CbtWMXsXxKHziwy8Lo1MxC1XENSmlengTHtnyTuR/ltScaCzssj9rVcy+IHGFy3L0l/ObdqNMq0CJ8NV6CMwrsou8x3eCkeMpS4bjbhsPn8q24SxrsOCnsn4RK6CvEQ8yHbUuhw9ALqBf8Ll6KE8Emm6OUbG+n7BFPXQocTzmKB7Mjt0ffBsY9k8KUR2ZnFSZ2DGtm1I5nGroaqT5c7TT2RMujXnHb0NDQ+nHZAeL2eoK8xmZloilr1yEe5oTV4nDtqvHTN6Dtsg3t+THnLJ4T4GTKFj2Emo5PPjgK7PGBYJauU0q2iOMcEQ6Xi6p6Ww6/Yqo7x4MeI9CX4abPatPLVKiO5H80qgZlsd8TlwvB/ocRWPP4U3mG/xWXx5FUZciJ9yM4Pqw1knkYo7IaiiZBXCru9XLr1Wjjmm1+Y+IjaVLIeN2HI6sDPIrW5jxq2jEhSV9ROdAJBD8Ma41E+VEnsAbq5XD76v54QFi0gQOoYHshSqnl+Xo7BxBFmhIchH4dFhuHGnk5gTr0DlSefsu43BZ+91ECpR4fzjbYuBGdFhZbk+wEeJVaCX4WnZptaBZZn1Ino5Jm8ImoRe3ZPODje3hF+J/asV3J4nnIMrboCCq/7s3zmjuAQZGUQI6gKs+90InZhuagpNQJVNqMIQE1yb6aB/0QpE5IayD1J/k2ulX/Q0X6XRzOc6qUI5eO29JwoYcQfA91fKyKuQOjqK+EA8SbmsCrjNePyHG2Jr5Nc0kXSglGw4lUUv8kmpdtqC9TYugE5saw31Bt0K5WBxAdO4HghGcSbIFuzzbUDw0nMz0sOpF7YthP6MHfjefxobBqoxQnEJxYXdpUwDkO9bSL3QLoI8leXF+drqkOaAjCuqfeKSh+9yWe9cJLojQnEFyAPkbtz6IG7lWhpteofnh7rml2WHVGwCbqf31VWOsLDuGeClXdl+oEI3AxMwnegdSsuld5Tw3ItSXXko0y5kzIGTFsOocSz0fG5foxPDz8ajQZ3Ye6xXTkk4/ngI0WR4/IYA1F/Vea00eEi10UfRydhTrpwN2OmWjreErHAPb6Uma55qH+AZYhQ3PpSd0+F780gYZL1AP7XrQmKnItKgypKYS+Jk4jScyG2nbsEBeaZXMW2jzb0AxU+7MD8V3KQMa1+MBFROgTvgamkjNoqlgN8qSJmDUhiKRaDHXSUUFXofL7qt24FkOoXtjpAOyviQM1ZVcTmpqrOv6LxHu/fudwegWOoG6WGlqzrsxBpXbNdJxx8JDJETRiX514ER2LvKLD6Q48bGuibg+FMxF6+KchZZMdp7vw4GlYTLX1zxvSsAo0FP8JSOVDx+ktPIhq1vxLVLUz6K1/JfoCUs1hV6l782enBvBgqjPLbkiDLbwTpY3iNjFqyqKqWbUuuKCXtXzuBE4SOIQG19W3nY2Q+meshuQk6qSjiS/UW0y9uv6DVLWth1tD3Wj+Nn3T0YSGt/LQa06xGrDQQv8DICetCC/Ulv0AAAAASUVORK5CYII='
      const right4 = 'data:image/png;base64,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'
      const right5 = 'data:image/png;base64,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'
      const fieldNumsL = [left1, left2, left3, left4, left5]
      const fieldNumsR = [right1, right2, right3, right4, right5]
      for(let i = 0; i < 9; i++){ 
        this.masterNumHolder.push({
        //zeros
          //right
            layer: 'below',
            x: 12,
            y: -38.2 + cnt,
            sizex: numberSize,
            sizey: numberSize,
            source: zero,
            sizing: 'stretch',
            xref: 'x',
            yref: 'y'
          },
          //left
          {
            layer: 'below',
            x: -14,
            y: -40.4 + cnt,
            sizex: numberSize,
            sizey: numberSize,
            source : zero,
            sizing: 'stretch',
            xref: 'x',
            yref: 'y'
          },{
        // other numbers
          //right
            layer: 'below',
            x: 12,
            y: -40.4 + cnt,
            sizex: numberSize,
            sizey: numberSize,
            source : fieldNumsR[cnt1],
            sizing: 'stretch',
            xref: 'x',
            yref: 'y'
          },
          //left
          {
            layer: 'below',
            x: -14,
            y: -38.2 + cnt,
            sizex: numberSize,
            sizey: numberSize,
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
      },
    triangleMachine(){
      const triangleDown = 'data:image/png;base64,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'
      const triangleUp = 'data:image/png;base64,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'
      let cnt = 0
      for(let i = 1; i < 5; i++){
        //push triangles
        this.masterNumHolder.push({
            layer: 'below',
            x: -13.7,
            y: 13.4 + cnt,
            sizex: .8,
            sizey: 1,
            source : triangleUp,
            sizing: 'stretch',
            xref: 'x',
            yref: 'y'
      },
      {
            layer: 'below',
            x: 12.4,
            y: 13.4 + cnt,
            sizex: .8,
            sizey: 1,
            source : triangleUp,
            sizing: 'stretch',
            xref: 'x',
            yref: 'y'
      },
      {
            layer: 'below',
            x: -13.7,
            y: -42.4 + cnt,
            sizex: .8,
            sizey: 1,
            source : triangleDown,
            sizing: 'stretch',
            xref: 'x',
            yref: 'y'
      },
      {
        
            layer: 'below',
            x: 12.4,
            y: -42.4 + cnt,
            sizex: .8,
            sizey: 1,
            source : triangleDown,
            sizing: 'stretch',
            xref: 'x',
            yref: 'y'
      }) 
      cnt += 10
      }
        },
    setPlayers (){
      this.aframes = []
      this.offJersey = []
      this.defJersey = []
      this.offPos = []
      this.defPos = []
      for(let i = 0; i < this.trackingData.playerroles.offense.length; i++){
        this.offJersey.push(this.trackingData.teamroster.offense[i].jersey)
        this.offPos.push(this.trackingData.teamroster.offense[i].position.name)
      }
      for(let i = 0; i < this.trackingData.playerroles.defense.length; i++){
        this.defJersey.push(this.trackingData.teamroster.defense[i].jersey)
        this.defPos.push(this.trackingData.teamroster.defense[i].position.name)
      }
      for(var i = 0; i < this.trackingData['balltrackingdata'].length; i++){
        //init arrs
        this.offensePlayersx = []
        this.offensePlayersy = []
        this.defensePlayersx = []
        this.defensePlayersy = []
        //populate off
        for(let j = 0; j < this.trackingData.playerroles.offense.length; j++){
          this.offensePlayersx.push(this.trackingData['playertrackingdata'][j]['playertracking'][i]['x'])
          this.offensePlayersy.push(this.trackingData['playertrackingdata'][j]['playertracking'][i]['y'])
        }
        //populate def
        for(let j = this.trackingData.playerroles.offense.length; j <this.trackingData.playerroles.offense.length + this.trackingData.playerroles.defense.length; j++){
          this.defensePlayersx.push(this.trackingData['playertrackingdata'][j]['playertracking'][i]['x'])
          this.defensePlayersy.push(this.trackingData['playertrackingdata'][j]['playertracking'][i]['y'])
        }
      this.populatePlayers(i, this.offensePlayersx, this.offensePlayersy, this.defensePlayersx, this.defensePlayersy, this.offJersey, this.defJersey)
      }
      },
    displayHandler(val){
      const hide = {
        opacity: '0'
      }
      const show = {
        opacity: '1'
      // offense off
      }
      if(val.player.off === false){
        Plotly.restyle('plotter', hide, 1)
      } else {
        Plotly.restyle('plotter', show, 1)
      }
      //defense off
      if(val.player.def === false) {
        Plotly.restyle('plotter', hide, 2)
      } else {
        Plotly.restyle('plotter', show, 2)
      }
      //handle jerseys & Position
      if(val.player.jersOrPos === 'jersey'){
        Plotly.restyle('plotter', {text: [this.offJersey]}, 1)
        Plotly.restyle('plotter', {text: [this.defJersey]}, 2)
      } else if(val.player.jersOrPos === 'position'){
        Plotly.restyle('plotter', {text: [this.offPos]}, 1)
         Plotly.restyle('plotter', {text: [this.defPos]}, 2)
      }
      }
      

  },
////////////////////////////////////////////////////



















  ////////////////////////////MOUNTED
///////////////////////////////////////////////////
  mounted () {
    //set values in store
    this.$store.commit('fieldStart')
    this.$store.commit('setMaxTime', this.trackingData.balltrackingdata.length - 1)
    //check if frames have already been populated
    if(this.aframes.length < this.trackingData['balltrackingdata'].length){
    this.setPlayers()
  }
    // ===================================
    //            Field Set Up
    // ===================================
  // Creating Hash markers
  this.HashMachine()
   // populate numbers
  this.NumMachine()
  //yardLines
  this.YardMachine()
  // populate triangles(?)
  this.triangleMachine()

    // Layout
    this.layout = {
    paper_bgcolor: '#1b7c00',
    plot_bgcolor: 'rgba(0,0,0,0)',
    grid: {
      domain: {
        x:[-26.6, 26.6],
        y: [-60,60]
      }
    },
      xaxis: {
        range: [-26.6, 26.6],
        showgrid: false,
        showlegend: false,
        zeroline: false,
        ticks: '',
        fixedrange: true,
        showline: true,
        autotick: true,
        hoverlabel: false,
        showticklabels: false
      },
      // for deployment: this.routeData.MinY, this.routeData.MaxY
      // for testing: this.trackingData['qbtrackingdata'][this.sliderTime]['y'] -7.5,this.trackingData['qbtrackingdata'][this.sliderTime]['y'] + 20
      yaxis: {
        range: [this.trackingData.playresult.minY,this.trackingData.playresult.maxY],
        showgrid: false,
        showlegend: false,
        fixedrange: true,
        hoverlabel: false,
        zeroline: false,
        ticks: '',
        showline: true,
        autotick: true,
        showticklabels: false
      },
      margin: {
          t: 0, //top margin
          l: 0, //left margin
          r: 0, //right margin
          b: 0 //bottom margin
      },
      showlegend: false,
      images: this.masterNumHolder,
      shapes: this.masterShapeHolder
    }

    this.aframes[1] //sample data 1
    this.aframes[2] //sample data 2

    let self = this
    Plotly.plot('plotter', {
      data: this.aframes[0].data,
      layout: this.layout
    }).then(function(){
      Plotly.addFrames('plotter',self.aframes)
    })
    //make animation responsive
    window.onresize = function () {
      Plotly.Plots.resize('plotter')
    }
    console.log(this.displayOptions, "display Options")
     this.$store.commit('setJerseyDefault')
  }    
}
</script>

<style scoped>
#timeline {
  position: absolute;
  z-index: 1000;
  height: 0vh;
  width: 100%;
}
#timeline[data-v-8eeda45e]{
  width: 100%;
}
#contain {
  padding: 0 0;
  width: 100%;
  height: 85vh;
}
#plotter {
  margin-bottom: 0px;
  padding: 0px;
  width: 100%;
  height: 100vh;
}
</style>
