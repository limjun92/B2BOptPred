import VueRouter from 'vue-router';
import routes from './routes';

// configure router
const router = new VueRouter({
  routes, // short for routes: routes
  
  base: process.env.BASE_URL,

  linkActiveClass: 'active'
});

export default router;
