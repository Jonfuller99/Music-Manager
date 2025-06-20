<template>
    <div class="container main">
      <div class="panel large-panel profile" >
        <Account></Account>
      </div>
      <div class="temp panel">
        wide varaity of settings and options!
      </div>
    </div>

</template>

<script setup>
  import Account from '@/components/Profile/Account.vue';      

</script>

<style scoped>
  .profile{
    width: 400px;
}
</style>