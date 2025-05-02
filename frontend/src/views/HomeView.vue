<template>
  <main>
    <div class="divcol">
    <h1>{{ title }}</h1>
    <div v-if="showTracksModal">
      <Modal theme="" @close="toggleAddTracks">
        <template v-slot:links>
          <a href="#">see artist</a>
          <a href="#">more info</a>
        </template>
        <h2>Add Tracks</h2>
        <p>A place to store your tracks</p>
        <AddSongs></AddSongs>

      </Modal>
    </div>

    <div v-if="showSampleModal">
      <Modal @close="toggleViewSamples">
        <template v-slot:links>
          <a href="#">previous</a>
          <a href="#">next</a>
        </template>
        <h2>Samples</h2>
        <p>A list of your samples</p>
      </Modal>
    </div>
    <button @click="toggleAddTracks" class="btn">Add Tracks</button>
    <button @click="toggleViewSamples" class="btn">View Samples</button>
  </div>
  </main>
</template>

<script>
import AddSongs from '@/components/AddSongs.vue'
import Modal from '@/components/Modal.vue'

  export default{
    
    name:'Home',
    components: {Modal, AddSongs, },
    data(){
      return {
        title: 'Music Manager',
        showTracksModal: false,
        showSampleModal: false,
      }
    },
    methods:{
      handleClick(){
        console.log(this.$refs.name)
        this.$refs.name.classList.add('active')
        this.$refs.name.focus()
      },
      toggleAddTracks(){
        this.showTracksModal = !this.showTracksModal;
        this.showSampleModal = false;

      },
      toggleViewSamples(){
        this.showSampleModal = !this.showSampleModal;
        this.showTracksModal = false;

      },
    }
  }
</script>


<style>
  .divcol {
  display: flex;
  flex-direction: column;
  margin: auto;
  padding: 10px;
}

</style>
