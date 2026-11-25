# Project selection

1. Establish the audience, SEO and rendering needs, access boundaries, data ownership, deployment constraints, and team capacity. For existing systems, inventory the stack and record any migration proposal separately.
2. Establish backend status. Distinguish an existing API, an API under development, a new backend requirement, and a frontend-only project. Evaluate Supabase when its capabilities and operating model fit.
3. Present eligible combinations and describe their deployment, authentication, maintenance, and testing implications. Recommend a choice and obtain explicit approval before scaffolding or materially changing the architecture.
4. Record the approved choices, assumptions and rationale in the [project profile template](../assets/project-profile.md).

| Requirement | Owner preference to evaluate | Decision factors |
| --- | --- | --- |
| Internal dashboard | React | Interaction density, access control, hosting |
| Public website | Next.js | Indexing, content freshness, rendering, hosting |
| Public website and dashboard | Next.js and React, or one application | Shared identity and deployment, access boundaries, independent releases |
| Frontend without backend capabilities | Static delivery where suitable | Data sources, publishing workflow, future integration cost |

These are candidate combinations. Record checked versions, integration constraints, and verification results before calling a combination validated.

The technology preferences and approval requirements above come from the workspace owner. Preserve those requirements when future profiles add evidence. A team may have an API under development and a new backend requirement in different areas. Record the state per integration boundary.

## Prepare an approval proposal

Use existing requirements to establish public and private audiences, discovery/indexing, content freshness, server rendering, interaction density, latency, permissions, shared functionality, team capacity, hosting and operating cost. Compare a React admin SPA, Next.js public site, split applications or one Next.js application using [compatibility](compatibility.md). A single app may fit a small team with common deployment and identity. Preserve existing technologies unless migration is approved.

Inventory each integration. Identify existing or in-progress APIs, persistence, authentication, storage, complex server logic, operational ownership and whether any backend is needed. Compare an existing or future external API, framework-native server capabilities, dedicated backend, Supabase as a conditional candidate, or frontend-only operation. For a pending API, agree on contract ownership and validate against fixtures. Include hosting cost and the failure and deployment model.

Summarize known facts, assumptions, viable architecture and backend options, trade-offs, recommendation and validation. Request approval for the material decisions and record the accepted choice in `docs/PROJECT_PROFILE.md`.

For every backend boundary record persistence, identity, authorization, storage, realtime, processing duration, regulation, residency and existing services. If requirements are unclear, resolve them before committing to a provider. Compare a static product, current or in-flight API, Next.js server capabilities backed by appropriate persistence, managed Supabase, dedicated backend and hybrid compositions. Weigh team capacity, hosting and egress, bandwidth, compute, Auth and Realtime quotas, backup/restore, exit cost and managed-service coupling. State which duties still require application checks, a worker or integration service. Obtain explicit owner approval for backend selection and before provisioning. Record the decision and scope in PROJECT_PROFILE and an ADR, then apply the [Supabase profile](supabase/profile.md) if selected.

## Discovery and implementation

Use the [discovery worksheet](../assets/discovery.md) for material decisions. Extract requirements from the request, project profile, dependency lockfile, scripts, infrastructure and existing flows. Distinguish explicit and implied requirements, unresolved material questions, delegated implementation choices and out-of-scope requests. Ask only about unknowns that change architecture, behavior, security, cost or owner expectations.

For greenfield work, establish objectives and audience, choose frontend and backend candidates, compare options using compatibility, obtain approval and record the outcome. Then initialize the approved stack, document standards and ship verified vertical slices. Compare no backend, external API, dedicated service, Next.js server features, Supabase and hybrid ownership against persistence, identities, storage, realtime, jobs, security, compliance, hosting, cost and portability.

For maintenance, inspect package manager and versions, conventions, existing API clients, data/access boundaries, design system, tests, deployment and relevant debt. Follow the current architecture and reuse the existing seams. Document a material mismatch and seek migration approval if it cannot be resolved in scope.
