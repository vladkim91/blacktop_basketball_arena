<template>
  <div class="team-details">
    <div class="team-container">
      <div class="team-name">{{ team.team_name }}</div>
      <div class="record">
        <div class="win">Wins: {{ team.wins }}</div>
        <div class="loss">Losses: {{ team.losses }}</div>
      </div>
    </div>
    <div class="history">
      <div class="log" v-for="log in history.slice().reverse()" :key="log.id">
        <h4 class="w" v-if="log.team_one_score >= 21">W</h4>
        <h4 class="l" v-else>L</h4>
        <div class="my-team">
          <table>
            <tr>
              <th>Points</th>
              <th>Reb</th>
              <th>Assists</th>
              <th>Steals</th>
              <th>Blocks</th>
              <th>TO</th>
              <th>FG%</th>
              <th>3P%</th>
            </tr>
            <tr>
              <td>{{ log.team_one_stats.points }}</td>
              <td>
                {{ log.team_one_stats.rebounds }}
              </td>
              <td>{{ log.team_one_stats.assists }}</td>
              <td>{{ log.team_one_stats.steals }}</td>
              <td>{{ log.team_one_stats.blocks }}</td>
              <td>
                {{ log.team_one_stats.turnovers }}
              </td>
              <td>
                <span>%</span
                >{{
                  Math.ceil(
                    (log.team_one_stats.fgm / log.team_one_stats.fga) * 100
                  )
                }}
              </td>
              <td v-if="log.team_one_stats.threeA !== 0">
                <span>%</span
                >{{
                  Math.ceil(
                    (log.team_one_stats.threeM / log.team_one_stats.threeA) *
                      100
                  )
                }}
              </td>
              <td v-else>%0</td>
            </tr>
          </table>
          <div
            class="player-names"
            v-for="player in log.team_one_squad"
            :key="player.id"
          >
            {{ player.name }}
          </div>
        </div>

        <div class="score">
          {{ log.team_one_score }} : {{ log.team_two_score }}
        </div>
        <div class="opposing-team">
          <table>
            <tr>
              <th>Points</th>
              <th>Reb</th>
              <th>Assists</th>
              <th>Steals</th>
              <th>Blocks</th>
              <th>TO</th>
              <th>FG%</th>
              <th>3P%</th>
            </tr>
            <tr>
              <td>{{ log.team_two_stats.points }}</td>
              <td>
                {{ log.team_two_stats.rebounds }}
              </td>
              <td>{{ log.team_two_stats.assists }}</td>
              <td>{{ log.team_two_stats.steals }}</td>
              <td>{{ log.team_two_stats.blocks }}</td>
              <td>
                {{ log.team_two_stats.turnovers }}
              </td>
              <td>
                <span>%</span
                >{{
                  Math.ceil(
                    (log.team_two_stats.fgm / log.team_two_stats.fga) * 100
                  )
                }}
              </td>
              <td v-if="log.team_two_stats.threeA !== 0">
                <span>%</span
                >{{
                  Math.ceil(
                    (log.team_two_stats.threeM / log.team_two_stats.threeA) *
                      100
                  )
                }}
              </td>
              <td v-else>%0</td>
            </tr>
          </table>
          <div
            class="player-names"
            v-for="player in log.team_two_squad"
            :key="player.id"
          >
            {{ player.name }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { GetHistory } from '../services/routes.js';
export default {
  name: 'TeamDetails',
  mounted() {
    this.getHistory();
  },
  computed: {
    team() {
      return JSON.parse(localStorage.getItem('team_name'));
    },
    history() {
      return this.$store.state.history;
    }
  },
  methods: {
    async getHistory() {
      const res = await GetHistory();
      this.$store.commit('getHistory', res);
    }
  }
};
</script>



<style scoped>
.history {
  font-family: 'Share', cursive;
  height: 100vh;
  overflow: auto;
}
table {
  font-size: 1rem;
  text-align: center;
}
th {
  width: 2.2rem;
  border-bottom: 2px solid rgb(142, 142, 142);
}
.log {
  display: flex;
  padding: 1rem;
  box-shadow: 0px 0px 10px 2px rgb(255, 255, 255);
  width: 70%;
  justify-content: space-evenly;
  align-items: center;
  margin: 2rem auto;
  background: linear-gradient(black, rgb(48, 48, 48));
  text-shadow: 2px 2px 2px black;
  border-radius: 0.7rem;
}

.w,
.l {
  font-size: 2rem;
}

.l {
  color: red;
}

.w {
  color: green;
}

.score {
  font-size: 2rem;
}
.my-team {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.player-names {
  font-size: 1.3rem;
}

.team-name {
  font-family: 'Comforter Brush', cursive;
  font-size: 4rem;
}

.team-container {
  padding: 1rem
}

.record {
  font-family: 'Share', cursive;
  font-size: 2rem;
}
</style>