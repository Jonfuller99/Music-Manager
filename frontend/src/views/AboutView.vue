<template>
  <div class="about">

    <!-- <div @click="changeMessage">
      <h1>{{message}}</h1>
    </div>
    <h1> {{age}}</h1>
    <button @click="age++">Increase age</button>
    <button @click="age--">Decrease age</button>  -->

    <div>
      <h1>All your songs:</h1>
      <ul>
        <li v-for="song in songs">
          <h3>{{ song.title }} - {{ song.artists.join(', ') }}</h3>
          <h4>Genre: {{ song.genre }}</h4>
          <h4>Beat: {{ song.beat }}</h4>
        </li>
      </ul>
    </div>
    <div>
      <a :href="url">click me pls</a>
    </div>

  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
<script setup>
  import { ref, onMounted } from 'vue'
  import { fetchSongs, fetchData } from '@/api.js'

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