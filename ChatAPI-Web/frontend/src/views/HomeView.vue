<template>
  <div class="view-box">

    <div class="header">
      <div class="header-mid">
        <h3>桂电北海网络中心</h3>
        <p>GUET Beihai Network Center</p>
      </div>
      <div class="header-bottom">
        <div class="header-bottom-bg"></div>
        <div class="header-bottom-content">
          <h3>平台</h3><br>
          <p>帮助成员提高编程和技术能力，提供一个交流、学习和合作的平台</p>
        </div>
        <div class="divider"></div>
        <div class="header-bottom-content">
          <h3>实践</h3><br>
          <p>通过组织比赛项目和日常任务，让成员得到实践经验和技能锻炼的机会</p>
        </div>
        <div class="divider"></div>
        <div class="header-bottom-content">
          <h3>环境</h3><br>
          <p>拥有独立自习室和办公桌椅，环境舒适 技术大拿共同交流，学习氛围好</p>
        </div>
        <div class="divider"></div>
        <div class="header-bottom-content">
          <h3>服务</h3><br>
          <p>负责校内网络维护维修事宜，服务师生 提供勤工俭学岗位，锻炼自己</p>
        </div>
      </div>
    </div>
    <div class="content-1-home">
      <div class="content-1">
        <div class="content-1-left">
          <div class="line2"></div>
          <p>专注打造服务师生优良教学环境</p>
        </div>
        <div class="content-1-right">
          <p class="content-1-right-top">
            网络中心是以培养学生科技素养为重心，提升科技竞赛能力为核心，提高专业学习兴趣为目标，有利于学院“以赛促学”风气的形成，鼓励引导大学生参加计算机科技竞赛，激发学习兴趣，学习更专业的技能，服务师生，造福社会，为学院的教学改革、课程体系构建、人才培养方案的完善等起到辅助和促进作用，但它同时作为一个交流的平台，也将专业性和学习性兼容起来，为你们提供了一个闪亮的舞台。
          </p>
          <div class="content-1-right-bottom">
            <div class="item-wrap">
              <p>学习区域</p>
              <div class="text-wrap">
                <p1>5</p1>
                <p>个</p>
              </div>
            </div>
            <div class="item-wrap">
              <p>覆盖专业</p>
              <div class="text-wrap">
                <p1>11</p1>
                <p>个</p>
              </div>
            </div>
            <div class="item-wrap">
              <p>服务师生范围</p>
              <div class="text-wrap">
                <p1>42</p1>
                <p>+</p>
              </div>
            </div>
          </div>
        </div>
        <div class="menu">
          <div class="icon-wrap">
            <img src="./assets/介绍-图标-决策智能化.png">
            <p>决策智能化</p>
          </div>
          <div class="icon-wrap">
            <img src="./assets/介绍-图标-运营数据化.png">
            <p>运营数据化</p>
          </div>
          <div class="icon-wrap">
            <img src="./assets/介绍-图标-业务在线化.png">
            <p>业务在线化</p>
          </div>
          <div class="icon-wrap">
            <img src="./assets/介绍-图标-数据资产化.png">
            <p>数据资产化</p>
          </div>
          <div class="icon-wrap">
            <img src="./assets/介绍-图标-触点数据化.png">
            <p>触点数据化</p>
          </div>
          <div class="icon-wrap">
            <img src="./assets/介绍-图标-基础设施云化.png">
            <p>基础设施云化</p>
          </div>
        </div>
      </div>
    </div>

    <div class="content-2">
      <el-carousel class="content-2-carousel" :interval="4000" type="card" height="300px">
        <el-carousel-item v-for="item in 6" :key="item">
          <!-- {{ item }} -->
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="content-3">
      <div class="content-3-tittle">
        <span>
          <img src="./assets/zx_title_blue_r.png">
          案例介绍
          <img src="./assets/zx_title_blue_l.png">
        </span>
        <p>CASE INTRODUCED</p>
      </div>
      <div class="content-3-main">
        <div class="content-3-left"> </div>
        <div class="content-3-middle">
          <p>
            "桂北汇APP"是由桂林电子科技大学北海校区(网络信息中心)进行开发的一款校内综合服务应用。<br>
            教务系统管理平台充分利用互联网络B/S管理系统模式，以网络为平台，为各个学校教务系统的管理提供一个平台，帮助学校管理教务系统，用一个帐号解决学校教务教学管理，并且学校可以自由选择学校需要的教务管理系统，灵活地定制符合学校自己实际情况的教务系统
          </p>
          <div class="button-wrap">
            <div class="button2">
              <p>查看案例</p>
            </div>
          </div>
        </div>
        <div class="content-3-right"> </div>
      </div>
    </div>
    <div class="content-4">
      <div class="content-3-tittle">
        <span>
          <img src="./assets/zx_title_blue_r.png">
          应用服务
          <img src="./assets/zx_title_blue_l.png">
        </span>
        <p>APPLICATION SERVICE</p>
      </div>
      <ul class="pic-ls">
        <li class="pic-ls1">
          <img class="pic-ls-bg" src="./assets/泛糖-440x342.png">
          <img src="./assets/应用服务-图标-泛糖.png">
          <p>泛糖</p>
          <div class="line4"></div>
          <div class="pic1-slogan">新型基础设施赋能涉农企业生产经营管理</div>
        </li>
        <li>
          <img class="pic-ls-bg" src="./assets/电子口岸-200x342.png">
          <img src="./assets/应用服务-图标-电子口岸.png">
          <p>电子口岸</p>
          <div class="invisible-bottom"></div>
        </li>
        <li>
          <img class="pic-ls-bg" src="./assets/装配式建筑-200x342.png">
          <img src="./assets/应用服务-图标-装配式建筑.png">
          <p>装配式建筑</p>
          <div class="invisible-bottom"></div>
        </li>
        <li>
          <img class="pic-ls-bg" src="./assets/建材采购-200x342.png">
          <img src="./assets/应用服务-图标-建材采购.png">
          <p>建材采购</p>
          <div class="invisible-bottom"></div>
        </li>
        <li>
          <img class="pic-ls-bg" src="./assets/金融服务-200x342.png">
          <img src="./assets/应用服务-图标-金融服务.png">
          <p>金融服务</p>
          <div class="invisible-bottom"></div>
        </li>
      </ul>
      <ul class="pic-ls" id="pic2-ls">
        <li>
          <img class="pic-ls-bg" src="./assets/行业咨询-248x342.png">
          <img src="./assets/应用服务-图标-行业咨询.png">
          <p>行业咨询</p>
          <div class="invisible-bottom"></div>
        </li>
        <li>
          <img class="pic-ls-bg" src="./assets/智联云-248x342.png">
          <img src="./assets/应用服务-图标-智联云.png">
          <p>智联云</p>
          <div class="invisible-bottom"></div>
        </li>
        <li>
          <img class="pic-ls-bg" src="./assets/路信云-248x342.png">
          <img src="./assets/应用服务-图标-路信云.png">
          <p>路信云</p>
          <div class="invisible-bottom"></div>
        </li>
        <li>
          <img class="pic-ls-bg" src="./assets/桂建云-248x342.png">
          <img src="./assets/应用服务-图标-桂建云.png">
          <p>桂建云</p>
          <div class="invisible-bottom"></div>
        </li>
        <li>
          <img class="pic-ls-bg" src="./assets/明建云-248x342.png">
          <img src="./assets/应用服务-图标-明建云.png">
          <p>明建云</p>
          <div class="invisible-bottom"></div>
        </li>
      </ul>
      <div class="content-3-tittle">
        <span>
          <img src="./assets/zx_title_blue_r.png">
          产业动态
          <img src="./assets/zx_title_blue_l.png">
        </span>
        <p>INDUSTRY DYNAMICS</p>
      </div>
      <div class="industry-dynamics-1">
        <h3>专注打造工业互联网操作系统</h3>
        <p>以客户为中心，通过市场需求驱动，助力产业链快速反应，布局云端信息化，打造产业操作系统。基于生态全链路对各个环节进行价值重构，将商流</p>
        <div class="button">
          <p>了解更多</p>
        </div>
      </div>
      <div class="industry-dynamics-wrap">
        <div class="industry-dynamics-2">
          <img src="./assets/产业动态-图2.png">
          <div class="industry-dynamics-text">
            <h3>装配式一体化解决方案</h3>
            <p>以软硬件结合、提供装配式建筑材料的质量溯源、协同、其他产业链资源等服务，助力建筑业转型升级 </p>
          </div>
        </div>
        <div class="industry-dynamics-3">
          <img src="./assets/产业动态-图3.png">
          <div class="industry-dynamics-text">
            <h3>营销一体化解决方案</h3>
            <p>仓储物流服务集成平台，接入厂仓、第三方仓储物流公司系统，实现企业、贸易商与物流公司和仓库之间的在线撮合与交易，提供便捷、高效的仓储物流服务。</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  }
}


