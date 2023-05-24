<template>

  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light">
        <router-link to="/" id="link">
          <img src="@/assets/title.png" alt="main">
        </router-link>
      <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <form class="d-flex" role="search" @submit="searchMovie">
              <input v-model="searchword" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            <div class="float-end" v-if="!token">
              <router-link to="/login" id="link">Login</router-link> 
              <router-link to="/signup" id="link">Signup</router-link>
            </div>
            <div class="float-end" v-else>
              <button @click="logout">Logout</button>
              <!-- <router-link @click="logout" id="link">Logout</router-link> -->
              <router-link :to="{name: 'profile', params: {username : user.username}}" id="link">
                <img :src="user.img" alt="profile">
                <span>{{ user.username }}</span>
              </router-link>
            </div>
          </ul>
        </div>
      </div>
    </nav>    
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      searchword: null,
    }
  },
  methods: { 
    searchMovie() {
      const word = this.searchword
      console.log(word)

      if (word) {
        this.$router.push({name: 'search', params: {word: word}})
        this.searchword = null
      } else {
        alert('검색어를 입력해주세요')
      }
    },
    logout() {
      this.$store.dispatch('logout')
    }
  }, 
  computed: {
    token() {
      return this.$store.state.token
    },
    user() {
      return this.$store.state.user
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.rl {
  display: flex;
  font-size: x-large;
  align-items: center;
}

#link {
  margin-right: 8px;
  margin-left: 8px;
}
</style>
