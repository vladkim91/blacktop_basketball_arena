<template>
  <div class="game-ui">
    <h1>GAME UI</h1>
    <h2>Team One</h2>
    <div v-for="team in teams.teamOne" :key="team.id">
      <div v-for="player in team" :key="player.id">
        {{player.attributes}}
      </div>
    </div>
    <h2>Team Two</h2>
    <div v-for="team in teams.teamTwo" :key="team.id">
      <div v-for="player in team" :key="player.id">
        {{player}}
      </div>
    </div>

    </div>
</template>

<script>
export default {
  data() {
    return {
      gameInProgress: false,
      gameStats: {},
      stats: {
        teamOne: {
          points: 0,
          rebounds: 0,
          assists: 0,
          steals: 0,
          blocks: 0,
          turnovers: 0,
          fgm: 0,
          fga: 0,
          threes: 0
        },
        teamTwo: {
          points: 0,
          rebounds: 0,
          assists: 0,
          steals: 0,
          blocks: 0,
          turnovers: 0,
          fgm: 0,
          fga: 0,
          threes: 0
        }
      },
      gameScore: {
        teamOne: 0,
        teamTwo: 0
      }
    };
  },
  computed: {
    teams() {
      return this.$store.state.teams;
    }
  }
};
</script>