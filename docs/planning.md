# Podcast Run Planner – Development Plan

**Timeline:** ~6-8 weeks (3 evenings/week + weekend hours)  
**Approach:** Sprint-based iterative development  
**Team:** Starting solo, designed for 2-3 contributors later

---

## Time Allocation Estimate

- **Per week:** ~8-10 hours
  - 3 evenings × 1.5-2 hours = 4.5-6 hours
  - Weekend: 3-4 hours
- **Total project:** ~50-70 hours

---

## Sprint Structure

**Sprint duration:** 1-2 weeks  
**Sprint goal:** Working increment that moves toward MVP  
**Definition of Done:** Feature works end-to-end, even if basic

---

## Sprint Breakdown

### Sprint 0: Foundation & Setup (Week 1)
**Goal:** Project structure, tooling, and basic infrastructure

**Engineering Tasks:**
- [ ] Choose tech stack (Python 3.11+, FastAPI, React frontend)
- [ ] Set up project structure (backend/ and frontend/ directories)
- [ ] Configure Python virtual environment
- [ ] Set up version control (Git) and branching strategy
- [ ] Create basic FastAPI app with health check endpoint
- [ ] Set up React frontend (Vite + React)
- [ ] Set up environment variables management (.env files)
- [ ] Add basic styling approach (Tailwind CSS recommended)
- [ ] Configure CORS for frontend-backend communication

**Product/UX Tasks:**
- [ ] Create low-fidelity wireframes for core flow
- [ ] Define design system basics (colors, typography, spacing)
- [ ] Document user flow with decision points

**Deliverable:** Working FastAPI backend and React frontend, can run both locally

**Time:** ~8-10 hours

---

### Sprint 1: Spotify Authentication (Week 1-2)
**Goal:** User can log in with Spotify and we can access their data

**Engineering Tasks:**
- [ ] Set up Spotify Developer account and app
- [ ] Implement Spotify OAuth flow in FastAPI
- [ ] Create API endpoint for OAuth callback (`/api/auth/callback`)
- [ ] Store access/refresh tokens securely (session-based for MVP)
- [ ] Implement session management (using `itsdangerous` or similar)
- [ ] Test token refresh mechanism
- [ ] Create dependency for authenticated requests

**Product/UX Tasks:**
- [ ] Design login/landing page
- [ ] Create loading states for auth flow
- [ ] Design error states (auth failures, token expiry)
- [ ] Test auth flow on mobile browser (since runners use phones)

**Deliverable:** User can log in with Spotify, see basic "logged in" state

**Time:** ~10-12 hours

**Dependencies:** Sprint 0 complete

---

### Sprint 2: Fetch User Podcast Data (Week 2-3)
**Goal:** Retrieve and display user's podcasts and episodes

**Engineering Tasks:**
- [ ] Implement Spotify API client (`services/spotify.py`)
- [ ] Create Pydantic models for episodes and podcasts
- [ ] Fetch user's followed podcasts
- [ ] Fetch user's saved episodes
- [ ] Fetch episode metadata (duration, title, description)
- [ ] Build basic caching strategy (in-memory, avoid rate limits)
- [ ] Create API endpoints for data fetching (`/api/episodes`)
- [ ] Handle pagination for large episode lists

**Product/UX Tasks:**
- [ ] Design podcast/episode list view
- [ ] Create loading states for data fetching
- [ ] Design empty states (no podcasts, no saved episodes)
- [ ] Test with real Spotify account (various podcast counts)

**Deliverable:** User sees their podcasts and episodes after login

**Time:** ~10-12 hours

**Dependencies:** Sprint 1 complete

---

### Sprint 3: Run Planning Form (Week 3-4)
**Goal:** User can input run parameters

**Engineering Tasks:**
- [ ] Create form component for run planning
- [ ] Implement form validation
- [ ] Create state management for form data
- [ ] Add duration input (slider or number input)
- [ ] Add run type selector (easy/tempo/long)
- [ ] Add content preference selector (light/mixed/deep)

**Product/UX Tasks:**
- [ ] Design run planning form (mobile-first)
- [ ] Create form validation feedback
- [ ] Design input controls (sliders, buttons, dropdowns)
- [ ] Test form on mobile device
- [ ] Create form error states
- [ ] Consider accessibility (keyboard navigation, screen readers)

**Deliverable:** User can fill out run planning form with all parameters

**Time:** ~8-10 hours

**Dependencies:** Sprint 2 complete (need episode data for context)

---

### Sprint 4: Playlist Generation Logic (Week 4-5)
**Goal:** Core algorithm to generate playlists matching run parameters

