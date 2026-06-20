# Playwright Trace System - Comprehensive Guide

## 1. Overview

The Playwright trace system captures:
- **Actions** (API calls, user interactions)
- **Network traffic** (HAR format)
- **Snapshots** (DOM snapshots at key moments)
- **Screencast frames** (video of page rendering)
- **Console messages** and events
- **Errors** and logs
- **Resources** (images, stylesheets, scripts, etc.)

## 2. File Structure

```
trace/src/
├── trace.ts        (183 lines) - Main trace event types
├── har.ts          (189 lines) - HAR format types
├── snapshot.ts     (62 lines)  - Snapshot data structures
└── DEPS.list
```

## 3. Trace Event Types

**VERSION: 8** (current format)

- `ContextCreatedTraceEvent` — context options, browser, platform, wallTime
- `BeforeActionTraceEvent` — callId, startTime, class, method, params, stack, pageId, parentId
- `InputActionTraceEvent` — callId, inputSnapshot, point
- `AfterActionTraceEvent` — callId, endTime, afterSnapshot, error, attachments, result
- `ActionTraceEvent` — composite of before+after+input
- `ScreencastFrameTraceEvent` — pageId, sha1, width, height, timestamp
- `EventTraceEvent` — time, class, method, params, pageId
- `ConsoleMessageTraceEvent` — time, pageId, messageType, text, args, location
- `LogTraceEvent` — callId, time, message
- `ResourceSnapshotTraceEvent` — HAR Entry (network request)
- `FrameSnapshotTraceEvent` — DOM snapshot
- `StdioTraceEvent` — stdout/stderr
- `ErrorTraceEvent` — message, stack

## 4. Trace Storage Format

```
traces-dir/
├── <traceName>.trace        # Main events (JSONL)
├── <traceName>.network      # Network events (JSONL)
├── <traceName>.stacks       # Stack trace metadata
└── resources/
    └── <sha1>               # Binary blobs
```

## 5. Trace Recording (tracing.ts)

`Tracing` class extends `SdkObject`, implements `InstrumentationListener`, `SnapshotterDelegate`, `HarTracerDelegate`.

What gets recorded:
1. Before action: metadata, stack, "before" DOM snapshot
2. Input actions: pointer coordinates
3. Action logs
4. After action: execution time, return value, error, "after" snapshot, attachments
5. Network traffic (HAR)
6. Full DOM snapshots
7. Console messages
8. Events (dialogs, navigation)
9. Screencast frames
10. Stdio/errors

## 6. Trace Loading (traceLoader.ts)

```typescript
interface TraceLoaderBackend {
  entryNames(): Promise<string[]>;
  readText(entryName: string): Promise<string | undefined>;
  readBlob(entryName: string): Promise<Blob | undefined>;
  isLive(): boolean;
}
```

Load process: find .trace files → parse with TraceModernizer → sort by startTime → build ContextEntry[]

## 7. Trace Model (traceModel.ts)

`TraceModel`: high-level data model with `pages`, `actions`, `attachments`, `events`, `resources`, `sources`.

```typescript
const traceLoader = new TraceLoader();
await traceLoader.load(new ZipTraceLoaderBackend('trace.zip'), () => {});
const traceModel = new TraceModel(traceUri, traceLoader.contextEntries);
for (const action of traceModel.actions) {
  console.log(action.method, action.params, action.result);
}
```

## 8. Version Support

- Version 3–8 supported. `TraceModernizer` upgrades older traces.
- Current: Version 8

## 9. Key Design Patterns

1. **Call ID Correlation** — unique callId correlates before/input/after/snapshots/logs
2. **Lazy Loading** — snapshots stored by SHA1, resources fetched on demand
3. **Snapshot References** — later snapshots reference earlier via `[[snapshotIndex, nodeIndex]]`
4. **Dual Time Bases** — wallTime (epoch ms) + monotonicTime (internal clock)
5. **Chunked Recording** — multiple chunks per test, separate .trace files

## 10. CLI Usage

```bash
playwright show-trace [trace] [options]
  -b, --browser <browserType>  (chromium/firefox/webkit)
  -h, --host <host>
  -p, --port <port>
  --stdin                       Accept trace URLs over stdin
```
