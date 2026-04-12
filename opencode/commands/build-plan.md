---
description: Build from a saved .plans artifact
agent: build
---
Implement the saved plan stored at `$ARGUMENTS`.

Requirements:
- stop if `$ARGUMENTS` is missing
- only accept normalized relative paths matching `.plans/<kebab-case>.md`
- reject absolute paths, traversal segments, nested directories, or non-markdown targets
- read the selected `.plans/*.md` artifact before editing
- stop if the plan is missing, blocked, incomplete, already done, or not ready for build
- restate the goal, scope, and verification target before making changes
- keep edits within the saved plan scope
- write user-facing status updates, summaries, and verification results in Korean
- keep code, diffs, `.plans/*.md` content, and other technical-document content in English
- run the smallest useful verification and report what was checked
- reconcile only execution-grounded plan sections after implementation
