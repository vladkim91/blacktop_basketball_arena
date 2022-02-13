<template>
  <div class="log-in">
    <h1>Log in</h1>

    <form>
      <input type="team_name" name="team_name" v-model="team_name" />
      <input type="password" name="password" v-model="password" />
      <button @click="submitForm" type="submit">Login</button>
    </form>
    <p>Don't have a team? <router-link to="/signup">Sign Up</router-link></p>
  </div>
</template>

<script>
import { GetTeamByNameAndPassword } from '../services/routes';
export default {
  name: 'Login',
  data() {
    return {
      team_name: '',
      password: ''
    };
  },
  methods: {
    async submitForm(e) {
      e.preventDefault();
      const formData = {
        team_name: this.team_name,
        password: this.password
      };
      const res = await GetTeamByNameAndPassword(formData);
      localStorage.setItem('team_name', JSON.stringify(res));
      this.$store.commit(
        'setTeam',
        JSON.parse(localStorage.getItem('team_name'))
      );
      this.$store.commit('setLoggedIn', true)
      this.$router.push('/home');
    }
  }
};
</script>
