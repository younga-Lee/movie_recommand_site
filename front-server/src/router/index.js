import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/MainView'
import DetailView from '@/views/DetailView'
import LoginView from '@/views/LoginView'
import SignupView from '@/views/SignupView'
import ResearchResultView from '@/views/ResearchResultView'
import ProfileView from '@/views/ProfileView'
import NoUserView from '@/views/NoUserView'
import EditProfileView from '@/views/EditProfileView'

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
    path: '/nouser',
    name: 'nouser',
    component: NoUserView
  },
  {
    path: '/edit/:username',
    name: 'edit',
    component: EditProfileView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
    // beforeEnter: (to, from, next) => {
    //   const username = to.params.username

    //   if (username) {
    //     next()
    //   } else {
    //     next({name: 'nouser'})
    //   }
    // }
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
