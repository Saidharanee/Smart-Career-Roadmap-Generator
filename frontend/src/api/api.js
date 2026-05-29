// Central file for all API calls to the Django backend
// Using Axios: it's simpler than Fetch and handles JSON automatically

import axios from 'axios';

// Base URL of the Django backend
const BASE_URL = 'http://127.0.0.1:8000/api';

// Create an Axios instance with the base URL set
const api = axios.create({
  baseURL: BASE_URL,
});

// Automatically attach the auth token to every request
// This runs before every API call
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token'); // Get token stored on login
  if (token) {
    config.headers.Authorization = `Token ${token}`; // Django expects "Token <key>"
  }
  return config;
});

// ─── Auth API ────────────────────────────────────────────────────────────────

// Register a new user
export const registerUser = (username, email, password) =>
  api.post('/users/register/', { username, email, password });

// Login and receive a token
export const loginUser = (username, password) =>
  api.post('/users/login/', { username, password });

// Get the current user's profile
export const getProfile = () =>
  api.get('/users/profile/');

// Update profile (career goal, skills)
export const updateProfile = (data) =>
  api.put('/users/profile/', data);

// ─── Roadmap API ─────────────────────────────────────────────────────────────

// Generate a new roadmap based on goal and skills
export const generateRoadmap = (career_goal, skills) =>
  api.post('/roadmap/generate/', { career_goal, skills });

// Get all roadmaps saved by the logged-in user
export const getRoadmaps = () =>
  api.get('/roadmap/list/');

// Get a specific roadmap by ID
export const getRoadmap = (id) =>
  api.get(`/roadmap/${id}/`);

// Delete a roadmap
export const deleteRoadmap = (id) =>
  api.delete(`/roadmap/${id}/`);

// Mark a topic as complete or incomplete
export const markTopic = (roadmap_id, topic_name, is_completed) =>
  api.post('/roadmap/mark-topic/', { roadmap_id, topic_name, is_completed });

export default api;
