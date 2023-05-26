<template>
  <div>
    <form @submit.prevent="createComment" class="rateform">
      <div class="commentform">
        <div class="commenttitle">
          <label for="comment" class="form-label">코멘트</label>
          <hr>
        </div>

        <div class="commentcontext">
          <div class="star-rating space-x-4 mx-auto" id="stars">
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
        </div>
      </div>
      <button type="submit">
        <p>평가하기</p>
      </button>
    </form>

    <div class="commentlist">
      <div class="cltitle">
        <p>코멘트 리스트</p>
        <hr>
      </div>

      <div class="comment" v-for="comment in comments?.slice().reverse()" :key="comment.id">
        <div class="commentone">
          <a @click="goProfile(comment.username)">{{ comment.username }}</a>
          <p>평점 : {{ comment.rating }}</p>
        </div>

        <div class="commenttwo">
          <p>내용 : {{ comment.comment_content }}</p>
          <button v-if="comment.username == loginuser.username" type="button" class="btn" data-bs-toggle="modal" data-bs-target="#commentModal">
            수정
          </button>
          <button v-if="comment.username == loginuser.username" @click="deleteComment(comment.id)">삭제</button>
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
                    <textarea class="form-control" id="editcomment" rows="3" v-model="editcontent"></textarea>
                    <button type="submit" class="editbtn">
                      <p>수정하기</p>
                    </button>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <!-- 버튼 누르면 수정할 수 있는 모달이 나와서 form 제출하도록 만들기 -->
        </div>
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
.rateform {
width: 1128px;
height: 448px;
margin: auto;
}

.commenttitle {
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

.commenttitle label {
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

.commenttitle hr {
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

.rateform button {
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
padding: 12px 24px;
gap: 6px;
margin-top: 40px;
margin-left: 1025px;

width: 104px;
height: 46px;

background: #3C4043;
/* Shadow/XSM */

box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
border-radius: 100px;
}

.rateform p {
width: 70px;
height: 22px;

/* Text Button/Semibold Large */

font-family: 'Inter';
font-style: normal;
font-weight: 600;
font-size: 15px;
line-height: 22px;
/* identical to box height, or 147% */


/* Base/White */

color: #FFFFFF;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.commentcontext {
width: 1128px;
height: 264px;


/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 0;
}

#comment {
box-sizing: border-box;

/* Auto layout */

display: flex;
flex-direction: row;
align-items: flex-start;
padding: 24px 16px;
gap: 8px;
margin-top: 20px;

width: 1128px;
height: 200px;

/* starbucks/white */

background: #FFFFFF;
/* starbucks/ref/neutral/neutral87 */

border: 1px solid #DBDAD3;
/* Shadow/XSM */

box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
border-radius: 24px;
}

.editcomment {
box-sizing: border-box;

/* Auto layout */

display: flex;
flex-direction: row;
align-items: flex-start;
padding: 24px 16px;
gap: 8px;
margin-top: 20px;

width: 450px;
height: 200px;

/* starbucks/white */

background: #FFFFFF;
/* starbucks/ref/neutral/neutral87 */

border: 1px solid #DBDAD3;
/* Shadow/XSM */

box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
border-radius: 24px;
}

.commentform {
display: flex;
flex-direction: column;
justify-content: center;
align-items: flex-start;
padding: 0px;
gap: 40px;

width: 1128px;
height: 362px;
}

.commentlist {
display: flex;
flex-direction: column;
align-items: flex-start;
padding: 0px;
gap: 24px;
}

.cltitle {
display: flex;
flex-direction: column;
align-items: flex-start;
padding: 0px;
gap: 24px;
margin: auto;

width: 1128px;
height: 58px;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.cltitle p {
width: 138px;
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

.cltitle hr {

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

.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
  margin-left: 0 !important;
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
  /* border: solid;
  width: 800px;
  margin-bottom: 20px; */
display: flex;
flex-direction: column;
align-items: flex-start;
padding: 40px 24px;
gap: 16px;
margin: auto;

width: 1128px;
height: 144px;

/* starbucks/sys/light/surface-container-high */

background: #E9E8E1;
border-radius: 24px;

/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 0;
}

.comment p {
  margin-bottom: 0 !important;
  width: 338px;
height: 24px;

/* MO/16/Regular */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 24px;
/* identical to box height, or 150% */


/* starbucks/ref/neutral/neutral20 */

color: #30312C;


/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 0;
}

.commentone {
display: flex;
flex-direction: row;
align-items: flex-start;
padding: 0px;
gap: 16px;

width: 158px;
height: 24px;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.commenttwo {
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

.commenttwo p {
width: 338px;
height: 24px;

/* MO/16/Regular */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 24px;
/* identical to box height, or 150% */


/* starbucks/ref/neutral/neutral20 */

color: #30312C;
/* identical to box height, or 133% */


/* starbucks/ref/neutral/neutral20 */

color: #30312C;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.commenttwo button {
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
padding: 12px 18px;
gap: 6px;

width: 117px;
height: 43px;

/* background: #3C4043; */
/* Shadow/XSM */

box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
border-radius: 100px;

/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 0;  
}
.commentone a {
width: 92px;
height: 22px;

/* MO/16/Bold */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 16px;
line-height: 21px;
/* identical to box height, or 133% */


/* starbucks/ref/neutral/neutral20 */

color: #30312C;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.commentone p {
width: 50px;
height: 24px;

/* MO/16/Regular */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 24px;
/* identical to box height, or 150% */


/* starbucks/ref/neutral/neutral20 */

color: #30312C;


/* Inside auto layout */

flex: none;
order: 1;
flex-grow: 0;
}

.editbtn {
margin-top: 40px;

width: 104px;
height: 46px;

background: #3C4043;
/* Shadow/XSM */

box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
border-radius: 100px;
}

.editbtn p {
color: #FFFFFF;

}
</style>