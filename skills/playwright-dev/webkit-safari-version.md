# Updating WebKit Safari Version

The Safari version string is declared in:
`packages/playwright-core/src/server/webkit/wkBrowser.ts` — `BROWSER_VERSION` constant

```ts
const BROWSER_VERSION = '26.4';
const DEFAULT_USER_AGENT = `Mozilla/5.0 ... Version/${BROWSER_VERSION} Safari/605.1.15`;
```

## Steps

1. **Find the latest stable Safari version** — check [Safari Release Notes](https://developer.apple.com/documentation/safari-release-notes)
2. **Update `BROWSER_VERSION`** in `wkBrowser.ts`
3. **Run lint**: `npm run flint`
