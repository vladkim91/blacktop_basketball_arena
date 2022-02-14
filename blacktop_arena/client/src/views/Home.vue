<template>
  <div class="home">
    <h2 class="title">Legend Lineups</h2>
    <div class="lineups">
      <div
        @click="clickHandler"
        :class="'c' + squad.team_name.split(' ').join('')"
        v-for="squad in squads"
        :key="squad.id"
      >
        <h3 class="team-name">{{ squad.team_name }}</h3>
      </div>
    </div>
    <div class="navigation">
      <div class="n-container draft">
        <button @click="goToDraft" class="btn-link">Draft</button>
      </div>
      <div class="n-container about">
        <button @click="goToTeamDetails" class="btn-link">About</button>
      </div>
      <div class="n-container players">
        <button @click="goToPlayers" class="btn-link">Players</button>
      </div>
    </div>
  </div>
</template>

<script>
import {
  GetAllSquads,
  GetPlayerById,
  GetSquadByName
} from '../services/routes.js';
export default {
  name: 'Home',
  components: {},
  data() {
    return {
      legends: [],
      array: [
        '../assets/lakers3.jpeg',
        '../assets/warriors3.jpeg',
        '../assets/bulls3.jpeg',
        '../assets/spurs3.jpeg',
        '../assets/boston3.jpeg',
        '../assets/heat3.jpeg'
      ]
    };
  },
  computed: {
    squads() {
      return this.$store.state.squads;
    }
  },
  mounted() {
    this.getSquads();
  },
  methods: {
    async getSquads() {
      const res = await GetAllSquads();
      this.$store.commit('setSquads', res);
    },
    async clickHandler(e) {
      const array = [];
      if (e.target.innerHTML.slice(0, 3) === '<h3') {
        const res = await GetSquadByName(e.target.firstElementChild.innerHTML);
        for (const key in res.players) {
          array.push(res.players[key]);
        }
      } else {
        const res = await GetSquadByName(e.target.innerHTML);
        for (const key in res.players) {
          array.push(res.players[key]);
        }
      }
      this.getLegendPlayers(array);
    },
    async getLegendPlayers(array) {
      const legendArray = [];
      for (let i = 0; i < array.length; i++) {
        const res = await GetPlayerById(array[i]);
        legendArray.push(res);
      }
      this.$store.commit('setLegends', legendArray);

      this.$router.push('/game');
    },
    goToDraft() {
      this.$router.push('/game')
    },
    goToTeamDetails() {
      this.$router.push('/views')
    },
    goToPlayers() {
      this.$router.push('/players')
    }
  }
};
</script>

<style scoped>
.home {
  text-align: center;
  display: flex;
  flex-direction: column;
}
.lineups {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 60rem;
  margin: 0.2rem auto;
}

.navigation {
  display: flex;
  margin: 1rem auto;
  background: linear-gradient(135deg, rgb(0, 0, 0) 60%, rgb(39, 39, 39));
  width: 100vw;
  height: 19rem;
  justify-content: center;
  align-items: center;
}

.n-container {
  margin: 2rem 4rem;
  width: 10rem;
  height: 14rem;
  background-color: grey;
  border-radius: 5px;
  border: grey 0.2px solid;
}

.btn-link {
  margin-top: 12.9rem;
  background-color: rgb(133, 0, 0);
  color: white;
  box-shadow: 0 3px 10px rgb(0 0 0 / 0.2);
  border-radius: 1rem;
  width: 8rem;
  border: none;
  font-family: 'Share', cursive;
  text-shadow: 2px 2px 4px #000000;
  font-size: 1.6rem;
  cursor: pointer;
  transition: ease-in-out;
}
.btn-link:hover {
  box-shadow: 0px 1px 1px #929292;
  transform: scale(1.02);
  transition: ease-in-out;
}
.draft,
.players,
.about {
  box-shadow: 0 2px 2px rgb(58, 55, 55);

  filter: grayscale(50%);
  transition: 0.35s ease-out;
}

.team-name {
  font-family: 'Share';
}
.draft:hover,
.players:hover,
.about:hover {
  box-shadow: 0px 5px 15px black;
  filter: grayscale(0%);
  transform: scale(1.04);
}

.draft {
  background-image: url('../assets/draft.jpeg');
  background-size: cover;
}
.players {
  background-image: url('../assets/players.png');
  background-size: cover;
}
.about {
  background-image: url('../assets/about.jpeg');
  background-size: cover;
}

.title {
  font-family: 'Share', cursive;
  margin: 0.5rem;
}
.cShowTimeLakers,
.c2018Warriors,
.cChicagoBulls3,
.cSanAntonioSpurs,
.cCelticsBig3,
.cMiamiHeatBig3 {
  width: 18rem;
  height: 10rem;
  background-size: cover;
  margin: 0.5rem;
  transition: 0.6s ease-out;
  cursor: pointer;
  font-size: 1.7rem;
}
.cShowTimeLakers:hover,
.c2018Warriors:hover,
.cChicagoBulls3:hover,
.cSanAntonioSpurs:hover,
.cCelticsBig3:hover,
.cMiamiHeatBig3:hover {
  transform: scale(1.08);
}

.cShowTimeLakers {
  background-image: url('../assets/lakers3.jpeg');
  border: #ffc60d 2px solid;
  border-radius: 0.2rem;
  color: #ffdc6b;
  text-shadow: 1px 1px #8400ff;
}
.c2018Warriors {
  background-image: url('../assets/warriors3.jpeg');
  border: #1200b4 2px solid;
  border-radius: 0.2rem;
  color: #ffffff;
  text-shadow: 1px 1px #1900ff;
}
.cChicagoBulls3 {
  background-image: url('../assets/bulls3.jpeg');
  border: #b60000 2px solid;
  border-radius: 0.2rem;
  color: #c00000;
  text-shadow: 1px 1px #000000;
}
.cSanAntonioSpurs {
  background-image: url('../assets/spurs.jpg');
  border: #ffffff 2px solid;
  border-radius: 0.2rem;
  color: rgb(255, 255, 255);
  text-shadow: 1px 1px #000000;
}
.cCelticsBig3 {
  background-image: url('../assets/boston3.png');
  border: #008d00 2px solid;
  border-radius: 0.2rem;
  color: #ffffff;
  text-shadow: 1px 1px #008d00;
}
.cMiamiHeatBig3 {
  background-image: url('../assets/heat3.jpeg');
  border: #a10000 2px solid;
  border-radius: 0.2rem;
  color: #ffffff;
  text-shadow: 1px 1px #000000;
}
</style>