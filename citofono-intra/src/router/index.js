import { createRouter, createWebHistory } from 'vue-router'
import Cookies from "js-cookie";
import login from '../../vistas/loginView.vue'
import home from '../../vistas/homeView.vue'
import videos from '../../vistas/videosView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/grabar",
      name: "home",
      component: home,
      meta: { requiresAuth: false }
    },
    {
      path: "/login",
      name: "login",
      component: login,
      meta: { requiresAuth: false }
    },
    {
      path: "/videos",
      name: "videos",
      component: videos,
      meta: { requiresAuth: false }
    },
  ],
})

router.beforeEach((to, from, next) => {
  // Check if the user is authenticated
  const isAuthenticated = Cookies.get("auth");

  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'login' });
  } else {
    next();
  }
});

export default router
