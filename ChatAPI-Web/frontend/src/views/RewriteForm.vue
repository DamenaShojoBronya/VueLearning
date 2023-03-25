<template>
  <el-form ref="form" label-position="top">
    <el-form-item label="原始文章">
      <el-input type="textarea" :rows="10" v-model="originalText"></el-input>
    </el-form-item>
    <el-form-item label="文章风格">
      <el-select v-model="selectedStyle" placeholder="请选择文章风格">
        <el-option v-for="style in articleStyles" :key="style.value" :label="style.label"
          :value="style.value"></el-option>
      </el-select>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="submitForm">提交</el-button>
      <el-button @click="copyText">复制改写后的文章</el-button>
      <el-button @click="clearForm">清除</el-button>
    </el-form-item>

    <el-form-item label="改写后的文章">
      <el-input type="textarea" :rows="10" v-model="rewrittenText" readonly></el-input>
    </el-form-item>
  </el-form>
</template>

<script>
import apiClient from "./apiClient";


export default {
  data() {
    return {
      originalText: "",
      rewrittenText: "",
      selectedStyle: "",
      articleStyles: [
        { label: "正式", value: "formal" },
        { label: "幽默", value: "humorous" },
        { label: "科幻", value: "sci-fi" },
        { label: "浪漫", value: "romantic" },
        { label: "叙事", value: "narrative" },
        { label: "说教式", value: "didactic" },
        { label: "抽象", value: "abstract" },
        { label: "新闻报道", value: "news" },
        { label: "评论/评价", value: "critique" },
        { label: "鼓舞/励志", value: "inspirational" },
        { label: "对话式", value: "dialogue" },
        { label: "调查/研究", value: "investigative" },
        { label: "诗歌", value: "poetry" },
        { label: "教育/指导", value: "educational" },
        { label: "报告/总结", value: "report" },
        { label: "随笔/随想", value: "essay" },
        { label: "童话/寓言", value: "fable" },
        { label: "悬疑/推理", value: "mystery" },
        { label: "RAP", value: "rap" },
        { label: "旅行/游记", value: "travel" },
        { label: "自传/传记", value: "biography" },
      ],
    };
  },
  methods: {
    //与后端通讯
    async sendRequest(data) {
      const response = await
        apiClient.post('/api/rewrite', data);
      return response.data;
    },
    async copyText() {
      try {
        await navigator.clipboard.writeText(this.rewrittenText);
        this.$message.success("已复制到剪贴板");
      } catch (err) {
        this.$message.error("复制失败");
      }
    },
    clearForm() {
      this.originalText = "";
      this.rewrittenText = "";
      this.selectedStyle = "";
    },
    async submitForm() {
      // 添加前置提示，告知用户正在处理请求
      this.$message({
        message: '正在处理您的请求，请稍候...',
        type: 'info',
        duration: 0,
        showClose: true,
        customClass: 'submitFormMessage'
      });

      try {
        const response = await apiClient.post("/api/change_style", { original_text: this.originalText, style: this.selectedStyle });
        this.rewrittenText = response.data.changed_text;

        // 添加成功提示
        this.$message({
          message: '文章已成功改写！',
          type: 'success',
          duration: 3000,
          showClose: true
        });
      } catch (error) {
        console.error("Error rewriting article:", error);

        // 添加报错提示
        this.$message({
          message: '改写文章时出现错误，请重试！',
          type: 'error',
          duration: 3000,
          showClose: true
        });
      } finally {
        // 删除前置提示
        this.$message.closeAll();
      }
    },

  },
};
</script>
