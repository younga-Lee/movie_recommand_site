<template>

  <div id="app">
    <header>
      <div class="oneline">
        <router-link to="/" id="link">
          <img class="logoimg" src="@/assets/logo.svg" alt="main">
        </router-link>
        <div class="yestoken" v-if="token? false : true ">
          <img src="@/assets/signupbtn.svg" alt="signup" @click="goSignup">
          <img src="@/assets/loginbtn.svg" alt="login" @click="goLogin" class="loginbtn">
          <!-- <button class="loginbtn"><router-link to="/login" id="link" class="loginlink">로그인</router-link></button> -->
        </div>
        <div class="notoken" v-if="token">
          <img src="@/assets/logoutbtn.svg" alt="logout" @click="logout" class="logoutlink">
          <router-link :to="{name: 'profile', params: {username : username}}" id="link">
            <img src="@/assets/UserImages.svg" alt="profile">
          </router-link>
        </div>
      </div>
      <div class="search">
        <form class="d-flex" role="search" @submit="searchMovie">
          <input id="searchinput" v-model="query" class="form-control me-2" type="search" placeholder="영화 제목 입력" aria-label="Search" maxlength="27">
          <img src="@/assets/search.svg" alt="search" id="searchbtn" @click="searchMovie">
          <!-- <button class="btn btn-outline-success" type="submit">Search</button> -->
        </form>        
      </div>
    </header>
    <div class="contents">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      query: null,
    }
  },
  methods: { 
    searchMovie() {
      const query = this.query

      if (query) {
        this.$router.push({name: 'search', params: {word:query}})
        this.$router.go(this.$router.currentRoute)        
        this.query = null
      } else {
        alert('검색어를 입력해주세요')
      }
    },
    logout() {
      this.$store.dispatch('logout')
    },
    goSignup() {
      this.$router.push({name: 'signup'})
    },
    goLogin() {
      this.$router.push({name: 'login'})
    },
  }, 
  computed: {
    token() {
      return this.$store.state.token
    },
    username() {
      return this.$store.state.username
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
  background: #F2F0EA !important;
}

header {
  background: #F2F0EA;
  /* Auto layout */

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
  padding: 40px 156px;
  gap: 32px;

  /* position: absolute; */
  /* width: 1440px; */
  height: 206px;
  left: 0px;
  top: 0px;
}

.contents {
  /* position: absolute; */
  /* width: 1440px; */
  height: 1447px;
  left: 0px;
  top: 206px;
  background: #F2F0EA;
  padding: 50px;
  padding-top: 0;
}

.logoimg {
  /* logo */
  width: 264px;
  height: 31px;

  /* Inside auto layout */
  flex: none;
  order: 0;
  flex-grow: 0;
}

.oneline {
  /* Auto layout */
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 0px;
  gap: 706px;
  width: 1128px;
  height: 46px;

  /* Inside auto layout */
  flex: none;
  order: 0;
  align-self: stretch;
  flex-grow: 0;
}

.signuplink {
  width: 56px;
  height: 22px;

  /* Text Button/Semibold Large */
  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-size: 15px;
  line-height: 22px;

  /* identical to box height, or 147% */
  color: #006240;

  /* Inside auto layout */
  flex: none;
  order: 0;
  flex-grow: 0;
}

.yestoken {
  /* Auto layout */

  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  padding: 0px;
  gap: 24px;

  width: 158px;
  height: 46px;


  /* Inside auto layout */

  flex: none;
  order: 1;
  flex-grow: 0;
}

.loginlink {
  width: 42px;
  height: 22px;

  /* Text Button/Semibold Large */
  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-size: 15px;
  line-height: 22px;
  
  /* Base/White */
  color: #FFFFFF;

  /* Inside auto layout */
  flex: none;
  order: 0;
  flex-grow: 0;
}

.logoutlink {
  width: 56px;
  height: 22px;

  /* Text Button/Semibold Large */

  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-size: 15px;
  line-height: 22px;
  /* identical to box height, or 147% */


  /* starbucks/ref/neutral/neutral60 */
  color: #91918A;

  /* Inside auto layout */
  flex: none;
  order: 0;
  flex-grow: 0;
}

.rl {
  display: flex;
  font-size: x-large;
  align-items: center;
}

#link {
  margin-right: 8px;
  margin-left: 8px;
  text-decoration-line: none;
}

.loginbtn {
  width: 78px;
  height: 46px;

  background: #006240;
  /* Shadow/XSM */

  box-shadow: 0px 1px 2px rgba(16, 24, 40, 0.04);
  border-radius: 100px;

  /* Inside auto layout */

  flex: none;
  order: 1;
  flex-grow: 0;
  transform: scale(1.2);
  transition-duration: 0.2s;
  

}

button {
  border: none;
}

.search {
  position: relative;
  width: 299px;
  height: 48px;
}

#searchbtn {
  position: absolute;
  right: 20px;
  top: 10px;
}

#searchinput {
  padding-right: 30px;
  border: 1px solid #EFEEE6;
  border-radius: 100px;
}

.notoken {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  padding: 0px;
  gap: 24px;

  width: 120px;
  height: 40px;


  /* Inside auto layout */

  flex: none;
  order: 1;
  flex-grow: 0;  
}

</style>
