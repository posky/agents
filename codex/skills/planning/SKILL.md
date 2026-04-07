---
name: planning
description: Main-session-only workflow for choosing, creating, updating, or reconciling task plan files under `.plans/` when `AGENTS.md` planning policy says a plan is warranted. Use when Codex needs to choose a plan file, reuse an existing plan, draft a new one, refresh stale execution notes, or turn planning policy into a concrete execution artifact.
---

# Planning

The main session uses this skill to decide whether a task needs a plan file, reuse an existing plan when possible, and keep the selected plan aligned with real execution state. Treat the plan as an execution artifact, not a diary. When the main session provides a plan artifact to a dependent subagent, that artifact should be treated as required input. Subagents should not create or edit `.plans/` files unless the main session explicitly delegates that side effect.

## Workflow

1. Read the active planning policy in `AGENTS.md` and follow it as the authority for when a plan is required.
2. Apply the plan-file precedence from `AGENTS.md` exactly: user-named file, explicitly carried-forward file from the current task lineage, relevant existing `.plans/` file, then create new.
3. Treat `prior context` as the current task lineage only. Ignore unrelated historical mentions.
4. When evaluating an existing `.plans/` file, treat `relevant` as closest current scope with the newest meaningful evidence that does not depend on stale assumptions likely to confuse execution.
5. Create a new plan only when `AGENTS.md` policy says a plan is warranted and no higher-precedence reusable file fits the current task.
6. Use the standard templates in [templates.md](./references/templates.md) instead of inventing a fresh format.
7. Keep the plan grounded in the current task: record the actual problem, intended outcome, non-goals, constraints, and verification path.
8. Update the plan when execution meaningfully changes state, such as after discovery, implementation, verification, or blockers.
9. Reconcile the plan before finalizing so completed work, residual risks, and verification notes match reality.

## Reuse Rules

- Prefer updating an existing relevant plan over creating a near-duplicate.
- Create a new plan when no higher-precedence file fits, the existing file covers a materially different task, stale assumptions would cause confusion, or the new work deserves independent verification tracking. In those cases, treat the older file as not relevant for precedence purposes.
- If multiple candidate plans exist, choose the one with the closest scope and newest meaningful evidence.
- If candidates tie on `updated_at`, prefer the closer scope. If scope still ties, prefer the file the main session has most recently revalidated in the current task. If the tie still cannot be resolved cleanly, create a new plan instead of guessing.
- When reusing an old plan, replace stale claims instead of appending contradictory notes.

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
