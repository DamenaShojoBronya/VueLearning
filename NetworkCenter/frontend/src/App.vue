<template>
  <HeaderComponent :class="headerClasses" />
  <router-view />
  <el-backtop :right="100" :bottom="100" />
  <PageFooter :class="{ 'blur-background': blur }" />
</template>

<script>
import HeaderComponent from './components/HeaderComponent.vue';
import PageFooter from './components/PageFooter.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'App',
  components: {
    HeaderComponent,
    PageFooter
  },
  data() {
    return {
      scrollY: 0,
      hideHeader: false
    };
  },
  computed: {
    ...mapGetters(['blur']),
    headerClasses() {
      return {
        'blur-background': this.blur,
        'hidden-header': this.hideHeader
      };
    }
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const scrollY = window.pageYOffset || document.documentElement.scrollTop;
      const hideHeader = scrollY > 700; // 滚动1000像素后隐藏header
      this.hideHeader = hideHeader;
    }
  }
};
</script>

<style>
* {
  margin: 0;
  padding: 0px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.blur-background {
  filter: blur(4px);
}


.hidden-header {
  opacity: 0; /* 使用opacity实现渐隐效果 */
  transition: opacity 1s ease-in-out; /* 过渡效果，使隐藏和显示的变化更平滑 */
}
</style>
