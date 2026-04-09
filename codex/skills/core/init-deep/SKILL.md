---
name: init-deep
description: Create or regenerate a repository root `AGENTS.md` and add child `AGENTS.md` files only when the user explicitly names target directories. Use when Codex needs to initialize repo context, rebuild `AGENTS.md` after a refactor, or conservatively document a repo without auto-generating hierarchy spam.
---

# Init Deep

Inspect a repository, choose the right operating mode first, write the root `AGENTS.md` when the mode calls for output, and add child files only for directories the user explicitly asks to document. Prefer conservative coverage, explicit user intent, and update-in-place over inferred hierarchy.

## Defaults

- Default to `update-in-place` when the user wants documentation changes but does not specify a mode.
- Treat child files as opt-in: create them only when the user explicitly names the target directory.
- Read existing `AGENTS.md` before changing anything.
- Use shell-visible structure and existing repo guidance for discovery.
- Work without LSP by default. If semantic tooling exists, treat it as bonus evidence only.
- Prefer update-in-place unless the user explicitly asks to recreate from scratch.

## Operating Modes

- `discover-only`: inspect and summarize likely documentation surfaces without writing any `AGENTS.md` files
- `update-in-place`: preserve and revise existing `AGENTS.md` files
- `recreate`: read existing guidance for context, then replace the relevant files

Apply a write gate before editing files: if the active mode is `discover-only`, do not write or update any `AGENTS.md`.

## Workflow

### 1. Read existing guidance first

- Read existing `AGENTS.md` before planning replacements.
- Preserve project-specific commands, conventions, forbidden changes, and local warnings unless they are clearly stale.
- If the user wants a clean rebuild, still mine the current files for non-obvious repo knowledge before replacing them.

### 2. Discover the repository shape

Use lightweight discovery commands from [discovery-heuristics.md](./references/discovery-heuristics.md) to understand:

- the top-level structure
- source roots and test locations
- existing local guidance files
- real commands and conventions worth preserving

Do not infer child `AGENTS.md` targets from discovery alone.

### 3. Decide the documentation scope

- Treat the root file as mandatory only in `update-in-place` and `recreate` modes.
- Default to root-only output.
- Add child files only when the user explicitly requests a named directory such as `apps/web` or `packages/cli`.
- When a user names a directory, confirm there is real local delta to document before creating a child file.
- Prefer skipping ambiguous or weak child requests rather than creating placeholder hierarchy.

### 4. Write the root file first

- Include a repo-wide overview, structure, where-to-look map, conventions, anti-patterns, commands, notes, and optional verification guidance when the repository has a stable verification workflow.
- Keep wording telegraphic and project-specific.
- Include generated date, branch, and short commit only when they are cheap to obtain and clearly available.
- Avoid restating generic language or framework knowledge unless this repo deviates from it.
- Include only commands that are confirmed by primary repository sources or clearly preserved from existing guidance.
- Treat `Verification` as policy, not as a second command dump: summarize the minimum checks to run after common change types only when those checks are supported by repository evidence.

Use [root-agents-template.md](./references/root-agents-template.md) as the section contract and quality gate.

### 5. Write child files only for explicitly requested local deltas

- Keep child `AGENTS.md` files short, usually 30 to 80 lines.
- Describe only what the parent does not already cover: local responsibilities, substructure, entrypoints, invariants, test patterns, and nearby anti-patterns.
- Do not duplicate repo-wide commands, global conventions, or obvious directory names.
- If a named directory has no strong local guidance to add, do not create a file there.
- Root-only output is the default success case.

### 6. Review before finalizing

- Remove generic advice, filler, and repeated parent content.
- Check that every child file has a clear reason to exist.
- Verify the root file can stand alone as the primary orientation document.
- Confirm the final hierarchy is sparse, plausible, and easy for future agents to follow.

## Shell Workflow

Use the portable shell workflow in [discovery-heuristics.md](./references/discovery-heuristics.md). Root-only is the default. Do not create child files unless the user explicitly names a target subdirectory and local evidence still shows a meaningful local delta.

## Optional User Intents

Map natural-language requests onto the same workflow:

- "update existing" means use `update-in-place`
- "recreate from scratch" means use `recreate`
- "root only" means write only the root file even if the user mentions hierarchy in passing
- "also write for `path/to/dir`" means create a child file only for that named directory if local evidence justifies it
- "show me the structure first" means use `discover-only`: run discovery commands and summarize likely documentation surfaces without writing files

## Commands Evidence Rule

Collect candidate commands using evidence tiers:

- Primary sources: `package.json`, `Makefile`, `Makefile.toml`, `justfile`, `Taskfile`, `pyproject.toml`, CI workflows
- Secondary sources: existing `AGENTS.md`, `README`
- Tertiary sources: broad repository text search

Use broad text search only to discover leads. Include a command in the final `Commands` section only when it is confirmed by a primary source or clearly preserved from existing guidance that still matches the repo.

## Verification Guidance Rule

- Add a `Verification` section only when the repository exposes a stable verification routine through primary sources or clearly preserved existing guidance.
- Keep it brief and change-type oriented, for example docs-only, app code, shared library, config, schema, or CI changes.
- Reference real commands already supported by the evidence rule instead of introducing new command variants.
- Omit the section when the repository has no clear default verification expectations or when the workflow is too team-specific to state confidently.

## Validation

- If the mode is `update-in-place` or `recreate`, confirm the root `AGENTS.md` was written or updated.
- If the mode is `discover-only`, confirm no `AGENTS.md` files were written.
- Confirm every child `AGENTS.md` corresponds to an explicitly named directory from the user request.
- Check that each child file adds local guidance instead of repeating the parent.
- Check that header metadata appears only when it was cheap to obtain and confident.
- Check that listed commands were confirmed by the commands evidence rule.
- Check that any `Verification` section is optional, evidence-based, and does not duplicate the `Commands` section.
- Sanity-check config-heavy or docs-heavy directories manually when the repository contains many data files, fixtures, or generated metadata.
- When evidence is ambiguous, choose fewer child files and explain the omission in your working notes rather than inventing certainty.
