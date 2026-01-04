# Podcast Run Planner - Frontend

React frontend for the Podcast Run Planner application.

## Setup

### Prerequisites

- Node.js 18 or higher
- npm or yarn

### Installation

1. Install dependencies:

```bash
npm install
```

2. Set up environment variables:

```bash
cp .env.example .env
# Edit .env if needed (defaults to http://localhost:8000)
```

3. Run the development server:

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── ui/              # Reusable UI components
│   │   └── features/        # Feature-specific components
│   ├── pages/               # Page components
│   ├── hooks/               # Custom React hooks
│   ├── lib/                 # Utilities, API client
│   ├── App.jsx              # Main app component
│   └── main.jsx             # Entry point
├── package.json
└── README.md
```

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Styling

This project uses Tailwind CSS for styling. The configuration is in `tailwind.config.js`.

## API Integration

The frontend communicates with the FastAPI backend. The API client is in `src/lib/api.js`.

Make sure the backend is running on the port specified in your `.env` file (default: `http://localhost:8000`).

## Next Steps

- Sprint 1: Implement login flow
- Sprint 2: Display user's episodes
- Sprint 3: Create run planning form
- Sprint 5: Display and save playlists
