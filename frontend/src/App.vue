<template>
  <div class="container-v ">
    <div class="main-nav" v-if="auth.isLoggedIn">
      <div class="nav-left">
        <router-link to="/home" class="nav-main-pos nav-link">Home</router-link>
        <router-link to="/songs" class="nav-main-pos nav-link">Songs</router-link>
      </div>
      <router-link to="/profile" class="profile nav-link ">Profile</router-link>
    </div>
    <div class="content-wrapper">
      <router-view/>
    </div>
  </div>
</template>


<script setup>
import { useAuthStore } from './stores/auth';
  const auth = useAuthStore()
</script>


<style scoped>

.main-nav {
  display: flex;
  justify-content: space-between;
  align-items: center; 
  width: 100%;
  gap: 1.5rem;
  padding: 1rem 2rem;
  background-color: var(--color-background);
  border-bottom: 1px solid var(--color-border);
  z-index: 100;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);

}
.nav-left {
  display: flex;
  gap: 1.5rem; 
}

.profile{
  margin-left: auto;
  text-decoration: none;
  color: var(--color-text);
  font-weight: 500;
  font-size: 0.95rem;
  margin-right: 2rem;
  transition: all 0.4s ease;
}

.content-wrapper {
  flex: 1;
}

/* Router Links */
.nav-main-pos{
  position: relative;
}

.nav-link {
  text-decoration: none;
  color: var(--color-text);
  font-weight: 500;
  font-size: 0.95rem;
  padding: 0.5rem 0;
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
