import Client from './api';

export const GetPlayers = async (players) => {
  const res = await Client.get('/api/players', players);
  return res.data;
};
