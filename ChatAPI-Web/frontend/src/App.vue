<template>
  <div :class="{ 'blur-background': blur }">
    <HeaderComponent />
    <router-view />
    <PageFooter />
  </div>
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
  computed: {
    ...mapGetters(['blur'])
  }
}

</script>

<style>
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
</style>
