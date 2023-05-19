<template>
  <div>
    <form class="row g-3" id="signupform" @submit.prevent="signUp">
      <h1>
        <img src="@/assets/coffee.png" alt="logo">
        회원가입
      </h1>
      <div class="col-md-4">
        <label for="validationDefaultUsername" class="form-label">Username</label>
        <input type="text" class="form-control" id="validationDefaultUsername"  aria-describedby="inputGroupPrepend2" required>
      </div>
      <div class="col-md-6">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email">
      </div>
      <div class="col-12">
        <label for="inputpassword" class="form-label">Password</label>
        <input
        v-model="password" @input="lengthCheck" 
        type="password" class="form-control" 
        id="inputpassword" placeholder="password">
        <p v-if="!long">비밀번호를 4자리 이상 입력해주세요</p>
      </div>
      <div class="col-12">
        <label for="checkpassword" class="form-label">Password Check</label>
        <input v-model="checkpassword" type="password" class="form-control" id="checkpassword" placeholder="password">
      </div>
      <div class="col-12" id="sbmbtn">
        <button type="submit" class="btn btn-success">Sign in</button>
      </div>
    </form>    
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      password: null,
      checkpassword: null,
      long: '',
    }
  },
  methods: {
    lengthCheck() {
      if (this.password.length < 5) {
        this.long = false
      } else {
        this.long = true
      }
    },
    signUp() {
      if (this.password != this.checkpassword) {
        alert('비밀번호를 다시 확인해주세요')
      } else {
        this.$router.push({name: 'main'})
      }
    }
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