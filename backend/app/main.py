"""FastAPI application entry point."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, episodes, playlists
from app.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Create logger for this module
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Podcast Run Planner API",
    description="API for generating podcast playlists for runs",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=settings.API_V1_PREFIX)
app.include_router(episodes.router, prefix=settings.API_V1_PREFIX)
app.include_router(playlists.router, prefix=settings.API_V1_PREFIX)


@app.on_event("startup")
async def startup_event():
    """Log application startup information."""
    logger.info("=" * 60)
    logger.info("🚀 Podcast Run Planner API Starting")
    logger.info("=" * 60)
    logger.info(f"Version: {app.version}")
    logger.info(f"API Prefix: {settings.API_V1_PREFIX}")
    logger.info(f"CORS Origins: {', '.join(settings.CORS_ORIGINS)}")
    logger.info(f"Session Expiry: {settings.SESSION_EXPIRE_MINUTES} minutes")
    
    # Check Spotify configuration
    if settings.SPOTIFY_CLIENT_ID:
        logger.info("✅ Spotify OAuth configured")
        logger.debug(f"Spotify Redirect URI: {settings.SPOTIFY_REDIRECT_URI}")
    else:
        logger.warning("⚠️  Spotify OAuth not configured (SPOTIFY_CLIENT_ID missing)")
    
    # Check secret key
    if settings.SECRET_KEY == "change-me-in-production":
        logger.warning("⚠️  Using default SECRET_KEY - change in production!")
    else:
        logger.info("✅ SECRET_KEY configured")
    
    # Log registered routes
    logger.info("Registered routes:")
    for route in app.routes:
        if hasattr(route, "path") and hasattr(route, "methods"):
            methods = ", ".join(sorted(route.methods))
            logger.info(f"  {methods:20} {route.path}")
    
    logger.info("=" * 60)
    logger.info("✅ Application startup complete")
    logger.info("=" * 60)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Podcast Run Planner API", "version": "0.1.0"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    logger.debug("Health check requested")
    return {"status": "healthy"}


@app.on_event("shutdown")
async def shutdown_event():
    """Log application shutdown."""
    logger.info("=" * 60)
    logger.info("🛑 Podcast Run Planner API Shutting Down")
    logger.info("=" * 60)

