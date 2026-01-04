# Podcast Run Planner - Backend

FastAPI backend for the Podcast Run Planner application.

## Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
cp env.example .env
# Edit .env with your Spotify app credentials
```

4. Run the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Configuration
│   ├── api/                 # API routes
│   │   ├── routes/          # Route modules
│   │   └── schemas.py       # Pydantic models
│   ├── core/                # Business logic
│   ├── services/            # External service clients
│   └── models/              # Data models
├── tests/                   # Tests
├── requirements.txt         # Python dependencies
└── README.md
```

## Development

### Code Quality

Format code:
```bash
black app/ tests/
```

Lint code:
```bash
ruff check app/ tests/
```

Type checking:
```bash
mypy app/
```

### Running Tests

```bash
pytest
```

## Environment Variables

See `.env.example` for required environment variables.

## Next Steps

- Sprint 1: Implement Spotify OAuth authentication
- Sprint 2: Implement episode fetching from Spotify
- Sprint 4: Implement playlist generation algorithm

