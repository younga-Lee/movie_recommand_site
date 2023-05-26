<template>
  <div class="nowishlist">
    <p class="nowish">영화를 주문해주세요!</p>
    <img src="@/assets/nowish.svg" alt="nowish">
  </div>
</template>

<script>
export default {
  name: 'NoWish',

}
</script>

<style>
.nowish {
font-family: 'Spoqa Han Sans Neo';
font-style: normal;
font-weight: 700;
font-size: 22px;
line-height: 29px;
/* identical to box height, or 133% */


/* starbucks/sys/light/on-secondary-fixed */

color: #00201A;
}

.nowishlist img {
  margin: auto;
  margin-left: 400px;
}
</style>