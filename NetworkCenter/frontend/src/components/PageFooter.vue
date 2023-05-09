<template>
  <footer :class="{ 'blur-background': blur }">
    <div class="footer">
      <div class="g-foot">
        <div class="wp">
          <div class="logo">
            <img src="../assets/网络中心logo-紫.png" alt="">
            <h3>计算机学院网络中心</h3>
          </div>
          <div class="list">
            <ul>
              <li>
                <div class="ico-wrap">
                  <img class="ico" src="../assets/电话.png" alt="">
                  <p>&nbsp;&nbsp;&nbsp;010-6277994</p>
                </div>
              </li>
              <li>
                <div class="ico-wrap"><img class="ico" src="../assets/邮箱.png" alt="">
                  <p>&nbsp;&nbsp;&nbsp;twinfo@jld.edu.cn</p>
                </div>
              </li>
              <li>
                <div class="ico-wrap"><img class="ico" src="../assets/位置.png" alt="">
                  <p>&nbsp;&nbsp;&nbsp;计算机学院网络中心</p>
                </div>
              </li>
            </ul>
          </div>
          <div class="info">
            <div>
              <p>版权所有 &copy; 计算机学院网络中心</p>
              <p>地址:京海市南珠区科技大道9号</p>
              <p>邮编:586000</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>



<script>
import { defineComponent } from 'vue';
import { mapState } from 'vuex';
// export default defineComponent({
//   name: 'PageFooter'
// });
export default defineComponent({
  name: 'PageFooter',
  computed: {
    ...mapState(['blur']),
  },
});
</script>

<!-- <style>
.blur-background {
  filter: blur(4px);
}

footer {
  margin-top: 50px;
  padding: 20px;
  background-color: #f2f2f2;
  font-size: 14px;
  text-align: center;
}

footer p {
  margin: 5px;
}

</style> -->

<style>
.footer {
  border-top: 1px solid #dedede;
  /* overflow: hidden; */
}

.wp {
  width: auto;
  max-width: 1500px;
  /* max-width: none; */
  padding: 0 10px;
  margin: 0 auto;
}

a {
  text-decoration: none;
  color: #444;
  -webkit-transition: .3s;
  -moz-transition: .3s;
  -ms-transition: .3s;
  -o-transition: .3s;
  transition: .3s
}

ul {
  list-style: none;
}

.foot-link .title {
  font-size: 30px
}

.foot-link .list a {
  font-size: 14px;
  line-height: 40px;
}

.foot-link {
  position: relative;
  min-height: 340px
}

.foot-link .title {
  font-size: 34px;
  color: #000;
  line-height: 1em;
  padding: 48px 0 18px
}

.foot-link .list {
  max-width: 759px;
  overflow: hidden
}

.foot-link .list li {
  float: left;
  width: 33.333%;
  padding: px 65px 0 0;
}

.ico-wrap {
  display: flex;
  justify-content: center;
  float: left
}

li .ico {
  width: 15px;
  height: 15px;
  filter: brightness(100);
}

.foot-link .list a {
  display: block;
  border-bottom: 1px solid #ddd;
  font-size: 16px;
  color: #616161;
  line-height: 45px
}

.foot-link .list a:hover {
  color: #000
}

.foot-link .ewm {
  width: 219px;
  position: absolute;
  z-index: 1;
  left: auto;
  right: 0;
  top: auto;
  bottom: -58px
}

.foot-link .ewm .pic {
  width: 100%;
  height: auto;
  margin-bottom: 14px;
  overflow: hidden
}

.foot-link .ewm .pic img {
  display: block;
  width: 100%;
  height: auto
}

.foot-link .ewm p {
  font-size: 12px;
  color: #fff;
  line-height: 1.5em;
  text-align: center;
  overflow: hidden
}


.g-foot {
  position: relative;
  color: #fff;
  font-size: 12px;
}

.g-foot a {
  color: #fff
}

.g-foot:before {
  content: "";
  display: block;
  position: absolute;
  left: 4.5%;
  bottom: 0;
  right: 0;
  height: 170px;
  background: rgb(112, 148, 203);
}

