<template>
  <div>
    <div class="header">
      <img src="@/assets/logo.png" alt="profile" id="profileimg">
      <div>
        <p>{{ user.username }}</p>
        <p>follower 2.3k  followings 3</p>
      </div>
    </div>
    <div id="wishlist" class="border">
      <h2>WishList</h2>
      <div>
        <br><br><br><br>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  computed: {
    user() {
      return this.$route.params.user
    },    
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