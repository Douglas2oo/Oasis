import { createRouter, createWebHistory } from 'vue-router'




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: () => import('../views/loginPage.vue')
    },
    {
      path: '/:catchAll(.*)',
      name: '404',
      component: () => import('../views/404Page.vue') 
    },
    {
      path: '/home',
      name: 'home',
      component: () => import('../views/Home.vue')
    },

  ]
})



export default router
