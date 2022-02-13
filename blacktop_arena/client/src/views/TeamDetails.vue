<template>
  <div class="team-details">

  </div>
</template>

<script>
export default {
  name: 'TeamDetails',
  mounted() {
    this.getTeamDetails(this.team_id)
  },
  computed: {
    team_id() {
      return this.$store.state.id
    }
  },
  methods: {
  
  }
}
</script>