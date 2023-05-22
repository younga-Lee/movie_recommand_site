import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    boxoffieList : [],
    popularList : [],
    TMDB_API_KEY : process.env.VUE_APP_TMDB_API_KEY,
    token: null,
    username: null,
  },
  getters: {
    isLogin(state) {
      // 토큰의 유무로 로그인 확인
      return state.token ? true : false
    }
  },
  mutations: {
    GET_DATA(state, movies){
      state.boxoffieList = movies
    },
    GET_POP(state, pops){
      state.popularList = pops
    },
    SAVE_TOKEN(state, token) {
      // 로컬스토리지 사용
      state.token = token
      // console.log('3')
      // console.log(token)
      // main으로 보내기, $router 접근 불가라 import 해줘야함
      router.push({name: 'main'})
    },
    LOGOUT(state) {
      state.token = null
      state.username = null
      // router.push({name: 'main'})
      router.go(0)
    }  
  },
  actions: {
    getBox(context) {
      
      axios({
        method: 'get',
        url : `https://api.themoviedb.org/3/movie/now_playing?api_key=${this.state.TMDB_API_KEY}`,
      })
      
      .then((res) => {
        // console.log(res.data.results)
        context.commit('GET_DATA', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getPop(context) {
      
      axios({
        method: 'get',
        url : `https://api.themoviedb.org/3/movie/popular?api_key=${this.state.TMDB_API_KEY}`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      
      .then((res) => {
        // console.log(res.data.results)
        context.commit('GET_POP', res.data.results.slice(0, 18))
      })
      .catch((err) => {
        console.log(err)
      })
    },
    signUp(context, payload) {
      // console.log('1')
      // console.log(payload)
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then((res) => {
        // console.log('2')
        // console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      }) 
      .catch((err) => {
        console.log(err)
      })      
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        this.state.username = username
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout(context) {
      context.commit('LOGOUT')
    }
  },
  modules: {
  }
})
