<template>
  <view-box>
    <!-- 找到我们  图标需要更换 -->
    <div class="content-1">
      <div class="content-1-home">
        <div class="content-1-tittle-wrap">
          <h3 class="background">FIND US</h3>
          <div class="content-1-tittle">
            <p>找到我们</p>
            <img src="../assets/标题装饰-1.png">
          </div>
        </div>

        <div class="content-1-mainbox">
          <div class="banner">
            <div class="banner-icon-wrap">
              <img src="../assets/图标-风控能力-文本鉴黄.png">
            </div>
            <div class="banner-text-wrap">
              <h3>桂电北海计算机学院</h3>
              <p>学习优秀，本领过硬。下辖专业：大数据管理与应用、网络工程</p>
            </div>
          </div>
          <div class="banner">
            <div class="banner-icon-wrap">
              <img src="../assets/图标-风控能力-涉政暴恐.png">
            </div>
            <div class="banner-text-wrap">
              <h3>桂电北海网络中心</h3>
              <p>牛人的聚集地，为全校师生提供优质网络技术服务</p>
            </div>
          </div>
          <div class="banner">
            <div class="banner-icon-wrap">
              <img src="../assets/图标-风控能力-违禁检测.png">
            </div>
            <div class="banner-text-wrap">
              <h3>科协优阅网</h3>
              <p>计算机学院科协官网，学院竞赛信息一网打尽</p>
            </div>
          </div>
          <div class="banner">
            <div class="banner-icon-wrap">
              <img src="../assets/图标-风控能力-篡改检测.png">
            </div>
            <div class="banner-text-wrap">
              <h3>Gmail</h3>
              <p>我们的邮箱</p>
            </div>
          </div>
          <div class="banner">
            <div class="banner-icon-wrap">
              <img src="../assets/图标-风控能力-挂马识别.png">
            </div>
            <div class="banner-text-wrap">
              <h3>Github</h3>
              <p>我们的代码仓库</p>
            </div>
          </div>
          <div class="banner">
            <div class="banner-icon-wrap">
              <img src="../assets/图标-风控能力-暗链识别.png">
            </div>
            <div class="banner-text-wrap">
              <h3>Wechat</h3>
              <p>我们的公众号</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 使用流程 -->
    <div class="content-3">
      <div class="content-1-home">
        <div class="content-1-tittle-wrap">
          <h3 class="background">SERVICE PROVISIONING</h3>
          <div class="content-1-tittle">
            <p>使用流程</p>
            <img src="../assets/标题装饰-1.png">
          </div>
        </div>
        <div class="content-1-mainbox" id="content-3-mainbox">
          <div class="banner3">
            <img src="../assets/图标-使用流程-试用申请.png">
            <h3>试用申请</h3>
            <p>提交申请，业务人员沟通业务需求，开通企业试用账号</p>
          </div>
          <div class="banner3">
            <img src="../assets/图标-使用流程-登录试用.png">
            <h3>登录试用</h3>
            <p>登录内容安全监测平台，即刻登录接入试用</p>
          </div>
          <div class="banner3">
            <img src="../assets/图标-使用流程-购买服务.png">
            <h3>购买服务</h3>
            <p>可根据业务需求自主选择监测服务，下单购买</p>
          </div>
          <div class="banner3">
            <img src="../assets/图标-使用流程-开启监测.png">
            <h3>开启监测</h3>
            <p>极速接入，立即体验东信网安一站式内容安全服务</p>
          </div>
        </div>
      </div>
    </div>
  </view-box>
</template>

<style scoped>
view-box {
  display: flex;
  flex-wrap: wrap
}

.banner {
  position: relative;
  border-radius: 25px 25px;
}

