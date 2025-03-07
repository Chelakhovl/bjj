import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const register = (userData) => axios.post(`${API_URL}/auth/register`, userData);

export const login = (userData) => axios.post(`${API_URL}/auth/login`, userData);

export const getProfile = (token) =>
  axios.get(`${API_URL}/auth/profile`, {
    headers: { Authorization: `Bearer ${token}` },
  });