</script>
<!-- 分辨率缩放bug -->
<style scoped>
.view-box {
  width: 100%;
  min-width: 1440px;
  height: auto;
  margin-top: -60px;
}

.header {
  margin: 0 auto;
  width: 100%;
  height: 36.45833vw;
  background: url('../assets/首页banner2.png') no-repeat center;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.header-mid {
  position: absolute;
  top: 18%;
  color: white;
  overflow: hidden;
}

.header-mid h3 {
  font-size: 79px;
  color: #fff;
  line-height: 1.5em;
  margin-bottom: 1px;
}

.header-mid p {
  font-size: 30px;
  color: rgb(255, 255, 255);
  line-height: 1.5em;
  font-family: Bold, 微软雅黑;
  text-transform: uppercase;
}

.header-bottom {
  margin-top: 353px;
  height: 192px;
  width: 1440px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.header-bottom-bg {
  position: absolute;
  z-index: 20;
  height: 192px;
  width: 100%;
  min-width: 1440px;
  opacity: 0.39;
  background-image: linear-gradient(180deg, #000000 0%, #000000 100%);
}

.header-bottom-content {
  width: 278px;
  height: 192px;
  z-index: 100;
  display: flex;
  /* align-items: flex-start; */
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.header-bottom-content>h3 {
  font-family: SourceHanSansCN-Bold;
  font-size: 28px;
  color: #FFFFFF;
  line-height: 28px;
  margin: 2px;
}

.header-bottom-content>p {
  font-family: 'SourceHanSansCN-Regular';
  font-size: 16px;
  color: #FFFFFF;
  line-height: 24px;
  /* text-align: left; */
}

.divider {
  opacity: 0.6;
  background: #FFFFFF;
  width: 3px;
  height: 54px;
  margin: 28px;
}

.content-1-home {
  margin: 0 auto;
  width: 100%;
  height: 583px;
  background-color: #f7f7f7;
}

.content-1 {
  margin: 0 auto;
  width: 1440px;
  height: 583px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  background-color: #f7f7f7;
}

.content-1-left {
  width: 580px;
  height: 447px;
  background: url('assets/介绍-底图.png');
  display: inline-block;
}

.line2 {
  margin-left: 58px;
  margin-top: 128px;
  width: 50px;
  height: 8px;
  background: #D7000F;
}

.content-1-left>p {
  margin-left: 58px;
  margin-top: 30px;
  font-family: 'SourceHanSansCN-Medium';
  font-size: 28px;
  font-weight: bold;
  color: #333333;
  line-height: 18px;
}

.content-1-right {
  margin: 0 auto;
  width: 860px;
  height: 447px;
  background: #FFFFFF;
  /* display: inline-block; */
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.content-1-right-top {
  width: 766px;
  height: 120px;
  font-family: SourceHanSansCN-Regular;
  font-size: 18px;
  color: #7A7C84;
  text-align: justify;
  line-height: 26px;
  word-wrap: break-word;
  word-break: normal;
}

/* .content-1-right-top>p{
    font-family: SourceHanSansCN-Regular;
    font-size: 18px;
    color: #7A7C84;
    text-align: justify;
    line-height: 26px;
} */
.content-1-right-bottom {
  width: 766px;
  height: 71px;
  margin-top: 46px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.item-wrap {
  width: auto;
  height: 71px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: column;
}

.item-wrap>p {
  font-family: 'SourceHanSansCN-Regular';
  font-size: 18px;
  color: #7A7C84;
  text-align: justify;
  line-height: 18px;
}

.text-wrap {
  display: flex;
  flex-direction: row;
  align-items: baseline;
  justify-content: center;
}

.text-wrap>p1 {
  font-family: 'DINAlternate-Bold';
  font-size: 49px;
  color: #D7000F;
  text-align: justify;
  line-height: 18px;
}

.text-wrap>p {
  font-family: 'SourceHanSansCN-Regular';
  font-size: 18px;
  color: #7A7C84;
  text-align: justify;
  line-height: 18px;
}

.menu {
  margin: 0 auto;
  background: #FFFFFF;
  width: 1321px;
  height: 158px;
  box-shadow: 0 0 43px 0 rgba(0, 0, 0, 0.13);
  border-radius: 8px;
  border-radius: 8px;
  margin-top: 368px;
  position: absolute;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

.icon-wrap {
  height: 110px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

.icon-wrap>p {
  font-family: 'SourceHanSansCN-Medium';
  font-size: 24px;
  font-weight: bolder;
  color: #333333;
  text-align: center;
  line-height: 18px;
}


.content-2 {
  display: flex;
  margin: 0 auto;
  width: 1440px;
  height: 420px;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background: #d3dce6;
}

.content-2-carousel {
  background: #475669;
  min-width: 100%;
}

.el-carousel__item:nth-child(3n) {
  /* background-color: #d3dce6; */
  background: url('../assets/首页banner2.png') no-repeat center;
}

.el-carousel__item:nth-child(3n+1) {
  /* background-color: #99a9bf; */
  background: url('../assets/profile.png') no-repeat center;
}

.el-carousel__item:nth-child(3n+2) {
  background: url('../assets/首页banner.png') no-repeat center;
}


.button {
  width: 124px;
  height: 42px;
  background: rgba(216, 216, 216, 0.00);
  border: 1px solid #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
}

.button:hover {
  background-color: burlywood;
}

.button>p {
  font-family: 'SourceHanSansCN-Regular';
  font-size: 16px;
  color: #FFFFFF;
  text-align: justify;
  line-height: 16px;
}

.content-3 {
  width: 1440px;
  height: 645px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  flex-direction: column;
}

.content-3-tittle {
  height: 143px;
  font-family: 'SourceHanSansCN-Bold';
  font-weight: bold;
  font-size: 34px;
  color: #333333;
  text-align: center;
  line-height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.content-3-tittle>span {
  display: flex;
  align-items: center;
  justify-content: center;
}

.content-3-tittle>span>img {
  /* display: inline-block; */
  transform: scaleX(-1);
  margin: 7px;
  margin-top: 10px;
}

.content-3-tittle>p {
  font-family: 'MicrosoftYaHeiUI';
  font-size: 18px;
  color: #999999;
  letter-spacing: 0.69px;
  text-align: center;
  margin-top: 5px;
}

.content-3-main {
  width: 1200px;
  height: 419px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
}

.content-3-left {
  width: 634px;
  height: 419px;
  background: url('./assets/占位图.png');
}

.content-3-middle {
  width: 652px;
  height: 343px;
  background: #F7F7FA;
  box-shadow: -13px 42px 65px 0 rgba(13, 29, 78, 0.09);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  position: relative;
  margin-left: -104px;
}

.content-3-middle>p {
  width: 583px;
  height: 174px;
  font-family: 'SourceHanSansCN-Regular';
  font-size: 18px;
  color: #7A7C84;
  text-align: justify;
  line-height: 26px;
}

.button-wrap {
  width: 583px;
}

.button2 {
  width: 124px;
  height: 42px;
  background: rgba(216, 216, 216, 0.00);
  border: 1px solid #333333;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.button2:hover {
  background-color: burlywood;
}

.button2>p {
  font-family: 'SourceHanSansCN-Regular';
  font-size: 16px;
  color: #333333;
  text-align: justify;
  line-height: 16px;
}

.content-3-right {
  width: 18px;
  height: 260px;
  background: #E12936;
}

.content-4 {
  width: 100%;
  height: 2106px;
  background: #f2f2f2bb;
  margin: 0 auto;
  position: relative;
  z-index: -10;
}

.pic-ls {
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
}

.pic-ls>li {
  width: 200px;
  height: 342px;
  margin: 20px;
  display: flex;
  align-items: flex-start;
  justify-content: flex-end;
  flex-direction: column;
}

.pic-ls>li>img:nth-child(2) {
  margin-left: 18px;
}

.pic-ls>li>p {
  font-family: 'SourceHanSansCN-Medium';
  font-size: 20px;
  line-height: 18px;
  margin-top: 20px;
  margin-left: 18px;
  color: #FFFFFF;
}

.line4 {
  width: 65px;
  height: 2px;
  margin-top: 8px;
  margin-bottom: 16px;
  margin-left: 18px;
  background: #FFFFFF;
}

.pic1-slogan {
  font-family: 'SourceHanSansCN-Regular';
  font-size: 14px;
  width: 397px;
  height: 59px;
  line-height: 26px;
  margin-left: 18px;
  color: #FFFFFF;
}

.invisible-bottom {
  height: 33px;
  width: auto;
  visibility: hidden;
}



li.pic-ls1 {
  width: 440px;
  height: 342px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-direction: column;
}

.pic-ls-bg {
  position: absolute;
  z-index: -1;
  opacity: 1;
}

#pic2-ls li {
  width: 248px;
  height: 342px;
}

.industry-dynamics-1 {
  margin: 0 auto;
  width: 1320px;
  height: 453px;
  background: url('./assets/产业动态-图1.png');
}

.industry-dynamics-1>h3 {
  font-family: 'SourceHanSansCN-Bold';
  font-size: 28px;
  color: #FFFFFF;
  line-height: 18px;
  margin-top: 94px;
  margin-left: 50px;
  position: absolute;
}

.industry-dynamics-1>p {
  font-family: 'SourceHanSansCN-Regular';
  font-size: 18px;
  width: 766px;
  color: #FFFFFF;
  text-align: justify;
  line-height: 26px;
  margin-top: 133px;
  margin-left: 50px;
  position: absolute;
}

.industry-dynamics-1>.button {
  background: rgba(216, 216, 216, 0.00);
  border: 1px solid #FFFFFF;
  border-radius: 6px;
  border-radius: 6px;
  margin-top: 224px;
  margin-left: 50px;
  position: absolute;
}

.industry-dynamics-wrap {
  margin: 0 auto;
  width: 1320px;
  height: 497px;
  margin-top: 30px;
}

.industry-dynamics-2 {
  margin: 0 auto;
  width: 647px;
  height: 497px;
  float: left;
}

.industry-dynamics-3 {
  margin: 0 auto;
  width: 647px;
  height: 497px;
  float: right;
}

.industry-dynamics-2>img {
  width: 647px;
  height: 344px;
}

.industry-dynamics-text {
  height: 153px;
  width: auto;
  border: 0.1px solid #FFFFFF;
  background: #FFFFFF;
}

.industry-dynamics-text>h3 {
  font-family: 'SourceHanSansCN-Medium';
  font-size: 28px;
  color: #333333;
  line-height: 18px;
  margin-left: 42px;
  margin-top: 33px;
}

.industry-dynamics-text>p {
  font-family: 'SourceHanSansCN-Regular';
  font-size: 16px;
  color: #666666;
  text-align: justify;
  line-height: 24px;
  margin-left: 42px;
  margin-top: 17px;
  margin-right: 36px;
}
</style>