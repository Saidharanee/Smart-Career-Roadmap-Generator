// This is the starting point — it connects React to the HTML page

import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';
import App from './App';

// Find the <div id="root"> in public/index.html and render the app inside it
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
