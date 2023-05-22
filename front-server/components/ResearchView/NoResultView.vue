<template>
  <div id="noresult">
    <h1># {{ word }}에 대한 결과가 없습니다</h1>
    <img src="@/assets/noresult.png" alt="noresult"
    >

    <h1># 이런 영화는 어떠세요?</h1>
    <div class="row row-cols-3 row-cols-md-4 g-4">
      <div class="col" v-for="movie in popularList" :key="movie.id">
        <img :src="imgurl + movie.poster_path" class="card-img-top" alt="poster"
        id="posterimg">
      </div>
    </div>    
  </div>
</template>

<script>
export default {
  name: 'NoResultView',
  props: {
    word: String,
  },
  data() {
    return {
      imgurl: 'https://image.tmdb.org/t/p/original',

    }
  },
  methods: {
    getPop() {
      this.$store.dispatch('getPop')
    },
  },
  created() {
    this.getPop()
  },
  computed: {
    popularList() {
      return this.$store.state.popularList
    }
  }
}
</script>

<style>
#noresult {
  text-align: left !important;
}
</style>