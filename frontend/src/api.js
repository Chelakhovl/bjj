import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export const register = (userData) => axios.post(`${API_URL}/register`, userData);

export const login = (userData) => axios.post(`${API_URL}/login`, userData);

export const getProfile = (token) =>
  axios.get(`${API_URL}/profile`, {
    headers: { Authorization: `Bearer ${token}` },
  });
