<template>
  <div>
    <MovieDetail 
    :movie='movie'
    :actors='actors'
    />
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetail from '@/components/DetailView/MovieDetail'

export default {
  name: 'DetailView',
  components: {
    MovieDetail
  },
  data() {
    return {
      movie: [],
      actors: [],
      TMDB_API_KEY: process.env.VUE_APP_TMDB_API_KEY,
    }
  },
  computed: {
    id() {
      return this.$route.params.id
    } 
  },
  methods: {    
    getDetail() {
      const movie_id = Number(this.id)

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${movie_id}?api_key=${this.TMDB_API_KEY}`,
      })
      .then((res) => {
        // console.log(res.data)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getActors() {
      const movie_id = Number(this.id)

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${movie_id}/credits?api_key=${this.TMDB_API_KEY}`
      })
      .then((res) => {
        console.log(res.data.cast.slice(0, 5))
        this.actors = res.data.cast.slice(0, 5)
      })
      .catch((err) => {
        console.log(err)
      })      
    }
  },
  created() {
    this.getDetail()
    this.getActors()
  }
}
</script>

<style>
#back {
  height: 500px;
}

#bgimage {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.5;
}

#poster {
  width: 200px;
}

.actors img {
  width: 50px;
}
</style>