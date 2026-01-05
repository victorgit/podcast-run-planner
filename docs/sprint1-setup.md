# Sprint 1: Spotify Authentication - Setup Guide

## ✅ What's Been Implemented

All the OAuth flow code is complete! You just need to add your Spotify credentials.

### Backend Implementation
- ✅ OAuth login endpoint (`/api/auth/login`)
- ✅ OAuth callback handler (`/api/auth/callback`)
- ✅ Session management with `itsdangerous`
- ✅ User profile endpoint (`/api/auth/me`)
- ✅ Logout endpoint (`/api/auth/logout`)
- ✅ Authentication dependency for protected routes
- ✅ Spotify API client with OAuth methods

### Frontend Implementation
- ✅ Login button that redirects to backend
- ✅ OAuth callback handling
- ✅ User profile display component
- ✅ Authentication state management hook
- ✅ Logout functionality
- ✅ Error handling and loading states

## 🔧 Setup Steps (When Spotify App Creation Reopens)

### Step 1: Create Spotify App
1. Go to https://developer.spotify.com/dashboard
2. Click "Create app"
3. Fill in:
   - **App name**: Podcast Run Planner
   - **Redirect URI**: `http://localhost:8000/api/auth/callback`
   - Check "Web API"
4. Save and get your credentials

### Step 2: Add Credentials to Backend

Create/update `backend/.env` file:

```bash
# Copy from env.example if you haven't already
cp backend/env.example backend/.env

# Edit backend/.env and add:
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
SPOTIFY_REDIRECT_URI=http://localhost:8000/api/auth/callback

# Also set a secure secret key:
SECRET_KEY=your-random-secure-string-here
```

**Generate a secure SECRET_KEY:**
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Step 3: Restart Backend Server

After adding credentials, restart your backend:

```bash
# Stop current server (Ctrl+C)
# Then restart:
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
```

### Step 4: Test the Flow

1. Open frontend: http://localhost:5173
2. Click "Login with Spotify"
3. Authorize the app on Spotify
4. You should be redirected back and see your profile!

## 🧪 Testing

### Test Login Flow
1. Click "Login with Spotify" button
2. Should redirect to Spotify authorization
3. After authorizing, should redirect back to app
4. Should see user profile with name/email

### Test Logout
1. Click "Logout" button
2. Should clear session and return to login screen

### Test Protected Endpoints
Once logged in, `/api/auth/me` should return your user info.

## 📝 API Endpoints

### `GET /api/auth/login`
- Redirects to Spotify OAuth
- No parameters needed

### `GET /api/auth/callback?code=...`
- Handles OAuth callback
- Creates session
- Redirects to frontend

### `GET /api/auth/me`
- Returns current user info
- Requires authentication (session cookie)

### `GET /api/auth/logout`
- Clears session
- Logs user out

## 🔒 Security Notes

- Session cookies are HTTP-only (can't be accessed by JavaScript)
- Sessions expire after 24 hours (configurable)
- Tokens are stored securely in signed session cookies
- In production, set `secure=True` in session cookie (requires HTTPS)

## 🐛 Troubleshooting

### "Spotify OAuth not configured" error
- Make sure `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` are set in `.env`
- Restart backend server after adding credentials

### Redirect URI mismatch
- Make sure redirect URI in Spotify dashboard matches exactly: `http://localhost:8000/api/auth/callback`
- No trailing slash!

### Session not persisting
- Check that cookies are enabled in browser
- Check CORS settings allow credentials
- Check that frontend and backend are on correct ports

### "Not authenticated" error
- Session may have expired
- Try logging in again
- Check browser cookies (should see "session" cookie)

## ✅ Success Criteria

- [x] User can click "Login with Spotify"
- [x] OAuth flow completes successfully
- [x] User profile displays after login
- [x] Session persists across page refreshes
- [x] Logout clears session
- [x] `/api/auth/me` returns user info when authenticated

## 🚀 Next Steps

Once authentication is working:
- Sprint 2: Fetch user's podcasts and episodes
- Sprint 3: Create run planning form
- Sprint 4: Implement playlist generation algorithm

