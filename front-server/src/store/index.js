import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    boxoffieList : [],
  },
  getters: {
  },
  mutations: {
    GET_DATA(state, movies){
      state.boxoffieList = movies
    },
  },
  actions: {
    getBox(context) {
      const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY
      
      axios({
        method: 'get',
        url : `https://api.themoviedb.org/3/movie/now_playing?api_key=${TMDB_API_KEY}`,
      })
      
      .then((res) => {
        // console.log(res.data.results)
        context.commit('GET_DATA', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
