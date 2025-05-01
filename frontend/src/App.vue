

<template>
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
  
</template>


<script>
import Modal from './components/Modal.vue'
export default{
  name: 'App',
  components: {Modal},
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
    },
    toggleViewSamples(){
      this.showSampleModal = !this.showSampleModal;
    },
  }

  
}
</script>


<style scoped>
h1 { 
  border-bottom: 1px solid #ddd;
  display: inline-block;
  padding-bottom: 10px;
  margin: 10px;
}
.divcol {
  display: flex;
  flex-direction: column;
  margin: auto;
  padding: 10px;
}
div{
  margin: 10px;
}
</style>
