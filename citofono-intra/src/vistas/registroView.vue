<template>
  <fullScreenSpinner v-if="spinner" class="spinner"/>
  <div class="registration-container">
    <div class="registration-form">
      <h2>Registro de Usuario</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="nombre">Nombre</label>
          <input type="text" id="nombre" v-model="form.nombre" required>
        </div>
        <div class="form-group">
          <label for="apellido_paterno">Apellido Paterno</label>
          <input type="text" id="apellido_paterno" v-model="form.apellido_paterno" required>
        </div>
        <div class="form-group">
          <label for="apellido_materno">Apellido Materno</label>
          <input type="text" id="apellido_materno" v-model="form.apellido_materno" required>
        </div>
        <div class="form-group">
          <label for="email">Correo Electrónico</label>
          <input type="email" id="email" v-model="form.email" required>
        </div>
        <div class="form-group">
          <label for="clave">Contraseña</label>
          <input type="password" id="clave" v-model="form.clave" required>
        </div>
        <button type="submit" class="submit-button">Registrar</button>
        <div class="back-button-container">
          <router-link to="/login" class="back-button">
            Volver
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import { registroUsuario } from '../services/users.js'; 
import { useRouter } from 'vue-router';
import fullScreenSpinner from '../components/fullScreenSpinner.vue';

const router = useRouter();
const spinner = ref(false);
const form = reactive({
  nombre: '',
  apellido_paterno: '',
  apellido_materno: '',
  email: '',
  clave: ''
});

const handleSubmit = async () => {
  spinner.value = true;
  const response = await registroUsuario(form);

  if (response.data.ok) {
    alert('¡Registro exitoso!');
    spinner.value = false;
    router.push("/login");
  } else {
    spinner.value = false;
    alert(`Error al registrar! Por favor, intente nuevamente.`);
  }
};
</script>

<style scoped>
.registration-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #fce4ec; 
}

.registration-form {
  background-color: #fff;
  padding: 3rem;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

h2 {
  color: #d32f2f;
  text-align: center;
  margin-bottom: 2rem;
  font-weight: 600;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
  box-sizing: border-box;
}

input:focus {
  border-color: #d32f2f;
  outline: none;
  box-shadow: 0 0 5px rgba(211, 47, 47, 0.5);
}

.submit-button {
  width: 100%;
  padding: 1rem;
  background-color: #d32f2f;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.back-button {
  width: 100%;
  padding: 1rem;
  background-color: transparent;
  color: red;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.back-button-container{
  margin-top: 1rem;
  text-align: center;
  
}
.submit-button:hover {
  background-color: #b71c1c;
}
</style>