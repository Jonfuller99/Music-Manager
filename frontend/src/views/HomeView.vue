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

    <div class="container-v panel">
      <div class="container temp" >
        <div class="box-1 panel fancy-panel">
          <Account></Account>

        </div>
        <div class="panel fancy-panel temp">
          <LinkToMP3></LinkToMP3>

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
<script setup>
import { ref } from 'vue'
import Account from '@/components/Profile/Account.vue'
import LinkToMP3 from '@/components/LinkToMP3.vue'
import AddSongs from '@/components/AddSongs.vue'
import Modal from '@/components/Modal.vue'
import ViewSongs from '@/components/ViewSongs.vue'

const title = 'Music Manager'

const showTracksModal = ref(false)
const showSampleModal = ref(false)
const showButtons = ref(true)

const nameRef = ref(null)

function handleClick() {
  console.log(nameRef.value)
  nameRef.value?.classList.add('active')
  nameRef.value?.focus()
}

function toggleAddTracks() {
  showTracksModal.value = !showTracksModal.value
  showSampleModal.value = false
  showButtons.value = !showButtons.value
}

function toggleViewSamples() {
  showSampleModal.value = !showSampleModal.value
  showTracksModal.value = false
  showButtons.value = !showButtons.value
}
</script>



<style>
.box-1{
  width: 600px;
  height: 550px;
}



</style>
