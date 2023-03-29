<template>
  <div class="content-1-mainbox">
    <div class="banner">
      <div class="banner-icon-wrap">
        <img src="../assets/图标-风控能力-文本鉴黄.png">
      </div>
      <div class="banner-text-wrap">
        <h3>文本鉴黄</h3>
        <p>色情传播、性行为、性器官描写、低俗段子、低俗隐晦等</p>
      </div>
    </div>
    <div class="banner">
      <div class="banner-icon-wrap">
        <img src="../assets/图标-风控能力-涉政暴恐.png">
      </div>
      <div class="banner-text-wrap">
        <h3>涉政暴恐</h3>
        <p>对国家、政府官员和英雄烈士的不当言论；恐怖组织和恐怖事件宣传相关信息</p>
      </div>
    </div>
    <div class="banner">
      <div class="banner-icon-wrap">
        <img src="../assets/图标-风控能力-违禁检测.png">
      </div>
      <div class="banner-text-wrap">
        <h3>违禁检测</h3>
        <p>赌博、毒品、非法传教、贩卖野生动物、非法办证考证等非法违禁信息 </p>
      </div>
    </div>
    <div class="banner">
      <div class="banner-icon-wrap">
        <img src="../assets/图标-风控能力-篡改检测.png">
      </div>
      <div class="banner-text-wrap">
        <h3>篡改检测</h3>
        <p>对网站内容主动监测，及时扼制因恶意篡改而造成内容违规风险 </p>
      </div>
    </div>
    <div class="banner">
      <div class="banner-icon-wrap">
        <img src="../assets/图标-风控能力-挂马识别.png">
      </div>
      <div class="banner-text-wrap">
        <h3>挂马识别</h3>
        <p>基于多种模型融合技术，及时发现页面挂马，并第一时间进行预警通知。</p>
      </div>
    </div>
    <div class="banner">
      <div class="banner-icon-wrap">
        <img src="../assets/图标-风控能力-暗链识别.png">
      </div>
      <div class="banner-text-wrap">
        <h3>暗链识别</h3>
        <p>全面防范，让暗链、黑链、死链无所遁形</p>
      </div>
    </div>
  </div>
</template>

<style scoped>

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
  height: 128px;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.banner-text-wrap>h3 {
  font-family: 'MicrosoftYaHeiUI-Bold';
  font-size: 16px;
  color: black;
  line-height: 18px;
}

.banner-text-wrap>p {
  margin-top: 4px;
  font-family: 'MicrosoftYaHeiUI';
  font-size: 14px;
  color: black;
  line-height: 22px;
}</style>
