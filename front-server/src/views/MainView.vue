<template>
  <div> 
    <h1># 기본 확인 중</h1>
    <div class="container">
      <BaseCard 
      v-for="movie in basemovies.slice(100, 111)"
      :key="movie.pk"
      :movie="movie"
      />
    </div>
    <h1># 현재 상영작</h1>
    <div class="container">
      <BoxCard 
      v-for="movie in boxmovies.slice(0, 11)"
      :key="movie.id"
      :movie="movie"
      />
    </div>
    <br><br>
    <h1># 다른 사람들이 즐긴 영화</h1>
    <div class="container">
      <PopCard 
      v-for="movie in popularmovies.slice(0,21)"
      :key="movie.pk"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import BoxCard from '@/components/MainView/BoxCard'
import BaseCard from '@/components/MainView/BaseCard'
import PopCard from '@/components/MainView/PopCard'

export default {
  name: 'MovieView',
  methods: {
    getBox() {
      this.$store.dispatch('getBox')
    },
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getLoginuser() {
      this.$store.dispatch('getLoginuser', this.$store.state.username)
    },
  },
  created() {
    this.getBox()
    // this.getPop()
    this.getMovies()
    this.getLoginuser()
  },
  computed: {
    basemovies() {
      return this.$store.state.basemovies
    },
    boxmovies() {
      return this.$store.state.boxoffieList
    },
    popularmovies() {
      return this.$store.getters.popularList
    },
    isLogin() {
      // 로그인 여부 확인
      return this.$store.getters.isLogin
    }    
  },
  components: {
    BoxCard,
    PopCard,
    BaseCard
  }
}
</script>
 
<style>
.container {
  display: flex;
  overflow-x: auto;
}

h1 {
  font-weight: bold;
  text-align: left;
  margin-left: 120px;
}
</style>