/**
 * Playlist API endpoints.
 * Handles playlist generation and saving to Spotify.
 */

import { apiRequest } from './client.js';

/**
 * Playlist API methods.
 */
export const playlists = {
  /**
   * Generate a playlist based on run parameters.
   * 
   * @param {object} params - Playlist generation parameters
   * @param {number} params.duration_minutes - Target duration in minutes
   * @param {string} params.run_type - Run type: 'easy' | 'tempo' | 'long'
   * @param {string} params.content_preference - Content preference: 'light' | 'mixed' | 'deep'
   * @returns {Promise<any>} Generated playlist object
   */
  generate: async (params) => {
    return apiRequest('/api/playlists/generate', {
      method: 'POST',
      body: JSON.stringify(params),
    });
  },
  
  /**
   * Save generated playlist to Spotify.
   * 
   * @param {object} playlistData - Playlist data
   * @param {string} playlistData.playlist_name - Name for the playlist
   * @param {string[]} playlistData.episode_ids - Array of episode IDs to include
   * @returns {Promise<any>} Saved playlist object with Spotify URL
   */
  save: async (playlistData) => {
    return apiRequest('/api/playlists/save', {
      method: 'POST',
      body: JSON.stringify(playlistData),
    });
  },
};

