<template>
    <div class="login-text">Sign up</div>
<form @submit.prevent="handleSubmit">
    <div class="form-group">
        <label for="username" class="form-label">Username:</label>
        <input required id="username" class="form-input login-form-input" type="text" v-model="username"/>
        <label for="artist_name" class="form-label">Artist Name:</label>
        <select id="artist" class="form-input login-form-input" v-model="artistId">
        <option v-for="artist in availableArtists" :key="artist.artist_id" :value="artist.artist_id">
            {{ artist.name }}
        </option>
        </select>
        <label for="password" class="form-label">Password:</label>
        <input required id="password" class="form-input login-form-input" type="password" v-model="password"/>
    </div>
    <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
    </div>
    <button type="submit" class="btn login-button">Sign up</button>
 
</form>   
</template>

<script setup>
    import { ref, onMounted, computed } from 'vue'
    import { fetchArtists, registerUser } from '@/api'

    const username = ref('')
    const artists = ref([])
    const artistName = ref('')
    const artistId = ref(-1)
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
            artist_id: artistId.value,
            password: password.value,
        }
        const result = await registerUser(newUser)
        console.log("User added successfully", result)
    }

    const availableArtists = computed(() =>
        artists.value.filter(artist => artist.user_id === null)
    )

    onMounted(async () =>{
        artists.value = await fetchArtists()
    })


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