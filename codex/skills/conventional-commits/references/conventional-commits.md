# Conventional Commits Reference

Use this file as the local source of truth for commit-message formatting in this skill.

## Required Structure

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

- The header must start with a type such as `feat`, `fix`, or another conventional noun.
- A scope is optional and must be a noun in parentheses, such as `feat(api):`.
- The description must immediately follow `: ` and act as a short summary.

## Type Rules

- Use `feat` when the commit adds a new feature.
- Use `fix` when the commit represents a bug fix.
- Other allowed conventional types include `build`, `chore`, `ci`, `docs`, `perf`, `refactor`, `revert`, `style`, and `test`.

## Body Rules

- A body is optional.
- If present, it starts one blank line after the header.
- In this skill, keep the optional body in Korean.

## Footer Rules

- Footers are optional and start one blank line after the body.
- Each footer uses a token plus `: ` or ` #`, for example `Refs: #123`.
- Use `-` instead of spaces in footer tokens, except `BREAKING CHANGE`.

## Breaking Changes

- A breaking change must be marked either with `!` before `:` in the header or with a `BREAKING CHANGE:` footer.
- If `!` is used in the header, the footer may be omitted.
- `BREAKING CHANGE` must stay uppercase.

## Practical Guidance

- Prefer lowercase commit headers without a trailing period.
- Use scope only when it adds useful context.
- Keep commits small and logically coherent whenever possible.
