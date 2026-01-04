"""Dependencies for API routes."""

from fastapi import HTTPException, status
from fastapi.security import HTTPBearer

# Placeholder for authentication dependency
# Will be implemented in Sprint 1
security = HTTPBearer()


async def get_current_user():
    """Get current authenticated user."""
    # TODO: Implement in Sprint 1
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Authentication not yet implemented",
    )

