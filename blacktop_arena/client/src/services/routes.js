import Client from './api';

export const GetPlayers = async () => {
  const res = await Client.get('/api/players');
  return res.data;
};

export const CreateTeam = async (team) => {
  const res = await Client.post('/api/team/create', team);
  return res.data;
};

export const GetTeamByNameAndPassword = async ({ team_name, password }) => {
  const res = await Client.get(`/api/team/${team_name}/${password}`);
  return res.data;
};
