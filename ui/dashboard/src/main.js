import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'

import VuePlyr from 'vue-plyr'
import 'vue-plyr/dist/vue-plyr.css'

Vue.config.productionTip = false

Vue.use(VuePlyr, {
  plyr: {}
})

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
