<template>
  <div>
    <div class="panel large-panel">
      <div v-if="authStore.isAdmin" class="container">
        <div class="item panel temp fancy-panel controls" @click="deleteSong">-</div>
        <div class="item panel temp fancy-panel controls" @click="toggleAddTracks">+</div>
      </div>
      <div v-for="song in songs" :key="song.title">
        <span class="item item__title" @click="showSongInfo(song)">{{ song.title }}</span>
      </div>
    </div>

    <div v-if="showTracksModal">
        <Modal @close="toggleAddTracks">
          <h2>Add Tracks</h2>
          <p>A place to store your tracks</p>
          <AddSongs @submit="refreshSongs"></AddSongs>
        </Modal>
    </div>
  </div>
</template>


<script setup>
  import { ref, onMounted, useAttrs } from 'vue'
  import { fetchSongs, removeSong} from '@/api.js'
  import Modal from './Modal.vue'
  import AddSongs from './AddSongs.vue'
  import { useAuthStore } from '@/stores/auth'



  const emit = defineEmits(['song-selected'])
  const authStore = useAuthStore()

  const songs = ref([])
  const songSelect = ref(null)
  const displayInfo = ref(false)
  const showTracksModal = ref(false)
  const token = authStore.token

  function showSongInfo(song){
    emit('song-selected', song)
    if(song === songSelect.value){
        displayInfo.value = !displayInfo.value;
        if(!displayInfo.value){
            songSelect.value = null;
        }
    } else{
        songSelect.value = song;
        displayInfo.value = true;
    }
  }

  function toggleAddTracks(){
    showTracksModal.value = !showTracksModal.value;
    if (showTracksModal.value === False){
      refreshSongs()
    }
  }

  async function refreshSongs(){
    songs.value = await fetchSongs()
  }

  async function deleteSong(){
    await removeSong(songSelect.value.id, token)    
    refreshSongs()
    showSongInfo(null)
  }

  onMounted(async () =>{
    songs.value = await fetchSongs()
  })
</script>



<style>
.controls{
  text-align: center;
  font-weight: 1000;
  user-select: none;
}

</style>