---
description: Save the latest matching plan into .plans
agent: save_plan
subtask: false
---
Save the latest matching plan artifact from the current conversation.

Requirements:
- if `$ARGUMENTS` is provided, only write to the exact path in `$ARGUMENTS`
- if `$ARGUMENTS` is omitted, infer the target path from the most recent `PLAN_ARTIFACT path=...` marker in the current conversation context
- only accept explicit or inferred normalized relative paths matching `.plans/<kebab-case>.md`
- reject absolute paths, traversal segments, nested directories, or non-markdown targets
- if `$ARGUMENTS` is provided, use only the most recent `PLAN_ARTIFACT path=$ARGUMENTS` marker and the fenced markdown block immediately following it in the current conversation context
- if `$ARGUMENTS` is omitted, use the most recent `PLAN_ARTIFACT path=...` marker in the current conversation context and the fenced markdown block immediately following it
- if the path or matching exact markdown body is missing, stop and report the blocking issue
- do not rewrite the plan's meaning
- write user-facing save status and blocking messages in Korean
- keep plan content, paths, and other technical-document content in English
- report whether the saved target path was explicit or inferred
- re-read the file after saving and confirm it matches