**Engineering Tasks:**
- [ ] Design playlist generation algorithm (`core/playlist_generator.py`)
- [ ] Implement duration matching (target ±5 minutes)
- [ ] Create content classifier (`core/content_classifier.py`)
- [ ] Implement episode filtering by content preference (basic heuristics)
- [ ] Implement run type considerations (if any)
- [ ] Handle edge cases (not enough episodes, too many short episodes)
- [ ] Add logging for debugging algorithm decisions
- [ ] Create unit tests for core algorithm (`pytest`)
- [ ] Create API endpoint (`POST /api/playlists/generate`)

**Product/UX Tasks:**
- [ ] Define content classification rules (light vs deep)
- [ ] Test algorithm with various scenarios
- [ ] Document algorithm behavior for future improvements
- [ ] Consider explaining why episodes were chosen (for transparency)

**Deliverable:** Algorithm generates playlists that match duration and preferences

**Time:** ~12-15 hours (most complex sprint)

**Dependencies:** Sprint 3 complete

---

### Sprint 5: Playlist Display & Actions (Week 5-6)
**Goal:** User can see generated playlist and take actions

**Engineering Tasks:**
- [ ] Create playlist display component (React)
- [ ] Show episode list with durations
- [ ] Display total duration vs target
- [ ] Implement "Regenerate" functionality (call API again)
- [ ] Implement "Save to Spotify" functionality
- [ ] Create API endpoint (`POST /api/playlists/save`)
- [ ] Create Spotify playlist via API
- [ ] Add episodes to Spotify playlist
- [ ] Handle save errors gracefully

**Product/UX Tasks:**
- [ ] Design playlist display (mobile-friendly)
- [ ] Create action buttons (Accept, Regenerate, Save)
- [ ] Design success/error feedback for save action
- [ ] Show duration difference clearly
- [ ] Test on mobile device
- [ ] Consider sharing preview before saving

**Deliverable:** User can see playlist, regenerate it, and save to Spotify

**Time:** ~10-12 hours

**Dependencies:** Sprint 4 complete

---

### Sprint 6: Polish & Edge Cases (Week 6-7)
**Goal:** Handle edge cases and improve UX

**Engineering Tasks:**
- [ ] Handle token expiry gracefully
- [ ] Add retry logic for API failures
- [ ] Improve error messages
- [ ] Add loading states throughout
- [ ] Optimize API calls (reduce unnecessary requests)
- [ ] Add basic analytics/logging
- [ ] Test with various Spotify accounts

**Product/UX Tasks:**
- [ ] Polish visual design
- [ ] Improve mobile experience
- [ ] Add helpful tooltips/explanations
- [ ] Test complete user flow end-to-end
- [ ] Document known limitations
- [ ] Create simple onboarding (first-time user hints)

**Deliverable:** Polished MVP ready for real-world use

**Time:** ~8-10 hours

**Dependencies:** Sprint 5 complete

---

### Sprint 7: Deployment & Documentation (Week 7-8)
**Goal:** Deploy to production and document for team

**Engineering Tasks:**
- [ ] Set up hosting (Railway, Render, or Fly.io for FastAPI)
- [ ] Deploy frontend (Vercel, Netlify, or same host)
- [ ] Configure production environment variables
- [ ] Set up domain (if needed)
- [ ] Add error monitoring (Sentry or similar)
- [ ] Create deployment pipeline
- [ ] Write technical documentation
- [ ] Create README with setup instructions (both backend and frontend)

**Product/UX Tasks:**
- [ ] Test on production environment
- [ ] Create user documentation (if needed)
- [ ] Document product decisions and trade-offs
- [ ] Prepare demo/walkthrough

**Deliverable:** Live application, documented codebase

**Time:** ~6-8 hours

**Dependencies:** Sprint 6 complete

---

## Technical Architecture Decisions

### Recommended Stack
- **Backend Framework:** FastAPI (Python 3.11+)
  - Fast, modern, async support
  - Auto-generated OpenAPI docs
  - Type hints throughout
- **Frontend Framework:** React + Vite
  - Fast development
  - Simple setup
  - Can upgrade to Next.js later if needed
- **Styling:** Tailwind CSS
  - Fast development
  - Mobile-first responsive
- **Language:** Python (backend), TypeScript (frontend)
  - Python: Great for algorithms and API integration
  - TypeScript: Better for team collaboration, catches errors early
- **HTTP Client:** `httpx` (async) for Spotify API
- **Session Management:** `itsdangerous` or `python-jose`
- **Database:** None for MVP (session-based auth)
  - Can add PostgreSQL later if needed
