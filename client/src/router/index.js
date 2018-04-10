import Vue from 'vue'
import Router from 'vue-router'
import Register from '@/components/Register'
import Timeline from '@/components/Timeline'
import Menu from '@/components/Menu'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Timeline',
      component: Timeline
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/',
      name: 'Menu',
      component: Menu
    }
  ]
})
