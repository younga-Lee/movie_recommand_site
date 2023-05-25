<template>
  <div>
    <img id="imglist" :src="url + movie.poster_path" alt="poster" @click="goDetail">
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'PopCard',
  data() {
    return {
      url : 'https://image.tmdb.org/t/p/w600_and_h900_bestv2',
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    goDetail() {
      // console.log(this.movie.pk)
      this.$router.push({name: 'detail', params: {id:`${this.movie.pk}`}})
      window.scrollTo(0,0)
    }
  }
}
</script>

<style>
#imglist {
  width: 200px;
  margin-right: 20px;
}
</style>