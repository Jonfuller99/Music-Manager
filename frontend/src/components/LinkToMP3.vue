<template>
    <div class="container-v container-fill">
        <div class="title padding">
            Link to MP3
        </div>
        <div class="container padding">
            <input id="url" v-model="url" ref="urlInput" class="input padding" type="text" placeholder="Paste link here">
        </div>
        <div class="container title padding">
            
            <div class="panel button btn" v-on:click="downloadMp3">Download <font-awesome-icon icon="download"/> </div>
            <div class="panel button btn-add convert" v-on:click="handleConvert">Convert <font-awesome-icon icon="rotate-right" /></div>
            <div class="panel button btn" v-on:click="handleNext">Next <font-awesome-icon icon="arrow-right"/></div>
        </div>
        <div class="temp">
            <div class="table-container">
                <table class="styled-table">
                <thead>
                    <tr>
                    <th class="table-header">Title</th>
                    <th class="table-header">Link</th>
                    </tr>
                </thead>
                <tbody>                    
                    <tr v-for="item in history" :key="item.title" class="table-row">
                        <td class="table-data url-cell">
                            <span class="url-text">{{ item.title}}</span>
                        </td>
                        <td class="table-data">
                            <a  
                            :href="item.url" 
                            target="_blank" 
                            class="table-link"
                            >
                            Download Link
                            <span class="link-icon">↗</span>
                            </a>
                        </td>
                    </tr>
                    <tr v-if="history.length === 0" class="table-row">
                        <td class="table-data url-cell">
                            <span class="url-text">Download History</span>
                        </td>
                        <td class="table-data">

                            Download Link
                            <span class="link-icon">↗</span>
                            
                        </td>
                    </tr>

                </tbody>
                </table>

            </div>
 
        </div>

    </div>

</template>

<script setup>
import { ref, nextTick } from 'vue';
import { convertToMp3 } from '@/api';

const url = ref('')
const mp3Data = ref(null)
const history = ref([])
const urlInput = ref(null)



async function handleConvert(){
    if(url.value.includes('&list=')){  
        const index = url.value.indexOf('&')
        if (index !== -1){  
            url.value = url.value.substring(0, index)  
        }
    }
    mp3Data.value = await convertToMp3(url.value)
    history.value.push({
        title: mp3Data.value.title,
        url: mp3Data.value.audio_url
    })
}

function downloadMp3(){
    if (mp3Data.value?.audio_url) {
        const link = document.createElement('a');
        link.href = mp3Data.value.audio_url;
        link.download = `${mp3Data.value.title || 'audio'}.mp3`; 
        link.click(); 
    }
}

async function handleNext(){
    url.value = ''
    await nextTick() 
    urlInput.value.focus()
    urlInput.value.select()
}


</script>

<style scoped>
.button{
    text-align: center;
    width: 200px;
    align-items: center;
    justify-content: center;
    font-size: medium;
    user-select: none;
    gap: .5rem;
}
.convert{
    font-size: large;
    font-weight: bold;
    background-color: var(login-form-input);
    user-select: none;

}
.green{
    color: var(login-form-input);
    font-style: italic;
}


.padding{
    padding-bottom: 10px;
}


.input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid var(--color-border);
  border-radius: 6px;
  background-color: var(--color-background);
  color: var(--color-text);
  font-family: inherit;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.input::placeholder {
  color: grey ;
  opacity: 0.7;
}

.input:focus {
  outline: none;
  border-color: hsla(160, 100%, 37%, 0.4);
  box-shadow: 
    0 0 0 2px hsla(160, 100%, 37%, 0.1),
    inset 0 1px 2px rgba(0, 0, 0, 0.05);
  background-color: var(--color-background);
}

.input:hover {
  border-color: var(--color-border-hover);
}


.table-container {
  border-radius: 12px;
  overflow-y:auto;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  max-height: 300px;

}

.styled-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--color-background-soft);
}

.table-header {
  background: linear-gradient(145deg, #2d2d2d, #1a1a1a);
  color: white;
  padding: 1rem 1.5rem;
  text-align: left;
  font-weight: 600;
  font-size: 0.95rem;
  border-bottom: 1px solid var(--color-border);
}

.table-row {
  transition: background-color 0.3s ease;
}

.table-row:hover {
  background-color: hsla(0, 0%, 32%, 0.197);
}

.table-data {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid var(--color-border);
  font-size: 0.9rem;
}

.url-cell {
  max-width: 0;
  width: 70%;
}

.url-text {
  display: inline-block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
  color: var(--color-text);
}

.table-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: hsla(160, 100%, 37%, 1);
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  padding: 0.3rem 0.6rem;
  border-radius: 4px;
}

.table-link:hover {
  background-color: hsla(160, 100%, 37%, 0.1);
  transform: translateY(-1px);
}

.link-icon {
  font-size: 0.85em;
}

.table-muted {
  color: var(--color-text-soft);
  font-style: italic;
}

.table-container::-webkit-scrollbar {
  width: 8px;
}

.table-container::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 10px;
}

.table-container::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 10px;
}

.table-container::-webkit-scrollbar-thumb:hover {
  background: #555;
}

/* Dark mode adjustments */
@media (prefers-color-scheme: dark) {
  .styled-table {
    background: var(--color-background-mute);
  }
  
  .table-header {
    background: linear-gradient(145deg, #1a1a1a, #111);
  }
  
  .url-text {
    color: var(--color-text-dark-1);
  }
}
</style>