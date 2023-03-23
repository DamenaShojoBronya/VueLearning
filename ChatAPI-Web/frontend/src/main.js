import { createApp } from 'vue';
import ElementPlus from 'element-plus';
import 'element-plus/theme-chalk/index.css'
import App from './App.vue';
import router from './router'

const app = createApp(App).use(router);
app.use(ElementPlus);
app.mount('#app');
