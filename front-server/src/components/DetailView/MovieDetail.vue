<template>
  <div>
    <div id="back">
      <img id="bgimage" :src="imgurl + movie.backdrop_path" alt="backimage">
    </div>

    <div id="front">
      <div class="container">
        <img class="col-2" id="poster" :src="imgurl + movie.poster_path" alt="poster">
        <div class="ptag col-7">
          <div>
            <h2 style="font-weight: bold">{{ movie.title }}</h2>
            <button @click="addWish(movie.id)">영화 주문하기</button>
            <button @click="addWish(movie.id)">영화 주문취소</button>
          </div>
          <p>
            <span>평점 : ★{{ (movie.vote_average / 2).toFixed(1) }}</span> • 
            <span>{{ genres ? genres[0]?.name : '' }}/{{ genres ? genres[1]?.name : '' }}/{{ genres ? genres[2]?.name : '' }}</span>
          </p>
          <p>줄거리</p>
          <p class="overview">{{ movie.overview }}</p>
        </div>
        <div class="col" id="trailer">
          <iframe :src="videourl + videoId" frameborder="0" height="200" width="300">영상</iframe>

        </div>
      </div>
      <br>
      <div id="mid">
        <div id="cast">
          <h3 class="actorlist">출연진</h3>
          <div class="card-group">
            <div class="card" v-for="(actor, index) in actors" :key="index">
              <img :src="imgurl + actor.profile_path" alt="actorimg">
              <span>{{ actor.name }}</span>
            </div>
          </div>
        </div>

      </div>


    </div>    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetail',
  data() {
    return {
      imgurl: 'https://image.tmdb.org/t/p/original',
      videourl: 'https://www.youtube.com/embed/',
    }
  },
  props: {
    movie: Object,
    actors: Array,
    videoId: String,
    thumbUrl: String,
  },
  methods: {
    addWish(id) {
      const movie_id = id
      
      axios({
        method: 'post',
        url: `${API_URL}/profile/${movie_id}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        } 
      })
      .then(() => {
        this.$router.go(this.$router.currentRoute)         
        // this.getLoginuser()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getLoginuser() {
      this.$store.dispatch('getLoginuser', this.$store.state.username)
    }    
  },
  computed: {
    genres() {
      return this.movie.genres
    },
    username() {
      return this.$store.state.username
    }
  },
  created() {
    this.getLoginuser()
  }
}
</script>

<style>
#back {
  height: 300px;
  position: relative;
  z-index: -1;
}

#bgimage {
  width: 100%;
  height: 130%;
  object-fit: cover;
  opacity: 0.5;
}

#poster {
  height: 300px;
}

#front {
  z-index: 1;
  margin-left: 20px;
}

.container {
  margin: 0;
  width: 100%;
}
.card-group img {
  width: 70px;
  text-align: center;
  object-fit: cover;
}

.card-group {
  display: flex;

}

.card {
  /* margin-right: 40px; */
  display: flex;
  flex-direction: row;
  text-align: center;
  justify-content: center;
  align-items: center;
}

.card img {
  height: 70px;
  border-radius: 30px;
}
.actorlist {
  text-align: left;
}

.detail {
  display: flex;
}

.ptag {
  margin-top: 70px;
  display: flex;
  flex-direction: column;
  justify-content: end;
  text-align: left;
  margin-left: 20px;
}

.ptag p {
  margin: 8px;
}

.overview {
  overflow: hidden;
  /* text-overflow: ellipsis; */
  /* display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical; */
}

#mid {
  display: flex;
}

#trailer img {
  width: 200px;
}
</style>