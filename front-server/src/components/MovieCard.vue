<template>
  <div class="col">
    <div class="card p-2">
      <img :src="url + movie.poster_path" alt="poster" id="poster" class="img-fluid">
      <h3 class="p-2">{{ movie.title }}</h3>
      <p>{{ movie.overview }}</p>
    </div>
  </div>
</template>

<script>
// const API_KEY = process.env.VUE_APP_API_KEY
export default {
  name: 'MovieCard',
  data() {
    return {
      url : 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'
      // url: `https://api.themoviedb.org/3/movie/${this.movie.id}/images?api_key=${API_KEY}&language=ko`
    }
  },
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>