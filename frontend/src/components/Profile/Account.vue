<template>
    <div class="container-v">
        <div class="panel fancy-panel temp">
            <div class="name white">Your Account: </div>
            <div class="name green">{{ authStore.user.artist_name }}</div>
        </div>
        
        <div class="panel ">
            <div><span class="info white">Username:</span>  {{ authStore.userName }}</div>
            <div><span class="info white">Account age:</span> {{ formatDate(authStore.user.created_at) }}</div>
            <div><span class="info white">Permission:</span> {{ authStore.userRole }}</div>
        </div>    
    </div>
    


</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
    const authStore = useAuthStore()

    const formatDate = (dateString)=>{
      const date = new Date(dateString);
      return date.toLocaleString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
      })
    };

</script>


<style scoped>
.info{
    font-weight:bold;
}
.name{
    font-size: 32px;
    font-weight: bolder;
}
.white{
    color: white;
}
.green{
    color: var(login-form-input);
    font-style: italic;
}

</style>