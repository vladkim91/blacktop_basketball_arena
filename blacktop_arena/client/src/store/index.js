import { createStore } from 'vuex';
import players from '../players';

export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
    players: players,
    teams: []
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token');
        state.isAuthenticated = true;
      } else {
        (state.token = ''), (state.isAuthenticated = false);
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = '';
      state.isAuthenticated = false;
    },
    setTeams(state, teams) {
      state.teams = teams;
    }
  },
  actions: {},
  modules: {}
});
