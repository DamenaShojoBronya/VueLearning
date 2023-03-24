<template>
    <div>
      <el-input v-model="searchKeyword" placeholder="输入搜索关键词"></el-input>
      <el-button type="primary" @click="searchImages">搜索图片</el-button>
      <div class="image-results">
        <el-image
          v-for="(image, index) in imageResults"
          :key="index"
          :src="image.src.medium"
          :preview-src-list="[image.src.large]"
          fit="cover"
          :alt="image.description"
          @click="selectImage(image)"
        ></el-image>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  const searchKeyword = ref("");
  const imageResults = ref([]);
  
  async function searchImages() {
    if (!searchKeyword.value.trim()) {
      return;
    }
  
    try {
      const response = await fetch(
        `https://api.pexels.com/v1/search?query=${searchKeyword.value}&per_page=10`,
        {
          headers: {
            Authorization: "Ohjn6qbReDKzeaUQm6YfeVNFnvY42aAO1e7jwigWOw3rVKwPXimu6wcZ", // 替换为您的Pexels API密钥
          },
        }
      );
  
      if (response.ok) {
        const data = await response.json();
        imageResults.value = data.photos;
      }
    } catch (error) {
      console.error("Error fetching images from Pexels API:", error);
    }
  }
  
  function selectImage(image) {
    // 处理用户选择的图片，例如将图片URL传递给其他组件或者将图片作为背景图显示
  }
  </script>
  
  <style scoped>
  .image-results {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
  
  .el-image {
    width: 150px;
    height: 150px;
    cursor: pointer;
    border: 1px solid #ccc;
  }
  </style>
  