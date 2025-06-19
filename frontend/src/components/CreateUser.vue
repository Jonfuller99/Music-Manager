<template>
    <div class="login-text">Sign up</div>
<form @submit.prevent="handleSubmit">
    <div class="form-group">
        <label for="username" class="form-label">Username:</label>
        <input id="username" class="form-input login-form-input" type="text" v-model="username"/>
        <label for="artist_name" class="form-label">Artist Name:</label>
        <input id="artist_name" class="form-input login-form-input" type="text" v-model="artistName"/>
        <label for="password" class="form-label">Password:</label>
        <input id="password" class="form-input login-form-input" type="password" v-model="password"/>
    </div>
    <button type="submit" class="btn login-button">Sign up</button>
 
</form>   
    <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import { registerUser } from '@/api'

    const username = ref('')
    const artistName = ref('')
    const password = ref('')
    const errorMessage = ref('')

    const emit = defineEmits(['close'])

    async function handleSubmit(){
        try{
            errorMessage.value = ''
            await userSignUp()
            emit('close')
        }catch (error){
            if (error.response?.status === 400) {
                errorMessage.value = error.response.data.detail || 'User already exists'
            } else if (error.response?.status === 401) {
                errorMessage.value = 'Incorrect username or password'
            } else {
                errorMessage.value = 'An error occurred. Please try again.'
            }
            console.error('Registration failed:', error)
        }

    }

    async function userSignUp(){
        const newUser = { 
            username: username.value,
            artist_name: artistName.value,
            password: password.value,
        }
        const result = await registerUser(newUser)
        console.log("User added successfully", result)
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
.error-message {
    color: #ff6b6b;
    background-color: rgba(255, 107, 107, 0.1);
    border: 1px solid #ff6b6b;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 20px;
    text-align: center;
}

</style>