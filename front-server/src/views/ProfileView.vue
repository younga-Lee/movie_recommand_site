<template>
  <div>
    <div>
      <div class="header">
        <!-- <img src="@/assets/logo.png" alt="profile" id="profileimg"> -->
        <img :src="API_URL + profileuser.image" alt="profile" id="profileimg">
        <div>
          <p>{{ profileuser.username }}</p>
          <p>follower 2.3k  followings {{ profileuser.followings.length }}</p>
          <button @click="follow" v-if="profileuser.username != loginuser.username">Follow</button>
        </div>
      </div>
      <div id="wishlist" class="border">
        <h2>WishList</h2>
        <div>
          <br><br><br><br>
        </div>
      </div>
    </div>
    <!-- <div>
      <h1>없는 회원입니다</h1>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'ProfileView',
  data() {
    return {
      API_URL: 'http://127.0.0.1:8000'
    }
  },
  computed: {
    username() {
      return this.$route.params.username
    },    
    profileuser() {
      return this.$store.state.profileuser
    },
    loginuser() {
      return this.$store.state.loginuser
    },
  },
  methods: {
    follow() {
      const username = this.username
      console.log(username)

      axios({
        method: 'POST',
        url: `${API_URL}/profile/${username}/follow/`,
        data: {username},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }        
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getProfileuser() {
      const username = this.username
      this.$store.dispatch('getProfileuser', username)
    },
  },
  created() {
    this.getProfileuser()
    // console.log(this.$route.params.username)
  }
}
</script>

<style>
.header {
  text-align: left !important;
  display: flex;
  vertical-align: bottom;
}

#profileimg {
  width: 200px;
}

#wishlist {
  width: 80%;
}
</style>