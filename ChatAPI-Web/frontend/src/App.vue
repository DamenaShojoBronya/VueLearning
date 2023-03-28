<template>
  <HeaderComponent :class="{ 'blur-background': blur }" />
  <router-view />
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
  computed: {
    ...mapGetters(['blur'])
  }
}

</script>

<style>
* {
    margin: 0;
    padding: 0px;
    /* margin:auto; */
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
</style>
