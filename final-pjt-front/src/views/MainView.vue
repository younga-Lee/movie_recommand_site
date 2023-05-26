<template>
  <div class="main"> 
    <p id="title">많이 본 영화</p>
    <div class="moviecontainer">
      <BaseCard 
      v-for="movie in manyseemovies.slice(23, 43)"
      :key="movie.pk"
      :movie="movie"
      />
    </div>

    <p id="title">현재 상영작</p>
    <div class="moviecontainer">
      <BoxCard 
      v-for="movie in boxmovies.slice(0, 21)"
      :key="movie.id"
      :movie="movie"
      />
    </div>

    <p id="title">평점 높은 순</p>
    <div class="moviecontainer">
      <PopCard 
      v-for="movie in popularmovies.slice(0,21)"
      :key="movie.pk"
      :movie="movie"
      />
    </div>

    <p id="title" v-if="token">[{{ username }}]님이 가장 많이 평가한 장르</p>
    <div class="moviecontainer" v-if="token">
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
    manyseemovies() {
      return this.$store.getters.manyseeList
    },
    isLogin() {
      // 로그인 여부 확인
      return this.$store.getters.isLogin
    },
    username() {
      return this.$store.state.username
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
#title {
  text-align: left;
  margin-left: 10px;

  /* MO/22/Bold */
  font-family: 'Spoqa Han Sans Neo';
  font-style: normal;
  font-weight: 700;
  font-size: 22px;
  line-height: 29px;
  /* identical to box height, or 133% */
  color: #00201A;
}

.moviecontainer {
  display: flex;
  overflow-x: auto;
  /* white-space: nowrap; */
  margin-bottom: 56px !important;
}

.container::-webkit-scrollbar-thumb {
  height: 30%;
  background: #217af4 !important;
}

h1 {
  font-weight: bold;
  text-align: left;
  margin-left: 120px;
}

.main {
  padding-left: 156px;
}

</style>