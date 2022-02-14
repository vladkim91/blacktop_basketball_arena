<template>
  <div class="app">
    <Nav />

    <router-view />
  </div>
</template>

<script>
import { GetPlayers, GetHistory } from './services/routes';
import Nav from './components/Nav.vue';

export default {
  name: 'App',
  mounted: function () {
    this.getAllPlayers();
    this.checkTeam();
    this.getHistory();
  },

  components: {
    Nav
  },
  computed: {
    team() {
      return this.$store.state.team;
    },
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    },
    activeSession() {
      return localStorage.getItem('team_name') !== null;
    }
  },
  methods: {
    async getAllPlayers() {
      const res = await GetPlayers();
      this.$store.commit('setPlayers', res);
    },
    checkTeam() {
      if (JSON.parse(localStorage.getItem('team_name')) === null) {
        this.$router.push('/login');
      }
    },
    async getHistory() {
      const res = await GetHistory();

      this.$store.commit('getHistory', res);
    }
  }
};
</script>

<style>
body {
  margin: 0;
}
@import url('https://fonts.googleapis.com/css2?family=Comforter+Brush&family=Roboto+Mono:wght@200&family=Share&display=swap');
.app {
  margin: 0;
  background-image: url('./assets/background.jpeg');
  background-repeat: no-repeat;
  background-size: cover;
  min-height: 100vh;
  color: white;
}
</style>