.g-foot:after {
  content: "";
  display: block;
  position: absolute;
  left: 7.1%;
  bottom: 0;
  right: 0;
  height: 100%;
  background: rgb(63, 110, 155);
}

.g-foot .wp {
  min-height: 213px;
  position: relative;
  z-index: 2
}

.g-foot .wp .logo {
  position: absolute;
  z-index: 1;
  left: 250px;
  right: auto;
  top: 46px;
  bottom: auto;
  width: 430px;
  display: flex;
  align-items: center
}

.g-foot .wp .logo img {
  max-width: 25%;
  height: auto;
}

.g-foot .wp .logo h3 {
  margin-left: 20px;
  font-size: 30px;
}

.g-foot .list {
  position: absolute;
  z-index: 1;
  left: 800px;
  right: auto;
  top: 50px;
  bottom: auto;
  width: 350px
}

.g-foot .list li {
  height: 24px;
  width: 220px;
  padding-right: 20px
}

.g-foot .list li p {
  display: inline-block;
  vertical-align: middle
}

.g-foot .info {
  margin-top: 60px;
  /* position: absolute; */
  z-index: 1;
  left: 0;
  right: 0;
  top: auto;
  bottom: 0;
  border-top: 1px solid rgba(255, 255, 255, .27);
}

.g-foot .info div {
  /* width: 1300px; */
  margin: 0 auto;
  text-align: left
}

.info p {
  display: inline-block;
  margin-left: 20px;
  opacity: .36;
  line-height: 45px;
}

.g-foot .info {
  position: absolute;
  z-index: 1;
  left: 250px;
  right: 0;
  top: 100px;
  bottom: 0;
}

/* .g-foot .info div p {
  float: left;
  opacity: .36;
  line-height: 45px;
  padding-right: 12px
} */

.g-foot .info .tel {
  float: right;
  height: 45px;
  line-height: 45px
}

@media only screen and (max-width: 1199px) {
  .g-foot .wp {
    min-height: 362px;
    padding: 140px 0 0;
    margin: 0 32px;

    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .g-foot .wp .logo {
    left: 220px;
  }
  .g-foot .wp .logo img{
    max-width:20%
  }

  .g-foot:before {
    height: 450px;
    left: 2.5%;
  }

  .logo {}

  .g-foot .list {
    position: static;
    width: 100%;
    padding: 32px 0 26px;
    text-align: center;
    /* left: 0px; */
    /* margin-left:200px; */
  }

  .g-foot .list li {
    padding-right: 0;
    height: 31px;
    justify-content: center;
    margin-left: 375px;
  }

  .g-foot .list li:nth-of-type(1) {
    margin-left: 395px;
  }

  .g-foot .list li:nth-of-type(2) {
    margin-left: 385px;
  }

  .g-foot .info {
    position: relative;
    margin-top: -80px;
  }

  .g-foot .info div {
    display: block;
    padding-top: 26px;
    width: 370px;
    margin: 0 auto;
    text-align: center;
  }
}

@media only screen and (max-width: 650px) {
  .g-foot .wp {
    min-height: 313px;
    padding: 85px 0 0;
  }

  .g-foot .wp {
    margin-left: -220px;
  }

  .g-foot:before {
    height: 350px;
    left: 0;
  }
  .g-foot .wp .logo {
    left: 200px;
    /* margin-top:-20px; */
  }
  .g-foot .wp .logo img{
    max-width:15%
  }
  .g-foot .wp .logo h3 {
    font-size:22px;
  }
  .logo {
    max-width: 400px;
  }

  .logo img {
    max-width: 340px;
    margin-left: 70px;
  }
  .g-foot .list li:nth-of-type(1) {
    margin-left: 355px;
  }

  .g-foot .list li:nth-of-type(2) {
    margin-left: 355px;
  }
  .g-foot .list li:nth-of-type(3) {
    margin-left: 355px;
  }
  .g-foot .info {
    margin-top: -100px;
  }
}</style>