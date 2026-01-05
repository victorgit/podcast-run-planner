"""Authentication routes."""

import logging

from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.responses import RedirectResponse

from app.config import settings
from app.core.session import create_session, get_session, clear_session
from app.services.spotify import SpotifyClient
from app.api.deps import get_current_user

# Create logger for this module
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login")
async def login():
    """
    Initiate Spotify OAuth login.
    Redirects user to Spotify authorization page.
    """
    if not settings.SPOTIFY_CLIENT_ID:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Spotify OAuth not configured. Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET in .env",
        )
    
    spotify = SpotifyClient()
    auth_url = spotify.get_authorization_url()
    
    return RedirectResponse(url=auth_url)


@router.get("/callback")
async def callback(
    request: Request,
    response: Response,
    code: str | None = None,
    error: str | None = None,
):
    """
    Handle Spotify OAuth callback.
    Exchanges authorization code for tokens and creates session.
    """
    if error:
        # User denied authorization or error occurred
        logger.warning(f"OAuth callback received error: {error}")
        return RedirectResponse(
            url=f"{settings.CORS_ORIGINS[0]}/?error={error}",
            status_code=status.HTTP_302_FOUND,
        )
    
    if not code:
        logger.warning("OAuth callback received without authorization code")
        return RedirectResponse(
            url=f"{settings.CORS_ORIGINS[0]}/?error=no_code",
            status_code=status.HTTP_302_FOUND,
        )
    
    try:
        logger.info("Processing OAuth callback")
        # Exchange code for tokens
        spotify = SpotifyClient()
        token_data = await spotify.exchange_code_for_tokens(code)
        
        access_token = token_data["access_token"]
        refresh_token = token_data.get("refresh_token")
        
        # Get user profile to get user ID
        spotify_with_token = SpotifyClient(access_token=access_token)
        user_profile = await spotify_with_token.get_user_profile()
        user_id = user_profile["id"]
        
        logger.info(f"OAuth successful for user: {user_id}")
        
        # Create session
        create_session(response, user_id, access_token, refresh_token or "")
        
        # Redirect to frontend
        return RedirectResponse(
            url=f"{settings.CORS_ORIGINS[0]}/?login=success",
            status_code=status.HTTP_302_FOUND,
        )
    
    except Exception as e:
        # Log error with full exception details
        logger.error(f"OAuth callback error: {e}", exc_info=True)
        return RedirectResponse(
            url=f"{settings.CORS_ORIGINS[0]}/?error=auth_failed",
            status_code=status.HTTP_302_FOUND,
        )


@router.get("/logout")
async def logout(response: Response):
    """
    Logout user by clearing session.
    """
    clear_session(response)
    return {"message": "Logged out successfully"}


@router.get("/me")
async def get_user_info(request: Request):
    """
    Get current authenticated user information.
    """
    try:
        user_data = await get_current_user(request)
        
        # Get fresh user profile from Spotify
        spotify = SpotifyClient(access_token=user_data["access_token"])
        user_profile = await spotify.get_user_profile()
        
        return {
            "id": user_profile["id"],
            "display_name": user_profile.get("display_name"),
            "email": user_profile.get("email"),
            "images": user_profile.get("images", []),
        }
    except HTTPException:
        raise
    except Exception as e:
        # Log full error details for debugging (not exposed to client)
        logger.error(f"Failed to get user info: {e}", exc_info=True)
        # Return generic error message to client (no sensitive details)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve user information. Please try again later.",
        )
