<template>
  <div>
    <div id="rateform">
      <h2>평점 남기기</h2>
      <form @submit.prevent="createComment" class="commentform">
        <label for="comment" class="form-label"><h3>코멘트</h3></label>
        <div class="star-rating space-x-4 mx-auto">
          <input type="radio" id="5-stars" name="rating" value="5" v-model="ratings"/>
          <label for="5-stars" class="star pr-4">★</label>
          <input type="radio" id="4-stars" name="rating" value="4" v-model="ratings"/>
          <label for="4-stars" class="star">★</label>
          <input type="radio" id="3-stars" name="rating" value="3" v-model="ratings"/>
          <label for="3-stars" class="star">★</label>
          <input type="radio" id="2-stars" name="rating" value="2" v-model="ratings"/>
          <label for="2-stars" class="star">★</label>
          <input type="radio" id="1-star" name="rating" value="1" v-model="ratings" />
          <label for="1-star" class="star">★</label>
        </div>
        <textarea class="form-control" id="comment" rows="3" v-model="content"></textarea>
        <input type="submit" value="등록하기">
      </form>
      <h3>코멘트 리스트</h3>
      <div class="comment" v-for="comment in comments" :key="comment.id">
        <p>내용 : {{ comment.comment_content }}</p>
        <p>평점 : {{ comment.rating }}</p>
        <p>작성자 : {{ comment.username }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieRated',
  data() {
    return {
      content: null,
      ratings: null,
    }
  },
  props: {
    movie: Object,
    comments: Array,
  },
  methods: {
    createComment() {
      const rating = this.ratings
      const comment_content = this.content
      const movie_id = this.movie.id

      if (!comment_content) {
        alert('내용을 입력해주세요')
        return
      } else if (!rating) {
        alert('평점을 매겨주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${movie_id}/comments/`,
        data: {rating, comment_content},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        } 
      })
      .then(() => {
        this.$router.go(this.$router.currentRoute)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
  }
}
</script>

<style>
#comment {
  width: 95%;
  margin: auto;
  margin-top: 20px;
  margin-bottom: 20px;
  resize: none;
}

.commentform {
  border: solid;
  width: 800px;
  padding: 10px;
}

.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}
 
.star-rating input {
  display: none;
}
 
.star-rating label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 2.3px;
  -webkit-text-stroke-color: #2b2a29;
  cursor: pointer;
}
 
.star-rating :checked ~ label {
  -webkit-text-fill-color: gold;
}
 
.star-rating label:hover,
.star-rating label:hover ~ label {
  -webkit-text-fill-color: #fff58c;
}

.comment {
  border: solid;
  width: 800px;
  margin-bottom: 20px;
}

</style>