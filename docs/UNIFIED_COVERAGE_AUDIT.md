# Unified coverage audit

Coverage describes actionable guidance. Evidence describes representative static observations. Runtime results apply only to neutral fixture boundaries. Historical counts and classifications remain in the [React](PHASE_1_COVERAGE_AUDIT.md), [Next.js](PHASE_2_COVERAGE_AUDIT.md) and [Supabase](PHASE_3_COVERAGE_AUDIT.md) audits. The [source register](SOURCE_EVIDENCE.md) and [validation backlog](VALIDATION_BACKLOG.md) own detailed limits.

| Domain | Rule, reference and workflow | Evidence and verification |
| --- | --- | --- |
| Discovery, existing systems, architecture and combined ownership | WEB-DEC-001, WEB-ARC-001, WEB-ARC-002, WEB-ARC-003. [Selection](../web-engineering/references/project-selection.md), [compatibility](../web-engineering/references/compatibility.md), discovery and ADR templates | E01, N01, S01. Guidance complete for selection. Combined live compatibility open. |
| Shared interface, dashboard, public content, locale and forms | WEB-UI-001, WEB-UI-002, WEB-UI-003, WEB-FORM-001, WEB-I18N-001. [Routes and profile workflows](../web-engineering/references/tasks.md), feature plan | E05, E08, N06, N07. Guidance complete for core flows. React DOM and Next HTTP fixtures cover selected states. Browser checks open. |
| External API, state and security | WEB-API-001, WEB-STATE-001, WEB-AUTH-001. [API](../web-engineering/references/external-api.md), profile adapters, inventory example | E02, N04, S03. Guidance complete for scope; live contract and deployment open. |
| Routing, rendering, SEO and deployment | WEB-NEXT-001, WEB-NEXT-002, WEB-SEO-001. [Next workflows](../web-engineering/references/next/workflows.md), route plan and catalog example | N01, N02, N03. Neutral production build and HTTP passed. Browser, cache invalidation and indexing open. [App Router docs](https://nextjs.org/docs/app) |
| Database, generated types, grants, RPC and security | WEB-SUP-001, WEB-SUP-002. [Supabase workflows](../web-engineering/references/supabase/workflows.md), backend plan and SQL fixture | S04, S05, S09, S12. SDK and synthetic PG checks passed. Reference replay and managed effective authorization open. |
| Auth, Storage, Realtime and Edge | WEB-AUTH-001, WEB-SUP-002. [Supabase profile](../web-engineering/references/supabase/profile.md), backend plan and sample data/storage client | S02, S06, S07, S08. SQL actor checks only for selected predicates. Managed service and frontend integration open. [Supabase docs](https://supabase.com/docs) |
| Quality, performance, delivery and maintenance docs | WEB-QA-001, WEB-PERF-001, WEB-DOC-001. [Standards](../web-engineering/references/standards.md) and document prompts | E06, N09, S10. Packaging and fixture regression passed. Production performance, recovery and runtime consumer execution open. |

## Six-gap reassessment

[Advanced feature contracts](../web-engineering/references/advanced-features.md) supplies ownership, failure handling and tests for all six domains. These are implementation patterns with mixed source support and do not replace historical audit results.

| Domain | Evidence and disposition | Pending |
| --- | --- | --- |
| Multiple audiences | E07 and S02 partially support role-aware composition. Added decisions for shells, permission checks and deployment boundaries. | V-01 |
| Bulk operations | S11 supports bounded processing. Added selection semantics, failure, per-item authorization and retry policy. | V-02 |
| Import and export | S11 supports chunking and export. Added mapping, preview, disclosure controls and spreadsheet safety. | V-03 |
| Dynamic fields | S02 provides partial form context. Added input lifetimes and shared payload/visibility rules. | V-04 |
| Multi-step forms | S02 provides first-login evidence. Added draft ownership and step recovery. | V-05 |
| Unsaved changes | S11 provides an upload guard. Added route, unload and sensitive draft decisions. | V-06 |

All six now have actionable design guidance. End-to-end coverage remains partial until the corresponding backlog tests run.

Phase 5.1 added focused browser evidence for executing a confirmed import through a synthetic server boundary and optional browser-local draft recovery. The original six domains remain partially verified against their full backlog acceptance criteria. See the [Phase 5.1 report](PHASE_5_1.md).
