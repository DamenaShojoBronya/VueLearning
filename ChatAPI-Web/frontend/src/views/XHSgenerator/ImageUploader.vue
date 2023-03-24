<template>
    <div>
        <el-upload :file-list="fileList" :action="uploadAction" :http-request="handleUpload" :on-success="handleSuccess"
            :on-error="handleError" :on-remove="handleRemove" :limit="image" list-type="picture-card"
            :auto-upload="false">
            <i class="el-icon-plus"></i>
        </el-upload>
        <el-button type="primary" @click="submitImage">上传图片</el-button>

    </div>
</template>
<script setup>
import { ref } from "vue";

const fileList = ref([]);
const uploadAction = "YOUR_UPLOAD_ENDPOINT"; // 请替换为您的图片上传API端点

function handleUpload(uploadData) {
    // 在这里处理上传图片的请求
    // 您可以使用fetch、Axios或其他HTTP客户端库发送请求
    // 这是一个使用fetch的示例：
    const { file, onSuccess, onError } = uploadData;
    const formData = new FormData();
    formData.append("file", file);

    fetch(uploadAction, {
        method: "POST",
        body: formData,
    })
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Upload failed");
            }
        })
        .then((data) => {
            onSuccess(data);
        })
        .catch((error) => {
            console.error("Error uploading image:", error);
            onError(error);
        });
}

function handleSuccess(response, file, fileList) {
    console.log("Upload successful:", response);
    // 在这里处理上传成功后的操作，例如显示上传的图片
}

function handleError(error, file, fileList) {
    console.error("Upload failed:", error);
    // 在这里处理上传失败后的操作，例如显示错误信息
}

function handleRemove(file, fileList) {
    console.log("File removed:", file);
    // 在这里处理移除文件后的操作，例如删除已上传的图片
}

function submitImage() {
    // 触发上传
    document.querySelector(".el-upload__input").click();
}
</script>  