# Discovery Heuristics

Use shell-visible repository evidence to orient the root `AGENTS.md`. Discovery helps map the repo; it does not authorize child `AGENTS.md` creation by itself.

## Default approach

- Inspect existing `AGENTS.md` files first.
- Determine the operating mode before writing: `discover-only`, `update-in-place`, or `recreate`.
- Map the top-level structure and likely source roots.
- Find test locations, entrypoints, real project commands, and any stable verification routines.
- Default to writing only the root `AGENTS.md` when the mode is a writing mode.
- Consider a child file only when the user explicitly names the directory.

## Common exclusions

Ignore common noise such as:

- `.git`
- `node_modules`
- `dist`
- `build`
- `.venv`
- `.next`
- `coverage`
- cache, generated, vendor, and Python bytecode folders

If the repository has additional generated trees, exclude them manually while inspecting the layout.

## When to create a child file

Create a child `AGENTS.md` only when both conditions hold:

- the user explicitly names the target directory
- the directory has real local guidance that the root file should not absorb

Examples of acceptable local delta:

- distinct entrypoints or lifecycle commands
- local invariants or forbidden edits
- separate test workflow or fixture rules
- generated files or migration quirks that are local to that subtree

If the named directory adds no real local delta, skip the child file and keep the guidance in the root.

## Shell discovery commands

### Command evidence tiers

Treat command discovery as evidence-ranked:

- Primary: `package.json`, `Makefile`, `Makefile.toml`, `justfile`, `Taskfile`, `pyproject.toml`, CI workflows
- Secondary: existing `AGENTS.md`, `README`
- Tertiary: targeted text search in likely task documentation

Use secondary evidence for corroboration, not as a sole confirmation source, unless you are explicitly preserving still-valid local guidance. Use tertiary evidence only to find candidates that you then confirm against stronger evidence.

When deciding whether to add a root `Verification` section, prefer workflows that are explicit in primary sources such as CI jobs, package scripts, make targets, or task runners. Treat ad hoc README advice as supporting evidence, not enough by itself unless it is clearly preserved local policy.

### Existing guidance files

```bash
find . -type f -name 'AGENTS.md' \
  -not -path '*/.git/*' \
  -not -path '*/node_modules/*'
```

Extract commands, local conventions, forbidden changes, and directory-specific notes worth preserving.

### Quick repository scan

```bash
find . -type d \
  -not -path '*/.git/*' \
  -not -path '*/node_modules/*' \
  -not -path '*/dist/*' \
  -not -path '*/build/*'
```

```bash
find . -type f \
  -not -path '*/.git/*' \
  -not -path '*/node_modules/*' \
  | sed 's|/[^/]*$||' \
  | sort | uniq -c | sort -rn | head -30
```

Use these results to spot source roots, unusually dense directories, and nested module clusters.

### Language mix

```bash
find . -type f \( -name '*.ts' -o -name '*.tsx' -o -name '*.js' -o -name '*.py' -o -name '*.go' -o -name '*.rs' \) \
  -not -path '*/node_modules/*' \
  | sed 's|/[^/]*$||' \
  | sort | uniq -c | sort -rn | head -30
```

### Boundary markers

```bash
rg --files | rg '(^|/)(index|main|cli|app|server|__init__)\.'
```

### Primary command sources

```bash
find . \( -name package.json -o -name Makefile -o -name Makefile.toml -o -name justfile -o -name Taskfile -o -name pyproject.toml \) \
  -not -path '*/.git/*' \
  -not -path '*/node_modules/*'
```

```bash
find . -path '*/.github/workflows/*' -type f
```

### Secondary command sources

```bash
find . \( -name AGENTS.md -o -name README -o -name README.md \) \
  -not -path '*/.git/*' \
  -not -path '*/node_modules/*'
```

### Tertiary command search

Tertiary search is optional and left to agent judgment.

- Keep it narrow and prefer likely task documentation such as `README*`, `docs/**`, or existing `AGENTS.md`
- Do not use repo-wide key-pattern scans as a default command discovery step
- Do not promote tertiary-only findings into the final `Commands` section without stronger corroboration

### Targeted lookup for a named child directory

```bash
find path/to/target -type f \
  -not -path '*/node_modules/*' \
  -not -path '*/dist/*' \
  -not -path '*/build/*'
```

```bash
rg -n 'TODO|FIXME|generated|do not edit|fixture|mock|migration|entrypoint|bootstrap' path/to/target
```

Adjust `path/to/target` to the explicitly requested directory.

## Conservative policy

If discovery is incomplete or noisy:

- in `update-in-place` or `recreate`, write only the root file
- in `discover-only`, write nothing
- treat root-only output as the default, not as a degraded fallback
- only consider a child file when the user explicitly names the directory and the local evidence still shows a distinct responsibility
- prefer omission over speculative documentation
