# Playwright Library Architecture

Playwright uses a client-server architecture connected by a protocol layer.

## Package Layout

```
packages/protocol/src/
  protocol.yml              — RPC protocol definition (source of truth)
  channels.d.ts             — generated TypeScript channel interfaces

packages/playwright-core/src/
  client/                   — public API objects (ChannelOwner subclasses)
  server/                   — browser automation implementation
  server/dispatchers/       — protocol bridge (Dispatcher subclasses)
  utils/isomorphic/         — shared code
```

## Dependency Rules (DEPS.list)

Enforced by `npm run flint`.
- **client/** can import from `../protocol/` and `../utils/isomorphic`
- **server/** can import from `../protocol/`, `../utils/`, `../utilsBundle.ts`
- **server/dispatchers/** can import from `../../protocol/`, `../../utils/`, `../**`
- **Key rule:** Client NEVER imports server. Server NEVER imports client.

## Protocol Layer

`protocol.yml` defines all RPC interfaces, commands, events, types.

Code generation: `node utils/generate_channels.js` produces:
- `channels.d.ts` — TypeScript types
- `validator.ts` — runtime validators
- `protocolMetainfo.ts` — method flags

Wire format:
```
Client → Server: { id, guid, method, params, metadata? }
Server → Client: { id, result } or { id, error, log? }
Server → Client (event): { guid, method, params }
```

## Client Layer

Every client API object extends `ChannelOwner<T>` with `_channel` (Proxy intercepting calls), `_connection`, `_guid`, `_type`.

| Class | File | Purpose |
|-------|------|--------|
| Playwright | playwright.ts | Root object |
| BrowserType | browserType.ts | launch() |
| Browser | browser.ts | newContext() |
| BrowserContext | browserContext.ts | Isolation boundary |
| Page | page.ts | Delegates to _mainFrame |
| Frame | frame.ts | goto(), click(), evaluate() |
| Locator | locator.ts | Delegates to Frame + strict: true |

## Server Layer

Every server object extends `SdkObject` with `guid`, `attribution`, `instrumentation`.

| Class | File | Purpose |
|-------|------|--------|
| Frame | frames.ts | Navigation, DOM queries |
| Page | page.ts | Owns FrameManager, workers |
| BrowserContext | browserContext.ts | Isolation boundary |
| PageDelegate | interface | Browser-specific operations |

Browser-specific implementations:
- `chromium/crPage.ts` — CDP
- `firefox/ffPage.ts`
- `webkit/wkPage.ts`

## Dispatcher Layer

Dispatchers translate protocol to server code calls. Base class: `Dispatcher<Type, ChannelType, ParentScopeType>`.

Dispatchers use static factory: `static from(parentScope, object)` — ensures one-dispatcher-per-object.

## End-to-End Flow (`page.goto('https://example.com')`)

```
CLIENT:
  Page.goto() → _wrapApiCall() → _channel.goto() → Proxy validates → sendMessageToServer()

SERVER:
  DispatcherConnection.dispatch() → PageDispatcher._runCommand('goto') →
  ProgressController.run() → PageDispatcher.goto() →
  this._object.mainFrame().goto() → PageDelegate.navigateFrame() → CDP call
  → sends { id: 1, result: { response: {...} } }
```

## Testing

- `tests/library/` — browser/context lifecycle, protocol, CDP features
- `tests/page/` — user interactions (click, type, navigate), locators, assertions

```bash
npm run ctest tests/library/browser-context-cookies.spec.ts  # Chromium only
npm run test tests/page/locator-click.spec.ts               # All browsers
```
