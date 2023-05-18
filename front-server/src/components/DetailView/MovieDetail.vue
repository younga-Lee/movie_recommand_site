<template>
  <div>
    <div id="back">
      <img id="bgimage" :src="url + movie.backdrop_path" alt="backimage">
    </div>
    <div>
      <img id="poster" :src="url + movie.poster_path" alt="poster">
      <span>{{movie.title}}</span>
      <span>{{ movie.overview }}</span>
      <div class="actors" v-for="actor in actors" :key="actor.id">
        <img :src="url + actor.profile_path" alt="">
        <span>{{ actor.name }}</span>
      </div>
    </div>    
  </div>
</template>

<script>
export default {
  name: 'MovieDetail',
  data() {
    return {
      url: 'https://image.tmdb.org/t/p/original',
    }
  },
  props: {
    movie: Object,
    actors: Object,
  }
}
</script>

<style>
.actors {
  width: 200px;
  display: flex;
  flex-wrap: nowrap;
  flex-direction: row;
  justify-content: flex-start;
}
</style>