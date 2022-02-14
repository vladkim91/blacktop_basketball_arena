<template>
  <div class="signup">
  

    <form>
        <h1>Sign Up</h1>
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

<style scoped>
form {
  background-color: white;
  text-align: center;
  width: 20%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 2rem auto;
  height: 15rem;
}
h1 {
  color: black;
  font-family: 'Share';
}
input {
  margin: 0.2rem 5rem;
  width: 10rem;
  height: 1.5rem;
}

button {
  background-color: #555555;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  background-color: white;
  color: black;
  border: 2px solid #c2c2c2; /* Green */
  font-size: 1.4rem;
  font-family: 'Share';
  padding: 0.4rem;
  border-radius: 1rem;
   margin-top:1rem;
}
p {
  text-align: center;
}
</style>