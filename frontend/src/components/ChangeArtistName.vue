<template>
        <div class="container-v button padding">
            <input id="url"  ref="urlInput" class="input padding" type="text" placeholder="New Artist Name">
            <button class="button panel btn">Change</button> 
        </div>

</template>


<script>
</script>

<style>
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

.button{
    text-align: center;
    width: 200px;
    align-items: center;
    justify-content: center;
    font-size: medium;
    user-select: none;
    gap: .5rem;
}
</style>