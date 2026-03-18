---
name: conventional-commits
description: Use when inspecting the current git changes, splitting them into small logical commits, drafting Conventional Commit messages, and creating commits only after the user approves the proposed plan.
---

# Conventional Commits

Inspect the current worktree, propose a small commit series, and commit only after the user confirms the plan. Keep commit headers in English and write an optional body in Korean only when extra context is useful.

## Workflow

1. Read `references/conventional-commits.md` before drafting any commit message.
2. From the target repo root, run `python3 /path/to/this-skill/scripts/inspect_git_changes.py --format markdown` to collect branch, status, staged and unstaged diff summaries, and an explicit untracked-file inventory. Resolve the script path from the installed skill directory, not from `.codex/` inside the repo.
3. Review the actual diff for the candidate files before deciding commit boundaries.
4. Ignore obvious junk files such as `.DS_Store` unless the user explicitly wants them included.
5. Split changes into the smallest safe logical units at file level.
6. If the same file mixes unrelated changes, stop and ask instead of forcing hunk-level staging.
7. Present the proposed commit sequence first. Include the files in each commit, the commit header, and whether a Korean body is needed.
8. After approval, stage only the files for the current commit, create the commit, then re-check the remaining worktree before continuing.

## Message Rules

- Follow the structure `<type>[optional scope]: <description>`.
- Write the type and short description in English.
- Use a scope only when it adds clarity.
- Prefer concise lowercase headers without a trailing period.
- Write an optional body in Korean only when the header alone is not enough to explain intent, rationale, or notable tradeoffs.
- Add footers only when the spec or context requires them.
- Mark breaking changes with `!` in the header or a `BREAKING CHANGE:` footer exactly as described in `references/conventional-commits.md`.

## Type Selection

- Use `feat` for new user-facing or API-facing functionality.
- Use `fix` for bug fixes.
- Use other conventional types such as `docs`, `refactor`, `test`, `build`, `ci`, `chore`, `perf`, `style`, or `revert` when they better match the change.
- Prefer the most specific valid type instead of defaulting everything to `chore`.

## Commit Execution

- Use non-interactive Git commands.
- Stage files explicitly with `git add -- <paths>`.
- Use `git commit -m "<header>"` when no body is needed.
- Use additional `-m` paragraphs for a Korean body or footers when needed.
- After each commit, run `git status --short` and confirm only the expected changes remain.
- If the working tree contains unrelated changes that make the split unsafe, report that clearly before committing.

## Script

Use `scripts/inspect_git_changes.py` as the skill-bundled inventory script. Resolve it from the installed skill directory while running it from the target repo root. The script is intentionally read-only: it summarizes the current worktree, keeps Git status paths in their raw porcelain form, reports staged and unstaged diff summaries, and exposes untracked files explicitly. It does not decide commit boundaries and it must not create commits.

## Reference

Use `references/conventional-commits.md` as the skill-local source of truth for:

- commit structure
- required `feat` and `fix` usage
- optional scope rules
- body and footer formatting
- breaking change markers

## Output Format

When proposing a commit series, keep the response compact and concrete:

- One item per proposed commit
- Conventional Commit header in English
- Optional Korean body only when needed
- File list for the commit
- Any blocker or ambiguity called out explicitly
