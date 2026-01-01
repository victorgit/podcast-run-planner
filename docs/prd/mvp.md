# Podcast Run Planner – MVP PRD

**Status:** Draft  
**Owner:** Victor  
**Last updated:** YYYY-MM-DD

---

## 1. Problem

Spotify is good at recommending podcasts, but bad at planning **time-bounded listening for runs**.

When I go out for a run, I think in terms of:
- how long I’ll run
- how hard the run will be
- how mentally demanding the content should be

Today, I often:
- lose track of good episodes
- spend too much time choosing
- end up with playlists that don’t fit the run duration

I want to start my run with confidence that my listening experience will “just work”.

---

## 2. Target User

Primary (MVP):
- A frequent podcast listener
- A runner who plans runs of varying duration (45–180 minutes)
- Uses Spotify as the main listening platform

MVP user = me.

---

## 3. Goals (MVP)

- Allow a user to plan a run and generate a podcast playlist
- Fit playlist duration to run duration with minimal over/under
- Prefer relevant and listenable episodes
- Require minimal interaction before starting the run

---

## 4. Non-Goals (Explicit)

- No real-time adaptation during the run
- No integration with Garmin, Strava, or other fitness platforms
- No social features or sharing
- No advanced personalization beyond Spotify listening history
- No mobile app (web only)

---

## 5. Core User Flow

1. User logs in with Spotify
2. User selects:
   - Planned run duration (minutes)
   - Run type (easy / tempo / long)
   - Content preference (light / mixed / deep)
3. System generates a podcast playlist
4. User can:
   - Accept playlist
   - Regenerate playlist
   - Save playlist to Spotify

---

## 6. Functional Scope (MVP)

- Spotify OAuth login
- Fetch user’s followed podcasts and saved episodes
- Generate a playlist based on:
  - Duration constraint
  - Run type
  - Content preference
- Display playlist with episode durations and total time
- Save playlist to Spotify

---

## 7. Success Criteria (MVP)

- Playlist total duration is within ±5 minutes of requested duration
- Episodes feel appropriate for the selected run type
- Playlist can be used on a real run without mid-run frustration
- End-to-end flow works reliably without manual fixes

---

## 8. Open Questions

- How to classify episodes as “light” vs “deep”?
- How strict should duration fitting be?
- Should the system explain *why* episodes were chosen?

---

## 9. Future Ideas (Out of Scope)

- Adaptive playlists during the run
- Run history and recommendations over time
- Cross-device sync
- Sharing playlists with others