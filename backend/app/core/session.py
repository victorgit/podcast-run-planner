"""Session management utilities."""

from datetime import datetime, timedelta
from itsdangerous import URLSafeTimedSerializer
from fastapi import Request, Response

from app.config import settings


# Create serializer for signing session data
serializer = URLSafeTimedSerializer(
    secret_key=settings.SECRET_KEY,
    salt="session",
)


def create_session(response: Response, user_id: str, access_token: str, refresh_token: str) -> None:
    """
    Create a signed session cookie with user tokens.
    
    Args:
        response: FastAPI response object
        user_id: Spotify user ID
        access_token: Spotify access token
        refresh_token: Spotify refresh token
    """
    session_data = {
        "user_id": user_id,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "created_at": datetime.utcnow().isoformat(),
    }
    
    # Sign the session data
    signed_token = serializer.dumps(session_data, max_age=settings.SESSION_EXPIRE_MINUTES * 60)
    
    # Set as HTTP-only cookie
    response.set_cookie(
        key="session",
        value=signed_token,
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        samesite="lax",
        max_age=settings.SESSION_EXPIRE_MINUTES * 60,
    )


def get_session(request: Request) -> dict | None:
    """
    Get and verify session data from cookie.
    
    Args:
        request: FastAPI request object
        
    Returns:
        Session data dict or None if invalid/expired
    """
    session_cookie = request.cookies.get("session")
    if not session_cookie:
        return None
    
    try:
        session_data = serializer.loads(session_cookie, max_age=settings.SESSION_EXPIRE_MINUTES * 60)
        return session_data
    except Exception:
        # Invalid or expired session
        return None


def clear_session(response: Response) -> None:
    """
    Clear the session cookie.
    
    Args:
        response: FastAPI response object
    """
    response.delete_cookie(key="session", httponly=True, samesite="lax")

