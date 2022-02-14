import { createStore } from 'vuex';
// import players from '../players';

export default createStore({
  state: {
    team: {},
    players: [],
    squads: [],
    legends: [],
    teams: {
      teamOne: [],
      teamTwo: []
    },
    history: []
  },
  mutations: {
    setTeams(state, array) {
      const [player, turn] = array;
      if (turn === 0) {
        state.teams.teamOne.push(player);
      } else {
        state.teams.teamTwo.push(player);
      }
    },
    setPlayers(state, players) {
      state.players = players;
    },
    setTeam(state, team) {
      state.team = team;
    },
    setLoggedIn(state, bool) {
      state.isLoggedIn = bool;
    },
    setSquads(state, squads) {
      state.squads = squads;
    },
    setLegends(state, legends) {
      state.legends = legends;
      if (state.teams.teamTwo.length > 1) {
        state.teams.teamTwo = legends;
      } else {
        state.teams.teamTwo.push(...legends);
      }
    },
    reset(state) {
      state.teams = {
        teamOne: [],
        teamTwo: []
      };
      state.legends = [];
    },
    getHistory(state, history) {
      state.history = history;
    }
  },
  actions: {},
  modules: {}
});
