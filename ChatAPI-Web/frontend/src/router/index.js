import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RewriteForm from '../views/RewriteForm.vue'
import TranslatorForm from '../views/TranslatorForm.vue'
import CodeInterpreter from '../views/CodeInterpreter.vue'
import XiaohongshuGenerator from '../views/XiaohongshuGenerator.vue' 

const routes = [
  // 默认首页index重定向到跳转的首页home
  {
    path: '/',
    name: 'index',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  //文章改写
  {
    path: '/rewrite',
    name: 'rewrite',
    component: RewriteForm
  },
  //翻译
  {
    path: '/translate',
    name: 'translate',
    component: TranslatorForm
  },
  //代码解释
  {
    path: '/code2txt',
    name: 'code2txt',
    component: CodeInterpreter
  },
    //代码解释
    {
      path: '/xiaohongshuGenerator',
      name: 'code2txt',
      component: XiaohongshuGenerator
    },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
