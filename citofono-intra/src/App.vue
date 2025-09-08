<script setup>
import { ref, provide } from 'vue';
import headerComponent from './components/headerComponent.vue';
import footerComponent from './components/footerComponent.vue';

const isAuthenticated = ref(false);

provide('isAuthenticated', isAuthenticated);


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
