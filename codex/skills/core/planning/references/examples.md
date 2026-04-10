# Planning Examples

Use these as compact models. Adapt them to the task instead of copying them mechanically.

## Example: New Multi-Step Plan

```md
---
task: split planning policy and skill
status: in_progress
updated_at: 2026-04-07
---

## Context

`AGENTS.md` currently mixes planning policy with detailed formatting and workflow guidance.

## Problem

The global policy document is carrying detailed plan-writing rules that would be better maintained in a dedicated skill.

## Goal

Leave policy-level planning rules in `AGENTS.md` and move the detailed workflow, templates, and examples into the planning skill.

## Non-Goals

- Reworking unrelated skills
- Introducing a new plan format

## Constraints

- `AGENTS.md` must remain safe on its own if the skill does not load.
- The resulting skill must stay concise and use references for detail.

## Plan

- [x] Define the policy versus skill boundary
- [ ] Update `AGENTS.md`
- [ ] Create the planning skill structure
- [ ] Verify the new documents are internally consistent

## Verification

- Pending
```

## Example: Mid-Execution Update

```md
---
task: split planning policy and skill
status: in_progress
updated_at: 2026-04-07
---

## Context

`AGENTS.md` is being reduced to policy-only planning guidance, with the detailed workflow moving into the planning skill.

## Problem

The detailed plan-writing instructions are still global, which makes the root guidance longer and harder to evolve.

## Goal

Finish the split with a policy-only `AGENTS.md` section and a usable planning skill.

## Non-Goals

- Adding scripts that are not required for the split

## Constraints

- The skill should work even if extra local tooling is unavailable.

## Plan

- [x] Define the split
- [x] Draft the policy-only `AGENTS.md` section
- [x] Create the planning skill structure
- [ ] Reconcile the plan and verify the resulting files

## Findings

- The document set still needs one consistency pass across policy text, templates, and examples.

## Verification

- Manually reviewed the new files for trigger wording, section structure, and reference links.
```

## Example: Blocked Plan

```md
---
task: add planning skill assets
status: blocked
updated_at: 2026-04-07
---

## Context

The planning skill needs branded assets for its agent configuration.

## Problem

The user has not provided the required asset files.

## Goal

Add the requested icons once the assets are available.

## Non-Goals

- Inventing substitute branding

## Constraints

- Only user-provided assets may be used.

## Plan

- [x] Confirm the required asset paths
- [ ] Add the assets to the skill

## Open Risks

- The UI metadata will remain text-only until the assets arrive.

## Verification

- Blocked on missing inputs; no asset validation performed.
```

## Example: Vertical Slice Plan With Checkpoints

```md
---
task: add review thread summary flow
status: in_progress
updated_at: 2026-04-10
---

## Context

The current GitHub helper can fetch review comments, but it does not produce a concise unresolved-thread summary for the main session.

## Problem

Addressing review feedback is slower than it should be because unresolved-thread context must still be reconstructed manually.

## Goal

Add a resumable implementation plan that introduces unresolved-thread summarization in small, verifiable slices.

## Non-Goals

- Reworking unrelated PR triage flows
- Adding write-back or auto-reply behavior

## Constraints

- Keep the first slice read-only
- Preserve the existing GitHub helper contract unless a later slice justifies a change

## Plan

### Phase 1: Foundation

- [ ] Task 1: Identify the unresolved-thread data shape
  Description: Confirm the minimum fields needed to summarize unresolved threads without changing tool behavior yet.
  Acceptance Criteria:
  - [ ] Required fields for thread identity, state, and latest comment are listed
  - [ ] Any contract uncertainty is called out explicitly
  Verification:
  - [ ] Read the current helper and one representative PR thread payload
  Dependencies: None
  Files Likely Touched:
  - `plugins/github/...`
  Estimated Scope: S

### Checkpoint

- [ ] The required thread-summary contract is explicit before implementation starts

### Phase 2: First Vertical Slice

- [ ] Task 2: Return one unresolved-thread summary path end to end
  Description: Add one working summary path that maps raw thread data into a compact unresolved-thread result.
  Acceptance Criteria:
  - [ ] One unresolved thread can be summarized without manual reconstruction
  - [ ] Existing consumers remain valid or are updated in the same slice
  Verification:
  - [ ] Targeted local validation covers one representative unresolved thread
  Dependencies: Task 1
  Files Likely Touched:
  - `plugins/github/...`
  - `tests/...`
  Estimated Scope: M

## Human Checkpoints

- Optional: Pause before Phase 3 if the shared contract still feels ambiguous or if downstream consumers need human sign-off on the summary shape.

## Verification

- Pending
```
