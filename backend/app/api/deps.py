"""Dependencies for API routes."""

from fastapi import HTTPException, Request, status
from app.core.session import get_session
from app.services.spotify import SpotifyClient


async def get_current_user(request: Request) -> dict:
    """
    Dependency to get current authenticated user.
    
    Raises 401 if user is not authenticated.
    
    Returns:
        Dict with user_id and access_token
    """
    session = get_session(request)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    
    return {
        "user_id": session["user_id"],
        "access_token": session["access_token"],
        "refresh_token": session.get("refresh_token"),
    }


async def get_spotify_client(request: Request) -> SpotifyClient:
    """
    Dependency to get authenticated Spotify client.
    
    Raises 401 if user is not authenticated.
    
    Returns:
        SpotifyClient instance with access token
    """
    user_data = await get_current_user(request)
    return SpotifyClient(access_token=user_data["access_token"])
