<template>

  <div id="app">
    <header>
      <div class="oneline">
        <router-link to="/" id="link">
          <img class="logoimg" src="@/assets/logo.svg" alt="main">
        </router-link>
        <div class="yestoken" v-if="token? false : true ">
          <img src="@/assets/signupbtn.svg" alt="signup" @click="goSignup">
          <a><img src="@/assets/loginbtn.svg" alt="login" @click="goLogin" class="loginbtn"></a>
          
          <!-- <button class="loginbtn"><router-link to="/login" id="link" class="loginlink">로그인</router-link></button> -->
        </div>
        <div class="notoken" v-if="token">
          <img src="@/assets/logoutbtn.svg" alt="logout" @click="logout" class="logoutlink">
          <router-link :to="{name: 'profile', params: {username : username}}" id="link">
            <img src="@/assets/UserImages.svg" alt="profile">
          </router-link>
        </div>
      </div>
      <div class="twoline">
        <div class="filter">
          <img src="@/assets/filter_list.svg" alt="filterimg">
          <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#commentMo">
            <p>필터</p>
          </button>
          <div class="modal fade" id="commentMo" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
              <div class="modal-content">
                <div class="modal-header">
                  <span class="modal-title fs-5" id="commentLabel">필터</span>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modalbody">
                  <div class="modalcontext">
                    <p>장르</p>
                    <div class="genres">
                      <button>판타지</button>
                      <button>공포</button>
                      <button>모험</button>
                      <button>역사</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="search">
          <form class="d-flex" role="search" @submit="searchMovie">
            <input id="searchinput" v-model="query" class="form-control me-2" type="search" placeholder="영화 제목 입력" aria-label="Search" maxlength="27">
            <img src="@/assets/search.svg" alt="search" id="searchbtn" @click="searchMovie">
          </form>        
        </div>
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
  /* text-align: center; */
  /* color: #2c3e50; */
  background-color: #F2F0EA !important;
  height: 3000px;

}

.modalbody {
  display: flex;
flex-direction: column;
/* align-items: flex-start; */
padding: 24px 24px 40px;
gap: 10px;

width: 480px;
height: 134px;
/* overflow-y: scroll; */


/* Inside auto layout */

flex: none;
order: 1;
align-self: stretch;
flex-grow: 0;
}

.modalcontext{
display: flex;
/* flex-direction: column; */
/* align-items: flex-start; */
padding: 0px;
gap: 16px;

width: 300px;
height: 70px;


/* Inside auto layout */

/* flex: none;
order: 0;
align-self: stretch;
flex-grow: 0; */
}

.modalcontext p {
width: 30px;
height: 22px;

/* MO/16/Bold */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 16px;
line-height: 21px;
/* identical to box height, or 133% */

display: flex;
align-items: center;
text-align: center;

color: #000000;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

#commentLabel {
width: 45px;
height: 32px;

/* PC/24 */

font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 24px;
line-height: 32px;
/* identical to box height, or 133% */

/* M3/sys/light/on-surface-variant */

color: #49454F;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

header {
display: flex;
flex-direction: column;
justify-content: center;
align-items: flex-end;
padding: 40px 156px;
gap: 32px;

/* position: absolute; */
width: 1440px;
height: 206px;
left: 0px;
top: 0px;

background: #F2F0EA;
}

.contents {
/* position: absolute; */
width: 1440px;
height: 1447px;
left: 0px;
top: 206px;
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

.modalbody img {
  width: 480px;
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

.twoline {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 0px;
  gap: 32px;

  width: 1128px;
  height: 48px;


  /* Inside auto layout */

  flex: none;
  order: 1;
  align-self: stretch;
  flex-grow: 0;
}

.filter {
display: flex;
flex-direction: row;
align-items: center;
padding: 0px;
gap: 8px;

width: 62px;
height: 24px;


/* Inside auto layout */

flex: none;
order: 0;
flex-grow: 0;
}

.filter p {
  width: 30px;
  height: 22px;
  margin-bottom: 0;

  /* MO/16/Bold */

  font-family: 'Spoqa Han Sans Neo';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 21px;
  /* identical to box height, or 133% */


  color: #000000;


  /* Inside auto layout */

  flex: none;
  order: 1;
  flex-grow: 0;
}
</style>
