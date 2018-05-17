// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
<<<<<<< HEAD
import vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import {store} from './store/store'

Vue.config.productionTip = false
Vue.use(vuetify)
=======
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.config.productionTip = false

Vue.use(Vuetify)
>>>>>>> 8e2be1ca5b19da6241609c08e42e7c7d096897b3
/* eslint-disable no-new */
new Vue({
  store: store,
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
