<template>
  <div>
    <form id="loginform">
      <div class="row mb-3">
        <label for="inputEmail4" class="form-label">ID</label>
        <input type="email" class="form-control" id="inputEmail4">
      </div>
      <div class="row mb-3">
        <label for="inputPassword4" class="form-label">Password</label>
        <input type="password" class="form-control" id="inputPassword4">
      </div>
      <button type="submit" class="btn btn-primary">Sign in</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView'
}
</script>

<style>
#loginform {
  width: 500px;
  height: 500px;
  margin: auto;
  margin-top: 100px;
}

label {
  text-align: left;
}

</style>