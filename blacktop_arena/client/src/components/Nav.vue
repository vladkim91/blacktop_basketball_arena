<template>
  <div class="nav">
    <router-link @click="clearTeamQuery" class="logo" to="/home">Blacktop</router-link>
    <button class="logout" @click="logout">Log out</button>
  </div>
</template>

<script>
export default {
  name: 'Nav',
  data() {
    return {
      
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('team_name');
      this.$router.push('/login');
      this.$store.commit('setLoggedIn', false);
    },
    clearTeamQuery() {
      this.$store.commit('reset')
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn
    }
  }
};
</script>

<style scoped>
.logo {
  font-family: 'Comforter Brush', cursive;
  color: black;
  text-decoration: none;
  font-size: 1.6rem;
  padding: .4rem 4rem;
}
.nav {
  background-color: #fbf5f3;
  display: flex;
  justify-content: space-between;
}
.logout {
  border: none;
  background: transparent;
  font-family: 'Share', cursive;
  font-weight: bold;
  font-size: 1.4rem;
  margin-right: 4rem
}
</style>