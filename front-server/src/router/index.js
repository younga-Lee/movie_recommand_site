import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/MainView'
import DetailView from '@/views/DetailView'
import LoginView from '@/views/LoginView'
import SignupView from '@/views/SignupView'
import ResearchResultView from '@/views/ResearchResultView'
import ProfileView from '@/views/ProfileView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/detail/:id',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/search/:word',
    name: 'search',
    component: ResearchResultView
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
