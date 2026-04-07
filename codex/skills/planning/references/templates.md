# Planning Templates

Use these templates as the default standard for `.plans/` artifacts. Keep them concise and adapt only when the task genuinely needs more structure.

## Standard Rules

- Keep YAML frontmatter limited to `task`, `status`, and `updated_at`.
- Keep `task` short and descriptive.
- Use one of these `status` values only: `in_progress`, `blocked`, `done`.
- Format `updated_at` as `YYYY-MM-DD`.
- Keep the substantive content in the Markdown body, not in frontmatter.
- Always include these core required sections in this order unless there is a strong reason not to: `Context`, `Problem`, `Goal`, `Non-Goals`, `Constraints`.
- Add `Plan` when explicit task tracking would otherwise be unclear. Add `Verification` when checks, residual risk, or blocked validation need to be recorded. For most non-trivial plans, include both.
- Add other optional sections only when they improve execution, verification, or handoff.

## Baseline Template

Use this as the default shape for a non-trivial plan:

```md
---
task: short task label
status: in_progress
updated_at: 2026-04-07
---

## Context

Short background that explains why the task exists now.

## Problem

What is wrong, missing, or uncertain.

## Goal

What completion looks like.

## Non-Goals

What this task will not do.

## Constraints

Hard limits, permissions, dependencies, or quality bars.

## Plan

- [ ] Discovery
- [ ] Implementation
- [ ] Verification

## Verification

- Pending, or brief notes about what was checked.
```

## Recommended Optional Sections

- `Progress`: Use when the task will span multiple passes and the current state matters.
- `Findings`: Use when discovery work produces facts that affect implementation.
- `Open Risks`: Use when unresolved risk needs to be tracked explicitly.
- `Outcome`: Use near the end to summarize what changed and what remains unverified.

## Checklist Rules

- Use short checkbox items when they improve tracking of deliverables, blockers, or verification.
- Do not force a checkbox list into every plan; use it when it adds clarity.
- Mark an item done only when the item’s stated outcome has actually happened.
- Add a short note under an item when the reason for completion would not otherwise be obvious.
- Prefer outcome-based items over command-based items.

Good:

- `[ ] Add policy-only Planning section to AGENTS.md`
- `[ ] Validate the planning skill references and trigger text`

Weak:

- `[ ] Think about edits`
- `[ ] Run some commands`

## Reconciliation Rules

- Update `status` to `done` only when the requested outcome has been achieved.
- Use `blocked` when the task cannot proceed and the blocker is explicit.
- Remove or rewrite stale statements that conflict with the current result.
- Keep verification notes tied to the real checks that were performed.
