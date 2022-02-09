<template>
  <div class="draft">
    <div v-for="player in players" :key="player.id">
      <button
        @click="
          (e) => {
            pickTeams(player);
            disableButton(e);
          }
        "
        :disabled="!isActive"
      >
        {{ player.name }}
      </button>
    </div>
    <button
      class="start-game"
      @click="startGame"
      v-if="!(teams.teamOne.length < 3 || teams.teamTwo.length < 3)"
    >
      Start
    </button>
    <button v-else :disabled="isActive">Start</button>
    <div class="teams">
      <div v-if="teams.teamOne.length" class="team-one">
        <h2>Team One</h2>
        <div
          class="team-one-player"
          v-for="player in teams.teamOne"
          :key="player.id"
        >
          {{ player['name'] }}
        </div>
      </div>
      <div v-if="teams.teamTwo.length" class="team-two">
        <h2>Team Two</h2>
        <div
          class="team-two-player"
          v-for="player in teams.teamTwo"
          :key="player.id"
        >
          {{ player['name'] }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Draft',
  data() {
    return {
      teams: {
        teamOne: [],
        teamTwo: []
      },
      turn: 0,
      isActive: true
    };
  },

  computed: {
    players() {
      return this.$store.state.players;
    }
  },
  methods: {
    pickTeams(player) {
      if (this.turn === 0) {
        this.teams.teamOne.push(player);
        this.turn++;
      } else {
        this.teams.teamTwo.push(player);
        this.turn--;
      }
    },
    startGame() {
      this.$store.commit('setTeams', this.teams);
      this.$router.push('/gameui');
    },
    disableButton(e) {
      if (this.teams.teamOne.length === 3 && this.teams.teamTwo.length === 3)
        this.isActive = false;
      console.log(e.target.classList);
    }
  }
};
</script>


<style scoped>
.disabled {
  pointer-events: none;
}
</style>