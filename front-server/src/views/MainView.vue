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
      this.$store.dispatch('getBox')
    },
    getPop() {
      this.$store.dispatch('getPop')
    },
  },
  created() {
    this.getBox()
    this.getPop()
  },
  computed: {
    boxmovies() {
      return this.$store.state.boxoffieList
    },
    popularmovies() {
      return this.$store.state.popularList
    },

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