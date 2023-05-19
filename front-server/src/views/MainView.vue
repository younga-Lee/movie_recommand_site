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
      <TopCard 
      v-for="movie in topmovies"
      :key="movie.id"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import BoxCard from '@/components/MainView/BoxCard'
import TopCard from '@/components/MainView/TopCard'

export default {
  name: 'MovieView',
  methods: {
    getBox() {
      this.$store.dispatch('getBox')
    },
    getTop() {
      this.$store.dispatch('getTop')
    },
  },
  created() {
    this.getBox()
    this.getTop()
  },
  computed: {
    boxmovies() {
      return this.$store.state.boxoffieList
    },
    topmovies() {
      return this.$store.state.toprateList
    },

  },
  components: {
    BoxCard,
    TopCard
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