- **Hosting:** Railway/Render (backend), Vercel/Netlify (frontend)
  - Free tiers sufficient for MVP

### Project Structure (Team-Friendly)
```
podcast-run-planner/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry point
│   │   ├── config.py            # Configuration
│   │   ├── api/                 # API routes
│   │   │   ├── routes/
│   │   │   │   ├── auth.py      # OAuth routes
│   │   │   │   ├── playlists.py # Playlist generation
│   │   │   │   └── episodes.py  # Episode fetching
│   │   │   └── schemas.py       # Pydantic models
│   │   ├── core/                # Business logic
│   │   │   ├── playlist_generator.py
│   │   │   └── content_classifier.py
│   │   ├── services/            # External services
│   │   │   └── spotify.py       # Spotify API client
│   │   └── models/              # Data models
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/              # Reusable UI components
│   │   │   └── features/        # Feature components
│   │   ├── pages/               # Page components
│   │   ├── hooks/               # Custom React hooks
│   │   ├── lib/                 # Utilities, API client
│   │   └── App.jsx
│   ├── package.json
│   └── README.md
├── docs/
└── README.md
```

**See `docs/architecture.md` for detailed architecture documentation.**

### Code Organization Principles
- **Feature-based structure** where possible
- **Clear separation** of concerns (API, UI, business logic)
- **Type safety** throughout
- **Documentation** in code (JSDoc comments)
- **Consistent naming** conventions

---

## Product/UX Considerations Per Sprint

### Design Principles
1. **Mobile-first:** Runners use phones
2. **Fast decisions:** Minimize clicks to start run
3. **Clear feedback:** Always show what's happening
4. **Graceful degradation:** Handle API failures well

### UX Challenges to Explore
- **Content classification:** How to determine "light" vs "deep"?
  - Start with heuristics (episode length, podcast category)
  - Can improve with ML later
- **Duration matching:** Balancing exact fit vs quality
  - Algorithm trade-offs
  - User tolerance for ±5 minutes
- **Regeneration UX:** How many times should user regenerate?
  - Limit attempts?
  - Show what changed?
- **Onboarding:** First-time user experience
  - Explain features?
  - Show example?

---

## Making It Team-Friendly

### From Day 1
- **Clear code structure** (see above)
- **README** with setup instructions
- **Git workflow:** Feature branches, clear commit messages
- **TypeScript:** Self-documenting code
- **Comments:** Explain "why" not "what"

### As Team Grows
- **Code reviews:** Even solo, review your own PRs
- **Documentation:** Keep docs/ updated
- **Issue tracking:** Use GitHub Issues for bugs/features
- **Testing:** Add tests as complexity grows
- **CI/CD:** Automate checks and deployment

### Collaboration Opportunities
- **Sprint 4:** Algorithm design (good for pairing)
- **Sprint 5:** UI polish (designer + developer)
- **Sprint 6:** Edge cases (QA perspective)
- **Sprint 7:** Documentation (technical writer)

---

## Risk Mitigation

### Technical Risks
- **Spotify API rate limits:** Cache aggressively, batch requests
- **Token management:** Use secure session storage, handle refresh
- **Algorithm complexity:** Start simple, iterate based on real usage

### Time Risks
- **Scope creep:** Stick to MVP, defer nice-to-haves
- **Integration complexity:** Spotify OAuth can be tricky, budget extra time
- **Algorithm perfectionism:** Ship working version, improve later

### Mitigation Strategy
- **Weekly check-ins:** Review progress, adjust scope if needed
- **MVP mindset:** Working > perfect
- **Document blockers:** Note what's hard for future reference

---

## Success Metrics Per Sprint

- **Sprint 0:** Can run backend (`uvicorn app.main:app`) and frontend (`npm run dev`)
- **Sprint 1:** Can log in with Spotify
- **Sprint 2:** Can see my podcasts/episodes
- **Sprint 3:** Can fill out form and see inputs
- **Sprint 4:** Algorithm generates reasonable playlists
- **Sprint 5:** Can save playlist to Spotify
- **Sprint 6:** Can use app on a real run without frustration
- **Sprint 7:** App is live and others can use it

---

## Next Steps

1. **Review this plan** and adjust based on your preferences
2. **Set up development environment** (Python 3.11+, Node.js, Git, editor)
3. **Start Sprint 0** - project setup
4. **Track progress** (simple checklist or GitHub Projects)

---

## Notes for Future Team Members

- **Onboarding:** Start with README, then Sprint 0 setup
- **Contributing:** Pick up any incomplete sprint or tackle edge cases
- **Questions:** Document decisions in code comments or docs/
- **Experimentation:** Each sprint has room for UX/engineering exploration

