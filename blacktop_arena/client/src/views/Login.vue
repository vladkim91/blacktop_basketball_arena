<template>
  <div class="log-in">
    <h1>Log in</h1>

    <form @submit.prevent="submitForm">
      <input type="username" name="username" v-model="username" />
      <input type="password" name="password" v-model="password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        password: this.password
      };

      axios
        .post('/api/v1/token/login', formData)
        .then((response) => {
          const token = response.data.auth_token;

          this.$store.commit('setToken', token);

          axios.defaults.headers.common['Authorization'] = 'Token ' + token;

          localStorage.setItem('token', token);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }
};
</script>
