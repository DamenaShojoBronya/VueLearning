// store.js
import { createStore } from 'vuex';
import App from '../App.vue';
import HeaderComponent from '../components/HeaderComponent.vue';
import PageFooter from '../components/PageFooter'

export default createStore({
  state: {
    blur: false
  },
  mutations: {
    setBlur(state, blur) {
      state.blur = blur;
    },
    SET_BLUR(state, value) {
      state.blur = value;
  },
  },
  getters: {
    blur: (state) => state.blur
  },
  modules: {
    App,
    HeaderComponent,
    PageFooter
  }
});
