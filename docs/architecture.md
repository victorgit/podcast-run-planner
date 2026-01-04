# Podcast Run Planner – Architecture Document

**Version:** 1.0  
**Last Updated:** 2024  
**Tech Stack:** Python, FastAPI, React (frontend)

---

## System Overview

The Podcast Run Planner is a web application that helps runners create Spotify playlists tailored to their run duration and preferences.

```
┌─────────────┐
│   Browser   │
│  (React)    │
└──────┬──────┘
       │ HTTP/REST
       │
┌──────▼──────────────────┐
│   FastAPI Backend       │
│  ┌──────────────────┐  │
│  │  API Routes      │  │
│  │  - Auth          │  │
│  │  - Playlists     │  │
│  │  - Episodes      │  │
│  └──────────────────┘  │
│  ┌──────────────────┐  │
│  │  Business Logic  │  │
│  │  - Playlist Gen  │  │
│  │  - Content Class │  │
│  └──────────────────┘  │
│  ┌──────────────────┐  │
│  │  Spotify Client  │  │
│  └──────────────────┘  │
└──────┬──────────────────┘
       │
       │ OAuth + REST API
       │
┌──────▼──────┐
│   Spotify   │
│     API     │
└─────────────┘
```

---

## Technology Stack

### Backend
- **Framework:** FastAPI
  - Fast, modern, async support
  - Auto-generated OpenAPI docs
  - Type hints throughout
- **Language:** Python 3.11+
- **HTTP Client:** `httpx` (async) or `requests`
- **OAuth:** `authlib` or manual implementation
- **Session Management:** `itsdangerous` or `python-jose` for JWT
- **Environment:** `pydantic-settings` for config

### Frontend
- **Framework:** React (or Next.js for SSR if preferred)
- **Styling:** Tailwind CSS
- **HTTP Client:** `fetch` or `axios`
- **State Management:** React Context or Zustand (simple)

### Development Tools
- **Package Management:** `poetry` or `pip` + `requirements.txt`
- **Code Quality:** `black`, `ruff`, `mypy`
- **Testing:** `pytest`, `pytest-asyncio`
- **Environment:** `.env` files with `python-dotenv`

### Deployment
- **Backend:** Railway, Render, or Fly.io (Python-friendly)
- **Frontend:** Vercel, Netlify, or same host as backend
- **Database:** None for MVP (session-based), PostgreSQL later if needed

---

## Project Structure

```
podcast-run-planner/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app entry point
│   │   ├── config.py            # Configuration (Pydantic settings)
│   │   │
│   │   ├── api/                 # API routes
│   │   │   ├── __init__.py
│   │   │   ├── deps.py          # Dependencies (auth, etc.)
│   │   │   ├── routes/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py      # OAuth routes
│   │   │   │   ├── playlists.py # Playlist generation
│   │   │   │   └── episodes.py  # Episode fetching
│   │   │   └── schemas.py       # Pydantic models for requests/responses
│   │   │
│   │   ├── core/                # Core business logic
│   │   │   ├── __init__.py
│   │   │   ├── playlist_generator.py  # Main algorithm
│   │   │   └── content_classifier.py  # Light vs deep classification
│   │   │
│   │   ├── services/            # External service clients
│   │   │   ├── __init__.py
│   │   │   └── spotify.py       # Spotify API client
│   │   │
│   │   └── models/              # Data models
│   │       ├── __init__.py
│   │       ├── user.py
│   │       ├── episode.py
│   │       └── playlist.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_playlist_generator.py
│   │   ├── test_spotify_client.py
│   │   └── conftest.py
│   │
│   ├── requirements.txt         # or pyproject.toml (poetry)
│   ├── .env.example
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/              # Reusable UI components
│   │   │   └── features/        # Feature components
│   │   ├── pages/               # Page components
│   │   ├── hooks/               # Custom React hooks
│   │   ├── lib/                 # Utilities, API client
│   │   └── App.jsx
│   ├── package.json
│   └── README.md
│
├── docs/
│   ├── prd/
│   ├── architecture.md
│   └── planning.md
│
├── .gitignore
└── README.md
```

