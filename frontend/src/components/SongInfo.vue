<template>
  <div class="panel song-info">
    <div class="song-info-header">
      <div class="info-icon">🎵</div>
      <div>
        <h3 class="song-title">{{ song.title }}</h3>
        <p class="info-subtitle">Track Details</p>
      </div>
    </div>
    
    <div class="song-details">
      <div class="detail-row">
        <span class="detail-label">Artists:</span>
        <span class="detail-value">{{ song.artist || 'Unknown' }}</span>
      </div>
      <div class="detail-row">
        <span class="detail-label">BPM:</span>
        <span class="detail-value">{{ song.bpm || 'N/A' }}</span>
      </div>
      <div class="detail-row" v-if="song.file_path">
        <span class="detail-label">File path:</span>
        <span class="detail-value">{{ song.file_path }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
    const props = defineProps({
        song: {
            type: Object,
            required: true,
        }
    })

</script>


<style scoped>
.song-info {
  background: linear-gradient(145deg, #2d2d2d, #1a1a1a);
  border: 1px solid #404040;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 
    0 4px 16px rgba(0, 0, 0, 0.4),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
  max-width: 350px;
}

.song-info-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid #333;
}

.info-icon {
  font-size: 1.5em;
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #4a90e2, #357abd);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.song-title {
  margin: 0;
  font-size: 1.1em;
  font-weight: 600;
  color: #fff;
}

.info-subtitle {
  margin: 0;
  font-size: 0.8em;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.song-details {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 6px 0;
}

.detail-label {
  font-weight: 500;
  color: #bbb;
  font-size: 0.9em;
}

.detail-value {
  color: #fff;
  font-size: 0.9em;
  text-align: right;
  flex: 1;
  margin-left: 12px;
}
</style>

