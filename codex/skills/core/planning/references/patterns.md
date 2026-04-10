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

Default shape:

- a short outcome-based checklist
- one direct verification section
- no extra phase structure unless the work starts to branch

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

Common additions:

- phase or slice-based task groups
- explicit checkpoints between phases
- optional human checkpoints when risk or ambiguity is high

## Dependency-First Ordering

Use dependency-first ordering when the implementation sequence is not obvious.

1. Identify the foundations that other work depends on.
2. Order tasks so each step leaves the system in a valid state.
3. Move higher-risk or assumption-heavy tasks earlier when failing fast would save rework.
4. Put checkpoints after meaningful dependency layers, not just at the very end.

Record the dependency logic in the plan only as far as it helps execution. The plan should explain order, not become a full architecture diagram.

## Vertical Slice Pattern

Prefer vertical slices when horizontal phases would hide integration risk.

Good vertical slices usually:

- deliver one coherent user or operator outcome
- include the required cross-layer changes for that outcome
- stay small enough to verify in one focused pass

Avoid slices that say "build all of X" unless the task genuinely is foundational work with no usable intermediate slice.

## Checkpoint Pattern

Add checkpoints when:

- several tasks must land before confidence improves
- the next phase increases blast radius
- a pause helps decide whether to continue, split, or reroute

Good checkpoints verify the current state directly, such as:

- critical tests or targeted checks still pass
- the current slice works end to end
- the system is ready for the next dependency layer

## Task Sizing Pattern

Prefer tasks that fit one focused session and a narrow review surface.

Signals that a task should be split:

- it would likely take more than one focused session
- acceptance criteria cannot stay short and testable
- the title needs "and" to describe the work
- it touches multiple independent subsystems
- the likely file list keeps growing during planning

Use the smallest practical scope labels only as planning aids:

- `XS`: one small edit or decision
- `S`: one focused change across one or two nearby files
- `M`: one vertical slice or compact multi-file change
- `L`: too large; split again

## Parallelization Pattern

Use the plan to record safe parallel boundaries, not to assign agent roles.

Usually safe to parallelize:

- independent slices with no shared contract drift
- tests or documentation for already-stable behavior
- follow-up tasks behind a fixed interface

Usually sequential:

- dependency chains
- shared contract changes
- migrations or other state-shaping work

If parallel work depends on a shared contract, define that contract first and note the boundary in the plan before splitting execution.

## Optional Human Checkpoint Pattern

Human checkpoints are optional risk controls, not default gates.

Consider adding one when:

- the task has external or irreversible impact
- the scope is still ambiguous after discovery
- multiple contributors will rely on a shared contract
- the cost of going down the wrong path is high

Do not require a human checkpoint for routine low-risk work unless the user explicitly asks for one.

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
- Making human approval sound mandatory for routine work.
- Turning checkpoints into vague status meetings instead of concrete go or no-go validations.