---

## API Design

### Authentication Endpoints

```
GET  /api/auth/login
     → Redirects to Spotify OAuth

GET  /api/auth/callback
     → Handles OAuth callback, sets session

GET  /api/auth/logout
     → Clears session

GET  /api/auth/me
     → Returns current user info
```

### Data Endpoints

```
GET  /api/episodes
     → Returns user's saved episodes and followed podcasts
     Query params: ?limit=50&offset=0

GET  /api/episodes/{episode_id}
     → Returns episode details
```

### Playlist Endpoints

```
POST /api/playlists/generate
     Body: {
       duration_minutes: int,
       run_type: "easy" | "tempo" | "long",
       content_preference: "light" | "mixed" | "deep"
     }
     → Returns generated playlist (episodes with metadata)

POST /api/playlists/save
     Body: {
       playlist_name: string,
       episode_ids: list[str]
     }
     → Creates Spotify playlist and returns playlist URL
```

---

## Data Flow

### 1. User Login Flow
```
User clicks "Login with Spotify"
  → Frontend redirects to /api/auth/login
  → Backend redirects to Spotify OAuth
  → User authorizes
  → Spotify redirects to /api/auth/callback?code=...
  → Backend exchanges code for tokens
  → Backend stores tokens in session (encrypted)
  → Backend redirects to frontend dashboard
```

### 2. Playlist Generation Flow
```
User fills form (duration, run type, preference)
  → Frontend POSTs to /api/playlists/generate
  → Backend fetches user episodes (cached if recent)
  → Backend runs playlist generation algorithm
  → Backend returns playlist with episodes
  → Frontend displays playlist
```

### 3. Save Playlist Flow
```
User clicks "Save to Spotify"
  → Frontend POSTs to /api/playlists/save
  → Backend creates Spotify playlist via API
  → Backend adds episodes to playlist
  → Backend returns playlist URL
  → Frontend shows success with link
```

---

## Core Components

### 1. Spotify Client (`services/spotify.py`)

**Responsibilities:**
- Handle OAuth flow
- Manage access/refresh tokens
- Make authenticated API requests
- Cache responses to avoid rate limits

**Key Methods:**
```python
async def get_access_token(user_id: str) -> str
async def refresh_token(user_id: str) -> str
async def get_user_profile() -> UserProfile
async def get_saved_episodes(limit: int, offset: int) -> List[Episode]
async def get_followed_podcasts() -> List[Podcast]
async def create_playlist(name: str, description: str) -> Playlist
async def add_episodes_to_playlist(playlist_id: str, episode_uris: List[str])
```

### 2. Playlist Generator (`core/playlist_generator.py`)

**Responsibilities:**
- Generate playlists matching duration
- Filter by content preference
- Consider run type (if applicable)
- Handle edge cases (not enough episodes, etc.)

**Key Methods:**
```python
def generate_playlist(
    episodes: List[Episode],
    target_duration: int,
    run_type: RunType,
    content_preference: ContentPreference
) -> Playlist
```

**Algorithm Approach:**
1. Filter episodes by content preference
2. Sort by relevance/recency
3. Use greedy algorithm or knapsack variant to fit duration
4. Return playlist with total duration

### 3. Content Classifier (`core/content_classifier.py`)

**Responsibilities:**
- Classify episodes as "light" or "deep"
- Use heuristics (can improve with ML later)

**Key Methods:**
```python
def classify_episode(episode: Episode) -> ContentType
```

**Heuristics (MVP):**
- Podcast category (comedy = light, news = mixed, science = deep)
- Episode description keywords
- Episode length (very short might be light)
- User's listening history patterns (future)

---

## Security Considerations

### Session Management
- Use secure, HTTP-only cookies for sessions
- Encrypt session data (tokens)
- Set appropriate expiration
- Use `itsdangerous` or similar for signing

