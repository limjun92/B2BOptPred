import Vue from 'vue'
import App from './App.vue'
import { store } from './store/store'
import router from './router'
import DashboardPlugin from './plugins/dashboard-plugin';

Vue.config.productionTip = false
Vue.use(DashboardPlugin);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
