<template>
    <div class="container center">
        <div class="container-h center login panel fancy-panel">
            <Login @show-create-user="handleCreateUser"></Login>
    
        </div>
        <div v-if="toggleCreateUser">
            <Modal @close="handleCreateUser">
                <div class="container-h center login panel fancy-panel">
                    <CreateUser/>
                </div>
            </Modal>    
        </div>

    </div>


</template>

<script setup>   
import Login from '@/components/Login.vue';  
import CreateUser from '@/components/CreateUser.vue';  
import Modal from '@/components/Modal.vue';
import { ref } from 'vue';

const toggleCreateUser = ref(false)

function handleCreateUser(){
    toggleCreateUser.value = !toggleCreateUser.value
}

</script>

<style scoped>
.login{
    width: 500px;
    height: 700px;
}
.center{
    align-items: center;
    justify-content: center;
}


</style>