<template>
  <div>
    <div id="rateform">
      <h2>평점 남기기</h2>
      <form action="">
        <label for="comment" class="form-label"><p>Comment</p></label>
        <textarea class="form-control" id="comment" rows="3"></textarea>
      </form>
      <p>코멘트 리스트</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieRated'
}
</script>

<style>
#comment {
  width: 1000px;
}

#rateform {
  text-align: left;
  margin-left: 20px;
}
</style>