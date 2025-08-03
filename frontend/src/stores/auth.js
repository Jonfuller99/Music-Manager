import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { loginUser, getCurrentUser } from '@/api'
import router from '@/router'

export const useAuthStore = defineStore('auth', () => {
  const isLoggedIn = ref(false)
  const user = ref(null)
  const token = ref(null)

  const isAuthenticated = computed(()=>!!token.value)
  const userName = computed(()=> user.value?.username|| '')
  const userRole = computed(()=> user.value?.role || 'user')
  const isAdmin = computed(()=> user.value?.role  === 'admin')
  const isUser = computed(()=> user.value?.role  === 'user')

  async function login(username, password){
    try{
      const resp = await loginUser(username, password)
      token.value = resp.access_token
      isLoggedIn.value = true

      await fetchCurrentuser()

      return resp
    }catch (error){
      logout()
      throw error
    }
  }

  function logout(){
    isLoggedIn.value = false
    user.value = null
    token.value = null
    router.push('/')
  }

  async function fetchCurrentuser(){
    if (!token.value) return
    try{
      const userData = await getCurrentUser(token.value)
      user.value = userData
    }catch(error){
      if (error.response?.status === 401){
        logout()
      }
      throw error
    }

  }

  function requireAdmin(){
    if (!isAdmin){
      throw new Error('Admin access required')
    }
  }

  return {
    isLoggedIn,
    user,
    token,
    isAuthenticated,
    userName,
    userRole,
    isAdmin,
    isUser,
    login,
    logout,
    fetchCurrentuser,
    requireAdmin,
  }
}, {
  persist:{
    key: 'auth',
    storage: localStorage,
    paths: ['isLoggedIn', 'user', 'token']
}

})
