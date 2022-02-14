import { createStore } from 'vuex';
// import players from '../players';

export default createStore({
  state: {
    team: {},
    players: [],
    teams: [],
    squads: []
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
    },
    setSquads(state, squads) {
      state.squads = squads;
    }
  },
  actions: {},
  modules: {}
});
