<template>
    <el-steps :active="1" finish-status="success" simple style="margin-top: 20px">
      <el-step title="Step 1" />
      <el-step title="Step 2" />
      <el-step title="Step 3" />
    </el-steps>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    setup() {
      // 这里添加需要的响应式数据和方法
    },
  });
  </script>
  