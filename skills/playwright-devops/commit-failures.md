# CI Health Report

Generate a CI health report for the last commit on the `main` branch of `microsoft/playwright`.

## Phase 1 — Fetch logs

```
bash .claude/skills/playwright-devops/fetch-commit-logs.sh [<sha>]
```

- If no SHA is provided, fetches the last commit on `main`.
- Creates `~/tmp/commit-<short-sha>/` with:
  - `summary.json` — commit info, failed workflows, failed job metadata
  - `<workflow-name>/<job-name>.log` — failed log output

## Phase 2 — Analyze

1. **Read `summary.json`** to get commit message and list of failed workflows/jobs.
2. **Read each `.log` file** and extract failing test names and error messages.
3. **Compile the report**:

```markdown
# CI Health Report — <short-sha>

Commit: `<commit message>`

## Summary
Brief overview: N workflows, N failed jobs, N total test failures.

### Possible regressions
- **N failures** in `test/file.spec.ts` — <brief description>

### Pre-existing / flaky
- **N failures** — <brief description>

## Detailed Failures
### Workflow: <name>
#### <job name> — N failures
| Test | Error |
|------|-------|
| `path/test.spec.ts:line` | error message |
```

4. **Save report** to `ci-failures-<short-sha>.md` in the repo root.
