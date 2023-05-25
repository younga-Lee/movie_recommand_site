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
      <div class="comment" v-for="comment in comments?.slice().reverse()" :key="comment.id">
        <p>내용 : {{ comment.comment_content }}</p>
        <p>평점 : {{ comment.rating }}</p>
        <a @click="goProfile(comment.username)">{{ comment.username }}</a>
        <p @click="goProfile(comment.username)">작성자 : {{ comment.username }}</p>
        <button v-if="comment.username == loginuser.username" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#commentModal">
          수정하기
        </button>
        <div class="modal fade" id="commentModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="commentModalLabel">코멘트 수정하기</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <form @submit.prevent="editComment(comment.id)">
                  <label for="comment" class="form-label"><h3>코멘트</h3></label>
                  <div class="star-rating space-x-4 mx-auto">
                    <input type="radio" id="5-edits" name="rating" value="5" v-model="editratings"/>
                    <label for="5-edits" class="star pr-4">★</label>
                    <input type="radio" id="4-edits" name="rating" value="4" v-model="editratings"/>
                    <label for="4-edits" class="star">★</label>
                    <input type="radio" id="3-edits" name="rating" value="3" v-model="editratings"/>
                    <label for="3-edits" class="star">★</label>
                    <input type="radio" id="2-edits" name="rating" value="2" v-model="editratings"/>
                    <label for="2-edits" class="star">★</label>
                    <input type="radio" id="1-edits" name="rating" value="1" v-model="editratings" />
                    <label for="1-edits" class="star">★</label>
                  </div>
                  <textarea class="form-control" id="comment" rows="3" v-model="editcontent"></textarea>
                  <button type="submit" class="btn btn-primary">수정하기</button>
                </form>
              </div>
            </div>
          </div>
        </div>
        <!-- 버튼 누르면 수정할 수 있는 모달이 나와서 form 제출하도록 만들기 -->
        <button v-if="comment.username == loginuser.username" @click="deleteComment(comment.id)">삭제하기</button>
      </div>
    </div>
    <!-- {{ commentlist }} -->
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
      editcontent: null,
      editratings: null,
      url: `http://127.0.0.1:8000/profile/${this}`
    }
  },
  props: {
    movie: Object,
    comments: Array,
  },
  computed: {
    loginuser() {
      return this.$store.state.loginuser
    }
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
    deleteComment(comment_pk) {
      const movie_id = this.movie.id

      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/movies/${movie_id}/comments/${comment_pk}/`,
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
    editComment(comment_pk) {
      const movie_id = this.movie.id
      const rating = this.editratings
      const comment_content = this.editcontent

      axios({
        method: 'PUT',
        url: `${API_URL}/api/v1/movies/${movie_id}/comments/${comment_pk}/`,
        data: { rating, comment_content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }         
      })
      .then(() => {
        this.$router.go(this.$router.currentRoute)
      })
      .catch((err) => {
        console.log(err)
        console.log(comment_pk)
      })
    },
    goProfile(username) {
      this.$store.dispatch('getProfileuser', username)
      this.$router.push({name: 'profile', params: {username:username}})
      
    }
  },
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