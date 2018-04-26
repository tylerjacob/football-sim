import Vue from 'vue'
import Router from 'vue-router'
import Register from '@/components/Register'
import Timeline from '@/components/Timeline'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'root',
      components: Timeline
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})
