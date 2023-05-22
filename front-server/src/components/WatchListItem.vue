<template>
  <div>
    <p v-for="watch in watchlist" :key="watch.title" :class="{canceled:cancellist.includes(watch.title)}" @click="cancelmovie(watch.title)">
      {{ watch.title }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  data(){
    return {
      cancellist : [],
    }
  },
  computed : {
    watchlist() {
      return this.$store.state.watchlist
    }
  }
  ,
  methods:{
    cancelmovie(title) {
      this.cancellist.push(title)
    }
  },
  created() {
    this.$store.dispatch('loadMessage')
  }
}
</script>

<style scoped>
  .canceled{
    text-decoration: line-through;
    background-color: grey;
  }

  p {
    height: 100px;
    font-size: 24px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgb(235, 233, 233);
    margin-bottom: 0;
  }
</style>