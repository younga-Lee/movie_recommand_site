<template>
  <div id="noresult">
    <div style="text-align:center">
      <img src="@/assets/noresult.gif" alt="GIFimg" id="gif">
    </div>

    <div class="noresulttext">
      <p id="nrt1">{{ word }}에 대한 결과가 없습니다</p>
      <p id="nrt2">다른 검색어로 검색해보세요</p>
    </div>

    <div class="nrcontent">
      <p>이런 영화는 어떠세요?</p>
      <div class="row row-cols-3 row-cols-md-5 g-4">
        <div class="col" v-for="movie in popularList" :key="movie.pk">
          <img :src="imgurl + movie.poster_path" class="card-img-top" alt="poster"
          id="posterimg" @click="goDetail(movie.pk)">
        </div>
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
#gif {
  width: 360px;
  height: 285px;
}

.noresulttext {
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
padding: 0px;
gap: 16px;
}

#nrt1 {
  width: 414px;
height: 39px;

/* PC/32 */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 32px;
line-height: 39px;
/* identical to box height, or 122% */


/* starbucks/ref/neutral/neutral17 */

color: #292A26;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

#nrt2 {
  width: 184px;
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
order: 1;
flex-grow: 0;
}

.nrcontent {
width: 1320px;
height: 562px;

margin: auto;
margin-top: 50px;
}

.nrcontent p {
font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 22px;
line-height: 29px;
/* identical to box height, or 133% */


/* starbucks/sys/light/on-secondary-fixed */

color: #00201A;
}
</style>