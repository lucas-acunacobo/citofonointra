<template>
  <header>
    <h1>INTRO</h1>
    <div class="menu" v-if="isAuthenticated">
      <router-link to="/" class="menu-button">
        Grabar Video
      </router-link>
      <router-link to="/videos" class="menu-button">
        Videos
      </router-link>
    </div>
    <div class="header-actions">

      <button v-if="isAuthenticated" @click="handleAuthAction('logout')" class="auth-button">
        Logout
      </button>
    </div>
  </header>
</template>

<script setup>
import { inject } from 'vue';
import Cookies from 'js-cookie';
import { useRouter } from 'vue-router';

const router = useRouter();

const isAuthenticated = inject('isAuthenticated');

const handleAuthAction = (action) => {
  if (action === 'logout') {
    Cookies.remove('usuario');
    isAuthenticated.value = false;
    router.push("/login");
    alert('Has cerrado sesión.');
  }
};
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background-color: #f44336; 
  color: white;
  border-bottom: 2px solid #d32f2f;
}

h1 {
  margin: 0;
  font-size: 1.5em;
}

.header-actions {
  display: flex;
  gap: 15px;
}

.auth-button {
  background-color: transparent;
  color: white;
  border: 2px solid white;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 1em;
  font-weight: bold;
  border-radius: 5px;
  transition: background-color 0.3s, color 0.3s;
}

.auth-button:hover {
  background-color: white;
  color: #f44336;
}

.menu-button {
  background-color: transparent;
  color: white;
  border: 2px solid white;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 1em;
  font-weight: bold;
  border-radius: 5px;
  transition: background-color 0.3s, color 0.3s;
}

.menu-button:hover {
  background-color: white;
  color: #f44336;
}

.menu {
  display: flex;
  gap: 15px;
}
</style>