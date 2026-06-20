# Developing Dashboard

`packages/dashboard` contains the sourcecode behind `playwright cli show`, a dashboard for supervising agents using Playwright CLI.

Key code paths:
- `packages/dashboard` — the UI
- `dashboardController.ts` — the backend
- `show` section in `cli-client/program.ts`

```bash
# Start the dashboard server
npx playwright cli show --port=0

# Open it with Playwright CLI
npx playwright cli open --session=dashboard localhost:PORT
npx playwright cli snapshot
npx playwright cli screenshot

# Record a video
npx playwright cli video-start video.webm
npx playwright cli video-chapter "Chapter Title" --description="Details" --duration=2000
npx playwright cli video-stop

# Convert to mp4
ffmpeg -i video.webm video.mp4
```

Full CLI reference: `packages/playwright-core/src/tools/cli-client/skill/SKILL.md`. In this repo, invoke as `npx playwright cli` instead of `playwright-cli`.
