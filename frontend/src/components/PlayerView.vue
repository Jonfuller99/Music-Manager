<template>
  <div class="">
    <div class="audio-player" :class="{ 'dark-mode': isDark }">
      <!-- Hidden native element for functionality -->
      <audio 
        ref="audioPlayer" 
        @timeupdate="updateProgress"
        @loadedmetadata="updateDuration"
      >
        <source :src="audioSrc" type="audio/mpeg">
      </audio>

      <!-- Custom controls -->
      <div class="player-controls">
        <button class="control-btn play-pause" @click="togglePlay">
          <svg v-if="!isPlaying" width="24" height="24" viewBox="0 0 24 24">
            <path fill="currentColor" d="M8 5v14l11-7z"/>
          </svg>
          <svg v-else width="24" height="24" viewBox="0 0 24 24">
            <path fill="currentColor" d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
          </svg>
        </button>

        <div class="progress-container">
          <div class="time-display">{{ formatTime(currentTime) }}</div>
          <div class="waveform" ref="waveform" @click="seekAudio">
            <canvas ref="waveformCanvas"></canvas>
            <div class="progress-bar" :style="{ width: progressPercentage + '%' }"></div>
          </div>
          <div class="time-display">{{ formatTime(duration) }}</div>
        </div>

        <div class="secondary-controls">
          <!-- Volume Control -->
          <div class="volume-control">
            <button class="control-btn" @click="toggleMute" title="Volume">
              <svg width="20" height="20" viewBox="0 0 24 24">
                <path fill="currentColor" v-if="isMuted" d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/>
                <path fill="currentColor" v-else-if="volume < 0.5" d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02z"/>
                <path fill="currentColor" v-else d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
              </svg>
            </button>
            <input 
              type="range" 
              class="volume-slider" 
              min="0" 
              max="1" 
              step="0.01" 
              v-model="volume" 
              @input="setVolume"
            >
          </div>

          <!-- Speed Control -->
          <div class="speed-control">
            <button class="control-btn speed-btn" @click="showSpeedOptions = !showSpeedOptions" title="Playback Speed">
              <svg width="20" height="20" viewBox="0 0 24 24">
                <path fill="currentColor" d="M13.5 5.5c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zM9.8 8.9L7 23h2.1l1.8-8 2.1 2v6h2v-7.5l-2.1-2 .6-3C14.8 12 16.8 13 19 13v-2c-1.9 0-3.5-1-4.3-2.4l-1-1.6c-.4-.6-1-1-1.7-1-.3 0-.5.1-.8.1L6 8.3V13h2V9.6l1.8-.7"/>
              </svg>
              <span class="speed-label">{{ playbackRate }}x</span>
            </button>
            <div class="speed-options" v-if="showSpeedOptions">
              <button @click="setSpeed(0.5)" :class="{ active: playbackRate === 0.5 }">0.5x</button>
              <button @click="setSpeed(1)" :class="{ active: playbackRate === 1 }">1x</button>
              <button @click="setSpeed(1.5)" :class="{ active: playbackRate === 1.5 }">1.5x</button>
              <button @click="setSpeed(2)" :class="{ active: playbackRate === 2 }">2x</button>
            </div>
          </div>

          <!-- Download Button -->
          <a class="control-btn download-btn" :href="audioSrc" download title="Download">
            <svg width="20" height="20" viewBox="0 0 24 24">
              <path fill="currentColor" d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/>
            </svg>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    audioSrc: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      isPlaying: false,
      isMuted: false,
      currentTime: 0,
      duration: 0,
      volume: 0.7,
      playbackRate: 1,
      showSpeedOptions: false,
      isDark: window.matchMedia('(prefers-color-scheme: dark)').matches
    }
  },
  computed: {
    progressPercentage() {
      return (this.currentTime / this.duration) * 100 || 0;
    }
  },
  mounted() {
    this.drawWaveform();
    this.setVolume(); // Initialize volume
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
      this.isDark = e.matches;
    });
  },
  methods: {
    togglePlay() {
      if (this.isPlaying) {
        this.$refs.audioPlayer.pause();
      } else {
        this.$refs.audioPlayer.play();
      }
      this.isPlaying = !this.isPlaying;
    },
    toggleMute() {
      this.$refs.audioPlayer.muted = !this.isMuted;
      this.isMuted = !this.isMuted;
    },
    setVolume() {
      this.$refs.audioPlayer.volume = this.volume;
      this.isMuted = this.volume === 0;
    },
    setSpeed(rate) {
      this.playbackRate = rate;
      this.$refs.audioPlayer.playbackRate = rate;
      this.showSpeedOptions = false;
    },
    updateProgress() {
      this.currentTime = this.$refs.audioPlayer.currentTime;
    },
    updateDuration() {
      this.duration = this.$refs.audioPlayer.duration;
    },
    seekAudio(e) {
      const rect = this.$refs.waveform.getBoundingClientRect();
      const seekPercentage = (e.clientX - rect.left) / rect.width;
      this.$refs.audioPlayer.currentTime = this.duration * seekPercentage;
    },
    formatTime(seconds) {
      if (isNaN(seconds)) return '0:00';
      const minutes = Math.floor(seconds / 60);
      const secs = Math.floor(seconds % 60);
      return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
    },
    drawWaveform() {
      // In a real app, you would analyze the audio file to generate the waveform
      // This is a simplified visualization for demo purposes
      const canvas = this.$refs.waveformCanvas;
      if (!canvas) return;
      
      const ctx = canvas.getContext('2d');
      const width = 1000;
      const height = 40;
      
      canvas.width = width;
      canvas.height = height;
      
      ctx.fillStyle = this.isDark ? 'rgba(255,255,255,0.2)' : 'rgba(0,0,0,0.1)';
      
      // Draw random waveform for demo
      for (let i = 0; i < width; i += 3) {
        const randomHeight = Math.random() * height;
        ctx.fillRect(i, height/2 - randomHeight/2, 2, randomHeight);
      }
    }
  }
}
</script>

