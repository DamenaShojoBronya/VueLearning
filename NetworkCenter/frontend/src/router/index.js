import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RewriteForm from '../views/RewriteForm.vue'
import TranslatorForm from '../views/TranslatorForm.vue'
import CodeInterpreter from '../views/CodeInterpreter.vue'
import XiaohongshuGenerator from '../views/XHSgenerator/XiaohongshuGenerator.vue'
import ProcessApproval from '../views/Products/ProcessApproval.vue';
import ActivitiesView from '../views/Activities/ActivitiesView.vue';

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
  //小红书生成器
  {
    path: '/xiaohongshuGenerator',
    name: 'code2txt',
    component: XiaohongshuGenerator
  },
  {
    path: '/timeline',
    name: 'timeline',
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "timeline" */ '../views/TimelineView.vue')
  },
  //关于我们
  {
    path: '/about',
    name: 'about',
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  //产品
  {
    path: '/products',
    name: 'products',
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Products/ProductsView.vue')
  },
  //活动
  {
    path: '/activities',
    name: 'activities',
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Activities/ActivitiesView.vue')
  },
  {
    path: '/activityPage1',
    name: 'activityPage1',
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Activities/ActivityPage1.vue')
  },
  {
    path: '/activityPage2',
    name: 'activityPage2',
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Activities/ActivityPage2.vue')
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
