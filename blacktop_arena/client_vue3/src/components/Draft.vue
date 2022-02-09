<template>
  <div class="draft">
    <div v-for="player in players" :key="player.id">
      <button
        @click="
          () => {
            pickTeams(player);
          }
        "
      >
        {{ player.name }}
      </button>
    </div>
    <div class="teams">
      <div v-if="teams.teamOne.length" class="team-one">{{ teams.teamOne[0]['name'] }}</div>
      <div v-if="teams.teamTwo.length" class="team-two">{{ teams.teamTwo[0]['name'] }}</div>
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
      turn: 0
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
    startGame() {}
  }
};
</script>
