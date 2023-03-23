<template>
    <div :class="['container', currentTheme]">
        <el-row>
            <el-col :span="24" class="header">
                <h1>代码解释器</h1>
                <el-switch v-model="darkTheme" active-color="#409EFF" inactive-color="#E4E7ED"
                    @click="switchTheme"></el-switch>
            </el-col>
        </el-row>
        <el-row class="instructions">
            <el-col :span="24">

            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-input type="textarea" :rows="10" placeholder="在此输入代码" v-model="codeInput"></el-input>
                <el-select v-model="selectedLanguage" placeholder="选择编程语言" @change="loadExample">
                    <el-option v-for="language in languages" :key="language.value" :label="language.label"
                        :value="language.value"></el-option>
                </el-select>
            </el-col>
            <el-col :span="12">
                <el-input type="textarea" :rows="10" readonly v-model="explanationOutput"></el-input>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="6">
                <el-button type="primary" @click="submitCode" :loading="loading">提交代码</el-button>
            </el-col>
        </el-row>
        <el-row v-if="errorMessage">
            <el-col :span="24">
                <el-alert :title="errorMessage" type="error" show-icon center :closable="false"></el-alert>
            </el-col>
        </el-row>
    </div>
</template>
  
<script>
import { ref, computed } from "vue";

export default {
    setup() {
        const codeInput = ref("");
        const explanationOutput = ref("");
        const selectedLanguage = ref(null);
        const errorMessage = ref("");
        const loading = ref(false);
        const darkTheme = ref(false);
        const currentTheme = computed(() => (darkTheme.value ? "dark-theme" : "light-theme"));

        const switchTheme = () => {
            darkTheme.value = !darkTheme.value;
            toggleTheme();
        };

        const languages = [
            { label: "Python", value: "python" },
            { label: "JavaScript", value: "javascript" },
            { label: "Java", value: "java" },
            // 更多编程语言
        ];

        const loadExample = () => {
            switch (selectedLanguage.value) {
                case "python":
                    codeInput.value = "import math\n\nprint(math.sqrt(9))";
                    break;
                case "javascript":
                    codeInput.value = "function greet(name) {\n console.log('Hello, ' + name + '!');\n}\n\ngreet('John');";
                    break;
                case "java":
                    codeInput.value = "public class HelloWorld {\n public static void main(String[] args) {\n System.out.println('Hello, World!') }\n}";
                    break;
                default:
                    break;
            }
        };
        const submitCode = async () => {
            if (!codeInput.value || !selectedLanguage.value) {
                errorMessage.value = "请确保输入代码和选择编程语言。";
                return;
            }
            errorMessage.value = "";
            loading.value = true;

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
                errorMessage.value = "请求失败，请稍后重试。";
                console.error(error);
            } finally {
                loading.value = false;
            }
        };

        const toggleTheme = () => {
            darkTheme.value = !darkTheme.value;
        };

        return {
            codeInput,
            explanationOutput,
            selectedLanguage,
            languages,
            submitCode,
            loadExample,
            errorMessage,
            loading,
            darkTheme,
            currentTheme,
            toggleTheme,
            switchTheme
        };
    },
};
</script>

<style>
.container {
    max-width: 1;
    margin: 0 auto;
    padding: 1rem;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.instructions {
    margin-bottom: 1rem;
}

.light-theme {
    --bg-color: #ffffff;
    --text-color: #303133;
}

.dark-theme {
    --bg-color: #303133;
    --text-color: #ffffff;
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
}

.container {
    background-color: var(--bg-color);
    color: var(--text-color);
}
</style>