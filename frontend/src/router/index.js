import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SongsView from '@/views/SongsView.vue'
import ProfileView from '@/views/ProfileView.vue'
import { useAuthStore } from '@/stores/auth'

function requireAdmin(to, from, next){
  const authStore = useAuthStore()
  if(!authStore.isAuthenticated){
    next('/')
  } else if(!authStore.isAdmin){
    next('/home')
  } else{
    next()
  } 
}

function requireAuth(to, from, next){
  const authStore = useAuthStore()
  if(!authStore.isAuthenticated){
    next('/')
  }else{
    next()
  }
}




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      beforeEnter: requireAuth,
      meta: {requiresAuth: true}
    },
    {
      path: '/songs',
      name: 'songs',
      component: SongsView,
      beforeEnter: requireAuth,
      meta: {requiresAuth: true}
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => ProfileView,
      beforeEnter: requireAuth,
      meta: {requiresAuth: true}
    },
  ],
})

router.beforeEach((to, from, next) =>{
  const authStore = useAuthStore()
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/')
  } else if (to.meta.reqquiresAdmin && !authStore.isAdmin){
    next('/home')
  } else {
    next()
  }
})

export default router
