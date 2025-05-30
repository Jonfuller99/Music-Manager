<template>
  <div class="songs">
    <div>
      <h1>Your Songs:</h1>
      <ViewSongs></ViewSongs>
    </div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .songs {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
<script setup>
  import { ref, onMounted } from 'vue'
  import { fetchSongs, fetchData } from '@/api.js'
  import ViewSongs from '@/components/ViewSongs.vue'

  const message = ref('Loading...')
  const age = ref('Loading...')
  const songs = ref([])
  const url = ref('Loading...')

  onMounted(async () => {    
    const data = await fetchData()
    message.value = data.message
    age.value = data.age
    url.value = data.url

    songs.value = await fetchSongs()
  }) 
</script>