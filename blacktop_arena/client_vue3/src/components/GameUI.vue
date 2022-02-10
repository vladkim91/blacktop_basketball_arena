<template>
  <div class="game-ui">
    <h1>GAME UI</h1>
    <h2>Team One</h2>
    <div v-for="player in teams.teamOne" :key="player.id">
      {{ player.name }}
    </div>
    <h2>Team Two</h2>
    <div v-for="player in teams.teamTwo" :key="player.id">
      {{ player.name }}
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.countdown();
    // setTimeout(this.startGame(), 5000)
  },

  data() {
    return {
      possession: null,
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
  },
  methods: {
    countdown() {
      this.startGame()
      // let audio = new Audio(require('../assets/whistle.mp3'));
      // setTimeout(() => console.log(3), 2000);
      // setTimeout(() => console.log(2), 3000);
      // setTimeout(() => console.log(1), 4000);
      // setTimeout(() => console.log('GO'), 4500);
      // setTimeout(() => {
      //   // audio.play();
      // }, 4500);
      
    },
    getPlayerOverall() {

    },
    startGame() {
      while (this.gameScore.teamOne < 21 && this.gameScore.teamTwo < 21) {
        if (!this.possession) {
          this.getTallest()
        }
        console.log(this.gameScore.teamOne)
        this.gameScore.teamOne++
        console.log(this.gameScore.teamOne)
        

        // console.log(this.gameScore)
      }
    },
    getTallest(){
      const tallestOne = this.teams.teamOne.sort((a,b) => {
        return b.height - a.height
      })
      const tallestTwo = this.teams.teamTwo.sort((a,b) => {
        return b.height - a.height
      })
      console.log(tallestOne[0], tallestTwo[0])
      return tallestOne, tallestTwo
  
    }
  }
};
</script>