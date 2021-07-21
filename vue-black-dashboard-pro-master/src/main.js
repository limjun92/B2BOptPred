import Vue from 'vue';
import VueRouter from 'vue-router';
import RouterPrefetch from 'vue-router-prefetch'
import DashboardPlugin from './plugins/dashboard-plugin';
import App from './App.vue';
import { store } from './store/store'

// router setup
import router from './routes/router';
import i18n from './i18n';
import './registerServiceWorker'
import VueSession from 'vue-session'

var sessionOptions = {
  persist: true
}
Vue.use(VueSession, sessionOptions)
// plugin setup
Vue.use(DashboardPlugin);
Vue.use(VueRouter);
Vue.use(RouterPrefetch);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router,
  store,
  i18n
});
