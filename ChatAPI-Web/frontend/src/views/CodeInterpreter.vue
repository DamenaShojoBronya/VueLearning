<template>
    <el-container>
      <el-header>
        <h1>代码解释器</h1>
      </el-header>
      <el-main>
        <el-row>
          <el-col :span="12">
            <el-input
              type="textarea"
              :rows="10"
              placeholder="在此输入代码"
              v-model="codeInput"
            ></el-input>
          </el-col>
          <el-col :span="12">
            <el-input
              type="textarea"
              :rows="10"
              readonly
              v-model="explanationOutput"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-select v-model="selectedLanguage" placeholder="选择编程语言">
              <el-option
                v-for="language in languages"
                :key="language.value"
                :label="language.label"
                :value="language.value"
              ></el-option>
            </el-select>
          </el-col>
          <el-col :span="6">
            <el-button type="primary" @click="submitCode">提交代码</el-button>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </template>
  
  <script>
  import { ref } from "vue";
  
  export default {
    setup() {
      const codeInput = ref("");
      const explanationOutput = ref("");
      const selectedLanguage = ref(null);
  
      const languages = [
        { label: "Python", value: "python" },
        { label: "JavaScript", value: "javascript" },
        { label: "Java", value: "java" },
        // 更多编程语言
      ];
  
      const submitCode = async () => {
        if (!codeInput.value || !selectedLanguage.value) {
          // 添加错误提示
          return;
        }
  
        try {
          // 调用API，此处应替换为实际API
          const response = await fetch("https://your-api-url", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              code: codeInput.value,
              language: selectedLanguage.value,
            }),
          });
  
          if (!response.ok) {
            throw new Error("请求失败");
          }
  
          const data = await response.json();
          explanationOutput.value = data.explanation;
        } catch (error) {
          // 添加错误处理
          console.error(error);
        }
      };
  
      return {
        codeInput,
        explanationOutput,
        selectedLanguage,
        languages,
        submitCode,
      };
    },
  };
  </script>  