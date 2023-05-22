<template>
  <div>
    <form @submit.prevent="addMovie">
      <br><br><br><br>
      <h1>보고싶은 영화</h1>
      <br>
      <input type="text" v-model="title">
      <button>Add</button>
      <br><br><br><br>

    </form>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'WatchListForm',
  data() {
    return {
      title: '',
    }
  },
  methods: {
    addMovie() {
      const title = this.title
      this.$store.dispatch('addMovie', title)
      this.title = null
    }
  }
}
</script>

<style scoped>
button {
  background-color: #cce8f4;
  border-radius: 10px;
  font-size: 24px;
}

input {
  border-radius: 10px;
  font-size: 24px;
}
</style>