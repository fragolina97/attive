# Adding and Modifying APIs

Before performing the implementation, go over the steps to understand and plan the work ahead. Follow the steps in order.

## Step 1: Define API in Documentation

Define (or update) API in `docs/src/api/class-xxx.md`.

### Documentation Format

```markdown
## async method: Page.methodName
* since: v1.XX
- returns: <[null]|[Response]>

Description.

### param: Page.methodName.paramName
* since: v1.XX
- `paramName` <[string]>

Description.

### option: Page.methodName.optionName
* since: v1.XX
- `optionName` <[string]>

Description.
```

Key syntax: `* since: v1.XX`, `* langs: js, python`, `<[TypeName]>`, `### param:` (required), `### option:` (optional)

Watch auto-generates: `packages/playwright-core/types/types.d.ts`, `packages/playwright/types/test.d.ts`

## Step 2: Implement Client API

Implement in `packages/playwright-core/src/client/xxx.ts`.

```typescript
// Direct channel call
async methodName(param: string, options: channels.FrameMethodNameOptions = {}): Promise<void> {
  await this._channel.methodName({ param, ...options, timeout: this._timeout(options) });
}

// With response wrapping
async goto(url: string, options: channels.FrameGotoOptions = {}): Promise<network.Response | null> {
  return network.Response.fromNullable(
    (await this._channel.goto({ url, ...options, timeout: this._timeout(options) })).response
  );
}
```

## Step 3: Define Protocol Channel

Define in `packages/protocol/src/protocol.yml`.

```yaml
Page:
  type: interface
  commands:
    methodName:
      title: Short description
      parameters:
        url: string
        timeout: float
        referer: string?          # optional
        waitUntil: LifecycleEvent?
        button:
          type: enum?
          literals: [left, right, middle]
      returns:
        response: Response?
      flags:
        slowMo: true
        snapshot: true
```

Watch auto-generates: `channels.d.ts`, `validator.ts`, `protocolMetainfo.ts`

## Step 4: Implement Dispatcher

In `packages/playwright-core/src/server/dispatchers/xxxDispatcher.ts`.

```typescript
// Simple pass-through
async methodName(params: channels.PageMethodNameParams, progress: Progress): Promise<void> {
  await this._page.methodName(progress, params.value);
}

// With response wrapping
async goto(params: channels.FrameGotoParams, progress: Progress): Promise<channels.FrameGotoResult> {
  return { response: ResponseDispatcher.fromNullable(this._browserContextDispatcher,
    await this._frame.goto(progress, params.url, params)) };
}
```

## Step 5: Implement Server Logic

In `packages/playwright-core/src/server/xxx.ts`. Browser-specific implementations:
- Chromium: `src/server/chromium/crPage.ts`
- Firefox: `src/server/firefox/ffPage.ts`
- WebKit: `src/server/webkit/wkPage.ts`

## Step 6: Write Tests

- Page-only: `tests/page/xxx.spec.ts`
- Context tests: `tests/library/xxx.spec.ts`

```typescript
import { test as it, expect } from './pageTest';

it('should do something @smoke', async ({ page, server }) => {
  await page.goto(server.EMPTY_PAGE);
  expect(page.url()).toBe(server.EMPTY_PAGE);
});
```

Running: `npm run ctest tests/page/xxx.spec.ts` (Chromium) or `npm run test` (all)
