<template>
  <div id="app">
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
    team_id() {
      return this.$store.state.id;
    }
  },
  data() {
    return {
      signedIn: false
    };
  },

  methods: {
    async getAllPlayers() {
      const res = await GetPlayers();
      this.$store.commit('setPlayers', res);
    },
    checkTeam() {
      console.log('checking');
      if (this.team_id) {
        console.log('has id');
        this.signedIn = true;
      } else {
        this.$router.push('/login');
      }
    }
  }
};
</script>
