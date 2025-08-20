<template>
    <div class="container ">
      <div class="panel large-panel profile" >
        <Account></Account>
      </div>
      <div class="temp panel container">
        <div class="panel fancy-panel box-1">
          <ChangeArtistName></ChangeArtistName>
        </div>
        <div class="btn" style="height: 50px;" v-on:click="authStore.logout">Logout</div>
      </div>
    </div>

</template>

<script setup>
  import Account from '@/components/Account.vue';      
  import ChangeArtistName from '@/components/ChangeArtistName.vue';
  import { useAuthStore } from '@/stores/auth';

  const authStore = useAuthStore()


</script>

<style scoped>
  .profile{
    width: 400px;
}
</style>