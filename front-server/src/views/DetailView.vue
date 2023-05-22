<template>
  <div>
    <MovieDetail 
    :movie="movie"
    :actors="actors"
    :videoId="videoId"
    :thumbUrl="thumbUrl"
    />
    <br><br>
    <MovieRated />
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetail from '@/components/DetailView/MovieDetail'
import MovieRated from '@/components/DetailView/MovieRated'

export default {
  name: 'DetailView',
  components: {
    MovieDetail,
    MovieRated
  },
  data() {
    return {
      movie: {},
      actors: [],
      videoId: '',
      thumbUrl: '',
      TMDB_API_KEY: process.env.VUE_APP_TMDB_API_KEY,
      YOUTUBE_API_KEY: process.env.VUE_APP_YOUTUBE_API_KEY,
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
      // console.log(movie_id)

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${movie_id}?api_key=${this.TMDB_API_KEY}`,
        params: {language: 'ko'},
      })
      .then((res) => {
        // console.log(res.data)
        this.movie = res.data
        // this.getVideo()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getActors() {
      const movie_id = Number(this.id)

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${movie_id}/credits?api_key=${this.TMDB_API_KEY}`,
        params: {language: 'ko'},
        })
      .then((res) => {
        // console.log(res.data.cast.slice(0, 5))
        this.actors = res.data.cast.slice(0, 5)
      })
      .catch((err) => {
        console.log(err)
      })      
    },
    getVideo(){

      axios({
        method: 'get',
        url: `https://www.googleapis.com/youtube/v3/search?key=${this.YOUTUBE_API_KEY}`,
        params: {
          part: 'snippet',
          type: 'video',
          q: `${this.movie.title + ' 예고'}`
        }
      })
      .then((response) => {
        console.log(response.data.items[0])
        this.videoId = response.data.items[0].id.videoId
        this.thumbUrl = response.data.items[0].snippet.thumbnails.default.url
        // this.url = `https://www.youtube.com/embed/${videoId}`
      })
      .catch((err) => {
        console.log(err)
      })
    }    
  },
  created() {
    this.getDetail()
    this.getActors()
  },
}
</script>

<style>

</style>