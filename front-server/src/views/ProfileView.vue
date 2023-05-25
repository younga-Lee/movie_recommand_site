<template>
  <div>
    <div class="profilecontent">
      <div class="profilehead">
        <img :src="API_URL + profileuser.image" alt="profile" id="profileimg">
        <div class="profiletext">
          <p class="profilename">{{ profileuser.username }}</p>
          <div class="followtext">
            <p>follower <span>{{ profileuser.followers_cnt }}</span> followings <span>{{ profileuser.followings.length }}</span>
            </p>
          </div>
        </div>
        <img src="@/assets/editbutton.svg" alt="edit" @click="goEdit" class="editimg" v-if="loginuser.username == profileuser.username">
        <img src="@/assets/followbtn.svg" alt="follow" @click="follow" class="editimg" 
        v-if="loginuser.username != profileuser.username && !loginuser.followings.includes(profileuser.id)">
      </div>
      <!-- <div class="header">
        <img :src="API_URL + profileuser.image" alt="profile" id="profileimg">
        <div>
          <p>{{ profileuser.username }}</p>
          <p>follower {{profileuser.followers_cnt}}  followings {{ profileuser.followings.length }}</p>
          <div v-if="!loginuser.username == profileuser.username">
            <button @click="follow" v-if="!loginuser.followings.includes(profileuser.id)">Follow</button>
            <button @click="follow" v-if="loginuser.followings.includes(profileuser.id)">Unfollow</button>
          </div>
          <button @click="goEdit" v-if="loginuser.username == profileuser.username">회원 정보 수정</button>
        </div>
      </div> -->
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
      .then(() => {
        this.getLoginuser()
        this.$router.go(this.$router.currentRoute)        
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goEdit() {
      const username = this.username
      this.$router.push({name: 'edit', params: {username: username}})
    },
    getProfileuser() {
      const username = this.username
      this.$store.dispatch('getProfileuser', username)
    },
    getLoginuser() {
      this.$store.dispatch('getLoginuser', this.$store.state.username)
    }
  },
  created() {
    this.getProfileuser()
    // console.log(this.$route.params.username)
  }
}
</script>

<style>
.profilecontent {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 16px 0px;
  gap: 32px;

  position: absolute;
  width: 1440px;
  height: 670px;
  left: 0px;
  top: 206px;
}

.profilehead {
display: flex;
flex-direction: column;
align-items: center;
padding: 0px;
gap: 40px;

width: 552px;
height: 310px;

/* Inside auto layout */
flex: none;
order: 0;
flex-grow: 0;
}

.profiletext {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0px;
  gap: 12px;

  width: 552px;
  height: 80px;


  /* Inside auto layout */

  flex: none;
  order: 1;
  flex-grow: 0;
}

.profilename {
  width: 552px;
  height: 44px;

  /* MO/36/Bold */
  font-family: 'Spoqa Han Sans Neo';
  font-style: normal;
  font-weight: 700;
  font-size: 36px;
  line-height: 43px;

  /* identical to box height, or 120% */
  text-align: center;

  /* starbucks/sys/light/on-secondary-fixed */
  color: #00201A;

  /* Inside auto layout */
  flex: none;
  order: 0;
  flex-grow: 0;
}

.header {
  text-align: left !important;
  display: flex;
  vertical-align: bottom;
}

#profileimg {
  width: 120px;
  height: 120px;
}

#wishlist {
  width: 80%;
}

.followtext {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 0px;
  gap: 8px;

  width: 111px;
  height: 24px;


  /* Inside auto layout */

  flex: none;
  order: 0;
  flex-grow: 0;
}

.editimg {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 0px;
  gap: 16px;

  width: 127px;
  height: 46px;


  /* Inside auto layout */

  flex: none;
  order: 1;
  flex-grow: 0;
}
</style>