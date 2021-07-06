import Vue from 'vue';
import VueRouter from 'vue-router';
import main from '../views/main.vue';

const fileUploadTest = () =>
  import(/* webpackChunkName: "pages" */ '../components/fileUploadTest.vue');

Vue.use(VueRouter)

let authPages = {
  path: '/a',
  component: fileUploadTest,
  name: 'Authentication',
  children: [
    {
      path: '/f',
      name: 'fileUploadTest',
      component: fileUploadTest
    },
    authPages,
  ]
};

const routes = [
    {
      path: '/',
      name: 'main',
      component: main
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router