import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faBars,
  faArrowCircleRight,
  faArrowCircleLeft,
  faTimes,
} from '@fortawesome/free-solid-svg-icons'
import {
  faFacebook,
  faGithub,
  faTwitter,
} from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Chat from 'vue-beautiful-chat'
import { rtdbPlugin } from 'vuefire'

library.add(
  faFacebook,
  faGithub,
  faTwitter,
  faBars,
  faArrowCircleLeft,
  faArrowCircleRight,
  faTimes,
)

import './assets/css/normalize.css'
import './assets/css/style.css'

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(rtdbPlugin)
Vue.use(Chat)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
