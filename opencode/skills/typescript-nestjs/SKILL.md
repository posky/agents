---
name: typescript-nestjs
description: "TypeScript and NestJS architecture patterns for broader server implementation, refactor, and design work: module boundaries, controllers, services, providers, DTO validation, Swagger decorators, guards, interceptors, exception filters, configuration, and tests. Use when Codex needs to read, create, refactor, or document NestJS TypeScript features, wire modules and providers, design DTOs, validate request and response shapes, or add unit and e2e coverage. For documentation-only Swagger or JSDoc updates without behavioral or architectural changes, prefer `nestjs-swagger-jsdoc`."
---

# TypeScript NestJS

## Overview

Use this skill to keep broader NestJS server changes type-safe, modular, and easy to reason about.
Prefer feature-local structure, thin transport layers, explicit provider boundaries, and validation that matches the real runtime contract.
Treat this skill as a decision guide for controllers, services, providers, modules, DTOs, Swagger decorators, guards, interceptors, filters, and tests when the task includes implementation, refactoring, contract changes, or architecture decisions.
If the task is only to add or refine Swagger/JSDoc documentation without changing behavior or architecture, prefer `nestjs-swagger-jsdoc`.

## Required Workflow

1. Read the target file end to end before editing.
2. Read the enclosing module, directly used DTOs, injected providers, guards, interceptors, filters, and nearby tests before changing behavior.
3. Trace request flow from controller entry to service orchestration, persistence or adapter boundary, and exception path before reshaping APIs.
4. Check module registration, exports, and injection tokens before adding or moving providers.
5. If the request is documentation-only Swagger or JSDoc work, stop and prefer `nestjs-swagger-jsdoc`; otherwise, when implementation work also touches API documentation, read the referenced DTOs, response wrappers, interceptors, and existing Swagger helper patterns before changing decorators.
6. Reuse repository patterns for folder layout, decorators, validation, error mapping, Swagger docs, and tests unless they are clearly broken.
7. Keep scope local to the requested feature unless the user asks for broader cleanup.

## Project Structure

Prefer feature-first layout with a small shared layer for cross-cutting concerns.
Use this as a shape example, not a mandatory directory contract.

```text
src/
├── users/
│   ├── dto/
│   ├── types/
│   ├── users.controller.ts
│   ├── users.service.ts
│   └── users.module.ts
├── common/
│   ├── decorators/
│   ├── filters/
│   ├── guards/
│   ├── interceptors/
│   └── utils/
├── config/
├── app.module.ts
└── main.ts
```

- Keep feature code under `src/<feature>/` by default.
- Add subfolders like `dto/`, `types/`, `commands/`, or `queries/` only when the feature complexity justifies them.
- Use `src/<feature>/types/` for feature-owned contracts that are reused across multiple functions or files inside the same feature; keep trivial one-off shapes inline or in the local file instead of creating a folder just to hold a single alias.
- Keep `src/common/` limited to cross-cutting concerns with clear reuse across features.
- Keep infrastructure or adapter code behind explicit providers instead of scattering SDK or ORM calls across controllers.

## Type-First Design

- Declare explicit public return types for exported functions, service methods, and factory helpers when the type is part of the module contract.
- Avoid `any`; prefer narrowed unions, generics, and small helper types.
- Separate transport DTOs from domain or persistence types.
- Introduce mapping functions when request or persistence shapes diverge from domain shapes.
- Keep trivial one-off object shapes inline or file-local when a named type would add more indirection than clarity.
- Extract a named feature-local type or interface when the same shape is repeated across signatures, reused across multiple files in one feature, or has become a stable feature-owned contract even if it is not yet shared outside that feature.
- Prefer `src/<feature>/types/` for those extracted feature-owned contracts. Keep DTO classes in `dto/`, and keep purely private helper aliases near the implementation until reuse makes the contract stable.
- Keep enums and discriminated unions close to the feature that owns them unless multiple modules genuinely share the contract.
- Promote a type to broader shared space only after repeated, stable cross-feature reuse is clear.

Example:

```ts
// Keep this inline when it is truly one-off and local.
async reserveSeat(input: { seatId: string; userId: string }): Promise<void> {
  // ...
}

// Extract this once the same feature-owned shape repeats across methods or files.
export interface ReservationLookup {
  showId: string;
  seatId: string;
}

async getReservation(input: ReservationLookup): Promise<Reservation | null> {
  // ...
}

async cancelReservation(input: ReservationLookup): Promise<void> {
  // ...
}
```

Example before:

```ts
async getSummary(input: { orderId: string; accountId: string }): Promise<OrderSummary> {
  // ...
}

async cancel(input: { orderId: string; accountId: string }): Promise<void> {
  // ...
}
```

