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
    basemovies: [],
    boxoffieList : [],
    // popularList : [],
    TMDB_API_KEY : process.env.VUE_APP_TMDB_API_KEY,
    token: null,
    username: null,
    loginuser: null,
    profileuser: null,
  },
  getters: {
    isLogin(state) {
      // 토큰의 유무로 로그인 확인
      return state.token ? true : false
    },
    popularList(state) {
      // vote_average 높은 순으로 정렬한 배열 반환
      return state.basemovies.slice().sort((a, b) => b.vote_average - a.vote_average) 
    },
    manyseeList(state) {
      // vote_average 높은 순으로 정렬한 배열 반환
      return state.basemovies.slice().sort((a, b) => b.vote_count - a.vote_count) 
    },
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.basemovies = movies
    },
    GET_DATA(state, movies){
      state.boxoffieList = movies
    },
    SAVE_TOKEN(state, token) {
      // 로컬스토리지 사용
      state.token = token
      // console.log('3')
      // console.log(token)
      // main으로 보내기, $router 접근 불가라 import 해줘야함
      // this.getUser(this.username)
      router.push({name: 'main'})
    },
    LOGOUT(state) {
      state.token = null
      state.user = null
      state.username = null
      state.loginuser = null

      if (router.currentRoute.name === 'main') {
        router.go(0) // 현재 페이지를 새로고침
      } else {
        router.push({ name: 'main' }) // 'main'으로 이동
      }
      // router.push({name: 'main'})
      // router.go(0)
    },
    GET_LOGINUSER(state, user) {
      state.loginuser = user
    },
    GET_PROFILEUSER(state, user) {
      state.profileuser = user
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
      .then((res) => {
        // console.log(res.data)
        context.commit('GET_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getBox(context) {
      
      axios({
        method: 'get',
        url : `https://api.themoviedb.org/3/movie/now_playing?api_key=${this.state.TMDB_API_KEY}&page=1&language=ko&region=KR`,
      })
      
      .then((res) => {
        // console.log(res.data.results)
        context.commit('GET_DATA', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    signUp(context, payload) {
      // console.log('1')
      console.log(payload)
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
        this.state.username = username
        context.commit('SAVE_TOKEN', res.data.key)
      }) 
      .catch((err) => {
        console.log(err)
      })      
    },
    editProfile(context, payload) {
      const password1 = payload.password1
      const image = payload.image
      
      axios({
        method: 'put',
        url: `${API_URL}/profile/edit/${this.state.username}`,
        data: {
          password1, image
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
        if (err.response && err.response.status === 400) {
          alert('이름과 비밀번호를 다시 확인해주세요')
        } else {
          console.log(err)
        }
      })
    },
    logout(context) {
      context.commit('LOGOUT')
    },
    getLoginuser(context, username) {
      // console.log(context)
      // console.log(username)
      if (this.state.token) {
        axios({
          method: 'get',
          url: `${API_URL}/profile/${username}/`,
        })
        .then((res) => {
          context.commit('GET_LOGINUSER', res.data)
          // console.log(res.data)
          // console.log(context)
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    getProfileuser(context, username) {
      // console.log(context)
      // console.log(username)
      if (this.state.token) {
        axios({
          method: 'get',
          url: `${API_URL}/profile/${username}/`,
        })
        .then((res) => {
          context.commit('GET_PROFILEUSER', res.data)
          // console.log(res.data)
          // console.log(context)
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
  },
  modules: {
  }
})
