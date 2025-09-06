<script setup>
import { ref, watchEffect, provide } from 'vue';
import Cookies from 'js-cookie';
import { useRouter } from 'vue-router';
import headerComponent from '../components/headerComponent.vue';
import footerComponent from '../components/footerComponent.vue';

const router = useRouter();

// 1. Centraliza el estado reactivo aquí
const isAuthenticated = ref(false);

// 2. Provee el estado y las acciones a los componentes hijos
provide('isAuthenticated', isAuthenticated);

// Aquí puedes añadir la lógica para redirigir si la cookie no existe,
// aunque la redirección principal para cerrar sesión se gestiona en el Header.
watchEffect(() => {
  const userCookie = Cookies.get('usuario');
  isAuthenticated.value = !!userCookie;
  if (!isAuthenticated.value && router.currentRoute.value.path !== '/login') {
    router.push('/login');
  }
});
</script>

<template>
  <headerComponent/>
  <div>
    <router-view />
  </div>
  <footerComponent/>
</template>

<style scoped>

</style>
