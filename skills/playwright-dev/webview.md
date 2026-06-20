# WebView (iOS Safari) Backend Reference

The `webkit/webview/` folder targets unmodified Safari on real iOS/iPadOS or iOS Simulator over the standard Web Inspector Protocol. The regular `webkit/` backend runs against a Playwright-patched WebKit build.

## Architecture

```
WebSocketTransport (ws://localhost:9222/devtools/page/<n>)
  → WVConnection (owns outerSession)
      → outerSession (Target.sendMessageToTarget bridge)
          → WVPage (owns per-target WVSessions, routes events, manages swaps)
              → _session (current) + WVProvisionalPage (during swap)
```

## Process Swap / Provisional Targets

Cross-origin navigation can spawn a new process:
```
Target.targetCreated  targetInfo:{ isProvisional:true, isPaused:true }
... events on provisional target ...
Target.didCommitProvisionalTarget  oldTargetId, newTargetId
Target.targetDestroyed  oldTargetId
```

`Target.setPauseOnStart` makes provisional targets arrive `isPaused`, so interception/bootstrap can be set up before resuming with `Target.resume`.

## What Is and Isn't Available

- **Available**: upstream Web Inspector Protocol methods
- **Not available**: anything added by Playwright's WebKit patches (e.g., `Playwright.*` domain, `Network.continueWithAuth`)

## Running Tests

```bash
./utils/run_webview_tests.sh           # ensures ios_webkit_debug_proxy is up on 9222
npm run wvtest -- -g "<test title>"    # single test
npm run wvtest -- tests/page/foo.spec.ts
```

CI: `.github/workflows/tests_webview_simulator.yml` on `macos-15`.
