<template>
  <div class="about">

    <div @click="changeMessage">
      <h1>{{message}}</h1>
    </div>
    <h1> {{age}}</h1>
    <button @click="age++">Increase age</button>

    <div>
      <ul>
        <li v-for="item in items">
          <img :src="item.img" :alt="item.game">
          <h3>{{ item.game }} - {{ item.year }}</h3>
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

  const message = ref('Loading...')
  const age = ref('Loading...')
  const items = ref('Loading...')
  const url = ref('Loading...')



  onMounted(async () => {
    const response = await fetch('http://localhost:8000/')
    const data = await response.json()
    message.value = data.message
    age.value = data.age
    items.value = data.items
    url.value = data.url
  })

  
</script>