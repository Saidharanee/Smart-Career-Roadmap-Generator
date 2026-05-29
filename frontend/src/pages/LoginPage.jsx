// Handles both user registration and login in one page

import { useState } from 'react';
import { loginUser, registerUser } from '../api/api';

function LoginPage({ onLogin }) {
  // Toggle between "login" and "register" mode
  const [mode, setMode] = useState('login');

  // Form field values
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  // Feedback messages for the user
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent page reload on form submit
    setError('');
    setLoading(true);

    try {
      let response;

      if (mode === 'register') {
        // Call register API, then log in automatically
        await registerUser(username, email, password);
        response = await loginUser(username, password);
      } else {
        response = await loginUser(username, password);
      }

      // Pass the token up to App.jsx to complete login
      onLogin(response.data.token, response.data.username);

    } catch (err) {
      // Show error message from the API, or a generic one
      setError(err.response?.data?.error || 'Something went wrong. Try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-page">
      <div className="login-card">
        <h1 className="app-title">Career Roadmap</h1>
        <p className="app-subtitle">Your personalised learning journey</p>

        {/* Tab toggle between Login and Register */}
        <div className="tab-toggle">
          <button
            className={mode === 'login' ? 'active' : ''}
            onClick={() => setMode('login')}
          >
            Login
          </button>
          <button
            className={mode === 'register' ? 'active' : ''}
            onClick={() => setMode('register')}
          >
            Register
          </button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Username</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter your username"
              required
            />
          </div>

          {/* Only show email field during registration */}
          {mode === 'register' && (
            <div className="form-group">
              <label>Email</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="your@email.com"
                required
              />
            </div>
          )}

          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              required
            />
          </div>

          {/* Show error if something went wrong */}
          {error && <p className="error-msg">{error}</p>}

          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? 'Please wait…' : mode === 'login' ? 'Login' : 'Create Account'}
          </button>
        </form>
      </div>
    </div>
  );
}

export default LoginPage;
