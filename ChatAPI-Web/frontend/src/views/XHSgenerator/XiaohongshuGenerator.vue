<template>
  <div>
    <el-container :class="{ 'blur-background': showImageDialog }">
      <el-main>
        <el-row>
          <el-col>
            <el-input type="textarea" :rows="15" v-model="generatedText" placeholder="生成的文案将显示在这里" readonly></el-input>
          </el-col>
        </el-row>
        <el-row>
          
          <div class="generate-buttons">
            <el-button type="primary" @click="copyText">复制文案</el-button>
            <el-button type="primary" @click="generateText">生成文案</el-button>
            <input type="file" ref="imageInput" @change="handleImageChange" accept="image/*" style="display: none" />
            <el-button type="primary" @click="uploadImage">上传图片</el-button>
          </div>
        </el-row>
        <el-row>
          <div @click="handleImageCardClick" v-if="imageSrc" class="image-card">
              <img :src="imageSrc" alt="Uploaded Image" />
            </div>
        </el-row>

        <el-row>
          <el-col>
            <el-input class="inputText" v-model="inputText" placeholder="输入要夸奖的食物或产品名称"></el-input>
          </el-col>
        </el-row>

        <el-row />

        <div>
        </div>

      </el-main>

    </el-container>

    <div v-if="showImageDialog" class="image-zoom">
      <div class="image-zoom-card" @click="handleImageCardClick">
        <img v-if="imageSrc" :src="imageSrc" alt="Uploaded Image" />
      </div>
    </div>
  </div>
</template>

<script>
// const apiClient = axios.create({
//   baseURL: 'http://localhost:5000/',
// });
export default {
  data() {
    return {

    }
  },
  methods: {
    //与后端通讯
    // async sendRequest(data) {
    //   const response = await
    //     apiClient.post('/api/rewrite', data);
    //   return response.data;
    // },
  },
}
</script>

<script setup>
import { ref } from "vue";
import { ElMessage } from "element-plus";
import apiClient from "../apiClient";
import { useStore } from 'vuex';
// 获取 Vuex store 实例
const store = useStore();

const inputText = ref("");
const generatedText = ref("");
const imageSrc = ref("");
const imageInput = ref();

// 将 showImageDialog 的值从 Vuex store 初始化
const showImageDialog = ref(false);

function handleImageCardClick() {
  // 切换 showImageDialog 的值
  const newShowImageDialogValue = !showImageDialog.value;

  console.log("showImageDialog.value1:", showImageDialog.value);
  // 提交新值到 Vuex store
  store.commit('setBlur', newShowImageDialogValue);

  // 更新本地的 showImageDialog 变量
  showImageDialog.value = newShowImageDialogValue;

  console.log("showImageDialog.value2:", showImageDialog.value);
}

async function generateText() {
  if (!inputText.value.trim()) {
    ElMessage.error("请输入要夸奖的食物或产品名称");
    return;
  }

  try {
    const response = await apiClient.post("/api/xiaohongshu", {
      input: inputText.value,
      // ...其他所需参数

    });

    if (response.status === 200) {
      generatedText.value = response.data.generated_text; // 根据实际API响应调整
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
.el-container,
.el-row{
  justify-content: center;
}
.el-main {
  display: flex;
  /* background-color: bisque; */
  border-radius: 8px;
  max-width: 70vw;
  min-height: 70vh;
  flex-wrap: wrap;
  flex-direction: column;
  align-content: stretch;
  justify-content: space-around;
  align-items: stretch;
}

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
  width: min(80vw, 80vh);
  height: min(80vw, 80vh);
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

.generate-buttons {
  display: flex;
  min-width: 30vw;
}
.inputText{
  max-width: 60vw;
}
.el-button{
  margin-left:2vw;
  margin-right:2vw;
}
</style>
  