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

Leave policy-level planning rules in `AGENTS.md` and move the detailed workflow, templates, and examples into `codex/skills/planning/`.

## Non-Goals

- Reworking unrelated skills
- Introducing a new plan format

## Constraints

- `AGENTS.md` must remain safe on its own if the skill does not load.
- The resulting skill must stay concise and use references for detail.

## Plan

- [x] Define the policy versus skill boundary
- [ ] Update `AGENTS.md`
- [ ] Create `codex/skills/planning/`
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

`AGENTS.md` is being reduced to policy-only planning guidance, with the detailed workflow moving into `codex/skills/planning/`.

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

The planning skill needs branded assets for `codex/skills/planning/agents/openai.yaml`.

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
