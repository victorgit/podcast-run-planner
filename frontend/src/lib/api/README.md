# API Client Structure

This directory contains the modular API client for communicating with the FastAPI backend.

## Structure

```
api/
├── index.js          # Main entry point - re-exports everything
├── client.js         # Core HTTP client (apiRequest function)
├── auth.js           # Authentication endpoints
├── episodes.js       # Episode-related endpoints
└── playlists.js      # Playlist-related endpoints
```

## Benefits of This Structure

1. **Single Responsibility**: Each file handles one feature area
2. **Parallel Development**: Multiple developers can work on different files without conflicts
3. **Easy to Find**: Know where to look for specific endpoints
4. **Maintainable**: Small, focused files are easier to understand and modify
5. **Scalable**: Easy to add new endpoint modules as the app grows

## Usage

Import from the main entry point (same as before):

```javascript
import { auth, episodes, playlists, healthCheck } from './lib/api';

// Or import specific modules
import { auth } from './lib/api';
import { episodes } from './lib/api';
```

## Adding New Endpoints

### Option 1: Add to existing module (if related)
```javascript
// api/episodes.js
export const episodes = {
  // ... existing methods
  getByPodcast: async (podcastId) => {
    return apiRequest(`/api/episodes/podcast/${podcastId}`);
  },
};
```

### Option 2: Create new module (for new feature)
```javascript
// api/podcasts.js
import { apiRequest } from './client.js';

export const podcasts = {
  getAll: async () => {
    return apiRequest('/api/podcasts');
  },
};
```

Then export from `index.js`:
```javascript
// api/index.js
export { podcasts } from './podcasts.js';
```

## Core Client

The `client.js` file contains the shared `apiRequest` function that all modules use. This ensures:
- Consistent error handling
- Centralized configuration
- Easy to add features (auth headers, logging, etc.)

## Best Practices

1. **One feature per file**: Keep related endpoints together
2. **Use the client**: Always use `apiRequest` from `client.js`, don't use `fetch` directly
3. **Document parameters**: Add JSDoc comments for function parameters
4. **Export from index**: Always export new modules from `index.js` for consistency

