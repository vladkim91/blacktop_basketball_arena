<template>
  <div class="nav">

    <button @click="logout">log out</button>
  </div> 
</template>

<script>
export default {
  name: 'Nav',
  methods: {
    logout() {
      localStorage.removeItem('team_name')
      this.$router.push('/login')
    }
  }
};
</script>