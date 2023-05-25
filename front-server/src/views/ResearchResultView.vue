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
const API_URL = 'http://127.0.0.1:8000'

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
      const query = this.word

        axios({
          method: 'get',
          url: `${API_URL}/api/v1/movies/search/`,
          params: {query:query}
        })
        .then((res) => {
          this.results = res.data
          // console.log(res.data)
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