<style scoped>
.audio-player-container {
  margin: 2rem 0;
  width: 100%;
}

.audio-player {
  --audio-primary: hsla(160, 100%, 37%, 1);
  --audio-bg: var(--color-background-soft);
  --audio-text: var(--color-text);
  --audio-border: var(--color-border);
  --audio-controls-bg: var(--color-background);
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}

.dark-mode {
  --audio-bg: var(--color-background-mute);
  --audio-border: var(--color-border-hover);
}

.player-controls {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  box-sizing: border-box;
}

.control-btn {
  background: var(--audio-controls-bg);
  border: 1px solid var(--audio-border);
  border-radius: 8px;
  min-width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--audio-text);
  transition: all 0.3s ease;
  text-decoration: none;
  padding: 8px;
  box-sizing: border-box;
}

.control-btn:hover {
  background: var(--audio-primary);
  color: white;
  transform: scale(1.05);
  border-color: var(--audio-primary);
}

.play-pause {
  background: var(--audio-primary);
  color: white;
  border-color: var(--audio-primary);
  border-radius: 50%;
  min-width: 48px;
  height: 48px;
}

.play-pause:hover {
  transform: scale(1.1);
}

.progress-container {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0; /* Allow shrinking */
}

.time-display {
  font-size: 0.8rem;
  color: var(--audio-text);
  min-width: 40px;
  text-align: center;
  flex-shrink: 0;
}

.waveform {
  flex: 1;
  height: 40px;
  border-radius: 4px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  min-width: 100px;
}

.waveform canvas {
  width: 100%;
  height: 100%;
}

.progress-bar {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  background: var(--audio-primary);
  opacity: 0.3;
  pointer-events: none;
  transition: width 0.1s ease;
}

.secondary-controls {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

/* Volume Control */
.volume-control {
  position: relative;
  display: flex;
  align-items: center;
}

/* Extended hover area for volume control */
.volume-control::before {
  content: '';
  position: absolute;
  top: -40px;
  left: -5px;
  right: -5px;
  bottom: 0;
  z-index: 1;
}

.volume-slider {
  position: absolute;
  top: -40px;
  left: 50%;
  transform: translateX(-50%) rotate(-90deg);
  transform-origin: center;
  width: 60px;
  height: 4px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
  background: var(--audio-border);
  outline: none;
  cursor: pointer;
  z-index: 2;
}

.volume-slider::-webkit-slider-thumb {
  appearance: none;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--audio-primary);
  cursor: pointer;
}

.volume-slider::-moz-range-thumb {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--audio-primary);
  cursor: pointer;
  border: none;
}

.volume-control:hover .volume-slider,
.volume-slider:hover {
  opacity: 1;
  pointer-events: all;
  transition-delay: 0s;
}

.volume-slider {
  transition-delay: 0.5s;
}

/* Speed Control */
.speed-control {
  position: relative;
}

.speed-btn {
  gap: 4px;
  min-width: auto;
  padding: 8px 12px;
}

.speed-label {
  font-size: 0.75rem;
  font-weight: 500;
}

.speed-options {
  position: absolute;
  top: -140px;
  right: 0;
  background: var(--audio-controls-bg);
  border: 1px solid var(--audio-border);
  border-radius: 8px;
  padding: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
  gap: 4px;
  z-index: 100;
  min-width: 60px;
}

.speed-options button {
  background: none;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  color: var(--audio-text);
  font-size: 0.85rem;
  transition: all 0.2s ease;
}

.speed-options button:hover,
.speed-options button.active {
  background: var(--audio-primary);
  color: white;
}

.download-btn {
  text-decoration: none;
}

/* Responsive Design */
@media (max-width: 768px) {
  .player-controls {
    gap: 8px;
  }
  
  .control-btn {
    min-width: 36px;
    height: 36px;
    padding: 6px;
  }
  
  .play-pause {
    min-width: 44px;
    height: 44px;
  }
  
  .speed-btn {
    padding: 6px 8px;
  }
  
  .speed-label {
    display: none;
  }
  
  .time-display {
    font-size: 0.75rem;
    min-width: 35px;
  }
}

@media (max-width: 600px) {
  .player-controls {
    flex-wrap: wrap;
    gap: 8px;
  }
  
  .progress-container {
    order: 3;
    flex: 0 0 100%;
    margin-top: 8px;
  }
  
  .secondary-controls {
    order: 2;
  }
  
  .volume-slider {
    top: -40px;
    width: 60px;
  }
  
  .speed-options {
    top: -120px;
    right: -10px;
  }
}

@media (max-width: 400px) {
  .secondary-controls {
    gap: 4px;
  }
  
  .control-btn {
    min-width: 32px;
    height: 32px;
  }
  
  .play-pause {
    min-width: 40px;
    height: 40px;
  }
}
</style>