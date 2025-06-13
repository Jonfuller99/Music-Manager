<template>
    <div class="login-text">Login</div>
<form class="" action="" @submit.prevent="userLogin">
    <div class="form-group">
        <label for="username" class="form-label">Username:</label>
        <input id="username" class="form-input login-form-input" type="username" v-model="username"></input>
        <label for="password" class="form-label">Password:</label>
        <input id="password" class="form-input login-form-input" type="password" v-model="password"></input>
    </div>
    <div class="btn-group">
        <button type="submit" class="btn login-button">Login</button>
    </div> 
</form>   
<p>No Account? <a @click="$emit('showCreateUser')">Sign up here</a></p>
</template>

<script setup>
    import { ref } from 'vue'
    import { loginUser } from '@/api'
    import router from '@/router'

    const emit = defineEmits(['showCreateUser'])

    const username = ref('')
    const password = ref('')

    async function userLogin(){
        try{
            const loginResult = await loginUser(username.value, password.value)
            console.log('Login successful:', loginResult)
            router.push('/home')
        } catch (error){
            console.error('Login Failed', error.message)
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
}

.login-button{
    color: white;
    background-color: rgb(24, 96, 125);
    width: 330px;
    height: 50px;
}
</style>