# Planning Patterns

Choose the lightest plan shape that still makes execution and verification easy to follow.

## Lightweight Plan

Use this pattern when the work has a clear path but still benefits from tracking:

- a few discrete steps
- one writer
- low coordination overhead
- straightforward verification

Core required sections:

- `Context`
- `Problem`
- `Goal`
- `Non-Goals`
- `Constraints`

Usually include:

- `Plan`
- `Verification`

## Execution-Tracking Plan

Use this pattern when the work is likely to evolve during execution:

- multiple phases
- coordination across agents or contributors
- meaningful discovery before implementation
- resumable work
- blocker tracking or risk tracking

Recommended extra sections:

- `Progress`
- `Findings`
- `Open Risks`
- `Outcome`

## Reuse Pattern

When continuing an existing task:

1. Read the current plan before starting new work.
2. Decide whether the scope still matches.
3. Replace stale assumptions with current evidence.
4. Update checklist state and verification notes after each meaningful milestone.
5. Reconcile the final result before closing the task.

## Split Pattern

Create a separate plan instead of stretching the current one when:

- the goal changed materially
- verification needs are independent
- the old plan’s history now obscures the current task
- the user explicitly asked for a separate artifact

## Anti-Patterns

- Using a plan for trivial one-step edits.
- Treating the plan as a full transcript of commands.
- Letting stale discovery notes survive after the implementation disproves them.
- Leaving checklist items ambiguous enough that “done” is subjective.
- Marking `done` while verification is still materially incomplete without calling that out explicitly.