.banner-text-wrap>p:after {
  width: 20px;
  height: 20px;
  content: "";
  display: block;
  position: absolute;
  bottom: 0;
  right: 0;
  width: 50px;
  height: 50px;
  border-radius: 25px 0;
  cursor: pointer;
  transition: inherit;
  background-color: #1d71ed;
  background-size: 20px 20px;
  background-repeat: no-repeat;
  background-position: center;
  background-image: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9JzMwMHB4JyB3aWR0aD0nMzAwcHgnICBmaWxsPSIjZmZmZmZmIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGRhdGEtbmFtZT0iTGF5ZXIgMSIgdmlld0JveD0iMCAwIDEwMCAxMDAiIHg9IjBweCIgeT0iMHB4Ij48dGl0bGU+NTI8L3RpdGxlPjxwYXRoIGQ9Ik04MS4zMDMyOSwzOC41MjkzOUExNC4wMTgsMTQuMDE4LDAsMSwwLDYxLjQ3NywxOC43MDY3MUw0Ny4wMDMxNSwzMy4xNzkxNGExNC4wMzAzNywxNC4wMzAzNywwLDAsMCwwLDE5LjgyMTcxLDQuODAxMTMsNC44MDExMywwLDAsMS02Ljc4OTc5LDYuNzg5ODcsMjMuNjQzMjcsMjMuNjQzMjcsMCwwLDEsMC0zMy40MDE0NUw1NC42ODcyMSwxMS45MTY4NEEyMy42MjAzLDIzLjYyMDMsMCwwLDEsODguMDkzMDgsNDUuMzE5MjdMODAuOTIzOCw1Mi40ODcxMWE0LjgwMTE0LDQuODAxMTQsMCwwLDEtNi43ODk4LTYuNzg5ODdaTTExLjkwNzQxLDg4LjA5MzlhMjMuNjUwNTMsMjMuNjUwNTMsMCwwLDAsMzMuNDA1ODYtLjAwMUw1OS43ODY2NCw3My42MjE0N2EyMy42MTU4MywyMy42MTU4MywwLDAsMCwwLTMzLjQwMTQ1LDQuODAxMTQsNC44MDExNCwwLDAsMC02Ljc4OTc5LDYuNzg5ODgsMTQuMDE1MzEsMTQuMDE1MzEsMCwwLDEsMCwxOS44MjI2OEwzOC41MjM0OCw4MS4zMDRBMTQuMDE4LDE0LjAxOCwwLDEsMSwxOC42OTcyLDYxLjQ4MTM1TDI1Ljg2Niw1NC4zMTM1YTQuODAxMTQsNC44MDExNCwwLDAsMC02Ljc4OTgtNi43ODk4N2wtNy4xNjg3OSw3LjE2Nzg1QTIzLjY0NDg5LDIzLjY0NDg5LDAsMCwwLDExLjkwNzQxLDg4LjA5MzlaIj48L3BhdGg+PC9zdmc+);
}

.content-1 {
  width: 100%;
  height: 564px;
  background: #eef2f7;
}

.content-1-home {
  width: 1400px;
  margin: auto;
}

.content-1-tittle-wrap {
  height: 126px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.background {
  width: 100%;
  height: inherit;
  opacity: 0.38;
  font-family: 'AlibabaSans-BoldItalic';
  font-size: 100px;
  color: transparent;
  letter-spacing: -4px;
  text-align: center;
  position: relative;
  background-image: linear-gradient(to bottom, #1d71ed, white);
  -webkit-background-clip: text;
}

.content-1-tittle {
  width: auto;
  height: 34px;
  position: absolute;
}

.content-1-tittle>p {
  font-family: 'MicrosoftYaHeiUI-Bold';
  font-size: 34px;
  font-weight: bold;
  color: black;
  text-align: center;
  line-height: 34px;
}

.content-1-mainbox {
  height: 398px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  overflow: hidden;
}

.banner {
  width: 386px;
  height: 128px;
  margin: 21px;
  background: #FFFFFF;
  border: 1px solid #DDDDDD;
  display: flex;
  justify-content: center;
  align-items: center;
}

.banner:hover {
  box-shadow: 0 6px 22px 0 rgba(0, 0, 0, 0.18);
  border: 0px;
}

.banner-icon-wrap {
  width: 104px;
  height: 128px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.banner-text-wrap {
  width: 256px;
  height: 90px;
  display: flex;
  justify-content: space-around;
  flex-direction: column;
  /* background: #666666; */
  text-align: center;
}

.banner-text-wrap>h3 {
  margin-left: -50px;
  font-family: 'MicrosoftYaHeiUI-Bold';
  font-size: 30px;
  color: black;
  line-height: 18px;
}

.banner-text-wrap>p {

  margin-top: 10px;
  width: 200px;
  font-family: 'MicrosoftYaHeiUI';
  font-size: 20px;
  color: black;
  line-height: 22px;
  /* background: #5c3939; */
}

.banner:nth-of-type(-n+3)>.banner-text-wrap>h3 {
  font-size: 20px;
}

.banner:nth-of-type(-n+3)>.banner-text-wrap>p {
  font-size: 15px;
}


.content-3 {
  height: 433px;
  background: #FFFFFF;
}

#content-3-mainbox {
  height: 307px;
  overflow: hidden;
}

.banner3 {
  width: 126px;
  height: 207px;
  margin: 21px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
}

.banner3>img {
  width: 73px;
  height: 73px;
}

.banner3>h3 {
  font-family: MicrosoftYaHeiUI-Bold;
  font-size: 16px;
  color: #333333;
  text-align: center;
  line-height: 18px;
  /* margin-bottom: 11px; */
}

.banner3>p {
  font-family: MicrosoftYaHeiUI;
  font-size: 14px;
  color: #666666;
  text-align: center;
  line-height: 22px;
}</style>