Example after:

```ts
// src/orders/types/order-scope.ts
export interface OrderScope {
  orderId: string;
  accountId: string;
}
```

```ts
async getSummary(input: OrderScope): Promise<OrderSummary> {
  // ...
}

async cancel(input: OrderScope): Promise<void> {
  // ...
}
```

## NestJS Architecture Patterns

- Keep controllers thin: parse input, enforce route-level concerns, and delegate use-case work.
- Keep services focused on orchestration and domain decisions rather than HTTP transport details.
- Inject repositories, gateways, and external clients through providers instead of constructing them inline.
- Export only the providers another module must consume.
- Revisit module boundaries before reaching for `forwardRef`.
- Promote a shared abstraction only after repeated, stable reuse is clear.

Read [references/nest-patterns.md](./references/nest-patterns.md) for concrete controller, provider, validation, and exception-mapping patterns.

## Validation And Serialization

- Default to DTO classes plus validation decorators and a global `ValidationPipe`.
- Keep request DTOs, response DTOs, and persistence entities separate unless the shapes are truly identical and stable.
- Ensure controller return types, serializers, interceptors, and documented response envelopes agree with the actual runtime shape.
- Normalize parsing and coercion at the edge instead of scattering manual checks across services.
- Reject hidden implicit conversions unless the repository already relies on them intentionally.

## Swagger Documentation During Implementation

- When implementation work changes or depends on API contracts, add or refine Swagger decorators without changing runtime behavior.
- For documentation-only Swagger or JSDoc tasks, prefer `nestjs-swagger-jsdoc`.
- Document controller endpoints with summaries, concrete success and failure responses, and auth or multipart behavior only when the code path actually supports them.
- Document externally visible request and response DTOs with `@ApiProperty` or `@ApiPropertyOptional` aligned to validation and transformation rules already present.
- Prefer existing schema helpers or wrapper patterns for paginated, nested, or envelope-style responses instead of inventing new shapes in docs.
- Read interceptors, serializers, and shared response builders before documenting wrapped responses.

Read [references/swagger-patterns.md](./references/swagger-patterns.md) for concrete controller and DTO documentation patterns.

## Error Handling

- Raise meaningful domain or application errors inside services instead of spreading HTTP exceptions everywhere.
- Prefer the repository's existing translation mechanism when one already exists; otherwise map expected business failures at controller edges, filters, or a dedicated translation layer.
- Log at boundary points with enough context to debug, but avoid duplicate log-and-rethrow chains.
- Keep exception filters focused on translation and response shaping, not business recovery.

## Configuration And Infrastructure

- Centralize environment parsing and validation in configuration modules or factories.
- Keep external SDK, queue, mailer, and database setup inside adapters or infrastructure providers.
- Avoid leaking ORM entities, transaction handles, or SDK-specific response types across feature boundaries.
- Keep background jobs, event handlers, and HTTP handlers aligned on shared application services when they implement the same use case.

## Testing

- Write unit tests around services, pure utilities, guards, and interceptors with meaningful branching logic.
- Use integration tests for module wiring and provider composition without the full HTTP stack.
- Use e2e tests for auth boundaries, validation, and response contracts at the transport edge.
- Mock external systems at the provider boundary for unit tests.
- Keep e2e coverage focused on representative happy paths and failure paths, not every permutation.

Read [references/testing-patterns.md](./references/testing-patterns.md) for unit, integration, and e2e test skeletons.

## Anti-Patterns

- Avoid fat controllers that own branching business logic.
- Avoid modules that export every provider by default.
- Avoid reusing persistence entities as public DTOs.
- Avoid broad `@Global()` usage when explicit imports keep dependencies clearer.
- Avoid pushing unrelated helpers into `common/` just to reduce one local import.
- Avoid repeating the same anonymous object shape across neighboring signatures or files once the feature already has a stable local contract for it.
- Avoid hiding circular dependencies behind habitual `forwardRef`.

## Guardrails

- Confirm affected controllers, DTOs, services, providers, modules, and tests were all read before changing behavior.
- Confirm request validation, response shape, and exception mapping still match after edits.
- Confirm Swagger decorators still match the actual request and response behavior after edits.
- Confirm new providers are registered, exported only when needed, and injected via stable tokens or class references.
- Confirm changed public contracts have direct tests or the strongest feasible local verification.
- Confirm at least one negative path when touching validation, auth, or exception mapping.
- Confirm module wiring or provider overrides locally when changing module composition.
- Confirm response-shape regressions with an integration or e2e check when controller contracts change.
- Keep the final diff aligned with existing repository patterns unless the task explicitly requires a new pattern.
