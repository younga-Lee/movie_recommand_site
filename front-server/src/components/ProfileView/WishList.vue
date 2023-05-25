<template>
  <div>
    <h2>WishList</h2>
    <a :href="url">하이</a>
    <div class="row row-cols-3 row-cols-md-4 g-4">
      <div class="col" v-for="movie in movielist" :key="movie.pk">
        <img v-if="movie.poster_path" :src="imgurl + movie.poster_path" class="card-img-top" alt="poster"
        id="posterimg" @click="goDetail(movie.pk)">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WishList',
  props: {
    wishList: Array,
  },
  data() {
    return {
      basemovies: this.$store.state.basemovies,
      imgurl: 'https://image.tmdb.org/t/p/original',
      movielist: [],
      url: 'http://localhost:8080/profile/coco2'
    }
  },
  computed: {
    username() {
      return this.$route.params.username
    },
  },
  methods: {
    getMovie() {
      return (Id) => this.basemovies.find(movie => movie.id === Id);
    },
    goDetail(id) {
      this.$router.push({name: 'detail', params: {id:id}})
      window.scrollTo(0,0)
    },
    getProfileuser() {
      const username = this.username
      this.$store.dispatch('getProfileuser', username)
      this.getMovielist()
    },
    getMovielist() {
      this.movielist = this.basemovies.filter(movie => this.wishList.includes(movie.pk))
    }
  },
  created() {
    // this.movielist = this.basemovies.filter(movie => this.wishList.includes(movie.pk))
    this.getProfileuser()
    // this.$router.go(this.$router.currentRoute)        

  }

}
</script>

<style>

</style>