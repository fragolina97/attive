# Bisecting a Regression Across Published Playwright Versions

When a user reports a regression between published versions (e.g. "works in 1.58, broken in 1.59.1"), reproduce both side by side from npm — do **not** bisect against the monorepo source.

## Setup (two side-by-side installs)

Use `~/tmp/<version-tag>/` (NOT `/tmp/`).

```bash
mkdir -p ~/tmp/<good>/tests ~/tmp/<bad>/tests

( cd ~/tmp/<good> && npm init -y && npm install @playwright/test@<good-ver> && npx playwright install chromium)
( cd ~/tmp/<bad>  && npm init -y && npm install @playwright/test@<bad-ver> && npx playwright install chromium )
```

Write a **minimal** `playwright.config.ts` with a single chromium project:

```ts
import { defineConfig, devices } from '@playwright/test';
export default defineConfig({
  testDir: './tests',
  projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }],
});
```

Run:
```bash
( cd ~/tmp/<good> && npx playwright test )
( cd ~/tmp/<bad>  && npx playwright test )
```

## Investigating the diff in node_modules

The compiled JS in `node_modules/playwright-core/lib/` is the source of truth. In recent versions these are bundled — extract files via grep and compare.

Edit the compiled JS in `~/tmp/<bad>/node_modules/playwright/lib/...` directly and re-run the test. No build step needed. Revert when done.

## Reporting

1. Quote offending lines from `node_modules/.../lib/...` of the **bad** version
2. Show equivalent code from the **good** version
3. Explain *why* the change breaks the case
4. Propose and verify a minimal fix by patching the bad install in place

## Pitfalls

- Don't run `npm init playwright@latest` — it's interactive
- Don't use the scaffold's default config — 3 browser projects multiply test runs by 3
- `/tmp/` is not `~/tmp/` — pick one and stay consistent
- Don't try to map the bug to monorepo source first
