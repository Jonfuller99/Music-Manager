<template>
    <div class="container-v">
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
          <YourSongs></YourSongs>
          
        </div>
        <div class="box-1 panel fancy-panel">

        </div>
      </div>
    </div>
</template>
<script setup>
import { ref } from 'vue'
import Account from '@/components/Account.vue'
import LinkToMP3 from '@/components/LinkToMP3.vue'

import AddSongs from '@/components/AddSongs.vue'
import Modal from '@/components/Modal.vue'
import ViewSongs from '@/components/ViewSongs.vue'
import YourSongs from '@/components/YourSongs.vue'


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
