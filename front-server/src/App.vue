<template>

  <div id="app">
    <nav>
      <!-- <img src="@/assets/ssafy.png" alt="" style="width: 150px; height: 90px;" id="ssafyimg"> -->
      <div class="rl">
        <!-- <router-link to="/" id="link">Home</router-link> -->
        <router-link to="/" id="link">
          <img src="@/assets/title.png" alt="main">
        </router-link> 
        <!-- <router-link to="/random" id="link">Random</router-link> 
        <router-link to="/watch-list" id="link">WatchList</router-link> -->
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  /* padding: 30px; */
  /* background-color: #cce8f4; */
  display: flex;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

#ssafyimg {
  /* display: flex; */
  margin-top: 10px;
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
