<template>
  <div>
    <div id="back">
      <img id="bgimage" :src="imgurl + movie.backdrop_path" alt="backimage">
      <div class="trailer-container">
        <iframe :src="videourl + videoId" frameborder="0" height="351" width="625">영상</iframe>
      </div>
    </div>

    <div class="container">
      <img id="poster" :src="imgurl + movie.poster_path" alt="poster">
      <div class="ptag">
        <div class="detailtitle">
          <p class="movietitle">{{ movie.title }}</p>
          <button v-if="!loginuser.likes_movies.includes(movie.id)" @click="addWish(movie.id)"><p>영화 주문하기</p></button>
          <button v-if="loginuser.likes_movies.includes(movie.id)" @click="addWish(movie.id)"><p>영화 주문취소</p></button>
        </div>
        <hr>
        <p class="rateavg">평점 : ★{{ (movie.vote_average / 2).toFixed(1) }}</p>
        <!-- <p>
          <span></span> • 
          <span>{{ genres ? genres[0]?.name : '' }}/{{ genres ? genres[1]?.name : '' }}/{{ genres ? genres[2]?.name : '' }}</span>
        </p> -->
        <div class="description">
          <p class="plot">줄거리</p>
          <p class="overview">{{ movie.overview }}</p>
        </div>
      </div>
    </div>

    <div id="cast">
      <div class="casttitle">
        <p>출연진</p>
        <hr>
      </div>
      <div class="castgroup">
        <div class="person" v-for="(actor, index) in actors" :key="index">
          <img :src="imgurl + actor.profile_path" alt="actorimg">
          <p>{{ actor.name }}</p>
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
    },
    loginuser() {
      return this.$store.state.loginuser
    }
  },
  created() {
    this.getLoginuser()
  }
}
</script>

<style>
#back {
height: 514px;
left: 0px;
top: 206px;
/* position: relative; */
}

.trailer-container {
  position: absolute;
  left: calc(50% - 625px/2 + 0.5px);
  top: 288px;
}

#bgimage {
  width: 120%;
  height: 100%;
  object-fit: cover;
  opacity: 0.5;
}

#poster {
width: 212px;
height: 294px;
flex: none;
order: 0;
flex-grow: 0;
border-radius: 8px;
}

#front {
display: flex;
flex-direction: row;
justify-content: space-between;
align-items: flex-start;
padding: 60px 156px;
gap: 24px;

/* position: absolute; */
width: 1440px;
height: 414px;
left: 0px;
top: 720px;
}

.container {
display: flex;
flex-direction: row;
justify-content: space-between;
align-items: flex-start;
padding: 60px 156px;
gap: 24px;

margin: 0;
margin-bottom: 0;
/* position: absolute; */
/* width: 1440px; */
height: 414px;
left: 0px;
top: 720px;

}

#cast {
display: flex;
flex-direction: column;
align-items: flex-start;
padding: 0px;
gap: 40px;

width: 1128px;
height: 178px;

margin: auto;
}

.castgroup {
display: flex;
flex-direction: row;
align-items: flex-start;
padding: 0px;
gap: 8px;

width: 1128px;
height: 80px;


/* Inside auto layout */

flex: none;
order: 1;
align-self: stretch;
flex-grow: 0;
}

.person {
  display: flex;
flex-direction: row;
align-items: center;
padding: 16px 12px;
gap: 16px;

width: 219.2px;
height: 80px;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 1;
}

.person img {
width: 48px;
height: 48px;

/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
border-radius: 50%
}

.person p {
width: 131.2px;
height: 48px;

/* MO/16/Regular */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 24px;
/* or 150% */

color: #000000;


/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 1;
}

.casttitle {
display: flex;
flex-direction: column;
align-items: flex-start;
padding: 0px;
gap: 24px;

width: 1128px;
height: 58px;

/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.casttitle p {
width: 67px;
height: 32px;

/* MO/24/Bold */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 24px;
line-height: 32px;
/* identical to box height, or 133% */


/* starbucks/ref/neutral/neutral20 */

color: #30312C;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.casttitle hr {
width: 1128px;
height: 2px;

/* starbucks/ref/neutral/neutral87 */

background: #DBDAD3;

/* Inside auto layout */

flex: none;
order: 1;
align-self: stretch;
flex-grow: 0;
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
display: flex;
flex-direction: column;
align-items: flex-start;
padding: 0px;
gap: 24px;

width: 864px;
height: 293px;


/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 0;
}

.detailtitle {
display: flex;
flex-direction: row;
justify-content: space-between;
align-items: center;
padding: 0px;
gap: 16px;

width: 864px;
height: 43px;


/* Inside auto layout */

flex: none;
order: 0;
align-self: stretch;
flex-grow: 0;
}

.detailtitle button {
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
padding: 12px 18px;
gap: 6px;

width: 117px;
height: 43px;

background: #3C4043;
/* Shadow/XSM */

box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
border-radius: 100px;

/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 0;
}

button p {
width: 81px;
height: 19px;
margin-bottom: 0;

/* MO/14/bold */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 14px;
line-height: 19px;
/* identical to box height, or 133% */

/* Base/White */
color: #FFFFFF;

/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.movietitle {
  width: 210px;
height: 32px;

/* MO/24/Bold */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 24px;
line-height: 32px;
/* identical to box height, or 133% */


/* starbucks/ref/neutral/neutral20 */

color: #30312C;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.description {
display: flex;
flex-direction: column;
align-items: flex-start;
padding: 0px;
gap: 8px;

width: 864px;
height: 152px;

/* Inside auto layout */

flex: none;
order: 3;
flex-grow: 0;
}

.plot {
width: 864px;
height: 24px;

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 16px;
line-height: 24px;
/* identical to box height, or 150% */


/* starbucks/ref/neutral/neutral50 */

color: #777771;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.overview {
overflow: hidden;
text-overflow: ellipsis;
display: -webkit-box;
-webkit-line-clamp: 4;
-webkit-box-orient: vertical;
width: 864px;
height: 91px;

/* MO/16/Regular */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 24px;
/* or 150% */

/* starbucks/ref/neutral/neutral50 */
color: #777771;

/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 0;
}

#mid {
  display: flex;
}

#trailer img {
  width: 200px;
}

.rateavg {
width: 864px;
height: 24px;

/* MO/16/Regular */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 24px;
/* identical to box height, or 150% */


/* starbucks/ref/neutral/neutral50 */

color: #777771;


/* Inside auto layout */

flex: none;
order: 2;
flex-grow: 0;  
}

.container hr {
width: 864px;
height: 2px;

/* starbucks/ref/neutral/neutral50 */
background: #777771;

/* Inside auto layout */

flex: none;
order: 1;
align-self: stretch;
flex-grow: 0;  
}
</style>

<style scoped>
p {
  margin-bottom: 0;
}
</style>