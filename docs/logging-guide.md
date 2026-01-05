# Logging Guide

## How to Add Log Messages

### 1. Import logging in your module

```python
import logging

# Create a logger for your module
logger = logging.getLogger(__name__)
```

### 2. Use different log levels

```python
# DEBUG - Detailed information for debugging
logger.debug("Detailed debug information")

# INFO - General informational messages
logger.info("User logged in successfully")

# WARNING - Something unexpected but not an error
logger.warning("Rate limit approaching")

# ERROR - Error occurred but application continues
logger.error("Failed to connect to Spotify API")

# CRITICAL - Serious error, application may stop
logger.critical("Database connection lost")
```

## Example: Adding Logs to a Method

```python
import logging

logger = logging.getLogger(__name__)

class MyService:
    def __init__(self):
        logger.info("MyService initialized")
    
    async def do_something(self, param: str):
        logger.debug(f"do_something called with param: {param}")
        
        try:
            # Your code here
            result = await some_operation()
            logger.info(f"Operation successful: {result}")
            return result
        except Exception as e:
            logger.error(f"Operation failed: {e}", exc_info=True)
            raise
```

## Log Levels Explained

| Level | When to Use | Example |
|-------|-------------|---------|
| **DEBUG** | Detailed diagnostic info | "Processing item 42 of 100" |
| **INFO** | General flow information | "User authenticated successfully" |
| **WARNING** | Unexpected but handled | "API rate limit at 80%" |
| **ERROR** | Error occurred | "Failed to fetch user data" |
| **CRITICAL** | Serious failure | "Database connection lost" |

## Current Configuration

Logging is configured in `backend/app/main.py`:

```python
logging.basicConfig(
    level=logging.INFO,  # Shows INFO and above
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
```

**Current level: INFO**
- Shows: INFO, WARNING, ERROR, CRITICAL
- Hides: DEBUG

## Changing Log Level

### For Development (see DEBUG logs)

In `backend/app/main.py`, change:
```python
level=logging.DEBUG,  # Shows all logs including DEBUG
```

### For Production

Keep at INFO or WARNING:
```python
level=logging.WARNING,  # Only warnings and errors
```

## What You'll See in Console

When you run the backend server, you'll see logs like:

```
2024-01-02 14:30:15 - app.main - INFO - Starting Podcast Run Planner API
2024-01-02 14:30:15 - app.services.spotify - INFO - Initializing SpotifyClient
2024-01-02 14:30:20 - app.services.spotify - INFO - Exchanging authorization code for tokens
2024-01-02 14:30:21 - app.services.spotify - INFO - Successfully exchanged code for tokens
```

## Best Practices

1. **Use appropriate log levels**
   - DEBUG for detailed flow
   - INFO for important events
   - ERROR for failures

2. **Include context**
   ```python
   # Good
   logger.info(f"User {user_id} logged in")
   
   # Less useful
   logger.info("User logged in")
   ```

3. **Log exceptions with exc_info**
   ```python
   try:
       # code
   except Exception as e:
       logger.error(f"Operation failed: {e}", exc_info=True)
   ```

4. **Don't log sensitive data**
   ```python
   # Bad
   logger.info(f"Access token: {token}")
   
   # Good
   logger.info("Access token received")
   ```

## Example in SpotifyClient

```python
import logging

logger = logging.getLogger(__name__)

class SpotifyClient:
    def __init__(self, access_token: str | None = None):
        logger.info("Initializing SpotifyClient")
        if access_token:
            logger.debug("SpotifyClient initialized with access token")
        # ...
```

## Quick Reference

```python
# In any Python file
import logging
logger = logging.getLogger(__name__)

# Add logs
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
```

