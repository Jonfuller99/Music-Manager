<template>
    <div class="container-v container-fill">
        <div class="title">
            Songs You Apeared On:
        </div>
        <div class="song-list-container">
            <div class="song-list">
                <div v-for="song in paginatedSongs">
                    <span class="song item item__title" @click="showSongInfo(song)">{{ song.title }} </span>    
                </div>
            </div>
        </div>
        <div class="container center">
            <button :disabled="currentPage === 1" @click="previousPage" class="btn-add btn "><</button>
            <button :disabled="currentPage === totalPages" @click="nextPage" class="btn-add btn">></button>
            <span class="pagination center">Page {{ currentPage }} of {{ totalPages }}</span>
        </div>
    </div>


</template>



<script setup>
    import { ref, onMounted, computed } from 'vue';
    import { fetchSongs } from '@/api';

    const songs = ref([])
    const songsPerPage = 12
    const currentPage = ref(1)


    const paginatedSongs = computed(() =>{
        const start = (currentPage.value - 1) * songsPerPage;
        const end = start + songsPerPage;
        return songs.value.slice(start, end);
    })

    const totalPages = computed(() => {
        return Math.ceil(songs.value.length / songsPerPage);
    });

    const nextPage = ()=>{
        if(currentPage.value < totalPages.value){
            currentPage.value++;
        }
    };

    const previousPage = ()=>{
        if(currentPage.value > 1 ){
            currentPage.value--;
        }
    };


    onMounted(async () =>{
        songs.value = await fetchSongs()
    })


</script>

<style scoped>

.pagination{
    flex: 1;
    text-align: right;
    margin: 10px;

}
.center{
    justify-content: center;
    align-items: center;
}

.width-100{
    width: 90px;
}


.song-list-container {
    padding: 30px;
    max-height: 60vh;
    width: 100%;
    height: 100%;
}

.song-list {
    column-count: 3;
    margin: 10px;
    column-gap: 3rem;
    overflow-y: auto; /* Vertical scroll when content overflows */
    break-inside: avoid;
}

.song {
  display: inline-block; 
  cursor: pointer;
  transition: all 0.3s ease;
  break-inside: avoid-column; 
  width: 100%;
}

.song:hover {
  background: var(--color-background-mute);
  border-color: var(--color-border-hover);
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .song-list {
    column-count: 2;
  }
}

@media (max-width: 480px) {
  .song-list {
    column-count: 1;
  }
}

</style>


