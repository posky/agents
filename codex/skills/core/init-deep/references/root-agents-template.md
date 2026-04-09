# Root AGENTS Template

Use this contract for the root `AGENTS.md`. Adapt sections to the repo, but keep the output lean and specific.

## Optional metadata

### Header

- Optional section
- Include `Project name` or a concise label when it is easy to state confidently
- Include `Generated date`, `Short commit`, and `Branch` only when they are cheap to obtain and confident
- Omit unknown header fields instead of inventing or placeholdering them

Only include values you can obtain cheaply and confidently. It is valid to omit the header entirely when it would contain little signal.

## Core sections

### Overview

- 1 to 2 sentences
- State what the project is and the core stack
- Mention only repo-specific architecture facts

### Structure

- Show a compact tree
- Include only important top-level directories and notable nested hotspots
- Annotate each entry with non-obvious purpose only

### Where To Look

Use a table when it helps:

| Task | Location | Notes |
|------|----------|-------|

Include practical lookup routes such as "add tool", "modify hook", "change config schema", "find tests", or equivalent repo-specific workflows.

### Conventions

- List local deviations from normal ecosystem defaults
- Focus on naming, runtime, tests, factories, config shape, module boundaries, or file organization
- Skip generic TypeScript/Python/Go advice

### Anti-Patterns

- Capture explicit "never do X here" rules
- Prefer project-specific forbidden moves over abstract best practices

### Commands

- Include only commands that are real and useful in this repository
- Prefer commands confirmed by primary repo sources such as `package.json`, `Makefile`, `Makefile.toml`, `justfile`, `Taskfile`, `pyproject.toml`, or CI workflows
- Treat existing `AGENTS.md` and `README` as secondary evidence: useful for corroboration, but not a sole confirmation source unless you are explicitly preserving still-valid local guidance
- Prefer build, test, typecheck, lint, doctor, or local dev entrypoints

### Verification

- Optional section
- Use it to state the minimum checks to run after common change types
- Prefer concise mappings such as docs-only, app code, shared library, config, schema, or CI changes
- Reuse only repo-confirmed commands already supported by the `Commands` evidence rule
- Omit the section when the repository has no stable default verification workflow

### Notes

- Keep gotchas, fallback behavior, migration quirks, generated files, logging locations, or deployment caveats here

## Quality gates

- Target roughly 50 to 150 lines
- Prefer telegraphic wording
- Avoid repeated prose paragraphs when a table or terse list is clearer
- Do not include sections with no content signal
- Do not let `Verification` repeat the `Commands` section as a second command list
- Do not duplicate child-file details unless they are needed to orient the whole repo
- Do not list commands discovered only by broad text search unless they were confirmed elsewhere

## Child-file handoff rule

Write the root file so child files are optional and rare. Create a child file only when the user explicitly requests that directory and it has local guidance that should not live in the root. If the root already explains a rule globally, child files should reference only the local exception or extension.
