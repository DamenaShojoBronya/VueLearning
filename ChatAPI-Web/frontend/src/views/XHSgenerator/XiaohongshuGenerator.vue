<template>
  <el-container>
    <el-main>
      <el-row>
        <el-col>
          <el-input v-model="inputText" placeholder="输入要夸奖的食物或产品名称"></el-input>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-button type="primary" @click="generateText">生成文案</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-input type="textarea" :rows="5" v-model="generatedText" placeholder="生成的文案将显示在这里" readonly></el-input>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-button type="primary" @click="copyText">复制文案</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <input type="file" ref="imageInput" @change="handleImageChange" accept="image/*" style="display: none" />
          <el-button type="primary" @click="uploadImage">上传图片</el-button>
          <img v-if="imageSrc" :src="imageSrc" alt="Uploaded Image" />
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
const imageSrc = ref("");
const imageInput = ref();

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

//上传图片
function uploadImage() {
  imageInput.value.click();
}

function handleImageChange(event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      imageSrc.value = e.target.result;
    };
    reader.readAsDataURL(file);
  }
}
</script>
  