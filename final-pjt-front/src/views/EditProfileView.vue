<template>
  <div>
    <form class="row g-3" id="signupform" @submit.prevent="editProfile" enctype="multipart/form-data">
      <h1>
        <img src="@/assets/coffee.png" alt="logo">
        회원정보 수정
      </h1>
      
      <div class="col-12">
        <label for="inputpassword" class="form-label">Password</label>
        <input
        v-model="password1" @input="lengthCheck" 
        type="password" class="form-control" 
        id="inputpassword" placeholder="password">
        <p v-if="!long">비밀번호를 4자리 이상 입력해주세요</p>
      </div>

      <!-- <div class="col-12">
        <label for="password2" class="form-label">Password Check</label>
        <input v-model="password2" type="password" class="form-control" id="password2" placeholder="password">
      </div> -->
      
      <div class="col-12">
        <label for="image"></label>
        <input type="file" @change="fileUpload" ref="profileimg" id="image" class="form-control" aria-label="file example">
      </div>

      <div class="col-12" id="sbmbtn">
        <button type="submit" class="btn btn-success">수정하기</button>
      </div>
    </form>    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'EditProfile',
  data() {
    return {
      username: null,
      password1: null,
      // password2: null,
      image: null,
      long: null,
    }
  },
  methods: {
    lengthCheck() {
      if (this.password1.length < 5) {
        this.long = false
      } else {
        this.long = true
      }
    },
    fileUpload() {
      this.image = this.$refs.profileimg.files
      console.log(this.image)
    },
    editProfile() {
      const formData = new FormData();
      formData.append('password1', this.password1);
      formData.append('image', this.image);

      axios({
        method: 'put',
        url: `${API_URL}/profile/edit/${this.state.username}`,
        headers: {
          Authorization: `Token ${this.state.token}`,
          'Content-Type': 'multipart/form-data',
        },
        data: formData,
      })   
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        })
    },
  }
}
</script>

<style>

</style>