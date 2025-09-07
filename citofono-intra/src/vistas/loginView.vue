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
        ¿No tienes cuenta? 
        <router-link to="/registro" class="register-link">
          Regístrate
        </router-link>
      </p>
    </main>
  </div>
</template>

<script>
import { ref } from 'vue';
import { login } from '../services/users'; 
import Cookies from "js-cookie";
import { useRouter } from 'vue-router';
import { inject } from 'vue';

export default {
   methods: {
    
  },
  setup() {
    const email = ref('');
    const password = ref('');
    const router = useRouter();
    

    const isAuthenticated = inject('isAuthenticated');

    const onSubmit = async() => {
      const response = await login(email.value, password.value);
      console.log(Object.keys(response.data).length)
      if (Object.keys(response.data).length > 0) {
        isAuthenticated.value = true;
        Cookies.set("usuario", response.data.id, { expires: 1 }); 
        router.push("/grabar");
      } 
      else {
        isAuthenticated.value = false;
        alert("Error al iniciar sesión. Por favor, verifica tus credenciales.");
      }
    };

    return { email, password, onSubmit };
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f9fafb; 
  padding: 1rem;
  box-sizing: border-box;
}

.login-box {
  background-color: #ffffff; 
  padding: 2rem;
  border: 2px solid #dc2626; 
  border-radius: 0.5rem; 
  box-shadow: 0 8px 15px rgba(220, 38, 38, 0.4); 
  width: 100%;
  max-width: 350px;
  box-sizing: border-box;
  text-align: center;
}

.title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #dc2626; 
  margin-bottom: 1.5rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.input-field {
  padding: 0.75rem 1rem;
  border: 1px solid #d1d5db; 
  border-radius: 0.375rem; 
  font-size: 1rem;
  transition: border-color 0.3s, box-shadow 0.3s;
  outline-offset: 2px;
}

.input-field:focus {
  border-color: #dc2626;
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.4);
  outline: none;
}

.btn-submit {
  background-color: #dc2626; 
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
  background-color: #b91c1c;
}

.register-text {
  margin-top: 1rem;
  color: #6b7280; 
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

@media (max-width: 400px) {
  .login-box {
    padding: 1.5rem;
    max-width: 100%;
  }
}
</style>