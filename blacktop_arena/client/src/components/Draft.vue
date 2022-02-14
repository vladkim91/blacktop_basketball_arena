<template>
  <div class="draft">
    <button
      class="start-game"
      @click="startGame"
      v-if="!(teams.teamOne.length < 3 || teams.teamTwo.length < 3)"
    >
      Start
    </button>
    <button class="start-game-disabled" v-else :disabled="isActive">
      Start
    </button>
    <h1 class="title">DRAFT</h1>
    <h3 v-if="!turn">Team 1 Turn</h3>
    <h3 v-else>Team 2 Turn</h3>

    <div class="teams">
      <div class="team-one-container">
        <h4>Team One</h4>
        <div class="team-one">
          <div
            class="team-one-player"
            v-for="player in teams.teamOne"
            :key="player.id"
          >
            <div class="p1-name">
              {{ player['name'] }}
            </div>
          </div>
        </div>
      </div>
      <div class="last-player">
        <h2 class="l-name">{{ last.name }}</h2>
        <img v-if="lastStats.defense" class="last" :src="last.image" alt="" />
        <div class="last" v-else></div>
        <div class="stats" v-if="lastStats.defense">
          <span class="stat">Rating Offense: {{ lastStats.offense }}</span>
          <span class="stat">Defense: {{ lastStats.defense }}</span>
          <span class="stat">Overall: {{ lastStats.overall }}</span>
        </div>
        <div v-else class='stats'></div>
        
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
        <div class="player-name">{{ player.nickname }}</div>
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
      if (this.checkId(this.ids, player.id)) {
        return null;
      }
      if (this.$store.state.teams.teamTwo.length === 3) {
        this.$store.commit('setTeams', [player, 0]);
        this.ids.push(player.id);
        this.last = player;
        this.getOverall(player);
      } else {
        if (turn === 0) {
          this.ids.push(player.id);
          this.$store.commit('setTeams', [player, turn]);
          this.last = player;
          this.getOverall(player);
          this.turn++;
        } else if (turn === 1) {
          this.ids.push(player.id);
          this.$store.commit('setTeams', [player, turn]);
          this.last = player;
          this.getOverall(player);
          this.turn--;
        }
      }
    },
    startGame() {
      this.ids = [];

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
h1 {
  font-family: 'Share', cursive;
}
.start-game {
  position: absolute;
  top: 5rem;
  right: 4rem;
  border: none;
  background-color: white;
  border: 2px solid black;
  border-radius: 1rem;
  padding: 1rem 1.5rem;
  cursor: pointer;
  font-family: 'Share', cursive;
  color: black;
  font-weight: black;
  font-size: 1.4rem;
}

.start-game-disabled {
  position: absolute;
  top: 5rem;
  right: 4rem;
  border: none;
  background-color: rgb(156, 156, 156);
  border: 2px solid rgb(0, 0, 0);
  border-radius: 1rem;
  padding: 1rem 1.5rem;
  cursor: pointer;
  font-family: 'Share', cursive;
  color: rgb(78, 78, 78);
  font-weight: bold;
  font-size: 1.4rem;
}

.draft {
  background-image: url('../assets/background.jpeg');
  background-repeat: no-repeat;
  background-size: cover;
  min-height: 100vh;
}

.teams {
  display: flex;
  justify-content: center;
}

.team-one-container,
.team-two-container {
  min-width: 9rem;
  padding: 1rem 5rem;
}

.team-one,
.team-two {
  background-color: rgb(71, 71, 71);
  min-width: 14rem;
  min-height: 14rem;
  border-radius: 0.7rem;
  font-family: 'Share', cursive;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  height: 10rem;
  font-size: 1.2rem;
  font-weight: bold;
  text-shadow: 2px 2px 2px black;
}

.team-one {
  align-items: flex-start;
}

.team-two {
  align-items: flex-end;
}

.p1-name,
.p2-name {
  padding: 1rem;
}
h4 {
  text-align: center;
  margin-bottom: 0.5rem;
  color: white;
  font-family: 'Share', cursive;
  font-size: 1.3rem;
}

.title,
h3 {
  margin: 1.2rem auto;
  text-align: center;
  font-family: 'Share', cursive;
}

.disabled {
  pointer-events: none;
}

.player-grid {
  display: flex;
  flex-wrap: wrap;
  margin: 0rem 12rem;
  justify-content: center;
}
.player-container {
  display: flex;
  flex-direction: column;
  border: goldenrod 2px solid;
  border-radius: 0.5rem;
  margin: 0.2rem;
  align-items: center;
  background-color: black;
  width: 7rem;
  cursor: pointer;
  filter: grayscale(40%);
  transition: ease-in .5s;
}

.player-container:hover {
  filter: grayscale(0);
  transform: scale(1.1)
}
.player-name {
  font-family: 'Share', cursive;
  padding: .1rem;

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

.l-name {
  position: absolute;
  top: 9rem;
font-family: 'Share', cursive;
}

.last {
  margin-top: 2rem;
  width: 20rem;
  height: 18rem;
  object-fit: cover;
  object-position: top;
  border-radius: 1rem;
}

.stats {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  font-family: 'Share', cursive;
  margin: 1rem auto;
  height: 2rem;
}

.last-player {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 26rem;
}

</style>