<template>
  <div class="app">
    <router-view />
  </div>
</template>

<script>
import { GetPlayers } from './services/routes';

export default {
  name: 'App',
  mounted: function () {
    this.getAllPlayers();
    this.checkTeam();
  },
  computed: {
    team() {
      return this.$store.state.team;
    }
  },
  methods: {
    async getAllPlayers() {
      const res = await GetPlayers();
      this.$store.commit('setPlayers', res);
    },
    checkTeam() {
        if (JSON.parse(localStorage.getItem('team_name')) === null) {
        this.$router.push('/login')
      }
    }
  }
};
</script>

<style>
.app {
  margin: 0;
  background-image: url('./assets/background.jpeg');
  background-repeat: no-repeat;
  background-size: cover;
  min-height: 100vh;
  color: white;
}
</style>