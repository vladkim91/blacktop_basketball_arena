<template>
  <div class="signup">
    <h1>Sign Up</h1>

    <form>
      <input
        placeholder="Team Name"
        type="team_name"
        name="team_name"
        v-model="team_name"
      />
      <input
        placeholder="Password"
        type="password"
        name="password"
        v-model="password"
      />
      <button @click="submitForm" type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import { CreateTeam } from '../services/routes';
export default {
  name: 'SignUp',
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
      await CreateTeam(formData);
      this.$router.push('/login');
    }
  }
};
</script>
