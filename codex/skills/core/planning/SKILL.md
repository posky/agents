---
name: planning
description: Main-session-only workflow for choosing, creating, updating, or reconciling task plan files under `.plans/` when `AGENTS.md` planning policy says a plan is warranted. Use when Codex needs to choose a plan file, reuse an existing plan, draft a new one, refresh stale execution notes, or turn planning policy into a concrete execution artifact.
---

# Planning

The main session uses this skill to decide whether a task needs a plan file, reuse an existing plan when possible, and keep the selected plan aligned with real execution state. Treat the plan as an execution artifact, not a diary. Follow `AGENTS.md` for planning policy, ownership, and precedence; this skill covers how to apply that policy to a concrete plan artifact.

## Workflow

1. Read the active planning policy in `AGENTS.md` and follow it as the authority for when a plan is required.
2. Stay in planning mode while shaping the artifact: gather evidence, map dependencies, and structure the work before mixing implementation details into the plan.
3. Treat `prior context` as the current task lineage only. Ignore unrelated historical mentions.
4. Create a new plan only when `AGENTS.md` policy says a plan is warranted and no policy-compliant reusable file fits the current task.
5. Use the standard templates in [templates.md](./references/templates.md) instead of inventing a fresh format.
6. Keep the plan grounded in the current task: record the actual problem, intended outcome, non-goals, constraints, and verification path.
7. Use [patterns.md](./references/patterns.md) when the work needs explicit decomposition guidance such as dependency ordering, vertical slices, checkpoints, or optional human checkpoints.
8. Update the plan when execution meaningfully changes state, such as after discovery, implementation, verification, or blockers.
9. Reconcile the plan before finalizing so completed work, residual risks, and verification notes match reality.

## Reuse Rules

- Apply the precedence and reuse policy from `AGENTS.md` rather than rewording it here.
- When an existing file covers a materially different task or would confuse execution with stale assumptions, treat it as not reusable for the current task.

## Naming And Placement

- Store plan files in `.plans/`.
- Use short, descriptive, hyphenated filenames tied to the task outcome.
- Prefer filenames that stay valid after the task evolves slightly; avoid timestamps or temporary wording unless the user explicitly wants them.
- If the user names a file, preserve that choice as the active artifact. If the user also points to an existing plan, reuse that older file only as source material to merge forward into the user-named file.

## Update Discipline

- Update `updated_at` whenever the plan changes in a meaningful way.
- Move checklist items to done only when the stated outcome has actually been met on explicit evidence.
- Replace stale statements with current evidence rather than letting the plan accumulate conflicting history.
- Keep notes brief. The plan should help execution and handoff, not narrate every command.

## References

- Use [templates.md](./references/templates.md) for the standard frontmatter and section structure.
- Use [patterns.md](./references/patterns.md) to choose between a lightweight plan and a richer execution-tracking plan.
- Use [examples.md](./references/examples.md) when you need a concrete example for a new plan or for a mid-stream update.

## Validation

- Confirm the selected plan file matches the current task scope.
- Confirm frontmatter uses the standard fields and valid values from [templates.md](./references/templates.md).
- Confirm the core required sections are present and the body is concise.
- Confirm optional sections are present only when they materially help execution, verification, or handoff.
- Confirm checklist state, verification notes, and outcome claims match the latest grounded evidence.
- Before finalizing, read the final plan once as a consumer: it should explain what is happening, what remains, and what was verified without requiring the full chat log.
