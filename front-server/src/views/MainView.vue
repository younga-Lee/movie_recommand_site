<template>
  <div> 
    <h1># 현재 상영작</h1>
    <div class="container">
      <BoxCard 
      v-for="movie in boxmovies"
      :key="movie.id"
      :movie="movie"
      />
    </div>
    <br><br>
    <h1># 다른 사람들이 즐긴 영화</h1>
    <div class="container">
      <PopCard 
      v-for="movie in popularmovies"
      :key="movie.id"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import BoxCard from '@/components/MainView/BoxCard'
import PopCard from '@/components/MainView/PopCard'

export default {
  name: 'MovieView',
  methods: {
    getBox() {
      // 로그인이 되어있으면 실행, 아니면 login page로 이동
      if (this.isLogin) {
        this.$store.dispatch('getPop')
      } else {
        alert('로그인이 필요한 페이지입니다')
        this.$router.push({name: 'login'})
      }


      // this.$store.dispatch('getBox')
    },
    getPop() {
      this.$store.dispatch('getPop')
    },
  },
  created() {
    // this.getBox()
    // this.getPop()
  },
  computed: {
    boxmovies() {
      return this.$store.state.boxoffieList
    },
    popularmovies() {
      return this.$store.state.popularList
    },
    isLogin() {
      // 로그인 여부 확인
      return this.$store.getters.isLogin
    }    
  },
  components: {
    BoxCard,
    PopCard
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