<template>
  <div class="view-box">
    <div class="header">
      <div class="header-mid">
        <h3>计算机学院网络中心</h3>
        <p>computer College Network Center</p>
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
            网络中心是以培养学生实践素养为重心，提升科技能力为核心，维护校园网络基础设施、服务师生为目标，有利于学院培养专业技能突出学子和“以赛促学”风气的形成，鼓励引导大学生参加计算机科技竞赛，激发学习兴趣，学习更专业的技能，服务师生，造福社会，为学院的教学改革、课程体系构建、人才培养方案的完善等起到辅助和促进作用。同时作为一个交流的平台，也将专业性和学习性兼容起来，为你们提供了一个闪亮的舞台
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
              <p>出勤次数</p>
              <div class="text-wrap">
                <p1>500</p1>
                <p>+</p>
              </div>
            </div>
          </div>
        </div>
        <div class="menu">
          <div class="icon-wrap">
            <img src="../assets/icon-computer.png">
            <p>立足专业</p>
          </div>
          <div class="icon-wrap">
            <img src="../assets/icon-server.png">
            <p>服务师生</p>
          </div>
          <div class="icon-wrap">
            <img src="../assets/icon-book_black.png">
            <p>以赛促学</p>
          </div>
          <div class="icon-wrap">
            <img src="../assets/icon-cloud.png">
            <p>数据上云</p>
          </div>
          <div class="icon-wrap">
            <img src="../assets/211904_social_github_icon.png">
            <p>代码开源</p>
          </div>
        </div>
      </div>
    </div>

    <div class="content-2">
      <el-carousel class="content-2-carousel" :interval="4000" type="card" height="400px">
        <el-carousel-item v-for="item in 6" :key="item">
          <!-- {{ item }} -->
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="content-3">
      <div class="content-3-tittle">
        <span>
          <img src="../assets/zx_title_blue_r.png">
          案例介绍
          <img src="../assets/zx_title_blue_l.png">
        </span>
        <p>CASE INTRODUCED</p>
      </div>
      <div class="content-3-main">
        <div class="content-3-left"> </div>
        <div class="content-3-middle">
          <p>设备报修管理系统网页端是由计算机学院网络中心开发的一款校园综合服务应用，主要实现设备损坏上报、出勤人员派遣、维修进度跟踪和流程记录展示等功能。
            不同于传统的纸质工单进行记录和汇总存在的报修进度无法实时进行跟踪和管理，维修结果也无法做到及时反馈，最终汇总报修工单与核算时难度比较大等问题，
            后勤设备报修应用模板通过平台实现从设备损坏上报到维修归档全流程可视化管理，实现跟踪监控、工单留痕等效果，实现了后勤设备报修的信息化管理。</p>
          <div class="button-wrap">
            <div class="button2">
              <router-link active-class="active" to="/products">
                <p>查看案例</p>
              </router-link>
            </div>
          </div>
        </div>
        <div class="content-3-right"> </div>
      </div>
    </div>
    <div class="content-4">

      <div class="content-3-tittle">
        <span>
          <img src="../assets/zx_title_blue_r.png">
          服务理念
          <img src="../assets/zx_title_blue_l.png">
        </span>
        <p>SERVICE PHILOSOPHY</p>
      </div>
      <div class="industry-dynamics-1"><br><br><br><br>
        <h3>专注打造师生服务平台</h3>
        <p>以师生为中心，其系统主要是为了帮助广大师生提高工作效率，节约资源，实现校园设备报修、学生信息管理等工作流程的系统化、规范化和自动化。</p>
        <div class="button">
          <p>了解更多</p>
        </div>
      </div>
      <div class="industry-dynamics-wrap">
        <div class="industry-dynamics-2">
          <img src="../assets/动态-two.jpg">
          <div class="industry-dynamics-text">
            <h3>系统一体化方案</h3>
            <p>采用一定的方式，对已经制定颁布的规范性文件或者流程进行归类、整理或加工，使其集中起来作有系统的排列，以便于使用的活动 </p>
          </div>
        </div>
        <div class="industry-dynamics-3">
          <img src="../assets/动态-three.jpg">
          <div class="industry-dynamics-text">
            <h3>规范一体化方案</h3>
            <p>改造关系模式，通过分解关系模式来消除其中不合适的数据依赖，以解决插入异常、删除异常、更新异常和数据冗余问题。</p>
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
  margin: auto;
  width: 100%;
  height: 625px;
  background: url('../assets/头图.jpg') no-repeat center;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.header-mid {
  margin-top: 150px;
  margin-bottom: -233px;
  color: white;
  /* z-index:999988; */
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
  align-items: flex-start;
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
  background: url('../assets/介绍-底图.png');
  display: inline-block;
}

.line2 {
  margin-left: 125px;
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
  z-index: 10;
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
  height: 430px;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  /* background: #d3dce6; */
}

.content-2-carousel {
  background: #FFFFFF;
  min-width: 100%;
}

.el-carousel__item:nth-child(3n) {
  background: url('../assets/ICT轮播.png')no-repeat center;
  background-size: cover;
}

.el-carousel__item:nth-child(3n+1) {
  background: url('../assets/北海校区领导带队赴华为技术服务（广西）有限公司参观交流.png')no-repeat center;
  background-size: cover;
}

.el-carousel__item:nth-child(3n+2) {
  background: url('../assets/ICT云赛道.png')no-repeat center;
  background-size: cover;
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
  background: url('../assets/占位图.png');
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
  font-size: 16px;
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
  height: 1206px;
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
  background: url('../assets/轮播图3.jpg') no-repeat center;
  background-size: cover;
  opacity: 0.9;
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