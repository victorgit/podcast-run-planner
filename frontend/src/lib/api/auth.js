/**
 * Authentication API endpoints.
 * Handles login, logout, and user information.
 */

import { apiRequest, getApiBaseUrl } from './client.js';

/**
 * Authentication API methods.
 */
export const auth = {
  /**
   * Redirects to backend login endpoint (Spotify OAuth).
   */
  login: () => {
    window.location.href = `${getApiBaseUrl()}/api/auth/login`;
  },
  
  /**
   * Logout current user.
   * @returns {Promise<any>}
   */
  logout: async () => {
    return apiRequest('/api/auth/logout', { method: 'GET' });
  },
  
  /**
   * Get current authenticated user information.
   * @returns {Promise<any>} User object
   */
  getCurrentUser: async () => {
    return apiRequest('/api/auth/me');
  },
};

