<template>
  <div>
    <div class="profilecontent">
      <div class="profilehead">
        <img :src="API_URL + profileuser.image" alt="profile" id="profileimg">
        <div class="profiletext">
          <p class="profilename">{{ profileuser.username }}</p>
          <div class="followtext">
            <p>followers</p>
            <p>{{ profileuser.followers_cnt }}</p>
            <p>followings</p>
            <p>{{ profileuser.followings.length }}</p>
          </div>
        </div>
        <img src="@/assets/editbutton.svg" alt="edit" @click="goEdit" class="editimg" v-if="loginuser.username == profileuser.username">
        <img src="@/assets/followbtn.svg" alt="follow" @click="follow" class="editimg" 
        v-if="loginuser.username != profileuser.username && !loginuser.followings.includes(profileuser.id)">
      </div>
      <div id="wishlist" class="border">
        <WishList 
        v-if="profileuser.likes_movies[0]"
        :wishList="wishlist"
        />
        <NoWish 
        v-if="!profileuser.likes_movies[0]"
        />
      </div>
    </div>
    <!-- <div>
      <h1>없는 회원입니다</h1>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios'
import WishList from '@/components/ProfileView/WishList'
import NoWish from '@/components/ProfileView/NoWish'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'ProfileView',
  components: {
    WishList,
    NoWish
  },
  data() {
    return {
      API_URL: 'http://127.0.0.1:8000',
      profileuser: null,
      wishlist: null,
    }
  },
  computed: {
    username() {
      return this.$route.params.username
    },    
    // profileuser() {
    //   return this.$store.state.profileuser
    // },
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
      this.profileuser = this.$store.state.profileuser
    },
    getLoginuser() {
      this.$store.dispatch('getLoginuser', this.$store.state.username)
    },
    getWishlist() {
      this.wishlist = this.$store.state.profileuser.likes_movies
    }
  },
  created() {
    // this.getProfileuser()
    window.scrollTo(0,0)
    this.profileuser = this.$store.state.profileuser

    // this.getWishlist()
    // this.$router.go(this.$router.currentRoute)
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
  gap: 35px;

  width: 243px;
  height: 24px;


  /* Inside auto layout */

  flex: none;
  order: 1;
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