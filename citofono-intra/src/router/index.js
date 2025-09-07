import { createRouter, createWebHistory } from 'vue-router'
import Cookies from "js-cookie";
import login from '../vistas/loginView.vue'
import home from '../vistas/homeView.vue'
import videos from '../vistas/videosView.vue'
import registro from '../vistas/registroView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/grabar",
      name: "home",
      component: home,
      meta: { requiresAuth: true }
    },
    {
      path: "/login",
      name: "login",
      component: login,
    },
    {
      path: "/videos",
      name: "videos",
      component: videos,
      meta: { requiresAuth: true }
    },
    {
      path: "/registro",
      name: "registro",
      component: registro,
    },
  ],
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!Cookies.get('usuario'); // Comprueba la cookie

  // Si la ruta a la que va requiere autenticación Y el usuario no está autenticado
  if (to.meta.requiresAuth && !isAuthenticated) {
    // Redirige a la página de login
    next({ name: 'login' });
  } else {
    // Si la ruta no requiere autenticación O el usuario está autenticado,
    // permite la navegación
    next();
  }
});

export default router
