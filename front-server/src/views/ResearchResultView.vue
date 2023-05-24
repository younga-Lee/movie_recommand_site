<template>
  <div>
    <NoResultView 
    v-if="results[0]? false : true"
    :word="word"/>
    <ResultView 
    v-if="results[0]? true : false"
    :results="results"
    :word="word"
    />
  </div>
</template>

<script>
import axios from 'axios'
import ResultView from '@/components/ResearchView/ResultView.vue'
import NoResultView from '@/components/ResearchView/NoResultView.vue'

export default {
  name: 'ResearchResultView',
  components: {
    ResultView,
    NoResultView
  },
  data() {
    return {
      results: [],
    }
  },
  computed: {
    word() {
      return this.$route.params.word
    },

  },
  methods: {
    getResult() {
      const word = this.word
      const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/search/multi?api_key=${TMDB_API_KEY}`,
        params: {query: word, language: 'ko'},
        // headers: {
        //   accept: 'application/json',
        //   Authorization: `Bearer ${TMDB_API_KEY}`
        // }
        })
      .then((res) => {
        // console.log(res.data.results)
        this.results = res.data.results
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    this.getResult()
  }
}
</script>

<style>

</style>