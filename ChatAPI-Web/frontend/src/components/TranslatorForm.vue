<!-- Translator.vue -->
<template>
    <div>
        <el-form ref="form" label-position="top">
            <el-form-item label="原文">
                <el-input type="textarea" :rows="5" v-model="sourceText" @input="translateText"></el-input>
            </el-form-item>
            <el-form-item label="源语言">
                <el-select v-model="sourceLanguage" @change="translateText">
                    <el-option v-for="language in languages" :key="language.value" :label="language.label"
                        :value="language.value"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="目标语言">
                <el-select v-model="targetLanguage" @change="translateText">
                    <el-option v-for="language in languages" :key="language.value" :label="language.label"
                        :value="language.value"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="译文">
                <el-input type="textarea" :rows="5" v-model="translatedText" readonly></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="translateText">翻译</el-button>
                <el-button @click="copyText">复制译文</el-button>
                <el-button @click="clearForm">清除</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            sourceText: "",
            translatedText: "",
            sourceLanguage: "",
            targetLanguage: "",
            languages: [
                { label: "自动检测", value: "auto" },
                { label: "英语", value: "en" },
                { label: "简体中文", value: "zh-CN" },
                { label: "繁体中文", value: "zh-TW" },
                { label: "日语", value: "ja" },
                // 添加其他支持的语言
            ],
        };
    },
    methods: {
        async translateText() {
            if (!this.sourceText || !this.sourceLanguage || !this.targetLanguage) {
                this.$message.error("请填写原文并选择源语言和目标语言");
                return;
            }

            try {
                // 调用翻译 API，替换以下代码
                // const response = await yourTranslateApiCall(this.sourceText, this.sourceLanguage, this.targetLanguage);
                // this.translatedText = response.data.translatedText;

                this.translatedText = this.sourceText; // 删除此行，仅用于示例
            } catch (error) {
                console.error("翻译出错：", error);
                this.$message.error("翻译时出现错误，请重试！");
            }
        },
        async copyText() {
            try {
                await navigator.clipboard.writeText(this.translatedText);
                this.$message.success("已复制到剪贴板");
            } catch (err) {

                this.$message.error("复制失败");
            }
        },
        clearForm() {
            this.sourceText = "";
            this.translatedText = "";
            this.sourceLanguage = "";
            this.targetLanguage = "";
        },
    },
};
</script>

<style scoped>
/* 在这里添加组件样式 */
</style>