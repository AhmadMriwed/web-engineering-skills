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
