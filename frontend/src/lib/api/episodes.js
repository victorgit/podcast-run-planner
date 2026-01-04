/**
 * Episode API endpoints.
 * Handles fetching user's episodes and episode details.
 */

import { apiRequest } from './client.js';

/**
 * Episode API methods.
 */
export const episodes = {
  /**
   * Get all user's saved episodes and followed podcasts.
   * 
   * @param {number} limit - Number of episodes to return (default: 50)
   * @param {number} offset - Pagination offset (default: 0)
   * @returns {Promise<any>} List of episodes
   */
  getAll: async (limit = 50, offset = 0) => {
    return apiRequest(`/api/episodes?limit=${limit}&offset=${offset}`);
  },
  
  /**
   * Get episode details by ID.
   * 
   * @param {string} episodeId - Episode ID
   * @returns {Promise<any>} Episode object
   */
  getById: async (episodeId) => {
    return apiRequest(`/api/episodes/${episodeId}`);
  },
};

