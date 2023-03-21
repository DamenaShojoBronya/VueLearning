<template>
    <div class="achievements">
      <h1>科学创新协会成就</h1>
      <ul>
        <li>2021年获得省级科技创新大赛一等奖</li>
        <li>2022年入选国家级科研项目</li>
        <li>2023年发表高水平论文10篇</li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Achievements',
  };
  </script>
  
  <style>
  .achievements {
    max-width: 800px;
    margin: 0 auto;
    padding: 50px 20px;
    font-size: 18px;
    text-align: left;
  }
  
  h1 {
    font-size: 36px;
    margin-bottom: 30px;
  }
  
  ul {
    list-style-type: disc;
    margin-left: 30px;
  }
  </style>
  