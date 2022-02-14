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

export const UpdateTeamById = async (id, body) => {
  const res = await Client.patch(`/api/team/update/${id}`, body);
  return res.data;
};

export const GetTeamById = async (id) => {
  const res = await Client.get(`/api/team/${id}`);
  return res.data;
};

export const CreateGame = async (obj) => {
  const res = await Client.post(`/api/games/`, obj);
  return res.data;
};

export const GetHistory = async () => {
  const res = await Client.get(`/api/games/`);
  return res.data;
};
