<template>
  <div id="noresult">
    <h1># {{ word }}에 대한 결과가 없습니다</h1>
    <img src="@/assets/noresult.png" alt="noresult"
    >

    <h1># 이런 영화는 어떠세요?</h1>
    <div class="row row-cols-3 row-cols-md-4 g-4">
      <div class="col" v-for="movie in popularList" :key="movie.pk">
        <img :src="imgurl + movie.poster_path" class="card-img-top" alt="poster"
        id="posterimg" @click="goDetail(movie.pk)">
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
    // getPop() {
    //   this.$store.dispatch('getPop')
    // },
    goDetail(id) {
      // console.log(id)
      // this.$router.push({name: 'main'})
      this.$router.push({name: 'detail', params: {id:id}})
    },   
  },
  created() {
    // this.getPop()
  },
  computed: {
    popularList() {
      return this.$store.getters.popularList.slice(178, 198)
    }
  }
}
</script>

<style>
#noresult {
  text-align: left !important;
}
</style>