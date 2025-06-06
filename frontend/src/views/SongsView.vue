<template>
    <div class="container main">
      <div>
        <ViewSongs @song-selected="handleSongSelection"/>
      </div>
      <div class="container panel temp">
        <div v-if="!selectedSong" class="container-h center-text temp">
          Select a song to play
        </div>
        <SongInfo v-if="selectedSong" :song="selectedSong"/>
        <div v-if="selectedSong" class="container-h temp">
          <div class="panel fancy-panel">
            <PlayerView :audioSrc="songPath"/>
 
          </div>
          <div class="panel fancy-panel temp">
            lyrics
          </div>
          <div class="panel fancy-panel temp">
            comments
          </div>
        </div>
      </div>
    </div>
  
</template>

<style>
  .center-text{
    text-align: center;
    justify-content: center;
    font-size: 50px;
    font-style: italic;
  }





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
  import { fetchSongs } from '@/api.js'
  import ViewSongs from '@/components/ViewSongs.vue'
  import SongInfo from '@/components/SongInfo.vue'
  import PlayerView from '@/components/PlayerView.vue'

  const songs = ref([])
  const selectedSong = ref(null)
  const songPath = ref()

  function handleSongSelection(song){
    selectedSong.value = song
    songPath.value = song.file_path
  }
  

  onMounted(async () => {    
    songs.value = await fetchSongs()
  }) 
</script>