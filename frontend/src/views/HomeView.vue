<template>
  <main>
    <!-- <div>
      <div class="divcol" v-if="showButtons">
        <h1>{{ title }}</h1>
        <button i @click="toggleAddTracks" class="btn">Add Tracks</button>
        <button @click="toggleViewSamples" class="btn">View Samples</button>
      </div>
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
    </div> -->

    <div class="container-h panel">
      <div class="container temp" >
        <div class="box-1 panel fancy-panel">

        </div>
        <div class="panel fancy-panel temp">

        </div>
      </div>
      <div class="container temp"> 
        <div class="panel fancy-panel temp">
          
        </div>
        <div class="box-1 panel fancy-panel">

        </div>
      </div>

    </div>

      



  </main>
</template>

<script>
import AddSongs from '@/components/AddSongs.vue'
import Modal from '@/components/Modal.vue'
import ViewSongs from '@/components/ViewSongs.vue'

  export default{
    
    name:'Home',
    components: {Modal, AddSongs, ViewSongs },
    data(){
      return {
        title: 'Music Manager',
        showTracksModal: false,
        showSampleModal: false,
        showButtons: true,
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
        this.showButtons = !this.showButtons;

      },
      toggleViewSamples(){
        this.showSampleModal = !this.showSampleModal;
        this.showTracksModal = false;
        this.showButtons = !this.showButtons;


      },
    }
  }
</script>


<style>
.box-1{
  width: 600px;
  height: 550px;
}



</style>
