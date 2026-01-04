# Podcast Run Planner

A web application that helps runners create Spotify playlists tailored to their run duration and preferences.

## Overview

This project generates podcast playlists that match:
- Run duration (45-180 minutes)
- Run type (easy/tempo/long)
- Content preference (light/mixed/deep)

## Tech Stack

- **Backend:** FastAPI (Python 3.11+)
- **Frontend:** React + Vite
- **Styling:** Tailwind CSS
- **API:** Spotify Web API

## Project Structure

```
podcast-run-planner/
├── backend/          # FastAPI backend
├── frontend/         # React frontend
└── docs/            # Documentation
    ├── prd/         # Product requirements
    ├── architecture.md
    └── planning.md
```

## Quick Start

### Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Edit with your Spotify credentials
uvicorn app.main:app --reload
```

Backend runs on `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env  # Optional, defaults work for local dev
npm run dev
```

Frontend runs on `http://localhost:5173`

## Documentation

- **PRD:** `docs/prd/mvp.md` - Product requirements
- **Architecture:** `docs/architecture.md` - Technical architecture
- **Planning:** `docs/planning.md` - Sprint-based development plan

## Development Status

Currently in **Sprint 0** - Foundation & Setup

See `docs/planning.md` for the full sprint breakdown.

## License

MIT

