<template>
    <div class="container main">
      <div class="panel large-panel profile" >
        <Account></Account>
      </div>
      <div class="temp panel">
        <div class="btn" v-on:click="authStore.logout">Logout</div>
      </div>
    </div>

</template>

<script setup>
  import Account from '@/components/Account.vue';      
  import { useAuthStore } from '@/stores/auth';

  const authStore = useAuthStore()


</script>

<style scoped>
  .profile{
    width: 400px;
}
</style>