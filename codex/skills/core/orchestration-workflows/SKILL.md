---
name: orchestration-workflows
description: Main-session workflow for choosing when to stay local, which existing subagent role fits the next bounded task, how to sequence discovery, planning, implementation, review, and validation, and how to keep orchestration procedure out of `AGENTS.md`.
---

# Orchestration Workflows

Use this skill when the task needs execution-shape decisions rather than domain knowledge: which role to use next, whether to stay local, which steps can run in parallel, or how to sequence review and validation without turning `AGENTS.md` into a playbook. Treat `AGENTS.md` as the source of policy and boundary rules; this skill only covers routing and sequencing within those boundaries.

## Role Routing

- `explorer`: breadth-first discovery, affected paths, nearby tests, validation commands, and where to look next.
- `code_mapper`: deep execution tracing from a known file, symbol, diff, stack frame, or runtime anchor.
- `architect`: decision-complete plan synthesis after enough evidence exists.
- `worker`: bounded code changes when the write scope is known.
- `validator`: targeted verification, regression confirmation, or an explicitly requested one-shot pre-fix repro.
- `reviewer`: general risk review when no narrower review axis is clearly dominant.
- `correctness_reviewer`, `compat_reviewer`, `security_reviewer`, `performance_reviewer`, `tests_obs_reviewer`: axis-specific review when the risk surface is already clear.
- `docs_researcher`: official documentation checks, version semantics, or release-behavior confirmation.
- `monitor`: progress tracking for an already-running command, watcher, retrying job, or log stream.
- `pr_explorer`: breadth-first mapping of a concrete diff or branch comparison before deeper review.

## Routing Heuristics

- If the task is still broad and you need entry points, validation paths, or affected files, start with `explorer`.
- If you already have an anchor and the next decision depends on the real execution path, use `code_mapper` instead of another broad scan.
- If enough grounded evidence exists and the remaining problem is execution order, interface impact, or risk framing, use `architect`.
- If the change is small, obvious, and tightly scoped, inspect locally and skip delegation overhead.
- If the task is review-only, stay in review mode. Do not mix implementation into the review pass.
- If the task is verification-only, use `validator` and keep the scope to requested behavior plus justified adjacent regressions.

## Common Sequences

### Discovery-first change

1. `explorer` for breadth-first discovery.
2. `code_mapper` only if a concrete anchor emerges and deep tracing is needed.
3. `planning` if `AGENTS.md` policy says a plan artifact is warranted.
4. `architect` if the main session needs a decision-complete implementation path before editing.
5. `worker` for bounded edits.
6. Independent review.
7. Main-session validation.

### Known-anchor change

1. Inspect locally or use `code_mapper` if execution flow is still unclear.
2. Edit directly or through a bounded `worker`.
3. Run the minimum sufficient independent review.
4. Validate the changed path directly.

### Review-only request

1. Choose the narrowest sufficient review axis. Default to `reviewer` if the axis is not obvious.
2. Keep the pass read-only and finding-focused.
3. If follow-up fixes are needed, return to the main session for scope control before implementation.

### Long-running command

1. Launch or approve the command in the main session.
2. Use `monitor` only for progress, stalling, retry, or blocker reporting.
3. Use `validator` for one-shot result checking, not for watching a live process.

## Sequencing Rules

- Use `planning` for plan-artifact mechanics; do not restate its procedure here.
- Prefer the smallest delegation that removes uncertainty.
- Do not parallelize dependent steps.
- Treat role files as the boundary contract for each delegated specialist.
- Parallelize independent read-only discovery or review passes when they do not determine one another.
- Synthesize parallel evidence in the main session before launching dependent follow-up work.
- Keep handoffs role-neutral: describe the work needed next, not the agent name.
- If a delegated task would require a new side effect, stop and return that requirement to the main session.
- Route repo-tracked writes through a single writer unless there is a deliberate, non-overlapping split.

## Review And Validation Gate

- Apply the review requirement, exceptions, and inconclusive-pass handling from `AGENTS.md`.
- Choose the smallest review surface that is sufficient for the real risk. One focused axis is often enough.
- After review-driven changes, the main session reruns critical-path checks directly or inspects the primary artifacts closely enough to validate the final state.
- Validation proves behavior. Review looks for latent risk. Use both when the task changes behavior.
