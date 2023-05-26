<template>
  <div>
    <div class="nrcontent">
      <p>{{ word }}에 대한 검색결과입니다</p>
      <div class="row row-cols-3 row-cols-md-4 g-4">
        <div class="col" v-for="result in results" :key="result.id">
          <img v-if="result.poster_path" :src="imgurl + result.poster_path" class="card-img-top" alt="poster"
          id="posterimg" @click="goDetail(result.id)">
        </div>
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
  },
  methods: {
    goDetail(id) {
      console.log(id)
      // this.$router.push({name: 'main'})
      this.$router.push({name: 'detail', params: {id:id}})
    },    
  }
}
</script>

<style>
#posterimg {
  width: 200px;
}
</style>