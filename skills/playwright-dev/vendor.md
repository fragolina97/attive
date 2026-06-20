# Vendor Dependencies & Bundling

## The Bundles

### playwright-core

| Output | Entry | Purpose |
|---|---|---|
| `lib/utilsBundle.js` | `src/utilsBundle.ts` | Vendored npm packages (debug, mime, ws, yauzl, @modelcontextprotocol/sdk, ...) |
| `lib/coreBundle.js` | `src/coreBundle.ts` | Re-exports of playwright-core modules as namespaces |

The `dynamicImportToRequirePlugin` rewrites vendored npm imports at bundle time:
```ts
import debug from 'debug';  // becomes: const debug = require('./utilsBundle').debug;
```

### playwright

| Output | Entry |
|---|---|
| `lib/transform/babelBundle.js` | Babel, traverse, code-frame, plugins |
| `lib/common/index.js` | compilationCache, test, configLoader, fixtures, globals |
| `lib/runner/index.js` | runner/*, reporters/*, plugins/* |
| `lib/matchers/expect.js` | Jest-style matchers |

## Adding a Vendored NPM Dependency

Three pieces need to line up:

1. **Install**: add to root `package.json` devDependencies
2. **Export from `src/utilsBundle.ts`**:
   ```ts
   import fooLibrary from 'foo';
   export const foo = fooLibrary;
   ```
3. **Add mapping to `utils/build/utilsBundleMapping.js`**:
   ```js
   'foo': { default: 'foo' },
   // or: { namespace: 'foo' }
   // or: { named: { namedSymbol: 'fooNamedSymbol' } }
   ```
4. **Update DEPS.list** with `node_modules/<pkg>`
5. **Run `npm run flint`**

## DEPS.list

| Syntax | Meaning |
|---|---|
| `./somefile.ts`, `@isomorphic/**` | Relative/alias import allowed |
| `node_modules/<pkg>` | npm package import allowed |
| `"strict"` | No other DEPS inherited |

Section headers `[filename.ts]` scope rules to a single file.

## Quick Reference

- New vendored dep: root `package.json` → `utilsBundle.ts` export → `utilsBundleMapping.js` entry → DEPS.list → `npm run flint`
- New in-tree helper: drop `.ts` under `server/utils/third_party/`, re-export from `server/utils/index.ts`, use `@utils/third_party/<name>`
- Check bundle contents: read `.js.txt` sidecar next to output
