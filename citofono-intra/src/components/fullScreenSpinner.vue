<template>
  <div class="overlay" style="animation: none; transform: none;">
    <div class="spinner-element"></div>
  </div>
</template>

<script>
export default {
  name: 'SafeSpinner'
}
</script>

<style scoped>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(128, 128, 128, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10000;
}

.spinner-element {
  width: 48px;
  height: 48px;
  border: 4px solid #e0e0e0;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  animation: rotate 1s linear infinite;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>