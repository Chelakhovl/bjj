import { useState } from 'react';
import { login, getProfile } from './api';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [user, setUser] = useState(null);

  const handleLogin = async () => {
    try {
      const { data } = await login({ email, password });
      localStorage.setItem('token', data.access_token);
      const profile = await getProfile(data.access_token);
      setUser(profile.data);
    } catch (error) {
      console.error('Login error:', error.response?.data);
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>

      {user && (
        <div>
          <h3>Profile</h3>
          <p>Username: {user.username}</p>
          <p>Email: {user.email}</p>
        </div>
      )}
    </div>
  );
};

export default Login;
