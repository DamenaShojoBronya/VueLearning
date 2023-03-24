<template>
  <div>
    <el-container :class="{ 'blur-background': showImageDialog }">
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
            <div @click="showImageDialog = true" v-if="imageSrc" class="image-card">
              <img :src="imageSrc" alt="Uploaded Image" />
            </div>
          </el-col>
        </el-row>
      </el-main>

    </el-container>

    <!-- <div v-if="showImageDialog" class="image-zoom" @click="showImageDialog = false">
      <div class="image-zoom-card">
        <img v-if="imageSrc" :src="imageSrc" alt="Uploaded Image" />
      </div>
    </div> -->
    <div v-if="showImageDialog" class="image-zoom" @click="showImageDialog = false">
      <div @click="toggleImageDialog" v-if="imageSrc" class="image-card">
        <img :src="imageSrc" alt="Uploaded Image" />
      </div>
    </div>
  </div>
</template>
  
<script setup>
import { ref } from "vue";
import { ElMessage } from "element-plus";

import { useStore } from 'vuex';
// 获取 Vuex store 实例
const store = useStore();
// 添加一个新方法 toggleImageDialog，用于切换图片对话框和更新模糊状态
const toggleImageDialog = () => {
  showImageDialog.value = !showImageDialog.value;
  store.commit('setBlur', showImageDialog.value);
};

const inputText = ref("");
const generatedText = ref("");
const imageSrc = ref("");
const imageInput = ref();
const showImageDialog = ref(false);

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

<style scoped>
.image-card {
  width: 200px;
  height: 200px;
  border: 1px solid #ccc;
  overflow: hidden;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-card img {
  max-width: 100%;
  max-height: 100%;
}

.dialog-fade-enter-active,
.dialog-fade-leave-active {
  transition: opacity 0.3s ease;
}

.dialog-fade-enter,
.dialog-fade-leave-to {
  opacity: 0;
}

.blur-background {
  filter: blur(4px);
}

.image-zoom {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  background-color: rgba(0, 0, 0, 0.5);
}

.image-zoom-wrapper {
  position: relative;
}

.image-zoom-card {
  background-color: white;
  border-radius: 8px;
  width: min(50vw, 50vh);
  height: min(50vw, 50vh);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}
.image-zoom-card img {
  max-width: 100%;
  max-height: 100%;
  object-fit: scale-down;
}
</style>
  