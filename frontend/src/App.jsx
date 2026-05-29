// Root component — handles which page to show based on login state

import { useState, useEffect } from 'react';
import LoginPage from './pages/LoginPage';
import DashboardPage from './pages/DashboardPage';
import './App.css';

function App() {
  // Track if the user is logged in
  // We check localStorage to keep them logged in after page refresh
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Check if a token exists in localStorage on first load
    const token = localStorage.getItem('token');
    if (token) setIsLoggedIn(true);
  }, []);

  // Called when user logs in successfully
  const handleLogin = (token, username) => {
    localStorage.setItem('token', token);       // Save token
    localStorage.setItem('username', username); // Save username
    setIsLoggedIn(true);
  };

  // Called when user clicks logout
  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    setIsLoggedIn(false);
  };

  // Show login page if not logged in, otherwise show dashboard
  return (
    <div className="app-wrapper">
      {isLoggedIn
        ? <DashboardPage onLogout={handleLogout} />
        : <LoginPage onLogin={handleLogin} />
      }
    </div>
  );
}

export default App;
