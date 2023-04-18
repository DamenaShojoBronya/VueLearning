<template>
  <footer :class="{ 'blur-background': blur }">
    <div class="footer">
      <div class="wp">
        <div class="foot-link">
          <!-- <div class="title">常用链接</div>
          <div class="list">
            <ul>
              <li></li>
              <li></li>
              <li></li>
              <li></li>
              <li></li>
            </ul>
          </div> -->
          <div class="ewm">
            <div class="pic"><img src="../assets/页尾-one.jpg" alt=""></div>
            <p>欢迎关注计算机工程学院公众号</p>
          </div>
        </div>
      </div>
      <div class="g-foot">
        <div class="wp">
          <div class="logo">
            <img src="../assets/GUETlogo.png">
          </div>
          <div class="list">
            <ul>
              <li>
                <div style="float: left;">
                  <img src="../assets/电话.png" alt="" width="15" height="15">
                  <p>&nbsp;&nbsp;&nbsp;&nbsp;010-62786244</p>
                </div>
              </li>
              <li>
                <div style="float: left;"><img src="../assets/邮箱.png" alt="" width="15" height="15">
                  <p>&nbsp;&nbsp;&nbsp;&nbsp;twinfo@guet.edu.cn</p>
                </div>
              </li>
              <li>
                <div style="float: left;"><img src="../assets/位置.png" alt="" width="15" height="15">
                  <p>&nbsp;&nbsp;&nbsp;&nbsp;北海市桂林电子科技大学北海校区</p>
                </div>
              </li>
            </ul>
          </div>
          <div class="info">
            <div>
              
              <p>版权所有 &copy; 桂林电子科技大学北海校区网络中心</p>
              <p>地址:北海市银海区银滩镇南珠大道9号桂林电子科技大学北海校区</p><br>
              <p style="float: right;">邮编:536000</p><br><br><br>
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
  overflow: hidden
}

.wp {
  width: auto;
  max-width: none;
  padding: 0 10px
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


.foot-link .title {
  font-size: 30px
}

.foot-link .list a {
  font-size: 14px;
  line-height: 40px
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
  padding: px 65px 0 0
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

.g-foot:before {
  left: 20px
}

.g-foot:after {
  left: 40px
}

.g-foot {
  position: relative;
  color: #fff;
  font-size: 12px
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
  background: #93b8f3;
}

.g-foot:after {
  content: "";
  display: block;
  position: absolute;
  left: 7.1%;
  bottom: 0;
  right: 0;
  height: 100%;
  background: #4c4c7b;
}

.g-foot .wp {
  min-height: 213px;
  position: relative;
  z-index: 2
}

.g-foot .logo {
  position: absolute;
  z-index: 1;
  left: 200px;
  right: auto;
  top: 46px;
  bottom: auto;
  width: 180px
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
  padding-right: 20px
}

.g-foot .list li p {
  display: inline-block;
  vertical-align: middle
}

/* .g-foot .info div {
  width: auto;
  padding-top: 17px
} */

.g-foot .info div {
  padding-top: 50px;
  width: 1300px;
  margin: 0 auto;
  text-align:left
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
</style>