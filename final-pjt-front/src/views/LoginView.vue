<template>
  <div>
    <div class="signupForm">
      <div class="formtitle">
        <p class="title1">로그인</p>
        <p class="title2">씨네벅스에 오신 것을 환영합니다! 로그인 후 이용해주세요!</p>
      </div>
      <form id="formbody" @submit.prevent="login">
        <div class="inputbox">
          <div id="inputusername">
            <label for="username" class="form-label" id="nameform">이름 *</label>
            <input type="text" class="form-control" id="username" v-model="username" required placeholder="aiden">
          </div>

          <div class="col-12" id="passwordsection">
            <div class="password1">
              <label for="inputpassword" class="form-label" id="passform">비밀번호 *</label>
              <input
              v-model="password"
              type="password" class="form-control" 
              id="inputpassword" placeholder="비밀번호">
            </div>
          </div>

          <button class="upbtn">
            <span>로그인</span>
          </button>
        </div>
      </form>    
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    }
  }
}
</script>

<style scoped>
.title2 {
  text-align: center;
}

#inputpassword {
  width: 552px;
}

</style>