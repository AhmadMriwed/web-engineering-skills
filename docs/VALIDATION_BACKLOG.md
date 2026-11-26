# Phase 5 validation backlog

All items are open. P1 items cover security boundaries or release-blocking evidence for the capability under test. P2 items cover quality, portability, or recovery evidence. Product-specific tests use synthetic data and approved disposable environments. See the [Phase 3 validation matrix](SUPABASE_VALIDATION_MATRIX.md) and the [Phase 1 coverage audit](PHASE_1_COVERAGE_AUDIT.md).

## Reusable skill and fixture validation

| ID | Profile and capability | Current evidence | Infrastructure and test scenario | Acceptance criteria | Security significance | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V-01 | React, multiple audiences | Partial source and design guidance | Browser with role-aware fixture and direct navigation | Correct shell, routes and data for each role, with server denial for forbidden requests | Audience and permission separation | P1 | Open |
| V-02 | React, bulk operations | Source workflows and review guidance | Browser and disposable API. Test mixed authorization, retry and cancellation | Execution matches promised atomicity, retries are safe and each outcome is visible | Unauthorized writes | P1 | Open |
| V-03 | React, import/export | Source chunking, deduplication and export | Browser and disposable API with synthetic files | Malformed or duplicate input handled, partial runs recover, exported scope is authorized | Data leakage and duplicate writes | P1 | Open |
| V-04 | React, dynamic fields | Partial source evidence | Browser with conditional form inputs | Hidden, disabled and reintroduced fields produce correct validation and payloads | Input integrity | P2 | Open |
| V-05 | React, multi-step forms | First-login flow evidence | Browser with validation, backward navigation and resume | Required steps cannot be bypassed and resumed data is consistent | Input integrity | P2 | Open |
| V-06 | React, unsaved changes | Upload unload guard | Browser with dirty form, back button, tab close and saved state | Warn when appropriate and clear the guard on save or discard | Data loss | P2 | Open |
| V-07 | React and Next.js, browser and accessibility | React DOM and Next HTTP fixtures | Real browser, keyboard, assistive technology and slow network | Hydration, focus, forms, RTL, responsive navigation, cache transitions and error states pass | Accessible recovery and isolation | P2 | Open |
| V-08 | React and Next.js, external API and deployment | Source traces and neutral regressions | Disposable API and intended hosting targets | Auth, CORS, direct navigation, static export where supported, failures and mutation/cache behavior pass | Transport and access control | P1 | Open |
| V-09 | Supabase Auth and Data API | PostgreSQL role tests | Disposable full stack with synthetic accounts and negative sessions | Auth lifecycle passes. Allowed CRUD succeeds and forbidden, anonymous, revoked, cross-user and cross-tenant requests are denied | Identity and tenant isolation | P1 | Open |
| V-10 | Supabase Storage | Object metadata policies tested in SQL | Disposable Storage API and synthetic private objects | Upload, download, signed URL and deletion honor permissions, expiry and bucket limits | File confidentiality | P1 | Open |
| V-11 | Supabase Realtime | Static channel and policy guidance | Disposable Realtime service and multiple actors | Unauthorized subscription denied, authorized delivery and cleanup pass, reconnect reconciles missed or duplicate events | Event confidentiality | P1 | Open |
| V-12 | Supabase Edge Functions | Static source and official guidance | Disposable Edge runtime and neutral handler | Validate requests, identity, permissions, CORS, retries and privileged effects | Service credential boundary | P1 | Open |
| V-13 | React with Supabase | DOM regression and SDK typecheck | Browser connected to a disposable stack | Session boundary, mutations, scoped invalidation, loading, empty and failure paths pass | Session and cache isolation | P1 | Open |
| V-14 | Next.js with Supabase | Official SSR guidance and neutral Next.js regression | App Router production build with disposable stack | Protected routes, cookie refresh, redirect, server/client import boundary and sequential user isolation pass | Private SSR/cache isolation | P1 | Open |
| V-15 | Combined and hybrid apps | Scenario review and architectural guidance | Disposable frontend deployments with shared API or backend and worker if applicable | Identity handoff, version skew, server roles, retry and independent release isolation pass | Cross-application access | P1 | Open |
| V-16 | Supabase migration and recovery | Clean synthetic replay and catalog-generated types | Disposable stack with previous-version synthetic snapshot | Upgrade and repeat reset pass, CLI types match schema, drift detected, DB/files/config recover within targets | Data integrity and recovery | P1 | Open |
| V-17 | Unified skill invocation | Packaging and scenario checks | Fresh neutral workspaces for representative profiles | Agent routes to correct profile, preserves existing backend and requests approval before material decisions | Technology and side-effect scope | P2 | Open |

## Reference-project evidence

