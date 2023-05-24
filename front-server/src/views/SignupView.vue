<template>
  <div>
    <form class="row g-3" id="signupform" @submit.prevent="signUp" enctype="multipart/form-data">
      <h1>
        <img src="@/assets/coffee.png" alt="logo">
        회원가입
      </h1>
      <div class="col-md-4">
        <label for="username" class="form-label">Username : </label>
        <input type="text" class="form-control" id="username" v-model="username"
        aria-describedby="inputGroupPrepend2" required>
      </div>

      <div class="col-12">
        <label for="inputpassword" class="form-label">Password</label>
        <input
        v-model="password1" @input="lengthCheck" 
        type="password" class="form-control" 
        id="inputpassword" placeholder="password">
        <p v-if="!long">비밀번호를 4자리 이상 입력해주세요</p>
      </div>

      <div class="col-12">
        <label for="password2" class="form-label">Password Check</label>
        <input v-model="password2" type="password" class="form-control" id="password2" placeholder="password">
      </div>
      
      <div class="col-12">
        <label for="image"></label>
        <input type="file" @change="fileUpload" ref="profileimg" id="image" class="form-control" aria-label="file example">
      </div>

      <div class="col-12" id="sbmbtn">
        <button type="submit" class="btn btn-success">Sign Up</button>
      </div>
    </form>    
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      img: null,
      long: '',
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
      this.img = this.$refs.profileimg.files
      console.log(this.img)
    },
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const img = this.img

      if (this.password1 != this.password2) {
        alert('비밀번호를 다시 확인해주세요')
      } else {
        const payload = {
          username, password1, password2, img
        }
        
        this.$store.dispatch('signUp', payload)
      }
    },
  }
}
</script>

<style>
#signupform {
  background-color: #A5DF00;
  width: 500px;
  margin: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#signupform h1 {
  width: 500px;
  text-align: center;
  margin: auto;
  margin-top: 20px;
  margin-bottom: 20px;
}

#sbmbtn {
  margin-bottom: 20px;
}
</style>