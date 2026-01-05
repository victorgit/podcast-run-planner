"""Spotify API client."""

import base64
import logging
import httpx
from urllib.parse import urlencode

from app.config import settings

# Create logger for this module
logger = logging.getLogger(__name__)


class SpotifyClient:
    """Client for interacting with Spotify API."""
    
    def __init__(self, access_token: str | None = None):
        """
        Initialize Spotify client.
        
        Args:
            access_token: Optional access token for authenticated requests
        """
        logger.info("Initializing SpotifyClient")
        if access_token:
            logger.debug("SpotifyClient initialized with access token")
        else:
            logger.debug("SpotifyClient initialized without access token (OAuth flow)")
        
        self.access_token = access_token
        self.base_url = "https://api.spotify.com/v1"
        self.auth_url = "https://accounts.spotify.com"
    
    def get_authorization_url(self, state: str | None = None) -> str:
        """
        Generate Spotify OAuth authorization URL.
        
        Args:
            state: Optional state parameter for CSRF protection
            
        Returns:
            Authorization URL
        """
        params = {
            "client_id": settings.SPOTIFY_CLIENT_ID,
            "response_type": "code",
            "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
            "scope": "user-read-private user-read-email user-library-read playlist-modify-public",
            "show_dialog": "false",
        }
        
        if state:
            params["state"] = state
        
        return f"{self.auth_url}/authorize?{urlencode(params)}"
    
    async def exchange_code_for_tokens(self, code: str) -> dict:
        """
        Exchange authorization code for access and refresh tokens.
        
        Args:
            code: Authorization code from OAuth callback
            
        Returns:
            Dict with access_token, refresh_token, expires_in, etc.
        """
        logger.info("Exchanging authorization code for tokens")
        
        # Create Basic Auth header
        client_credentials = f"{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_CLIENT_SECRET}"
        encoded_credentials = base64.b64encode(client_credentials.encode()).decode()
        
        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
        }
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.auth_url}/api/token",
                    headers=headers,
                    data=data,
                )
                response.raise_for_status()
                token_data = response.json()
                logger.info("Successfully exchanged code for tokens")
                return token_data
        except httpx.HTTPStatusError as e:
            logger.error(f"Failed to exchange code for tokens: {e.response.status_code} - {e.response.text}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error exchanging tokens: {e}")
            raise
    
    async def refresh_access_token(self, refresh_token: str) -> dict:
        """
        Refresh access token using refresh token.
        
        Args:
            refresh_token: Refresh token
            
        Returns:
            Dict with new access_token, expires_in, etc.
        """
        # Create Basic Auth header
        client_credentials = f"{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_CLIENT_SECRET}"
        encoded_credentials = base64.b64encode(client_credentials.encode()).decode()
        
        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.auth_url}/api/token",
                headers=headers,
                data=data,
            )
            response.raise_for_status()
            return response.json()
    
    async def get_user_profile(self) -> dict:
        """
        Get current user's profile.
        
        Returns:
            User profile dict
        """
        logger.debug("Getting user profile from Spotify API")
        
        if not self.access_token:
            logger.error("Access token required but not provided")
            raise ValueError("Access token required")
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/me",
                    headers=headers,
                )
                response.raise_for_status()
                user_data = response.json()
                logger.info(f"Successfully retrieved user profile: {user_data.get('id')}")
                return user_data
        except httpx.HTTPStatusError as e:
            logger.error(f"Failed to get user profile: {e.response.status_code} - {e.response.text}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error getting user profile: {e}")
            raise
    
    async def get_saved_episodes(self, limit: int = 50, offset: int = 0):
        """Get user's saved episodes."""
        # TODO: Implement in Sprint 2
        raise NotImplementedError("Not yet implemented")
    
    async def get_followed_podcasts(self):
        """Get user's followed podcasts."""
        # TODO: Implement in Sprint 2
        raise NotImplementedError("Not yet implemented")
    
    async def create_playlist(self, name: str, description: str = ""):
        """Create a new playlist."""
        # TODO: Implement in Sprint 5
        raise NotImplementedError("Not yet implemented")
    
    async def add_episodes_to_playlist(self, playlist_id: str, episode_uris: list[str]):
        """Add episodes to a playlist."""
        # TODO: Implement in Sprint 5
        raise NotImplementedError("Not yet implemented")
