<template>
  <div>
    <h1>#{{ word }}에 대한 검색결과입니다</h1>
    <div class="row row-cols-3 row-cols-md-4 g-4">
      <div class="col" v-for="result in results" :key="result.id">
        <img :src="imgurl + result.poster_path" class="card-img-top" alt="poster"
        id="posterimg">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResultView',
  props: {
    results: Array,
    word: String,
  },
  data() {
    return {
      imgurl: 'https://image.tmdb.org/t/p/original',
    }
  }
}
</script>

<style>
#posterimg {
  width: 200px;
}
</style>