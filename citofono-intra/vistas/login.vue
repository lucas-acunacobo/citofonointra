<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="w-full max-w-md bg-white shadow-lg rounded-2xl p-8">
      <h2 class="text-2xl font-bold text-red-600 mb-6 text-center">Iniciar Sesión</h2>

      <form @submit.prevent="login">
        <!-- Email -->
        <div class="mb-4">
          <label class="block text-gray-700 mb-1" for="email">Correo</label>
          <input
            v-model="email"
            id="email"
            type="email"
            required
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
            placeholder="tu@correo.com"
          />
        </div>

        <!-- Password -->
        <div class="mb-4">
          <label class="block text-gray-700 mb-1" for="password">Contraseña</label>
          <input
            v-model="password"
            id="password"
            type="password"
            required
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
            placeholder="********"
          />
        </div>

        <!-- Botón -->
        <button
          type="submit"
          class="w-full bg-red-600 hover:bg-red-700 text-white font-semibold py-2 px-4 rounded-lg transition duration-200"
        >
          Entrar
        </button>
      </form>

      <!-- Enlaces -->
      <div class="mt-4 text-center">
        <a href="#" class="text-sm text-red-600 hover:underline">¿Olvidaste tu contraseña?</a>
      </div>
      <div class="mt-2 text-center">
        <span class="text-sm text-gray-600">¿No tienes cuenta?</span>
        <a href="#" class="text-sm text-red-600 font-medium hover:underline">Regístrate</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"

const email = ref("")
const password = ref("")

const login = () => {
  console.log("Login con:", email.value, password.value)
  // Aquí llamarías a tu API
}
</script>
