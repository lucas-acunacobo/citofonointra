<template>
  <div class="container">
    <main class="login-box">
      <h1 class="title">Iniciar Sesión</h1>
      <form @submit.prevent="onSubmit" novalidate>
        <input 
          v-model="email"
          type="email" 
          placeholder="Correo electrónico" 
          required 
          class="input-field"
        />
        <input 
          v-model="password"
          type="password" 
          placeholder="Contraseña" 
          required 
          class="input-field"
        />
        <button type="submit" class="btn-submit">Entrar</button>
      </form>
      <p class="register-text">
        ¿No tienes cuenta? <a href="#" class="register-link">Regístrate</a>
      </p>
    </main>
  </div>
</template>

<script>
import { ref } from 'vue';
import { login } from '../services/users'; 

export default {
  setup() {
    const email = ref('');
    const password = ref('');

    const onSubmit = async() => {
      console.log('Email:', email.value);
      console.log('Password:', password.value);
      const response = await login(email.value, password.value);
      console.log('Response:', response);
    };

    return { email, password, onSubmit };
  },
};
</script>

<style scoped>
/* Centrado horizontal y vertical con Flexbox */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh; /* Altura pantalla completa */
  background-color: #f9fafb; /* gris muy claro */
  padding: 1rem;
  box-sizing: border-box;
}

/* Caja principal del login */
.login-box {
  background-color: #ffffff; /* blanco */
  padding: 2rem;
  border: 2px solid #dc2626; /* rojo */
  border-radius: 0.5rem; /* borde redondeado */
  box-shadow: 0 8px 15px rgba(220, 38, 38, 0.4); /* sombra en rojo */
  width: 100%;
  max-width: 350px;
  box-sizing: border-box;
  text-align: center;
}

/* Título */
.title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #dc2626; /* rojo */
  margin-bottom: 1.5rem;
}

/* Formulario: disposición en columna con espacio */
form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

/* Inputs */
.input-field {
  padding: 0.75rem 1rem;
  border: 1px solid #d1d5db; /* gris claro */
  border-radius: 0.375rem; /* rounded-md */
  font-size: 1rem;
  transition: border-color 0.3s, box-shadow 0.3s;
  outline-offset: 2px;
}

.input-field:focus {
  border-color: #dc2626; /* rojo */
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.4);
  outline: none;
}

/* Botón */
.btn-submit {
  background-color: #dc2626; /* rojo */
  color: white;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  font-weight: 600;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-submit:hover {
  background-color: #b91c1c; /* rojo oscuro */
}

/* Texto de registro */
.register-text {
  margin-top: 1rem;
  color: #6b7280; /* gris medio */
  font-size: 0.875rem;
}

.register-link {
  color: #dc2626;
  text-decoration: none;
  font-weight: 500;
  transition: text-decoration 0.3s;
}

.register-link:hover {
  text-decoration: underline;
}

/* Responsive: ajusta márgenes y tamaños en pantallas chicas */
@media (max-width: 400px) {
  .login-box {
    padding: 1.5rem;
    max-width: 100%;
  }
}
</style>