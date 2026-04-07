---
task: tighten planning policy-skill split
status: done
updated_at: 2026-04-07
---

## Context

`codex/AGENTS.md` was reduced to planning policy while detailed plan-writing guidance moved into `codex/skills/planning/`. Review found that the split direction is correct, but the current policy boundary and skill contract are still inconsistent.

## Problem

The current planning guidance has three gaps:

- `AGENTS.md` can require a plan without preserving enough standalone safety for plan shape.
- The planning skill and references disagree on which sections and checklist structures are required versus optional.
- Scope, authority, and example text still contain ambiguity or stale references.

## Goal

Make the planning split internally consistent so:

- `AGENTS.md` stays policy-level without becoming unsafe on its own.
- The planning skill becomes the unambiguous operational source of truth.
- Plan selection, mutation authority, and examples are consistent across the files.

## Non-Goals

- Reworking unrelated skills or agent role files.
- Introducing a new planning system beyond the current `.plans/` workflow.
- Expanding planning requirements for trivial tasks.

## Constraints

- Keep the policy/skill split intact instead of moving all detailed formatting rules back into `AGENTS.md`.
- Preserve the existing high-level planning triggers and precedence unless a contradiction requires clarification.
- Keep examples concise and repo-accurate.

## Plan

- [x] Decide the minimum standalone guarantees `AGENTS.md` must retain
  Keep only the smallest policy-level contract needed so main-session behavior remains safe even when the planning skill is not explicitly loaded.
- [x] Normalize the planning skill contract
  Make required versus optional sections, checklist usage, and validation rules agree across `SKILL.md`, `templates.md`, and `patterns.md`.
- [x] Clarify authority boundaries
  Remove or rewrite text that conflicts with main-session-only scope, especially around subagent behavior and who may mutate `.plans/`.
- [x] Resolve plan-selection ambiguity
  Tighten the rule for user-named files versus reused plans and define a deterministic tie-break when “newest meaningful evidence” is otherwise ambiguous.
- [x] Clean up stale examples and references
  Replace repo-inaccurate paths or nonexistent helper references in the planning examples.
- [x] Verify the final document set
  Re-read `codex/AGENTS.md` and the planning skill references together to confirm a single coherent workflow with no contradictory instructions.

## Findings

- `AGENTS.md` now keeps a minimal fallback contract for plan shape while leaving the detailed workflow in the planning skill.
- The planning skill and references now distinguish core required sections from conditional `Plan` and `Verification` sections.
- Reuse versus split behavior is now explicit: independent verification or blocker tracking makes the older plan non-relevant.
- User-visible example paths were updated to match the actual `codex/skills/planning/` layout.

## Outcome

The planning policy and planning skill now divide responsibilities more cleanly:

- policy decides when a plan is required, what fallback guarantees must hold, and who controls plan-file edits
- the skill defines how to choose, shape, update, and validate `.plans/` artifacts

## Open Risks

- If `AGENTS.md` retains too little structure, malformed plan files remain possible when the skill is not invoked.
- If it retains too much procedure, the policy/skill split becomes muddy again.

## Verification

- Re-read `codex/AGENTS.md`, `codex/skills/planning/SKILL.md`, and the planning references after editing.
- Ran a follow-up reviewer pass on the updated documents and addressed the remaining ambiguity it found around fallback structure, plan splitting, and dependent subagent input.
- Performed a final direct read of the updated policy, skill, templates, patterns, and examples to confirm the post-fix text is internally consistent.
