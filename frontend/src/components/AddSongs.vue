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
        <div class="btn-group">
          <button type="submit" class="btn btn-add">Add</button>
        </div>
      </div>
    </form>
  </template>
  
  <script>
  import { postSong } from "@/api.js";
  export default {
    data(){
        return{
            title: '',
            artist: '',
            genre: '',
        }
    },
    methods:{
      async submitSong(event){
        event.preventDefault();
        try{
          const newSong = {
            title: this.title,
            artist: this.artist,
            genre: this.genre,
            bpm: 120,
            file_path: 'temp/file/path.mp3'
          }
          const result = await postSong(newSong);
          console.log("Song added successfully", result)

          this.title = '';
          this.artist = '';
          this.genre = '';
        
        } catch (error){
          console.error("Failed to add song:", error)
        }
      }
    }
  }
  </script>
  
  <style scoped>
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
  </style>