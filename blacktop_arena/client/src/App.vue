<template>
  <div id="nav">
    <router-link to="/signup">Sign Up</router-link> |
    <router-link to="/login">Log In</router-link> |
    <router-link to="/game">Game</router-link>
  </div>
  <router-view />
</template>

<script>
import { GetPlayers } from './services/routes';
export default {
  name: 'App',
  mounted: function () {
    this.getAllPlayers();
  },
  methods: {
    async getAllPlayers() {
      const res = await GetPlayers();
      console.log(res)
      this.$store.commit('setPlayers', res);
    }
  }
};
</script>
