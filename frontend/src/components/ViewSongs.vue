<template>
  <div class="grid">
    <div class="panel large-panel">
      <div v-for="song in songs" :key="song.title">
        <span class="item item__title" @click="showSongInfo(song)">{{ song.title }}</span>
      </div>
    </div>

    <SongInfo v-if="displayInfo" :song="songSelect"/>
  </div>
</template>


<script setup>
  import { ref, onMounted } from 'vue'
  import { fetchSongs } from '@/api.js'
  import SongInfo from './SongInfo.vue'

  const songs = ref([])
  const songSelect = ref(null)
  const displayInfo = ref(false)

  function showSongInfo(song){
    if(song === songSelect.value){
        displayInfo.value = !displayInfo.value;
        if(!displayInfo){
            songSelect.value = null;
        }
    } else{
        songSelect.value = song;
        displayInfo.value = true;
    }
  }

  onMounted(async () =>{
    songs.value = await fetchSongs()
  })
</script>



<style>
    .large-panel{
        width: 450px;
    }
    .grid{
        display: grid;
        grid-template-columns: 450px 400px;
        gap: 20px;
        justify-content: center;
        align-items: start;
    }
    
</style>