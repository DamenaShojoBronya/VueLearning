<template>
    <el-container>
      <el-main>
        <el-row>
          <el-col>
            <el-input
              v-model="inputText"
              placeholder="输入要夸奖的食物或产品名称"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <el-button type="primary" @click="generateText">生成文案</el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <el-input
              type="textarea"
              :rows="5"
              v-model="generatedText"
              placeholder="生成的文案将显示在这里"
              readonly
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <el-button type="primary" @click="copyText">复制文案</el-button>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import { ElMessage } from "element-plus";
  
  const inputText = ref("");
  const generatedText = ref("");
  
  async function generateText() {
  if (!inputText.value.trim()) {
    ElMessage.error("请输入要夸奖的食物或产品名称");
    return;
  }

  try {
    const response = await fetch("YOUR_API_ENDPOINT", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        input: inputText.value,
        // ...其他所需参数
      }),
    });

    if (response.ok) {
      const data = await response.json();
      generatedText.value = data.generated_text; // 根据实际API响应调整
    } else {
      ElMessage.error("生成文案失败，请稍后重试");
    }
  } catch (error) {
    console.error("Error calling ChatGPT API:", error);
    ElMessage.error("生成文案失败，请稍后重试");
  }
}

  
  function copyText() {
    if (!generatedText.value.trim()) {
      ElMessage.error("没有可复制的文案");
      return;
    }
  
    navigator.clipboard.writeText(generatedText.value).then(() => {
      ElMessage.success("文案已复制");
    });
  }
  </script>
  