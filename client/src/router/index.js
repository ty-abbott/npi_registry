import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Search from '../components/Search.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Search',
      component: Search
    },
    {
      path:'/home',
      name: 'Home',
      component: Home
  },
  ]
})

export default router
