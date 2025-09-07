<template>
  <footer class="footer">
    <div class="footer-content">
      <p>&copy; 2025 INTRO.</p>
      <div class="contact-info">
        <p>Contacto: info@micompania.com</p>
        <p>Teléfono: +123 456 7890</p>
        <p>Dirección: Calle Falsa 123, Ciudad, País</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
// No se necesita lógica en el script para este footer simple.
</script>

<style scoped>
.footer {
  background-color: #f44336; /* Color rojo */
  color: white;
  padding: 20px;
  text-align: center;
  /* Posicionamiento para que el footer se quede en la parte inferior de la página */
  width: 100%;
  box-sizing: border-box; /* Asegura que el padding no añada ancho extra */
}

.footer-content {
  max-width: 960px;
  margin: 0 auto;
}

.contact-info {
  margin-top: 10px;
}

.contact-info p {
  margin: 5px 0;
}
</style>
