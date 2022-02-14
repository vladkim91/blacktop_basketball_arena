<template>
  <div class="game-ui">
    <h1>GAME UI</h1>
    <h2>Team One</h2>
    <div
      class="team-2-players"
      v-for="player in teams.teamOne"
      :key="player.id"
    >
      <div class="p1-container">{{ player.name }}</div>
    </div>
    <h2>Team Two</h2>
    <div
      class="team-2-players"
      v-for="player in teams.teamTwo"
      :key="player.id"
    >
      <div class="p2-container">{{ player.name }}</div>
    </div>
    <div class="log">
      <div class="line" v-for="line in gameLog" :key="line.id">
        {{ line }}
      </div>
    </div>
  </div>
</template>

<script>
import { GetTeamById, UpdateTeamById, CreateGame } from '../services/routes.js';
export default {
  mounted() {
    this.countdown();
    // setTimeout(this.startGame(), 5000)
  },
  components: {},
  data() {
    return {
      gameObject: {},
      gameLog: [],
      record: {},
      possession: null,
      gameInProgress: false,
      teamStats: {
        teamOne: {
          points: 0,
          rebounds: 0,
          assists: 0,
          steals: 0,
          blocks: 0,
          turnovers: 0,
          fgm: 0,
          fga: 0,
          threeA: 0,
          threeM: 0
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
          threeA: 0,
          threeM: 0
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
    },
    playerStatTemplate() {
      return this.assignToTeams(this.teams.teamOne, this.teams.teamTwo);
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
      this.gameInProgress = true;
      this.gameCycle();
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
        this.gameLog.unshift(`${playerOne.name} won the tip! `);
      } else {
        this.possession = 1;
        this.gameLog.unshift(`${playerTwo.name} won the tip! `);
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

      const log = (string) => {
        let assistingPlayer;
        let message = '';
        const chance = Math.random().toFixed(2);
        if (type !== 'shoot_three') {
          // TEAM 1
          if (this.possession === 0) {
            assistingPlayer = this.calcAssist(this.teams.teamOne, player);
            if (chance < 0.45) {
              message += `Assisted by ${assistingPlayer.name}. `;
              this.teamStats.teamOne.assists++;
              this.playerStatTemplate.teamOne[`${player.name}`].assists++;
            }
            this.teamStats.teamOne.fga++;
            this.teamStats.teamOne.fgm++;
            this.teamStats.teamOne.points += 2;
            this.playerStatTemplate.teamOne[`${player.name}`].fga++;
            this.playerStatTemplate.teamOne[`${player.name}`].fgm++;
            this.playerStatTemplate.teamOne[`${player.name}`].points += 2;
            this.gameScore.teamOne += 2;
            this.possession++;
            this.gameLog.unshift(
              string[Math.floor(Math.random() * string.length)] +
                `${message}` +
                `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
            );
          } else {
            // TEAM 2
            assistingPlayer = this.calcAssist(this.teams.teamTwo, player);
            if (chance < 0.45) {
              message += `Assisted by ${assistingPlayer.name}. `;
              this.teamStats.teamTwo.assists++;
              this.playerStatTemplate.teamTwo[`${player.name}`].assists++;
            }
            this.teamStats.teamTwo.fga++;
            this.teamStats.teamTwo.fgm++;
            this.teamStats.teamTwo.points += 2;
            this.playerStatTemplate.teamTwo[`${player.name}`].fga++;
            this.playerStatTemplate.teamTwo[`${player.name}`].fgm++;
            this.playerStatTemplate.teamTwo[`${player.name}`].points += 2;
            this.gameScore.teamTwo += 2;
            this.possession--;
            this.gameLog.unshift(
              string[Math.floor(Math.random() * string.length)] +
                `${message}` +
                `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
            );
          }
        } else {
          // TEAM 1
          if (this.possession === 0) {
            assistingPlayer = this.calcAssist(this.teams.teamOne, player);
            if (chance < 0.3) {
              message += `Assisted by ${assistingPlayer.name}. `;
              this.teamStats.teamOne.assists++;
              this.playerStatTemplate.teamOne[`${player.name}`].assists++;
            }
            this.teamStats.teamOne.fga++;
            this.teamStats.teamOne.fgm++;
            this.teamStats.teamOne.points += 3;
            this.teamStats.teamOne.threeA++;
            this.teamStats.teamOne.threeM++;
            this.playerStatTemplate.teamOne[`${player.name}`].fga++;
            this.playerStatTemplate.teamOne[`${player.name}`].fgm++;
            this.playerStatTemplate.teamOne[`${player.name}`].points += 3;
            this.playerStatTemplate.teamOne[`${player.name}`].threeA++;
            this.playerStatTemplate.teamOne[`${player.name}`].threeM++;

            this.gameScore.teamOne += 3;
            this.possession++;
            this.gameLog.unshift(
              string[Math.floor(Math.random() * string.length)] +
                `${message}` +
                `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
            );
          } else {
            // TEAM 2
            assistingPlayer = this.calcAssist(this.teams.teamTwo, player);
            if (chance < 0.3) {
              message += `Assisted by ${assistingPlayer.name}. `;
              this.teamStats.teamTwo.assists++;
              this.playerStatTemplate.teamTwo[`${player.name}`].assists++;
            }
            this.teamStats.teamTwo.fga++;
            this.teamStats.teamTwo.fgm++;
            this.teamStats.teamTwo.points += 3;
            this.teamStats.teamTwo.threeA++;
            this.teamStats.teamTwo.threeM++;
            this.playerStatTemplate.teamTwo[`${player.name}`].fga++;
            this.playerStatTemplate.teamTwo[`${player.name}`].fgm++;
            this.playerStatTemplate.teamTwo[`${player.name}`].points += 3;
            this.playerStatTemplate.teamTwo[`${player.name}`].threeA++;
            this.playerStatTemplate.teamTwo[`${player.name}`].threeM++;
            this.gameScore.teamTwo += 3;
            this.possession--;
            this.gameLog.unshift(
              string[Math.floor(Math.random() * string.length)] +
                `${message}` +
                `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
            );
          }
        }
      };
      const logMiss = (string, type) => {
        // TEAM 1
        if (this.possession === 0) {
          if (type === '3') {
            this.teamStats.teamOne.threeA++;
            this.teamStats.teamOne.fga++;
            this.playerStatTemplate.teamOne[`${player.name}`].threeA++;
            this.playerStatTemplate.teamOne[`${player.name}`].fga++;
          } else {
            this.playerStatTemplate.teamOne[`${player.name}`].fga++;
            this.teamStats.teamOne.fga++;
          }
          this.gameLog.unshift(
            string[Math.floor(Math.random() * string.length)] +
              `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
          );
        } else {
          if (type === '3') {
            this.teamStats.teamTwo.threeA++;
            this.teamStats.teamTwo.fga++;
            this.playerStatTemplate.teamTwo[`${player.name}`].threeA++;
            this.playerStatTemplate.teamTwo[`${player.name}`].fga++;
          } else {
            this.playerStatTemplate.teamTwo[`${player.name}`].fga++;
            this.teamStats.teamTwo.fga++;
          }
          this.gameLog.unshift(
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
            if (chance > 0.3) {
              messageVariation.unshift(
                ...[
                  `${player.name} missed an acrobatic layup. `,
                  `${player.name}'s finger roll layup is short. `,
                  `${player.name}'s shot at the rim was contested by ${matchup.name}. ${player.name} missed the shot. `
                ]
              );
              logMiss(messageVariation);
            } else {
              if (this.possession === 0) {
                this.playerStatTemplate.teamTwo[`${matchup.name}`].blocks++;
                this.teamStats.teamTwo.blocks++;
              } else {
                this.playerStatTemplate.teamOne[`${matchup.name}`].blocks++;
                this.teamStats.teamOne.blocks++;
              }

              messageVariation.unshift(
                ...[
                  `${player.name}'s layup attempted was sent to the bleachers by ${matchup.name} `,
                  `${player.name} was blocked by ${matchup.name} `
                ]
              );
              logMiss(messageVariation);
            }
          } else if (layupDunk === 'dunk') {
            if (chance > 0.15) {
              messageVariation.unshift(
                ...[
                  `${player.name}'s dunk attempt was unsuccessful. `,
                  `${player.name} attempts a dunk in traffic. ${matchup.name}'s contest is too perfect. `,
                  `${player.name} think he has an open lane for a slam, but ${matchup.name} is there to contest. ${player.name} misses the dunk attempt. `
                ]
              );
              logMiss(messageVariation);
            } else {
              if (this.possession === 0) {
                this.playerStatTemplate.teamTwo[`${matchup.name}`].blocks++;
                this.teamStats.teamTwo.blocks++;
              } else {
                this.playerStatTemplate.teamOne[`${matchup.name}`].blocks++;
                this.teamStats.teamOne.blocks++;
              }

              messageVariation.unshift(
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
          logMiss(messageVariation, '3');
        } else if (type === 'post_up') {
          const chance = Math.random().toFixed(2);
          const messageVariation = [];
          if (chance > 0.2) {
            messageVariation.unshift(
              ...[
                `${player.name} misses a jump hook. `,
                `${player.name} attempts a skyhook and misses. `,
                `${matchup.name} nearly blocks ${player.name}'s post fadeaway. Shot bounces off the rim. `
              ]
            );
            logMiss(messageVariation);
          } else {
            if (this.possession === 0) {
              this.playerStatTemplate.teamTwo[`${matchup.name}`].blocks++;
              this.teamStats.teamTwo.blocks++;
            } else {
              this.playerStatTemplate.teamOne[`${matchup.name}`].blocks++;
              this.teamStats.teamOne.blocks++;
            }
            //
            messageVariation.unshift(
              ...[
                `${matchup.name} stuffs ${player.name}'s jump hook. `,
                `${matchup.name} sends ${player.name}'s weak layup under the rim the stands. `,
                `${player.name} is blocked at the rim by ${matchup.name}. `
              ]
            );
            logMiss(messageVariation);
          }
        }
        this.rebound(this.teams.teamOne, this.teams.teamTwo);
      }
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
    },
    rebound(team1, team2) {
      // Team 1
      const calcRebound = (team) => {
        let def = 0;
        let off = 0;
        team.forEach((e) => {
          def += e.attributes.defense.def_rebound;
          off += e.attributes.offense.off_rebound;
        });
        let teamDefRebound = parseFloat((def / 300).toFixed(2));
        let teamOffRebound = parseFloat((off / 300).toFixed(2));
        return [teamDefRebound, teamOffRebound];
      };

      const [t1DefRebound, t1OffRebound] = calcRebound(team1);
      const [t2DefRebound, t2OffRebound] = calcRebound(team2);

      const chance = Math.random().toFixed(2);
      if (this.possession === 0) {
        const offReboundChance = parseFloat(
          (t1OffRebound / (t1OffRebound + t2DefRebound) - 0.25).toFixed(2)
        );
        let rebounder;
        if (chance > offReboundChance) {
          rebounder = this.calcRebounder(team2);
          this.playerStatTemplate.teamTwo[`${rebounder.name}`].rebounds++;
          this.teamStats.teamTwo.rebounds++;
          const messageVariation = [
            `${rebounder.name} grabs defensive rebound. `,
            `${rebounder.name} boxes out offensive players and succesfully grabs the rebound. `,
            `${rebounder.name} snatches devensive rebound. `
          ];
          this.possession++;
          this.logRebounds(messageVariation);
        } else {
          rebounder = rebounder = this.calcRebounder(team1);
          this.playerStatTemplate.teamOne[`${rebounder.name}`].rebounds++;
          this.teamStats.teamOne.rebounds++;
          const messageVariation = [
            `${rebounder.name} uses his strengh to grab offensive rebound. `,
            `${rebounder.name} outhustles opposing to team and get offensive board. `
          ];
          this.logRebounds(messageVariation);
        }
      } else {
        const offReboundChance = parseFloat(
          (t2OffRebound / (t2OffRebound + t1DefRebound) - 0.25).toFixed(2)
        );
        let rebounder;
        if (chance > offReboundChance) {
          rebounder = this.calcRebounder(team1);
          this.playerStatTemplate.teamOne[`${rebounder.name}`].rebounds++;
          this.teamStats.teamOne.rebounds++;
          const messageVariation = [
            `${rebounder.name} grabs defensive rebound. `,
            `${rebounder.name} boxes out offensive players and succesfully grabs the rebound. `,
            `${rebounder.name} snatches devensive rebound. `
          ];
          this.possession--;
          this.logRebounds(messageVariation);
        } else {
          rebounder = this.calcRebounder(team2);
          this.playerStatTemplate.teamTwo[`${rebounder.name}`].rebounds++;
          this.teamStats.teamTwo.rebounds++;
          const messageVariation = [
            `${rebounder.name} uses his strengh to grab offensive rebound. `,
            `${rebounder.name} outhustles opposing to team and get offensive board. `
          ];
          this.logRebounds(messageVariation);
        }
      }
    },
    calcRebounder(team) {
      let rebounder;
      let player1 = 0,
        player2 = 0,
        player3 = 0;
      team.forEach((e, i) => {
        if (i === 0) {
          player1 += e.attributes.defense.def_rebound;
          player1 += e.attributes.offense.off_rebound;
        } else if (i === 1) {
          player2 += e.attributes.defense.def_rebound;
          player2 += e.attributes.offense.off_rebound;
        } else {
          player3 += e.attributes.defense.def_rebound;
          player3 += e.attributes.offense.off_rebound;
        }
      });
      const p1Chance = parseFloat(
        (player1 / (player1 + player2 + player3)).toFixed(2)
      );
      const p2Chance = parseFloat(
        (player2 / (player1 + player2 + player3)).toFixed(2)
      );

      const chance = Math.random().toFixed(2);

      if (chance < p1Chance) {
        rebounder = team[0];
      } else if (chance > p1Chance && chance < p1Chance + p2Chance) {
        rebounder = team[1];
      } else {
        rebounder = team[2];
      }

      return rebounder;
    },
    logRebounds(string) {
      this.gameLog.unshift(
        string[Math.floor(Math.random() * string.length)] +
          `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
      );
    },
    calcSteal(offTeam, defTeam) {
      const chance = Math.random().toFixed(2);
      const teamPassingIq = this.calcPassing(offTeam);
      const teamPerimeterDefense = this.calcPerimeterDefense(defTeam);
      const stealChance = parseFloat(
        (
          teamPerimeterDefense / (teamPassingIq + teamPerimeterDefense) -
          0.4
        ).toFixed(2)
      );

      if (chance > stealChance) {
        return false;
      } else {
        return true;
      }
    },
    calcPassing(team) {
      let teamPassing = 0;
      team.forEach((e) => {
        teamPassing +=
          (e.attributes.offense.handles + e.attributes.offense.pass) / 6;
      });

      return parseFloat(teamPassing.toFixed(2));
    },
    calcPerimeterDefense(team) {
      let teamDefense = 0;
      team.forEach((e) => {
        teamDefense +=
          (e.attributes.defense.outside_defense +
            e.attributes.defense.steal +
            e.tendencies.defense.steal +
            e.tendencies.defense.intercept) /
          12;
      });
      return parseFloat(teamDefense.toFixed(2));
    },
    logSteal(stealPlayer, turnoverPlayer) {
      const messageVariation = [
        `${stealPlayer.name} stole the ball from ${turnoverPlayer.name}. `,
        `${stealPlayer.name} intercepts a sloppy entry pass by ${turnoverPlayer.name}. `,
        `${turnoverPlayer.name} with a turnover. ${stealPlayer.name} with a steal. `
      ];
      this.gameLog.unshift(
        messageVariation[Math.floor(Math.random() * messageVariation.length)] +
          `${this.gameScore.teamOne}:${this.gameScore.teamTwo}`
      );
    },
    calcAssist(team, player) {
      let player1 = 0,
        player2 = 0;

      const excludePlayer = team.filter((e) => {
        if (e.name !== player.name) {
          return e;
        }
      });
      excludePlayer.forEach((e, i) => {
        if (i === 0) {
          player1 += e.attributes.offense.handles;
          player1 += e.attributes.offense.pass;
          player1 += e.tendencies.offense.pass;
        } else {
          player2 += e.attributes.offense.handles;
          player2 += e.attributes.offense.pass;
          player2 += e.tendencies.offense.pass;
        }
      });

      const chance = Math.random().toFixed(2);
      const p1AssistChance = player1 / (player1 + player2);

      if (chance < p1AssistChance) {
        return excludePlayer[0];
      } else {
        return excludePlayer[1];
      }
    },

    assignToTeams(team1, team2) {
      let teamOne = {};
      let teamTwo = {};
      team1.forEach((e) => {
        teamOne[`${e.name}`] = {
          points: 0,
          rebounds: 0,
          assists: 0,
          steals: 0,
          blocks: 0,
          turnovers: 0,
          fgm: 0,
          fga: 0,
          threeA: 0,
          threeM: 0
        };
      });
      team2.forEach((e) => {
        teamTwo[`${e.name}`] = {
          points: 0,
          rebounds: 0,
          assists: 0,
          steals: 0,
          blocks: 0,
          turnovers: 0,
          fgm: 0,
          fga: 0,
          threeA: 0,
          threeM: 0
        };
      });
      return { teamOne, teamTwo };
    },
    gameCycle() {
      if (this.possession === null) {
        this.jumpBall();
      }

      let currentPlayer;
      let shotType;
      let matchup;
      let steal;
      if (this.possession === 1) {
        const currentPlayerIndex = this.checkShootPass(this.teams.teamTwo);
        shotType = this.pickTypeOfShot(this.teams.teamTwo[currentPlayerIndex]);
        currentPlayer = this.teams.teamTwo[currentPlayerIndex];
        matchup = this.teams.teamOne[currentPlayerIndex];
        steal = this.calcSteal(this.teams.teamTwo, this.teams.teamOne);
        if (steal === true) {
          this.logSteal(currentPlayer, matchup);
          this.playerStatTemplate.teamTwo[`${currentPlayer.name}`].steals++;
          this.teamStats.teamTwo.steals++;
          this.playerStatTemplate.teamOne[`${matchup.name}`].turnovers++;
          this.teamStats.teamOne.turnovers++;
        }
      } else {
        const currentPlayerIndex = this.checkShootPass(this.teams.teamOne);
        shotType = this.pickTypeOfShot(this.teams.teamOne[currentPlayerIndex]);
        currentPlayer = this.teams.teamOne[currentPlayerIndex];
        matchup = this.teams.teamTwo[currentPlayerIndex];
        steal = this.calcSteal(this.teams.teamOne, this.teams.teamTwo);
        if (steal === true) {
          this.logSteal(currentPlayer, matchup);
          this.playerStatTemplate.teamOne[`${currentPlayer.name}`].steals++;
          this.teamStats.teamOne.steals++;
          this.playerStatTemplate.teamTwo[`${matchup.name}`].turnovers++;
          this.teamStats.teamTwo.turnovers++;
        }
      }

      this.shootBall(currentPlayer, shotType, matchup);
      if (this.gameScore.teamOne < 21 && this.gameScore.teamTwo < 21) {
        setTimeout(this.gameCycle, 0);

        return;
      }
      this.gameInProgress = false;
      this.getTeamById(JSON.parse(localStorage.getItem('team_name')).id);
      this.createGame(this.createGameObject());
      // console.log()
    },
    async updateTeamById(id, body) {
      const res = await UpdateTeamById(id, body);

      return res;
    },
    async getTeamById(id) {
      const res = await GetTeamById(id);
      this.record = {
        wins: res.wins,
        losses: res.losses
      };
      if (this.gameScore.teamOne >= 21) {
        this.record.wins++;
        this.updateTeamById(id, this.record);
      } else {
        this.record.losses++;
        this.updateTeamById(id, this.record);
      }
    },
    async createGame(obj) {
      const res = await CreateGame(obj);
      return res;
    },
    createGameObject() {
      const obj = {
        name: 'game_name',
        team_one_stats: this.teamStats.teamOne,
        team_two_stats: this.teamStats.teamTwo,
        team_one_player_stats: this.playerStatTemplate.teamOne,
        team_two_player_stats: this.playerStatTemplate.teamTwo,
        team_one_score: this.gameScore.teamOne,
        team_two_score: this.gameScore.teamTwo,
        team_one_squad: this.teams.teamOne,
        team_two_squad: this.teams.teamTwo,
        date: new Date().toLocaleDateString('en-CA')
      };
      return obj;
    }
  }
};
</script>
