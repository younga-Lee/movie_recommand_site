<template>
  <div>
    <img id="imglist" :src="url + movie.poster_path" alt="poster" @click="goDetail">
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'BoxCard',
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
      this.$router.push({name: 'detail'})
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