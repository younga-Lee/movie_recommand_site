import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    boxoffieList : [],
    popularList : [],
    TMDB_API_KEY : process.env.VUE_APP_TMDB_API_KEY,
  },
  getters: {
  },
  mutations: {
    GET_DATA(state, movies){
      state.boxoffieList = movies
    },
    GET_POP(state, pops){
      state.popularList = pops
    },
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
      })
      
      .then((res) => {
        // console.log(res.data.results)
        context.commit('GET_POP', res.data.results.slice(0, 18))
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
