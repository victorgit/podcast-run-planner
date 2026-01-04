"""Authentication routes."""

from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login")
async def login():
    """Initiate Spotify OAuth login."""
    # TODO: Implement in Sprint 1
    return {"message": "Login endpoint - to be implemented"}


@router.get("/callback")
async def callback(code: str | None = None, error: str | None = None):
    """Handle Spotify OAuth callback."""
    # TODO: Implement in Sprint 1
    return {"message": "Callback endpoint - to be implemented"}


@router.get("/logout")
async def logout():
    """Logout user."""
    # TODO: Implement in Sprint 1
    return {"message": "Logout endpoint - to be implemented"}


@router.get("/me")
async def get_current_user():
    """Get current user info."""
    # TODO: Implement in Sprint 1
    return {"message": "Get user endpoint - to be implemented"}

