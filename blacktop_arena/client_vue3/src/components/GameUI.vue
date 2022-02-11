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
    <div class="log">
      <div class="line" v-for="line in gameLog" :key="line.id">{{ line }}</div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.countdown();
    // setTimeout(this.startGame(), 5000)
  },
  components: {},
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
      console.log(this.gameLog);
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
      while (this.gameScore.teamOne < 21 && this.gameScore.teamTwo < 21) {
        if (this.possession === null) {
          this.jumpBall();
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

        this.shootBall(currentPlayer, shotType, matchup);
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

      let defensiveTendencies = matchup.tendencies.defense;
      let defensiveAttributes = matchup.attributes.defense;
      let defensivePhysicalAttributes = matchup.attributes.physical;
      // let contested = false;
      let defensiveContest;
      let layupDunk = '';
      let percentage;

      switch (type) {
        case 'attack_rim':
          defensiveContest =
            (defensiveTendencies.block +
              defensiveAttributes.inside_defense +
              defensivePhysicalAttributes.vertical +
              defensivePhysicalAttributes.strength) /
            4;
          layupDunk += this.layupOrDunk(
            player.attributes.offense.dunk,
            defensiveContest
          );

          //

          percentage = this.calcAttackRim(
            defensiveContest,
            player.attributes.offense[layupDunk],
            defaultPercentages[0]
          );
          percentage;

          break;
        case 'shoot_mid':
          defensiveContest =
            (defensiveTendencies.block +
              defensiveAttributes.outside_defense +
              defensivePhysicalAttributes.vertical) /
            3;
          percentage = this.calcShotPercentage(
            defensiveContest,
            player.attributes.offense['mid_range'],
            defaultPercentages[1]
          );
          percentage;
          //
          break;
        case 'shoot_three':
          defensiveContest =
            (defensiveTendencies.block +
              defensiveAttributes.outside_defense +
              defensivePhysicalAttributes.vertical) /
            3;
          percentage = this.calcShotPercentage(
            defensiveContest,
            player.attributes.offense['three'],
            defaultPercentages[2]
          );
          percentage;
          break;
        case 'post_up':
          defensiveContest =
            (defensiveTendencies.block +
              defensiveAttributes.post_defense +
              defensiveAttributes.inside_defense +
              defensivePhysicalAttributes.vertical +
              defensivePhysicalAttributes.strength) /
            5;
          percentage = this.calcAttackRim(
            defensiveContest,
            player.attributes.offense['post_shot'],
            defaultPercentages[3]
          );
          percentage;
          break;
      }
      const makeOrMiss = this.shoot(percentage);
      // MAKES

      const log = (string) => {
        if (type !== 'shoot_three') {
          // TEAM 1
          if (this.possession === 0) {
            this.gameScore.teamOne += 2;
            this.possession++;
            this.gameLog.push(
              string[Math.floor(Math.random() * string.length)] +
                `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
            );
          } else {
            // TEAM 2
            this.gameScore.teamTwo += 2;
            this.possession--;
            this.gameLog.push(
              string[Math.floor(Math.random() * string.length)] +
                `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
            );
          }
        } else {
          // TEAM 1
          if (this.possession === 0) {
            this.gameScore.teamOne += 3;
            this.possession++;
            this.gameLog.push(
              string[Math.floor(Math.random() * string.length)] +
                `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
            );
          } else {
            // TEAM 2
            this.gameScore.teamTwo += 3;
            this.possession--;
            this.gameLog.push(
              string[Math.floor(Math.random() * string.length)] +
                `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
            );
          }
        }
      };
      const logMiss = (string) => {
        // TEAM 1
        if (this.possession === 0) {
          this.gameLog.push(
            string[Math.floor(Math.random() * string.length)] +
              `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
          );
        } else {
          this.gameLog.push(
            string[Math.floor(Math.random() * string.length)] +
              `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
          );
        }
      };
      if (makeOrMiss === 'make') {
        // MAKE LAYUP & DUNK
        if (type === 'attack_rim') {
          const messageVariation = [
            `${player.name} drove to the rim and finished strong with a ${
              layupDunk === 'layup' ? 'layup' : 'dunk'
            }. `,
            `${player.name} scores with a ${
              layupDunk === 'layup' ? 'layup' : 'dunk'
            } at the rim. `,
            `${player.name} drives baseline and scores 2 with a reverse ${
              layupDunk === 'layup' ? 'layup' : 'dunk'
            }. `
          ];
          log(messageVariation);
        } else if (type === 'shoot_mid') {
          // MAKE MID
          const messageVariation = [
            `${player.name} hits a pull up midrange jumper from ${Math.floor(
              Math.random() * (19 - 10) + 10
            )} feet. `,
            `${player.name} nails a contested midrange jumper. `,
            `${player.name} with a leaning fadeaway. `
          ];
          log(messageVariation);
        } else if (type === 'shoot_three') {
          // MAKE THREE
          const messageVariation = [
            `${player.name} hits a spot up corner 3 pointer. `,
            `${matchup.name}'s defensive effort is not enough! ${player.name} makes a heavely contested 3 from deep. `,
            `${player.name} drains a three pointer from downtown. `
          ];
          log(messageVariation);
        } else if (type === 'post_up') {
          const messageVariation = [
            `${player.name} makes a jump hook over ${matchup.name}. `,
            `${player.name} hits an wrong shoulder fadeway in ${matchup.name}'s face. `,
            `${player.name} used drop step to get a easy bucket under the rim `
          ];
          log(messageVariation);
        }

        // MISSES
      } else {
        if (type === 'attack_rim') {
          const messageVariation = [];
          const chance = Math.random().toFixed(2);
          if (layupDunk === 'layup') {
            //
            if (chance > 0.3) {
              messageVariation.push(
                ...[
                  `${player.name} missed an acrobatic layup. `,
                  `${player.name}'s finger roll layup is short. `,
                  `${player.name}'s shot at the rim was contested by ${matchup.name}. ${player.name} missed the shot. `
                ]
              );
              logMiss(messageVariation);
            } else {
              messageVariation.push(
                ...[
                  `${player.name}'s layup attempted was sent to the bleachers by ${matchup.name} `,
                  `${player.name} was blocked by ${matchup.name} `
                ]
              );
              logMiss(messageVariation);
            }
          } else if (layupDunk === 'dunk') {
            if (chance > 0.15) {
              messageVariation.push(
                ...[
                  `${player.name}'s dunk attempt was unsuccessful. `,
                  `${player.name} attempts a dunk in traffic. ${matchup.name}'s contest is too perfect. `,
                  `${player.name} think he has an open lane for a slam, but ${matchup.name} is there to contest. ${player.name} misses the dunk attempt. `
                ]
              );
              logMiss(messageVariation);
            } else {
              messageVariation.push(
                ...[
                  `${player.name} get's stuffed at the rim by ${matchup.name}. `,
                  `${player.name} is blocked at the rim by ${matchup.name}. `
                ]
              );
              logMiss(messageVariation);
            }
            //
          }
        } else if (type === 'shoot_mid') {
          const messageVariation = [
            `${player.name} misses elbow jumper. `,
            `${player.name} was contested by ${matchup.name} and missed a midrange jumper. `,
            `${player.name} misses a contested midrange pullup. `
          ];
          logMiss(messageVariation);
        } else if (type === 'shoot_three') {
          const messageVariation = [
            `${player.name} misses a wide open three. `,
            `${matchup.name} contested ${player.name}'s 3 point shot. ${player.name} misses. `,
            `${player.name} airballs a logo 3. `
          ];
          logMiss(messageVariation);
        } else if (type === 'post_up') {
          const chance = Math.random().toFixed(2);
          const messageVariation = [];
          if (chance > 0.2) {
            messageVariation.push(
              ...[
                `${player.name} misses a jump hook. `,
                `${player.name} attempts a skyhook and misses. `,
                `${matchup.name} nearly blocks ${player.name}'s post fadeaway. Shot bounces off the rim`
              ]
            );
            logMiss(messageVariation);
          } else {
            messageVariation.push(
              ...[
                `${matchup.name} stuffs ${player.name}'s jump hook. `,
                `${matchup.name} sends ${player.name}'s weak layup under the rim the stands`,
                `${player.name} is blocked at the rim by ${matchup.block}`
              ]
            );
            logMiss(messageVariation);
          }
        }
      }

      // console.log(name, makeOrMiss)
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
      const multiplier =
        parseFloat(
          (offense / (defense + offense) / defaultPercentage).toFixed(2)
        ) - 0.1;

      return parseFloat((defaultPercentage * multiplier).toFixed(2));
    },
    calcShotPercentage(defense, offense, defaultPercentage) {
      const multiplier =
        parseFloat(
          (offense / (defense + offense) / defaultPercentage).toFixed(2)
        ) - 0.1;
      return parseFloat((defaultPercentage * multiplier).toFixed(2));
    },
    shoot(percentage) {
      const chance = Math.random().toFixed(2);
      if (chance < percentage) {
        return 'make';
      } else if (chance > percentage) {
        return 'miss';
      }
    }
  }
};
</script>
