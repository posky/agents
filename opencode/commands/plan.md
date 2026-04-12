---
description: Prepare an execution-ready plan artifact
agent: plan
---
Turn the current request into an execution-ready implementation plan.

Use `$ARGUMENTS` as the primary goal when it is provided. Otherwise use the current conversation goal.

Requirements:
- inspect relevant local code and config before making claims
- choose the correct `.plans/*.md` path when a save-ready plan exists
- do not claim the plan file was already written
- write user-facing explanations, section headings, and status messages in Korean
- keep code, inline code, `.plans/*.md` artifact bodies, and other technical-document content in English
- if important decisions remain open or the plan is not ready for build, return a concise planning status instead of forcing exact markdown output
- only put the exact markdown body inside a fenced block when the plan is ready to save
- if the user explicitly asks to see draft markdown for an incomplete plan, show it only as a clearly labeled draft preview without a `PLAN_ARTIFACT` marker
- when returning exact markdown, place it inside a fenced block immediately preceded by a marker line in this exact form: `PLAN_ARTIFACT path=.plans/your-plan-name.md`

If clarification is required or the plan is not yet save-ready, return exactly these sections:
1. 이해한 내용
2. 준비를 막는 점
3. 빌드 준비 여부
4. 다음 행동

If the user explicitly asked to see draft markdown for an incomplete plan, append:
5. 초안 마크다운

Otherwise, when the plan is save-ready, return exactly these sections:
1. 계획 경로
2. 빌드 준비 여부
3. 열린 결정사항
4. 정확한 마크다운
