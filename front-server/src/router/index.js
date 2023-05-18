import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/MainView'
// import DetailView from '@/views/DetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },
  // {
  //   path: '/detail/:title',
  //   name: 'detail',
  //   component: DetailView
  // },
  // {
  //   path: '/watch-list',
  //   name: 'watchs',
  //   component: WatchListView
  // },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
