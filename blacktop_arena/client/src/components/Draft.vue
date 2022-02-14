<template>
  <div class="draft">
    <h1 class="title">DRAFT</h1>
    <h3 v-if="!turn">Team 1 Turn</h3>
    <h3 v-else>Team 2 Turn</h3>
    <button
      class="start-game"
      @click="startGame"
      v-if="!(teams.teamOne.length < 3 || teams.teamTwo.length < 3)"
    >
      Start
    </button>
    <button v-else :disabled="isActive">Start</button>
    <div class="teams">
      <div class="team-one-container">
        <h4>Team One</h4>
        <div class="team-one">
          <div
            class="team-one-player"
            v-for="player in teams.teamOne"
            :key="player.id"
          >
            <div class="p1name">
              {{ player['name'] }}
            </div>
          </div>
        </div>
      </div>
      <div class="last-player">
        {{ last.name }}
        <img class="last" :src="last.image" alt="" />
        Rating Offense: {{ lastStats.offense }} Defense:
        {{ lastStats.defense }} Overall: {{ lastStats.overall }}
      </div>
      <div class="team-two-container">
        <h4>Team Two</h4>
        <div class="team-two">
          <div
            class="team-two-player"
            v-for="player in teams.teamTwo"
            :key="player.id"
          >
            <div class="p2-name">
              {{ player['name'] }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="player-grid">
      <div class="player-container" v-for="player in players" :key="player.id">
        <div class="player-name">{{ player.name }}</div>
        <button
          class="player-button"
          @click="
            (e) => {
              pickTeams(player, turn);
              disableButton(e);
            }
          "
          :disabled="!isActive"
        >
          <img class="avatar" :src="player.avatar" alt="" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Draft',
  data() {
    return {
      teams: this.$store.state.teams,
      last: {},
      lastStats: {
        offense: 0,
        defense: 0,
        overall: 0
      },
      turn: 0,
      isActive: true,
      ids: []
    };
  },
  mounted() {
    this.extractLegendId();
  },
  computed: {
    players() {
      return this.$store.state.players;
    }
  },
  methods: {
    pickTeams(player, turn) {
      this.checkId(this.ids, player.id);
      if (this.$store.state.teams.teamTwo.length === 3) {
        this.$store.commit('setTeams', [player, turn]);
        this.last = player;
        this.getOverall(player);
      } else {
        if (turn === 0) {
          this.$store.commit('setTeams', [player, turn]);
          this.last = player;
          this.getOverall(player);
          this.turn++;
        } else if (turn === 1) {
          this.$store.commit('setTeams', [player, turn]);
          this.last = player;
          this.getOverall(player);
          this.turn--;
        }
      }
    },
    startGame() {
      // this.$store.commit('setTeams', this.teams);
      this.$router.push('/gameui');
    },
    disableButton() {
      if (this.teams.teamOne.length === 3 && this.teams.teamTwo.length === 3)
        this.isActive = false;
    },
    getOverall(player) {
      let off = 0,
        def = 0,
        phys = 0,
        overall = 0;
      let offenseOv = Math.ceil(off / 8 / 0.9);
      let defenseOv = Math.ceil(def / 6 / 0.9);

      for (const key in player) {
        if (key == 'attributes') {
          for (const stat in player[key].offense) {
            off += player[key].offense[stat];
          }
          for (const stat in player[key].defense) {
            def += player[key].defense[stat];
          }
          for (const stat in player[key].physical) {
            phys += player[key].physical[stat];
          }
          offenseOv = Math.ceil(off / 8 / 0.9);
          defenseOv = Math.ceil(def / 6 / 0.9);

          overall = Math.ceil((off + def + phys) / 17 / 0.9);
        }
      }
      this.lastStats.overall = overall;
      this.lastStats.offense = offenseOv;
      this.lastStats.defense = defenseOv;
    },
    extractLegendId() {
      const array = [];
      if (this.$store.state.teams.teamTwo.length === 3) {
        this.$store.state.teams.teamTwo.forEach((e) => {
          array.push(e.id);
        });
        this.ids = array;
      }
    },
    checkId(array, playerId) {
      return array.includes(playerId);
    }
  }
};
</script>


<style scoped>
.draft {
  background-image: url('../assets/background.jpeg');
  background-repeat: no-repeat;
  background-size: cover;
  min-height: 100vh;
}

.teams {
  display: flex;
  justify-content: space-evenly;
}

.team-one-container,
.team-two-container {
  min-width: 9rem;
}

.team-one,
.team-two {
  background-color: blue;
  min-width: 9rem;
  min-height: 12rem;
  border-radius: 0.7rem;
}
h4 {
  text-align: center;
  margin-bottom: 0.5rem;
  color: white;
}

.title,
h3 {
  margin: 1.2rem auto;
  text-align: center;
}

.disabled {
  pointer-events: none;
}

.player-grid {
  display: flex;
  flex-wrap: wrap;
  margin: 4rem 12rem;
  justify-content: center;
}
.player-container {
  display: flex;
  flex-direction: column;
  border: goldenrod 2px solid;
  border-radius: 0.5rem;
  margin: 0.2rem;
}

.player-container:hover {
  cursor: pointer;
}

.player-button {
  border: none;
  background-color: transparent;
}

.avatar {
  width: 4rem;
  height: 4rem;
  object-fit: cover;
  margin: 0;
  padding: 0;
}

.last {
  width: 20rem;
  height: 20rem;
  object-fit: contain;
}

.last-player {
  display: flex;
  flex-direction: column;
}
</style>