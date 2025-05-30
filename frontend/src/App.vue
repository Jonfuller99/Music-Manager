<template>
  <div class="divcol">
    <div class="main-nav">
      <router-link to="/" class="nav-link">Home</router-link>
      <router-link to="/songs" class="nav-link">Songs</router-link>
    </div>
    <div class="content-wrapper">
      <router-view/>
    </div>
  </div> 
</template>


<script>
  export default{
    name: 'App',
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

.main-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  gap: 1.5rem;
  padding: 1rem 2rem;
  background-color: var(--color-background);
  border-bottom: 1px solid var(--color-border);
  z-index: 100;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.content-wrapper {
  margin-top: 60px; 
  padding: 20px;
  flex: 1;
}

/* Router Links */
.nav-link {
  text-decoration: none;
  color: var(--color-text);
  font-weight: 500;
  font-size: 0.95rem;
  padding: 0.5rem 0;
  position: relative;
  transition: all 0.4s ease;
}

.nav-link:hover {
  color: hsla(160, 100%, 37%, 1);
}

/* Active route indicator */
.nav-link.router-link-exact-active {
  color: hsla(160, 100%, 37%, 1);
}

.nav-link.router-link-exact-active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: hsla(160, 100%, 37%, 1);
  transform: scaleX(1);
  transition: transform 0.4s ease;
}

/* Modal Links */
.modal-links {
  display: flex;
  gap: 1.5rem;
  margin: 1rem 0;
}

.modal-links a {
  color: hsla(160, 100%, 37%, 1);
  text-decoration: none;
  font-size: 0.9rem;
  transition: all 0.4s ease;
}

.modal-links a:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

/* Dark mode adjustments */
@media (prefers-color-scheme: dark) {
  .nav-link {
    color: var(--vt-c-text-dark-2);
  }
  
  .nav-link:hover,
  .nav-link.router-link-exact-active {
    color: hsla(160, 100%, 37%, 1);
  }
}
</style>
