import { createStore } from 'vuex';
// import players from '../players';

export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
    players: [],
    teams: []
  },
  mutations: {
    setTeams(state, teams) {
      state.teams = teams;
    },
    setPlayers(state, players) {
      state.players = players;
    }
  },
  actions: {},
  modules: {}
});
