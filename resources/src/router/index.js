import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'inicio',
    props: true,
    component: Home
  },
  {
    path: '/acerca',
    name: 'acerca',
    props: true,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "acerca" */ '../views/acerca')
  },
  {
    path: '/trabajos',
    name: 'trabajos',
    props: true,
    component: () => import(/* webpackChunkName: "trabajos" */ '../views/trabajos')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
