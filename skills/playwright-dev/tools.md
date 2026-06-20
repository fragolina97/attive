# MCP Tools and CLI Commands

## Adding MCP Tools

### Step 1: Create the Tool File

`packages/playwright-core/src/tools/backend/<your-tool>.ts`

```typescript
import { z } from '../../zodBundle';
import { defineTool, defineTabTool } from './tool';

const myTool = defineTabTool({
  capability: 'core',
  schema: {
    name: 'browser_my_tool',
    title: 'My Tool',
    description: 'Does something',
    inputSchema: z.object({
      ref: z.string().describe('Element reference from snapshot'),
      value: z.string().optional().describe('Optional value'),
    }),
    type: 'action',  // 'input' | 'assertion' | 'action' | 'readOnly'
  },
  handle: async (tab, params, response) => {
    await tab.page.click(`[ref="${params.ref}"]`);
    response.addCode(`await page.click('[ref="${params.ref}"]');`);
    response.setIncludeSnapshot();
  },
});

export default [myTool];
```

Use `defineTabTool` for most tools; `defineTool` when you need `context.ensureBrowserContext()`.

### Step 2: Add ToolCapability (if needed)

In `packages/playwright-core/src/tools/mcp/config.d.ts`:
```typescript
export type ToolCapability = 'config' | 'core' | 'core-navigation' | 'core-input' | 'network' | 'storage' | 'vision' | ...
```

### Step 3: Register the Tool

In `packages/playwright-core/src/tools/backend/tools.ts`, add to `browserTools` array.

### Step 4: Write Tests

`tests/mcp/<category>.spec.ts`:
```typescript
import { test, expect } from './fixtures';
test('browser_my_tool', async ({ client, server }) => {
  await client.callTool({ name: 'browser_navigate', arguments: { url: server.PREFIX } });
  expect(await client.callTool({
    name: 'browser_my_tool',
    arguments: { ref: 'e1' },
  })).toHaveResponse({
    code: `await page.click('[ref="e1"]');`,
    snapshot: expect.stringContaining('content'),
  });
});
```

Run: `npm run ctest-mcp <category>`

---

## Adding CLI Commands

### Step 1: Implement the MCP tool first.

### Step 2: Add the Command Declaration

In `packages/playwright-core/src/tools/cli-daemon/commands.ts`:

```typescript
const myCommand = declareCommand({
  name: 'my-command',
  description: 'Does something',
  category: 'core',
  args: z.object({ url: z.string().describe('URL') }),
  options: z.object({ submit: z.boolean().optional() }),
  toolName: 'browser_my_tool',
  toolParams: ({ url, submit }) => ({ url, submit }),
});
```

Add to `commandsArray` in the correct category.

### Step 3: Update SKILL File

`packages/playwright/src/skill/SKILL.md` with new command docs.

### Step 4: Write CLI Tests

`tests/mcp/cli-<category>.spec.ts`:
```typescript
import { test, expect } from './cli-fixtures';
test('my-command', async ({ cli, server }) => {
  await cli('open', server.PREFIX);
  const { output, snapshot } = await cli('my-command', 'arg1', '--option=value');
  expect(output).toContain('expected text');
});
```

---

## Adding Config Options

1. `packages/playwright-core/src/tools/mcp/config.d.ts` — add to `Config` type
2. `packages/playwright-core/src/tools/mcp/config.ts` — add to `CLIOptions`, `FullConfig`, `defaultConfig`
3. `configFromCLIOptions()` — map CLI option
4. `configFromEnv()` — add env variable (`PLAYWRIGHT_MCP_MY_OPTION`)
5. `packages/playwright-core/src/tools/mcp/program.ts` — add `--my-option <value>` CLI flag

Resolution order: `defaultConfig` → config file → env vars → CLI args (last wins)
