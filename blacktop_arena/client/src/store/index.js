import { createStore } from 'vuex';
// import players from '../players';

export default createStore({
  state: {
    id: '',
    players: [],
    teams: []
  },
  mutations: {
    setTeams(state, teams) {
      state.teams = teams;
    },
    setPlayers(state, players) {
      state.players = players;
    },
    setId(state, id) {
      state.id = id;
    }
  },
  actions: {},
  modules: {}
});