| ID | Profile and capability | Current evidence | Infrastructure and test scenario | Acceptance criteria | Security significance | Priority | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | Reference migration replay | Snapshot plus 206 files analyzed in two candidate orders | Sanitized historical starting schema, reviewed order, disposable Supabase stack and disabled runtime egress | Repeat approved replay. Record exclusions, order, failures, drift and catalog comparison | Reproducibility of security configuration | P1 | Open |
| R-02 | Reference effective authorization | Static table, policy, ACL and privileged-function inventory | R-01 plus synthetic actors and separate data, Storage and RPC checks | Resolve inherited/default grants, procedural changes, owner bypass and tenant scope. Verify the isolated replay configuration | Cross-user and privileged access | P1 | Open |
| R-03 | Reference production deployment security | No deployment certification in Phase 3 | Separate owner-approved review scope | Independently established evidence for deployment configuration and its stated limits | Deployment assurance | P1 | Open |

Phase 4 expands the guidance for V-01 through V-06 and retains their open runtime status. V-17 uses the independent [Phase 5 plan](PHASE_5_VALIDATION_PLAN.md), including separate activation, reference loading and workflow evidence. The 17 reusable and three reference items retain their priorities.

## Phase 5 reconciliation

Evidence IDs below refer to artifact names in the external evaluation workspace. Original criteria and priorities above remain authoritative.

| ID | Phase 5 result and environment | Disposition and remaining evidence |
| --- | --- | --- |
| V-01 | A browser and live REST tests plus advanced actor tests with synthetic roles. | PARTIALLY_VERIFIED. Cross-audience shells and tenant transitions pending. |
| V-02 | Advanced domain and DOM tests passed filtered selection, partial action and retry. | PARTIALLY_VERIFIED. Confirmation and transaction behavior in a persistent target remain open. |
| V-03 | Advanced tests passed invalid input, preview, scope and formula escape; Chrome performed a real download. | PARTIALLY_VERIFIED. Commit, recovery and large-file workflows open. |
| V-04 | Advanced tests passed lot-code validation and clearing; Chrome checked the required field. | PARTIALLY_VERIFIED. Additional browser and service payload combinations open. |
| V-05 | Advanced tests passed two-step gating, backward navigation and failed-save recovery; Chrome reached step two. | PARTIALLY_VERIFIED. Persistent draft resume open. |
| V-06 | Advanced DOM guard tests passed; Chrome dismissed the native in-app confirmation and preserved the draft. | PARTIALLY_VERIFIED. Native unload and persistence open. |
| V-07 | `browser-neutral.log` and `generated-browser.log` cover selected Chrome desktop, mobile, RTL and keyboard checks, and F has jsdom tests. | PARTIALLY_VERIFIED. Screen reader, broad responsive coverage and remaining states open. |
| V-08 | `inventory-api.log` covers direct REST actor checks. `B-export-http.log` covers localized export. | PARTIALLY_VERIFIED. Host-specific deployment, production identity and broader cache behavior open. |
| V-09 | `synthetic-postgres.log` passes local role and policy checks with stand-ins. | BLOCKED_BY_INFRASTRUCTURE for actual Auth/Data API. |
| V-10 | Synthetic SQL policy checks only. | BLOCKED_BY_INFRASTRUCTURE for objects and signed access through Storage. |
| V-11 | No Realtime service run. | BLOCKED_BY_INFRASTRUCTURE. |
| V-12 | No Edge service run. | BLOCKED_BY_INFRASTRUCTURE. |
| V-13 | React DOM and strict SDK compile rerun. | BLOCKED_BY_INFRASTRUCTURE for integrated Supabase React. |
| V-14 | Neutral Next build/HTTP and D discovery. | BLOCKED_BY_INFRASTRUCTURE for actual authenticated sessions/cache and cookies. |
| V-15 | E discovery, builds and loopback combined browser flow passed. | PARTIALLY_VERIFIED. Independent deployments and version skew open. |
| V-16 | Neutral PostgreSQL migration and SDK compile rerun. | PARTIALLY_VERIFIED. Managed reset, upgrade and recovery open. |
| V-17 | Actual Codex explicit and automatic reads, focused routing and independent projects. | PARTIALLY_VERIFIED across workloads and consumers. Claude Code unavailable. |
| R-01 | No sanitized historical starting schema supplied. | REQUIRES_MORE_EVIDENCE. Reference replay not executed. |
| R-02 | No replay catalog or effective actor checks from the reference. | REQUIRES_MORE_EVIDENCE. |
| R-03 | Production infrastructure outside authorization. | NOT_EXECUTED. |

## Phase 5.1 focused checks

V-03 stays PARTIALLY_VERIFIED. The supplemental Chrome fixture verified a selected CSV file through preview, manager confirmation, mixed outcome and server readback after reload, and denied a direct operator commit. Persistence beyond the server process and production actor identity remain open.

V-05 and V-06 stay PARTIALLY_VERIFIED. Browser-local optional draft recovery, actor/record key separation and clearing after local acceptance or discard passed. The existing wizard's persistent resumption, native unload and managed identities remain open. Other dispositions are unchanged. See the [Phase 5.1 report](PHASE_5_1.md).
