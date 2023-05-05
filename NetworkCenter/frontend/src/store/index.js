// store.js
import { createStore } from 'vuex';
import App from '../App.vue';
import HeaderComponent from '../components/HeaderComponent.vue';
import PageFooter from '../components/PageFooter'
import workflow from './workflow';

export default createStore({
  state: {
    blur: false
  },
  mutations: {
    setBlur(state, blur) {
      state.blur = blur;
    },
  },
  getters: {
    blur: (state) => state.blur
  },
  modules: {
    App,
    HeaderComponent,
    PageFooter,
    workflow
  }
});
