<template>
  <div>
    <div id="rateform">
      <h2>평점 남기기</h2>
      <form @submit.prevent="createComment">
        <label for="comment" class="form-label"><p>Comment</p></label>
        <textarea class="form-control" id="comment" rows="3" v-model="content"></textarea>
        <input type="submit" value="작성하기">
      </form>
      <p>코멘트 리스트</p>
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
      movieRate: null,
    }
  },
  methods: {
    createComment() {
      const content = this.content

      if (!content) {
        alert('내용을 입력해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/<int:movie_id>/comments/`,
        data: {content},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        } 
      })
    }
  }
}
</script>

<style>
#comment {
  width: 1000px;
}

#rateform {
  text-align: left;
  margin-left: 20px;
}
</style>