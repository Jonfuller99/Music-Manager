<template>
    <div class="container-v">
        <div class="temp title">
            Link to MP3
        </div>
        <div class="container temp">
            <input class="input" type="text">
        </div>
        <div class="container title">
            <div class="panel temp">

            </div>
            <div class="panel temp">

            </div>
        </div>

    </div>

</template>

<script setup>
</script>

<style scoped>
.title{
    text-align: center;
    justify-content: center;
    font-size: 25px;
    color: white;
    font-weight: bold;
    font-weight: bold;
    font-weight: bold;
}
.input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid var(--color-border);
  border-radius: 6px;
  background-color: var(--color-background-soft);
  color: var(--color-text);
  font-family: inherit;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.input::placeholder {
  color: var(--color-text-soft);
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
</style>