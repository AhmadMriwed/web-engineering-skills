# Phase 1 React extraction report

**Status on 2026-11-25** — READY_FOR_OWNER_APPROVAL. The final audit authorization supersedes the earlier extraction prompt. The [coverage audit](PHASE_1_COVERAGE_AUDIT.md) records every requested domain, evidence, workflow and practical portability check.

## Previous and current state

The initial workspace had one React profile containing six source-informed rules, two shared owner-defined rules, a project profile template, and a preliminary evidence table. The existing clone was reused at its original pinned main revision. The local Flutter repository supplied the methodology for stable IDs, registries, compatibility, project selection, progressive disclosure and validation. Both references were inspected read-only.

The skill now has 15 rules. All eight original IDs were retained. The inventory identifies the added architecture, interface, forms, localization, and performance rules. The four implementation references now include configuration, lifecycle, design foundations, CRUD, defensive API handling, localized formatting and delivery controls. A fifth reference routes engineering workflows.

The audit classified previous guidance as 36 complete, 126 partial and 33 missing. Final guidance covers 189 domains completely and six partially. The partial rows concern multiple audiences, bulk operations, import and export, dynamic fields, multi-step forms and unsaved changes. Source and runtime evidence are tracked separately.

## Guide reconciliation and dispositions

The [guide reconciliation](REACT_GUIDE_RECONCILIATION.md) compares all guide sections with the implementation. It confirms feature-first organization, representative service/hook boundaries, reusable responsive tables, schema-backed forms, semantic tokens, locale registration and explicit list states. It also records scoped transport composition, persisted session state, conditional detail polling, cache invalidation, eager route imports, static-host fallback and UI transitions.

| Disposition | Practices |
| --- | --- |
| Adopt in draft | App composition root, feature ownership, typed transport seam, URL/query/local state ownership, shared UI contracts, catalogs, and workflow validation |
| Conditional | Vite and the observed library assembly, client stores, card representations, invalidation versus exact cache updates, polling, route splitting, and shared component extraction |
| Correct or exclude as a default | Reverse imports from shared to feature internals, browser credential persistence by convention, route visibility as authorization, compile-time types as response validation, untranslated fallbacks as proof of catalog coverage, and click-only row interaction |
| Pending evidence | Deployed authorization and expiry behavior, accessibility interaction, route performance, layout across locales, and multi-audience reuse |

## Rule and knowledge inventory

| Category | Rules and coverage |
| --- | --- |
| Shared guidance | WEB-DEC-001 material stack approval and rationale, WEB-DOC-001 living documentation under the project docs directory |
| Architecture | WEB-ARC-001 composition root, providers, guarded nested routes and navigation, WEB-ARC-002 feature folders, strict typing, aliases and dependencies, WEB-ARC-003 local helpers, file extraction and shared component criteria |
| API and state | WEB-API-001 transport, services, query hooks, validated contracts, cancellation, errors, keys, polling and mutation reconciliation. WEB-STATE-001 URL parsing, search and pagination, query ownership, component state and scoped client state |
| Identity | WEB-AUTH-001 session states, backend authorization, persistence decisions, 401/403 handling and cache cleanup |
| Interface | WEB-UI-001 semantic tokens, primitives and shell. WEB-UI-002 tables, filters, responsive alternatives, keyboard access and UI states. WEB-UI-003 interaction motion and reduced motion |
| Forms and localization | WEB-FORM-001 schema, request mapping and backend feedback. WEB-I18N-001 locale catalogs, formatting and RTL |
| Quality and performance | WEB-QA-001 layered verification and deployment checks. WEB-PERF-001 measurement, route splitting, request costs and list performance |

The [React dashboard profile](../web-engineering/references/react-dashboard.md) defines the observed client-rendered, feature-first assembly. The [project selection workflow](../web-engineering/references/project-selection.md) routes alternatives by rendering, identity, API, hosting and team constraints. A dashboard without an API can skip transport and query layers. For a combined public site and dashboard, separate deployment and a single application remain candidates.

| Combination | Compatibility assessment |
| --- | --- |
| Vite SPA, browser router, feature-first boundaries and existing API | Observed in source. Confirm build compatibility and production route fallback on the chosen host. |
| Router URL state, TanStack Query and Zustand | Observed with different owners. Keep a client store conditional and validate scope changes and cleanup. |
| React Hook Form, Zod, shared accessible primitives and i18next | Observed together. Exercise locale coverage and real form interaction before relying on the assembly. |
| Frontend-only React | Architectural candidate. Remove API and identity infrastructure when product requirements allow. |
| React and Next.js | Owner-defined candidate. Phase 2 will supply implementation evidence. |
| React and Supabase | Candidate pending an authorized reference and integration review. |

