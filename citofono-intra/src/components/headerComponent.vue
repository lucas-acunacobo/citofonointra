<template>
  <header class="headder">
    <div>
      <h1>INTRO</h1>
    </div>
    <div class="header-actions">
      <div>
        <div class="dropdown" v-if="Cookies.get('usuario')">
          <button class="dropbtn"><img src="../assets/icons8-opciones-64.png"/></button>
          <div class="dropdown-content">
            <router-link to="/">Grabar Video</router-link>
            <router-link to="/videos">Videos</router-link>
            <router-link to="/login" @click="handleAuthAction('logout')">Logout</router-link>
          </div>
        </div>
      </div>
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
.headder {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background-color: #f44336; 
  color: white;
  border-bottom: 2px solid #d32f2f;
}

.header-actions {
  display: flex;
  gap: 15px;
}

.dropdown {
  position: relative;
  display: inline-block;
  margin-right: 20px;
}

.dropbtn {
  background: #8b0000;
  color: white;
  padding: 10px 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  border-radius: 6px;
}

.dropbtn:hover {
  background: #a30000;
}

.dropdown-content {
  display: none;
  position: absolute;
  background: white;
  min-width: 160px;
  box-shadow: 0px 8px 16px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background: #f1f1f1;
}

img{
  width: 30px;
  height: 20px;
}
.dropdown:hover .dropdown-content {
  display: block;
}
</style>