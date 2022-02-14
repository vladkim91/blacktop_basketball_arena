import { createRouter, createWebHistory } from 'vue-router';
import SignUp from '../views/SignUp.vue';
import Login from '../views/Login.vue';
import Game from '../views/Game.vue';
import Home from '../views/Home.vue';
import GameUi from '../components/GameUI.vue';
import TeamDetails from '../views/TeamDetails.vue';
import Players from '../views/Players.vue';

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
  },
  {
    path: '/game',
    name: 'Game',
    component: Game
  },
  {
    path: '/gameui',
    name: 'GameUi',
    component: GameUi
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/views',
    name: 'TeamDetails',
    component: TeamDetails
  },
  {
    path: '/players',
    name: 'Players',
    component: Players
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
