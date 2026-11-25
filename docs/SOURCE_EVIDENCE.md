# Source and evidence registry

| Source | Scope | Status |
| --- | --- | --- |
| WEB-SRC-001 | Pinned React dashboard implementation and tracked configuration, inspected 2026-11-25 | Static implementation evidence |
| WEB-SRC-002 | Owner-supplied dashboard guide, inspected 2026-11-25 | Design intent and comparison evidence |
| Workspace brief | Owner-approved phase boundaries and project selection and documentation preferences | Policy input |
| Flutter Engineering Skills v0.2.0 | Local methodology for stable rules, profiles, compatibility, evidence and validation | Methodology only |

Private anchors, revision, source location and the guide fingerprint are recorded outside this repository. The code inventory spans 458 tracked paths, including 419 paths under the frontend source directory. Static traces focused on the app shell, auth, data-heavy list and detail flows, shared UI, locales and build/hosting seams. This is representative coverage across subsystems.

| Evidence | Trace | Related rules | Limits |
| --- | --- | --- | --- |
| E01 | App root, route table and compiler options | WEB-ARC-001, WEB-ARC-002, WEB-PERF-001 | Route behavior and bundle cost unmeasured |
| E02 | List page, query hook and typed service | WEB-API-001, WEB-UI-002 | Backend response guarantees unverified |
| E03 | URL state utility and shared query configuration | WEB-STATE-001, WEB-API-001 | Browser history and cancellation unverified |
| E04 | Route guard, session persistence and logout | WEB-AUTH-001 | Backend enforcement unverified |
| E05 | Login form, theme and localization | WEB-UI-001, WEB-FORM-001, WEB-I18N-001 | Interaction and cross-locale behavior unverified |
| E06 | Package scripts, container build and static web server | WEB-QA-001 | Build and deployed serving unexecuted |
| E07 | Layout, navigation and cross-layer dependency | WEB-ARC-001, WEB-ARC-002, WEB-UI-001 | Responsive shell observed in code |
| E08 | Generic table, feature cards and state components | WEB-ARC-003, WEB-UI-001, WEB-UI-002, WEB-UI-003 | Accessibility and motion untested |
| E09 | Detail polling, mutation cache effects and API auth callback | WEB-API-001, WEB-AUTH-001, WEB-UI-002, WEB-PERF-001 | Failure timing and server response untested |
| E10 | Locale resources and language initialization | WEB-I18N-001 | Catalog completeness and dialect behavior untested |
| E11 | Motion utility scan and test/build inventory | WEB-UI-003, WEB-PERF-001, WEB-QA-001 | No conventional tracked test suite found |
| Owner requirements | Technology approval and living documentation | WEB-DEC-001, WEB-DOC-001 | Policy |

Guide evidence G01–G10 and its dispositions are in the [reconciliation matrix](REACT_GUIDE_RECONCILIATION.md).

## Final audit evidence

| Evidence | Trace | Related rules | Limits |
| --- | --- | --- | --- |
| E12 | Theme CSS, local fonts, image and icon assets, shell and primitive inventory | WEB-UI-001, WEB-UI-003 | Asset licensing and browser interaction unverified |
| E13 | Dashboard overview, KPI grid, responsive chart and reporting export link | WEB-UI-001, WEB-UI-002, WEB-I18N-001 | Metric correctness, chart accessibility and export response unverified |
| E14 | Entity management page, create/edit and delete dialogs, schema, list/mutation hooks, profile multipart upload | WEB-UI-002, WEB-FORM-001, WEB-API-001, WEB-AUTH-001 | Bulk, import, server sorting, download contract and end-to-end authorization lack verified evidence |
| E15 | Locale switcher, locale catalogs, and sampled date, number and money helpers | WEB-I18N-001 | Complete formatting coverage and automated catalog checks unverified |
| E16 | Entrypoint, project configuration, CI, package lock and transport/auth wiring | WEB-ARC-002, WEB-API-001, WEB-AUTH-001, WEB-QA-001, WEB-PERF-001 | Refresh, monitoring, build automation behavior and backend security unverified |

## Phase 2 implementation evidence

WEB-SRC-003 is the pinned Next.js public website, acquired externally and inspected read-only. The lockfile resolves Next.js 16.2.4. Private repository location, branch and revision are kept in external provenance. These are static traces.

| Evidence | Trace | Related rules and limits |
| --- | --- | --- |
| N01 | Locale segment layout, translation provider, route registry and Proxy | WEB-NEXT-001, WEB-I18N-001. Runtime negotiation and invalid locale outcomes unverified. |
| N02 | Locale parameter enumeration, catalog request rendering, URL selection and page reuse | WEB-NEXT-001, WEB-NEXT-002. No source build classification. |
| N03 | Localized metadata helper, canonical alternates, sitemap and robots | WEB-SEO-001. Ranking and indexing unverified. |
| N04 | Native Fetch, envelopes, API helpers and parallel server reads | WEB-API-001, WEB-NEXT-002. Runtime shape, auth and cache freshness not verified. |
| N05 | JSON-LD helper, structured site metadata and internal link/code paths | WEB-SEO-001. No crawler or rich results verification. |
| N06 | Navigation, public sections, theme CSS, assets, image usage and selective reduced motion | WEB-UI-001, WEB-UI-003. Interaction and vitals unverified. |
| N07 | Localized content, browser hooks, URL filters, debounced search and cleanup | WEB-STATE-001, WEB-I18N-001. No framework client cache or network cancellation shown on sampled paths. |
| N08 | Contact/partner submit paths, sanitization and public transport | WEB-FORM-001, WEB-AUTH-001. Backend validation and private session flows unverified. |
| N09 | Config, package/lock, documentation, test file, build/lint scripts and absence inventory | WEB-QA-001, WEB-PERF-001. No source scripts run or deployment artifacts verified. |

## Phase 3 Supabase evidence

| ID | Portable evidence anchor |
| --- | --- |
| S01 | Browser client configuration and committed SDK/framework locks |
| S02 | Browser Auth lifecycle, password entry and profile RPC |
| S03 | Folder flow, feature query and SQL boundary |
| S04 | Baseline PostgreSQL snapshot, grants and policy overlays |
| S05 | Migration history, ledger, CLI metadata and DB shell tooling |
| S06 | File helpers, private object policy overlays and cleanup |
| S07 | Participant RLS, Realtime publication and cache hooks |
| S08 | Deno HTTP handlers and integration boundaries |
| S09 | Handwritten web TypeScript data contracts |
| S10 | Frontend, mobile, integration and infrastructure checks |
| S11 | Import/export, bulk quota and upload lifecycle |
| S12 | Ordered PostgreSQL syntax and static authorization ledger, with separate neutral SQL and upstream type generation validation |

The [architecture analysis](SUPABASE_ARCHITECTURE_ANALYSIS.md) records source and official documentation separately. Exact source mapping and revision are in private staging provenance.
