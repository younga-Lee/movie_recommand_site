<template>
  <div> 
    <h1># 현재 상영작</h1>
    <div class="container">
      <BoxCard 
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import BoxCard from '@/components/MainView/BoxCard'

export default {
  name: 'MovieView',
  methods: {
    getBox() {
      this.$store.dispatch('getBox')
    }
  },
  created() {
    this.getBox()
  },
  computed: {
    movies() {
      return this.$store.state.boxoffieList
    }
  },
  components: {
    BoxCard
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