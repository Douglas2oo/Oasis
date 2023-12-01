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
      component: () => import('../views/Home.vue'),
      children: [
        {
          path: '/home',
          name: 'YourHome',
          component: () => import('../views/YourHome.vue'),

        },
        {
          path: '/ForumSquare',
          name: 'ForumSquare',
          component: () => import('../views/ForumSquare.vue'),

        },]
    }

  ]
})



export default router
