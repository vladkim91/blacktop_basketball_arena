import { createRouter, createWebHistory } from 'vue-router';
import SignUp from '../views/SignUp.vue';
import Login from '../views/Login.vue';

const routes = [
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
