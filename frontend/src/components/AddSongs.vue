<template>
    <form class="auth-form" @submit="submitSong">
      <div class="form-group">
        <label for="title" class="form-label">Title:</label>
        <input 
          id="title" 
          class="form-input" 
          type="text" 
          required
          placeholder="Enter title..."
          v-model="title"
        >
        <label for="Artist" class="form-label">Artist:</label>
        <input 
          id="artist" 
          class="form-input" 
          type="text" 
          required
          placeholder="Enter artist..."
          v-model="artist"
        >

        <label for="Bpm" class="form-label">BPM:</label>
        <input 
          id="bpm" 
          class="form-input" 
          type="number" 
          required
          placeholder="Enter bpm..."
          v-model="bpm"
        >

        <label for="genre" class="form-label">Genre:</label>
        <div class="select-group">
            <select name="genres" id="genres" class="form-select" v-model="genre">
                <option value="" disabled selected>Select a genre...</option>
                <option value="Pop">Pop</option>
                <option value="Hip-Hop">Hip-Hop</option>
                <option value="Trap">Trap</option>
                <option value="RnB">RnB</option>
            </select>
            <span class="select-arrow">▼</span>
        </div>


        <label for="file" class="form-label">File:</label>
        <div class="file-input-container">
          <input type="file" id="file" accept=".mp3,.wav" @change="handleFileChange">
          <label for="file" >{{ fileName || 'No file selected' }}</label>
        </div>

        <div class="btn-group">
          <button type="submit" class="btn btn-add">Add</button>
        </div>
      </div>
    </form>
  </template>
  
  <script>
  import { postSong, uploadFile } from "@/api.js";
  export default {
    data(){
        return{
            title: '',
            artist: '',
            bpm:'',
            genre: '',
            file: '',
            fileName: ''
        }
    },
    methods:{
      async submitSong(event){
        event.preventDefault();
        try{
          const newSong = {
            title: this.title,
            artist: this.artist,
            bpm: this.bpm,
            genre: this.genre,
            file_path: `http://localhost:8000/uploads/${this.fileName}`
          }
  
          const [result, upload] = await Promise.all([
            postSong(newSong),
            uploadFile(this.file)
          ]);
          
          console.log("Song added successfully", result)        
          console.log("File uploaded successfully", upload)


          this.title = '';
          this.artist = '';
          this.bpm = '';
          this.genre = '';
          this.fileName = '';
        
        } catch (error){
          console.error("Failed to add song:", error)
        }
      },
      handleFileChange(event){
        this.fileName = event.target.files[0] ? event.target.files[0].name : '';
        this.file = event.target.files[0];
      }
    }
  }
  </script>
  
  <style>
  .auth-form {
    max-width: 420px;
    margin: 30px auto;
    background: var(--color-background-soft);
    text-align: left;
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid var(--color-border);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    transition: all 0.4s ease;
  }
  
  .form-group {
    margin-bottom: 1.5rem;
  }
  
  .form-label {
    display: block;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--color-heading);
    transition: color 0.4s ease;
    width: 100%;
  }
  
  .form-group:focus-within .form-label {
    color: hsla(160, 100%, 37%, 1);
  }
  
  .form-input {
    width: 100%;
    padding: 0.6rem 1rem;
    border: 1px solid var(--color-border);
    border-radius: 6px;
    background-color: var(--color-background);
    color: var(--color-text);
    font-family: inherit;
    font-size: 0.95rem;
    transition: all 0.4s ease;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  }
  
  .form-input::placeholder {
    color: var(--vt-c-text-light-2);
    opacity: 0.7;
  }
  
  .form-input:focus {
    outline: none;
    border-color: hsla(160, 100%, 37%, 0.4);
    box-shadow: 0 0 0 2px hsla(160, 100%, 37%, 0.1);
    background-color: var(--color-background);
  }
  
  .form-input:hover {
    border-color: var(--color-border-hover);
  }

  .select-group {
  position: relative;
  margin-bottom: 1.5rem;
}

.btn-group{
  text-align: center;
}

.form-select {
  width: 100%;
  padding: 0.6rem 2.5rem 0.6rem 1rem;
  border: 1px solid var(--color-border);
  border-radius: 6px;
  background-color: var(--color-background) !important;
  color: var(--color-text);
  font-family: inherit;
  font-size: 0.95rem;
  transition: all 0.4s ease;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  appearance: none;
  cursor: pointer;
}

/* Focus state */
.form-select:focus {
  outline: none;
  border-color: hsla(160, 100%, 37%, 0.4);
  box-shadow: 0 0 0 2px hsla(160, 100%, 37%, 0.1);
}

/* Hover state */
.form-select:hover {
  border-color: var(--color-border-hover);
}

/* Custom dropdown arrow */
.select-arrow {
  position: absolute;
  top: 50%;
  right: 1rem;
  transform: translateY(-50%);
  pointer-events: none;
  color: var(--color-text);
  font-size: 0.8rem;
  transition: all 0.4s ease;
}

/* Arrow animation on focus */
.form-select:focus ~ .select-arrow {
  color: hsla(160, 100%, 37%, 1);
  transform: translateY(-50%) rotate(180deg);
}

/* Dark mode adjustments */
@media (prefers-color-scheme: dark) {
  .form-select {
    background-color: var(--color-background-mute);
  }
  
  .form-select option {
    background-color: var(--color-background-soft);
  }
}

/* Disabled state */
.form-select:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
  
  @media (prefers-color-scheme: dark) {
    .auth-form {
      background: var(--color-background-mute);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .form-input::placeholder {
      color: var(--vt-c-text-dark-2);
    }
  }

.file-input-container {
  position: relative;
  display: flex;
  flex-direction: column;
}

  input[type="file"] {
  position: absolute;
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  z-index: -1;
}

/* Custom File Input Styling */
input[type="file"] + label {
  width: 100%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  background-color: var(--color-background);
  color: var(--color-text);
  border: 1px solid var(--color-border);
  font-family: inherit;
  font-weight: 500;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  gap: 0.5rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;

}

/* Hover State */
input[type="file"] + label:hover {
  border-color: var(--color-border-hover);
  background-color: hsla(160, 100%, 37%, 0.1);
  color: hsla(160, 100%, 37%, 1);
}

/* Focus State */
input[type="file"]:focus + label {
  outline: 2px solid hsla(160, 100%, 37%, 0.4);
  outline-offset: 2px;
}

/* Active State */
input[type="file"]:active + label {
  transform: translateY(1px);
  background-color: hsla(160, 100%, 37%, 0.2);
}

/* Icon (optional) */
input[type="file"] + label::before {
  content: "📁";
  font-size: 1.1em;
}

</style>