import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { loginUser, getCurrentUser } from '@/api'

export const useAuthStore = defineStore('auth', () => {
  const isLoggedIn = ref(false)
  const user = ref(null)
  const token = ref(null)

  const isAuthenticated = computed(()=>!!token.value)
  const userName = computed(()=> user.value?.username|| '')

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
  return {
    isLoggedIn,
    user,
    token,
    isAuthenticated,
    userName,
    login,
    logout,
    fetchCurrentuser
  }
}, {
  persist:{
    key: 'auth',
    storage: localStorage,
    paths: ['isLoggedIn', 'user', 'token']
}

})
