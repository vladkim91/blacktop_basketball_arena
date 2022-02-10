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
    <button @click="countdown">run</button>
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
      gameLog: [],
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
      this.startGame();
      // let audio = new Audio(require('../assets/whistle.mp3'));
      // setTimeout(() => console.log(3), 2000);
      // setTimeout(() => console.log(2), 3000);
      // setTimeout(() => console.log(1), 4000);
      // setTimeout(() => console.log('GO'), 4500);
      // setTimeout(() => {
      //   // audio.play();
      // }, 4500);
    },
    getPlayerOverall() {},
    startGame() {
      while (this.gameScore.teamOne < 1 && this.gameScore.teamTwo < 1) {
        if (!this.possession) {
          this.jumpBall();
          console.log(this.gameLog);
        }

        let currentPlayer;
        let shotType;
        let matchup;
        if (this.possession === 1) {
          const currentPlayerIndex = this.checkShootPass(this.teams.teamTwo);
          shotType = this.pickTypeOfShot(
            this.teams.teamTwo[currentPlayerIndex]
          );
          currentPlayer = this.teams.teamTwo[currentPlayerIndex];
          matchup = this.teams.teamOne[currentPlayerIndex];
        } else {
          const currentPlayerIndex = this.checkShootPass(this.teams.teamOne);
          shotType = this.pickTypeOfShot(
            this.teams.teamOne[currentPlayerIndex]
          );
          currentPlayer = this.teams.teamOne[currentPlayerIndex];
          matchup = this.teams.teamTwo[currentPlayerIndex];
        }

        // this.shootBall(currentPlayer, 'attack_rim', matchup);
        this.shootBall(currentPlayer, shotType, matchup);

        this.gameScore.teamOne += 2;
      }
    },
    jumpBall() {
      const [playerOne, playerTwo] = this.getTallest();
      const p1v = playerOne.height * playerOne.attributes.physical.vertical;
      const p2v = playerTwo.height * playerTwo.attributes.physical.vertical;
      const percentage = [
        parseFloat((p1v / (p1v + p2v)).toFixed(2)),
        parseFloat((p2v / (p1v + p2v)).toFixed(2))
      ];
      if (parseFloat(Math.random().toFixed(2)) < percentage[0]) {
        this.possession = 0;
        this.gameLog.push(`${playerOne.name} won the tip! `);
      } else {
        this.possession = 1;
        this.gameLog.push(`${playerTwo.name} won the tip! `);
      }
    },

    getTallest() {
      const tallestOne = this.teams.teamOne.sort((a, b) => {
        return b.height - a.height;
      })[0];
      const tallestTwo = this.teams.teamTwo.sort((a, b) => {
        return b.height - a.height;
      })[0];

      return [tallestOne, tallestTwo];
    },

    checkShootPass(team) {
      const currentTeam = team;

      let player1 = 0;
      let player2 = 0;
      let player3 = 0;

      currentTeam.forEach((e, i) => {
        const offensiveTendencies = e.tendencies.offense;
        for (const property in offensiveTendencies) {
          if (i === 0) {
            if (property === 'pass' || property === 'set_screen') continue;

            player1 += parseInt(offensiveTendencies[property]);
          } else if (i === 1) {
            if (property === 'pass' || property === 'set_screen') continue;

            player2 += parseInt(offensiveTendencies[property]);
          } else {
            if (property === 'pass' || property === 'set_screen') continue;

            player3 += parseInt(offensiveTendencies[property]);
          }
        }
      });

      return this.calcShotTendencies(player1, player2, player3);
    },

    calcShotTendencies(p1, p2, p3) {
      const p1ST = parseFloat((p1 / (p1 + p2 + p3)).toFixed(2));
      const p2ST = parseFloat((p2 / (p1 + p2 + p3)).toFixed(2));
      const chance = Math.random().toFixed(2);
      return chance <= p1ST
        ? 0
        : chance > p1ST && chance <= p1ST + p2ST
        ? 1
        : 2;
    },
    pickTypeOfShot(player) {
      let rim = 0;
      let mid = 0;
      let three = 0;
      let post = 0;
      for (const property in player.tendencies.offense) {
        if (property === 'pass' || property === 'set_screen') {
          continue;
        } else if (property == 'attack_rim') {
          rim += player.tendencies.offense[property];
        } else if (property == 'shoot_mid') {
          mid += player.tendencies.offense[property];
        } else if (property == 'shoot_three') {
          three += player.tendencies.offense[property];
        } else {
          post += player.tendencies.offense[property];
        }
      }
      // console.log(rim, mid, three, post);

      return this.calcChanceShotType(rim, mid, three, post);
    },
    calcChanceShotType(shot1, shot2, shot3, shot4) {
      const sum = shot1 + shot2 + shot3 + shot4;
      const rim = parseFloat((shot1 / sum).toFixed(2));
      const mid = parseFloat((shot2 / sum).toFixed(2));
      const three = parseFloat((shot3 / sum).toFixed(2));
      const post = parseFloat((shot4 / sum).toFixed(2));
      const chance = Math.random().toFixed(2);

      if (chance < rim) {
        return 'attack_rim';
      } else if (chance >= rim && chance < rim + mid) {
        return 'shoot_mid';
      } else if (chance >= rim + mid && chance < rim + mid + three) {
        return 'shoot_three';
      } else if (chance >= 1 - post) {
        return 'post_up';
      }
    },
    shootBall(player, type, matchup) {
      const defaultPercentages = [0.45, 0.35, 0.3, 0.4];
      // const chance = Math.random().toFixed(2);

      console.log('current', player.name, type);
      let defensiveTendencies = matchup.tendencies.defense;
      let defensiveAttributes = matchup.attributes.defense;
      let defensivePhysicalAttributes = matchup.attributes.physical;
      // let contested = false;
      let defensiveContest;
      let layupOrDunk = '';
      let percentage;

      switch (type) {
        case 'attack_rim':
          defensiveContest =
            (defensiveTendencies.block +
              defensiveAttributes.inside_defense +
              defensivePhysicalAttributes.vertical +
              defensivePhysicalAttributes.strength) /
            4;
          layupOrDunk += this.layupOrDunk(
            player.attributes.offense.dunk,
            defensiveContest
          );
          percentage = this.calcAttackRim(
            defensiveContest,
            player.attributes.offense[layupOrDunk],
            defaultPercentages[0]
          );
          
          percentage

          break;
        case 'shoot_mid':
          defensiveContest =
            (defensiveTendencies.block +
              defensiveAttributes.outside_defense +
              defensivePhysicalAttributes.vertical) /
            3;
          console.log(defensiveContest);

          break;
        case 'shoot_three':
          defensiveContest =
            (defensiveTendencies.block +
              defensiveAttributes.outside_defense +
              defensivePhysicalAttributes.vertical) /
            3;
          console.log(defensiveContest);

          break;
        case 'post_up':
          defensiveContest =
            (defensiveTendencies.block +
              defensiveAttributes.outside_defense +
              defensiveAttributes.inside_defense +
              defensivePhysicalAttributes.vertical +
              defensivePhysicalAttributes.strength) /
            5;
          console.log(defensiveContest);

          break;
      }
      console.log(type, percentage);

      console.log(
        'matchup',
        matchup.name,
        defensiveTendencies,
        defensiveAttributes,
        defensivePhysicalAttributes
      );
      // if (matchup.tendencies.defense) {
      //   console.log(first)
      // }
    },
    layupOrDunk(dunk, defensiveRating) {
      const dunkPenalty = parseFloat(
        (dunk / (dunk + defensiveRating)).toFixed(2)
      );
      const layupChance = 1 - dunkPenalty + 0.15;
      const chance = Math.random().toFixed(2);

      return chance < layupChance ? 'layup' : 'dunk';
    },
    calcAttackRim(defense, offense, defaultPercentage) {
      console.log(defense, offense, defaultPercentage);
      const multiplier = parseFloat(
        (offense / (defense + offense) / defaultPercentage).toFixed(2)
      );
      return parseFloat((defaultPercentage * multiplier).toFixed(2));
    }
  }
};
</script>