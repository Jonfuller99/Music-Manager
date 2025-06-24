<template>
    <div class="login-text">Login</div>
    <form class="" action="" @submit.prevent="userLogin">
        <div class="form-group">
            <label for="username" class="form-label">Username:</label>
            <input required id="username" class="form-input login-form-input" type="username" v-model="username"></input>
            <label for="password" class="form-label">Password:</label>
            <input required id="password" class="form-input login-form-input" type="password" v-model="password"></input>
        </div>

        <div v-if="errorMessage" class="error-message">
            {{ errorMessage }}
        </div>

        <div class="btn-group">
            <button type="submit" class="btn login-button">Login</button>
        </div> 
    </form>   
    <p>No Account? <a @click="$emit('showCreateUser')">Sign up here</a></p>
</template>

<script setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    import { useAuthStore } from '@/stores/auth'

    const emit = defineEmits(['showCreateUser'])
    const authStore = useAuthStore()
    const router = useRouter()

    const username = ref('')
    const password = ref('')
    const errorMessage = ref('')

    async function userLogin(){
        try{
            await authStore.login(username.value, password.value)
            router.push('/home')
        } catch (error){
            console.log(error)
            errorMessage.value = error.response?.data?.detail || 'Login failed'
        }

    }



</script>

    

<style scoped>
.login-text{
    text-align: center;
    font-size: 50px;
    color: white;
    margin-bottom: 50px;
    margin-top: -100px;
}

.login-form-input{
    height: 50px;
    width: 350px;
}

a{
 color: rgb(117, 117, 182) ;   
 user-select: none;
 cursor:pointer;
}

.login-button{
    color: white;
    background-color: rgb(24, 96, 125);
    width: 330px;
    height: 50px;
}
</style>