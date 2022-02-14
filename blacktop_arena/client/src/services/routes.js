import Client from './api';

export const GetPlayers = async () => {
  const res = await Client.get('/api/players');
  return res.data;
};
export const GetPlayerById = async (id) => {
  const res = await Client.get(`/api/players/${id}`);
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

export const GetSquadByName = async (team_name) => {
  const res = await Client.get(`/api/squad/${team_name}`);
  return res.data;
};
export const GetAllSquads = async () => {
  const res = await Client.get(`/api/squad`);
  return res.data;
};
