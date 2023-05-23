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
      // 로그인이 되어있으면 실행, 아니면 login page로 이동
      // if (this.isLogin) {
      //   this.$store.dispatch('getPop')
      // } else {
      //   alert('로그인이 필요한 페이지입니다')
      //   this.$router.push({name: 'login'})
      // }
      this.$store.dispatch('getBox')
    },
    // getPop() {
    //   this.$store.dispatch('getPop')
    // },
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  },
  created() {
    this.getBox()
    // this.getPop()
    this.getMovies()
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