## Workflows, templates and examples

The [delivery reference](../web-engineering/references/react/delivery.md) includes an approved-stack bootstrap, a vertical-slice feature workflow, deployment checks and testing by layer. The skill includes a [project profile](../web-engineering/assets/project-profile.md), [feature plan](../web-engineering/assets/feature-plan.md), and [neutral inventory examples](../web-engineering/assets/examples/README.md). The examples demonstrate a URL codec, page reset, presentation state, identity-scoped query keys, cancellation and response decoding. The example README shows how to connect a query and accessible form. These patterns use invented inventory data.

The [source and evidence registry](SOURCE_EVIDENCE.md) links 16 implementation evidence groups to rule IDs and records their limits. The guide matrix contains 10 comparison groups. Private provenance is kept outside the central repository.

## Repository tree and change inventory

The paths below are relative to the repository root. The deliverables remain untracked in the local Git repository.

```text
README.md
docs/KNOWLEDGE_MAINTENANCE.md
docs/PHASE_1.md
docs/PHASE_1_COVERAGE_AUDIT.md
docs/REACT_GUIDE_RECONCILIATION.md
docs/SOURCE_EVIDENCE.md
scripts/smoke_react.cjs
scripts/validate.py
scripts/validate_examples.cjs
web-engineering/SKILL.md
web-engineering/assets/architecture-decision.md
web-engineering/assets/examples/README.md
web-engineering/assets/examples/inventory-api.ts
web-engineering/assets/examples/list-state.ts
web-engineering/assets/feature-plan.md
web-engineering/assets/project-profile.md
web-engineering/references/project-documentation.md
web-engineering/references/project-selection.md
web-engineering/references/react-dashboard.md
web-engineering/references/react/architecture.md
web-engineering/references/react/data-and-identity.md
web-engineering/references/react/delivery.md
web-engineering/references/react/interface.md
web-engineering/references/react/workflows.md
web-engineering/references/standards.md
```

Created in the final audit: coverage audit, consolidated workflows, architecture decision template and React DOM smoke script. Updated: README, this report, source registry, React profile and its four implementation references, project documentation and selection, and the repository validator. The rule inventory, prior reconciliation, feature and project templates, and standalone TypeScript examples were retained.

## Validation and limitations

| Command or check | Actual result |
| --- | --- |
| `python3 scripts/validate.py` | Passed skill metadata, local links, cited rule and audit evidence definitions, and 15 unique rule IDs. |
| `python quick_validate.py web-engineering` using the installed skill-creator script and a temporary Python 3.12 environment with PyYAML 6.0.4 | Passed. |
| `tsc --strict --target ES2022 --module NodeNext --moduleResolution NodeNext --outDir <temporary-dir> web-engineering/assets/examples/*.ts` | Passed with TypeScript 5.9.3 and emitted both examples. |
| `node scripts/validate_examples.cjs <temporary-dir>` | Passed in Node 22.23.2. Assertions cover invalid pages, state precedence, cache scope, signal forwarding and invalid responses. |
| `NODE_PATH=<temporary-node-modules> node scripts/smoke_react.cjs <compiled-examples>` | Passed. React DOM rendered the neutral shell, simulated session boundary, URL filter, RTL metadata, table and feedback states in jsdom. |
| Audit reconciliation and file inventory comparison | All 195 requested matrix rows were present in order. All 25 deliverable files were listed. |
| Distributable file scan and reference revision check | No private host, source slug, pinned revision, guide fingerprint or reference path found in deliverable files. Reference HEAD matched the pinned revision. |

The neutral React DOM smoke also passed using React and React DOM 19.2.4 with jsdom 26.1.0 installed into a temporary directory. It exercised a sign-in boundary, shell navigation markup, RTL metadata, URL filter/page reset and a typed mock service feeding the table. This is DOM execution with fixtures. Actual browser layout, assistive technology, full CRUD, deployed API authorization, production serving and agent invocation remain unverified. The pinned implementation was inspected through Git blobs, and source scripts were left unexecuted.

## Owner review and next phase readiness

**READY_FOR_OWNER_APPROVAL.** The [coverage audit](PHASE_1_COVERAGE_AUDIT.md) maps all 195 requested domains and distinguishes guidance, source evidence and verification gaps. Review the React profile, the shared-versus-profile-specific boundaries, and the prescribed project documentation. The repository is ready for a future Next.js comparison after explicit owner approval and Phase 2 authorization. Next.js and Supabase extraction remain pending.
