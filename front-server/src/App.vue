<template>

  <div id="app">
    <header>
      <div class="oneline">
        <router-link to="/" id="link">
          <img class="logoimg" src="@/assets/logo.svg" alt="main">
        </router-link>
        <div class="yestoken" v-if="token? false : true ">
          <router-link to="/signup" id="link" class="signuplink">회원가입</router-link>
          <button class="loginbtn"><router-link to="/login" id="link" class="loginlink">로그인</router-link></button>
        </div>
        <div class="notoken" v-if="token">
          <button @click="logout" class="logoutlink">로그아웃</button>
          <router-link :to="{name: 'profile', params: {username : username}}" id="link">
            <img  src="@/assets/UserImages.svg" alt="profile">
          </router-link>
        </div>
      </div>
      <div class="search">
        <form class="d-flex" role="search" @submit="searchMovie">
          <input id="searchinput" v-model="searchword" class="form-control me-2" type="search" placeholder="영화 제목 입력" aria-label="Search" maxlength="27">
          <img src="@/assets/search.svg" alt="search" id="searchbtn" @click="searchMovie">
          <!-- <button class="btn btn-outline-success" type="submit">Search</button> -->
        </form>        
      </div>
    </header>
    <!-- <nav class="navbar navbar-expand-lg">
        <router-link to="/" id="link">
          <img src="@/assets/logo.svg" alt="main">
        </router-link>
      <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <form class="d-flex" role="search" @submit="searchMovie">
              <input v-model="searchword" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            <button class="loginbtn">로그인</button>
            <div class="float-end" v-if="!token">
              <router-link to="/login" id="link">Login</router-link> 
              <router-link to="/signup" id="link">Signup</router-link>
            </div>
            <div class="float-end" v-else>
              <button @click="logout">Logout</button>
              <router-link :to="{name: 'profile', params: {username : username}}" id="link">
                <img src="@/assets/profile.png" alt="profile">
                <span>{{ username }}</span>
              </router-link>
            </div>
          </ul>
        </div>
      </div>
    </nav>     -->
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
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 12px 18px;
  gap: 6px;

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
</style>
