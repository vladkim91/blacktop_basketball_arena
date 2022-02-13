import { createStore } from 'vuex';
// import players from '../players';

export default createStore({
  state: {
    team: {},
    players: [],
    teams: [],
    isLoggedIn: false
  },
  mutations: {
    setTeams(state, teams) {
      state.teams = teams;
    },
    setPlayers(state, players) {
      state.players = players;
    },
    setTeam(state, team) {
      state.team = team;
    },
    setLoggedIn(state, bool) {
      state.isLoggedIn = bool;
    }
  },
  actions: {},
  modules: {}
});
