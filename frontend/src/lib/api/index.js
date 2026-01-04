/**
 * API client - main entry point.
 * 
 * This file re-exports all API modules, providing a single import point
 * while keeping the code organized in separate files.
 * 
 * Usage:
 *   import { auth, episodes, playlists, healthCheck } from './lib/api';
 */

import { apiRequest } from './client.js';
import { auth } from './auth.js';
import { episodes } from './episodes.js';
import { playlists } from './playlists.js';

/**
 * Health check endpoint.
 * @returns {Promise<any>}
 */
export async function healthCheck() {
  return apiRequest('/health');
}

// Re-export all API modules
export { auth, episodes, playlists };

// Re-export client for advanced usage
export { apiRequest } from './client.js';

