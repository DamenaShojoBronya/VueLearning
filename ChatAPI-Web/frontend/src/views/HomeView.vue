<template>
  <el-container>
    <el-carousel class="home" :interval="4000" type="card" height="200px">
      <el-carousel-item v-for="item in 6" :key="item">
        <h3 text="2xl" justify="center">{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>
  </el-container>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  }
}
</script>
<!--  <div data-v-9ea40744="" class="el-carousel el-carousel--horizontal el-carousel--card">
<div class="el-carousel__container" style="height: 200px;">
<button type="button" class="el-carousel__arrow el-carousel__arrow--left" style="display: none;"><i class="el-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M609.408 149.376 277.76 489.6a32 32 0 0 0 0 44.672l331.648 340.352a29.12 29.12 0 0 0 41.728 0 30.592 30.592 0 0 0 0-42.752L339.264 511.936l311.872-319.872a30.592 30.592 0 0 0 0-42.688 29.12 29.12 0 0 0-41.728 0z"></path></svg></i></button>
<button type="button" class="el-carousel__arrow el-carousel__arrow--right" style="display: none;"><i class="el-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><path fill="currentColor" d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z"></path></svg></i></button>
<div data-v-9ea40744="" class="el-carousel__item el-carousel__item--card" style="transform: translateX(218.31px) scale(0.83);">
<div class="el-carousel__mask" style=""></div>
<h3 data-v-9ea40744="" text="2xl" justify="center">1</h3></div>
<div data-v-9ea40744="" class="el-carousel__item el-carousel__item--card" style="transform: translateX(218.31px) scale(0.83);"><div class="el-carousel__mask" style=""></div> -->

<style scoped>
.el-container{
  background-color: white;
  justify-content: center;
}
.home{
  width:90%;
  /* min-width: 60vw; */
  background-color:antiquewhite;
}
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>