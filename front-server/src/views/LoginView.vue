<template>
  <div>
    <form id="loginform" @submit.prevent="login">
      <div class="row mb-3">
        <label for="username" class="form-label">username</label>
        <input type="text" class="form-control" id="username" v-model="username">
      </div>

      <div class="row mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" v-model="password">
      </div>

      <button type="submit" class="btn btn-primary">Sign in</button>
    </form>
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

<style>
#loginform {
  width: 500px;
  height: 500px;
  margin: auto;
  margin-top: 100px;
}

label {
  text-align: left;
}

</style>