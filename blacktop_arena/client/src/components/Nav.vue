<template>
  <div class="nav">
    <router-link class="logo" to="/"> Blacktop</router-link>
    <button v-if="isLoggedIn" class="logout" @click="logout">Log out</button>
  </div>
</template>

<script>
export default {
  name: 'Nav',
  methods: {
    logout() {
      localStorage.removeItem('team_name');
      this.$router.push('/login');
      this.$store.commit('setLoggedIn', false);
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
  font-size: 3rem;
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