### Token Storage
- Store refresh tokens securely (encrypted in session)
- Never expose tokens to frontend
- Implement token refresh before expiry

### CORS
- Configure CORS for frontend domain only
- Allow credentials for session cookies

### Environment Variables
- Never commit secrets
- Use `.env` files (gitignored)
- Provide `.env.example` template

---

## Error Handling

### API Error Responses
```python
{
  "error": "error_code",
  "message": "Human-readable message",
  "details": {}  # Optional
}
```

### Common Error Cases
- **401 Unauthorized:** Token expired, redirect to login
- **403 Forbidden:** Insufficient permissions
- **429 Too Many Requests:** Rate limited, retry after delay
- **500 Internal Server Error:** Log error, return generic message

### Logging
- Log errors with context (user_id, request_id)
- Use structured logging (JSON format)
- Don't log sensitive data (tokens, PII)

---

## Performance Considerations

### Caching Strategy
- Cache user's episodes for 5-10 minutes
- Cache podcast metadata longer (changes less frequently)
- Use in-memory cache (Redis later if needed)

### API Rate Limits
- Spotify: 10,000 requests/hour per app
- Batch requests where possible
- Implement exponential backoff for retries

### Async Operations
- Use FastAPI's async capabilities
- Make concurrent API calls when possible
- Use `asyncio.gather()` for parallel requests

---

## Testing Strategy

### Unit Tests
- Test playlist generation algorithm
- Test content classification
- Mock Spotify API responses

### Integration Tests
- Test OAuth flow (with test Spotify app)
- Test playlist generation end-to-end
- Test error scenarios

### Test Data
- Create fixtures for episodes
- Use Spotify's test mode if available
- Mock external API calls in tests

---

## Deployment Architecture

### Development
```
Local machine:
  - Backend: uvicorn app.main:app --reload
  - Frontend: npm run dev
  - Both on localhost, different ports
```

### Production
```
┌─────────────┐
│   CDN/      │
│  Frontend   │
└──────┬──────┘
       │
┌──────▼──────┐
│   Backend   │
│  (FastAPI)  │
└─────────────┘
```

**Options:**
- **Railway:** Easy Python deployment, good free tier
- **Render:** Similar to Railway, good docs
- **Fly.io:** More control, good for scaling
- **Vercel:** Can deploy Python, but optimized for Next.js

---

## Future Scalability Considerations

### Database (Post-Sprint 7)
- Store user preferences
- Cache episode metadata
- Track playlist history
- Store algorithm performance metrics

### Background Jobs
- Pre-fetch user episodes periodically
- Update episode metadata
- Generate playlists in background

### Caching Layer
- Redis for session storage
- Redis for API response caching
- CDN for static assets

---

## Development Workflow

### Local Setup
1. Create virtual environment
2. Install dependencies (`pip install -r requirements.txt`)
3. Copy `.env.example` to `.env`
4. Set Spotify app credentials
5. Run `uvicorn app.main:app --reload`
6. Frontend: `npm install && npm run dev`

### Code Quality
- Run `black` for formatting
- Run `ruff` for linting
- Run `mypy` for type checking
- Run `pytest` before committing

### Git Workflow
- Feature branches
- Clear commit messages
- PR reviews (even solo, review your own)

---

## Open Questions / Decisions Needed

1. **Frontend Framework:** React standalone or Next.js?
   - Recommendation: React + Vite for simplicity

2. **Session Storage:** In-memory or Redis?
   - Recommendation: In-memory for MVP, Redis later

3. **Content Classification:** Heuristics only or ML?
   - Recommendation: Start with heuristics, document for ML later

4. **Playlist Algorithm:** Greedy or optimization?
   - Recommendation: Start simple (greedy), optimize if needed

---

## Next Steps

1. Set up project structure
2. Create `requirements.txt` with initial dependencies
3. Set up FastAPI app with basic routes
4. Configure environment variables
5. Set up frontend project (React + Vite)
6. Connect frontend to backend

