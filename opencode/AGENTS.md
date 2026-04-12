# AGENTS.md

Prefer small, safe, well-verified changes. Read code before editing, avoid guesses, and follow the project's existing patterns.

## Core Rules

- Inspect the relevant files and direct usages before changing code. Read enough context to understand the behavior you are modifying.
- Prefer the smallest correct change set. Do not broaden scope with unrelated refactors unless they are clearly needed.
- Follow existing project conventions, architecture, and naming before introducing new structure.
- Write user-facing explanations, summaries, status updates, and clarification messages in Korean unless a prompt explicitly requires another language. Keep code, code comments, diffs, `.plans/*.md` artifacts, and technical documents in English.
- Record assumptions briefly when they affect behavior, scope, or verification.
- Never commit or log secrets. Validate inputs and normalize or encode outputs where appropriate.
- Do not ignore warnings, failed checks, or unexpected side effects.

## Decision Making

- For non-trivial changes, compare at least two approaches briefly and choose the simplest one that meets the goal.
- Treat new abstractions, new dependencies, and hardcoded thresholds as choices that need justification.
- Ask the user only when a decision materially changes behavior, architecture, scope, or risk.

## Implementation

- Use intention-revealing names and explicit code.
- Keep functions and files manageable, but favor local clarity over arbitrary numeric limits.
- Isolate I/O, network access, and global state at the boundaries when practical.
- Prefer specific error handling and clear failure messages over broad exception swallowing.
- Add comments only when they explain non-obvious intent, constraints, or tradeoffs.

## Verification

- Run the narrowest useful checks first, then broaden verification when the scope or risk warrants it.
- Add or update tests for behavioral changes when the project has a test harness and the change justifies it.
- For bug fixes, prefer a regression test when practical.
- If verification cannot run, state what remains unverified and the resulting risk.

## Planning And Delegation

- For multi-step, resumable, or review-heavy work, create or update a `.plans/*.md` artifact before major implementation.
- When a plan file exists, read it before editing and keep it reconciled as discovery, implementation, or verification changes the grounded state.
- Keep user interaction, scope control, and final decisions in the primary agent.
- Use subagents for bounded discovery, implementation, validation, or review only when they reduce noise or improve confidence.
- Keep subagents read-only by default. If repo-tracked non-plan edits are delegated, use a single writer path. Keep `.plans/*.md` materialization or reconcile with the responsible primary agent.
- Treat delegated verification as supporting evidence, not final proof; rerun or directly inspect the critical path before finalizing.

## Scope Guards

- Keep tasks, commits, and pull requests small when possible.
- Do not make silent product or architecture decisions that are not grounded in the request or the codebase.
- Avoid premature abstraction, speculative optimization, and broad cleanup outside the task.
