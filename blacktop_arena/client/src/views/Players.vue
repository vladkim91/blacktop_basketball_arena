<template>
  <div class="players">
    <div class="player-list-container">
      <div class="player" v-for="player in players" :key="player.id">
        <div @click="pickCurrentPlayer">{{ player.name }}</div>
      </div>
    </div>

    <div class="player-details">
      <h1>{{ currentPlayer.name }}</h1>
      <h2>{{ currentPlayer.nickname }}</h2>
      <img v-if="currentPlayer.name" :src="currentPlayer.image" alt="" />
      <p>{{ currentPlayer.description }}</p>
    </div>
    <div v-if="currentPlayer.name" class="stat-table">
      <h2>Offense</h2>
      <table>
        <tr>
          <th>Dunk</th>
          <td>{{ currentPlayer.attributes.offense.dunk }}</td>
        </tr>
        <tr>
          <th>Passing</th>
          <td>{{ currentPlayer.attributes.offense.pass }}</td>
        </tr>
        <tr>
          <th>Layup</th>
          <td>{{ currentPlayer.attributes.offense.layup }}</td>
        </tr>
        <tr>
          <th>Three Pointer</th>
          <td>{{ currentPlayer.attributes.offense.three }}</td>
        </tr>
        <tr>
          <th>Handles</th>
          <td>{{ currentPlayer.attributes.offense.handles }}</td>
        </tr>
        <tr>
          <th>Mid Range</th>
          <td>{{ currentPlayer.attributes.offense.mid_range }}</td>
        </tr>
        <tr>
          <th>Post Shot</th>
          <td>{{ currentPlayer.attributes.offense.post_shot }}</td>
        </tr>
        <tr>
          <th>Offensive Rebound</th>
          <td>{{ currentPlayer.attributes.offense.off_rebound }}</td>
        </tr>
      </table>
      <h2>Defense</h2>
      <table>
        <tr>
          <th>Block</th>
          <td>{{ currentPlayer.attributes.defense.block }}</td>
        </tr>
        <tr>
          <th>Interior Defense</th>
          <td>{{ currentPlayer.attributes.defense.inside_defense }}</td>
        </tr>
        <tr>
          <th>Perimeter Defense</th>
          <td>{{ currentPlayer.attributes.defense.outside_defense }}</td>
        </tr>
        <tr>
          <th>Steal</th>
          <td>{{ currentPlayer.attributes.defense.steal }}</td>
        </tr>
        <tr>
          <th>Post Defense</th>
          <td>{{ currentPlayer.attributes.defense.post_defense }}</td>
        </tr>
        <tr>
          <th>Defensive Rebound</th>
          <td>{{ currentPlayer.attributes.defense.def_rebound }}</td>
        </tr>
      </table>
      <h2>Physical</h2>
      <table>
        <tr>
          <th>Speed</th>
          <td>{{ currentPlayer.attributes.physical.speed }}</td>
        </tr>
        <tr>
          <th>Strength</th>
          <td>{{ currentPlayer.attributes.physical.strength }}</td>
        </tr>
        <tr>
          <th>Vertical</th>
          <td>{{ currentPlayer.attributes.physical.vertical }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Players',
  data() {
    return {
      currentPlayer: {}
    };
  },
  computed: {
    players() {
      return this.$store.state.players;
    }
  },
  methods: {
    pickCurrentPlayer(e) {
      this.players.forEach((el) => {
        if (el.name === e.target.innerHTML) {
          this.currentPlayer = el;
        }
      });
    }
  }
};
</script>

<style scoped>
.players {
  display: flex;
}

.player-list-container {
  overflow: auto;
  height: 90vh;
}

.player-list-container::-webkit-scrollbar {
  width: 12px;
}

.player-list-container::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(255, 206, 83, 0.3);
  border-radius: 10px;
}

.player-list-container::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.5);
}
.player {
  display: flex;
  flex-direction: column;
  font-size: 1.7rem;
  margin: 2.2rem 9rem;
  border-radius: 1rem;
  background: linear-gradient(to right, #bf953f, #b38728, #fbf5b7, #aa771c);
  text-align: center;
  padding: 1rem;
  color: black;
  font-family: 'Comforter Brush', cursive;
  font-weight: bold;
  cursor: pointer;

  transition: ease-in-out 1s;
}
.player:hover {
  transform: scale(1.1);
}
.player-details {
  width: 25rem;
  font-family: 'Share', cursive;
  margin-left: 1rem;
}

.player-details > img {
  width: 20rem;
  height: 22rem;
  contain: content;
  object-fit: cover;
  object-position: top;
}
.player-details > p {
  width: 20rem;
}

h1 {
  background: linear-gradient(to top right, #bf953f, #b38728, #fbf5b7, #aa771c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.stat-table > h2 {
  background: linear-gradient(to top right, #bf953f, #b38728, #fbf5b7, #aa771c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-family: 'Share';
  text-align: center;
}
table {
  font-family: 'Share';
  text-align: center;
}
table {
  width: 22rem;
  background: linear-gradient(to right, #bf953f, #b38728, #fbf5b7, #aa771c);
  text-shadow: 2px 2px 2px black;
  border-radius: 1rem;
}

th {
  width: 12rem;
  height: 1.3rem;
}
</style>

