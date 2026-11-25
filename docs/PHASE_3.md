# Phase 3 Supabase engineering extraction

**READY_FOR_CONDITIONAL_OWNER_APPROVAL**

The staged proposal adds Supabase as an optional backend with two provider-specific rules, framework integration guidance, workflows, a backend plan and a synthetic notes fixture. All 18 baseline rule IDs survive. Existing React and Next.js neutral regressions passed. PostgreSQL executed the new schema and access assertions twice on isolated empty databases with service stand-ins. Knowledge is complete for conditional owner review. Source evidence remains partial, and runtime behavior is partially verified. See the [validation completion report](PHASE_3_VALIDATION_COMPLETION.md) and [test matrix](SUPABASE_VALIDATION_MATRIX.md). Effective authorization and full-stack verification remain open.

## Scope and stack

The reference was inspected read-only from its Git root. The committed revision, exact root and paths are in private staging provenance. Inspection used the committed baseline, tracked-tree inventory, and focused static traces through configuration, login, profile, documents, chat, import/export, SQL, Edge Functions, and operations. The current checkout also contains pre-existing lockfile and stylesheet edits and an untracked tool working tree. Those are outside committed evidence. Lockfile package versions for the main web stack matched the read-back values for the selected packages. The initial compile used a different installed SDK. The completion audit reran strict TypeScript with the reference-pinned SDK and the generated synthetic schema.

The reference includes a React 19.2.7 SPA, Vite 8.0.16, TypeScript 6.0.3, Supabase JS 2.107.0, TanStack Query 5.101.0, React Router 7.17.0 and a Flutter client using supabase_flutter 2.17.2. Nginx/deploy scripts, original schema, 206 migration SQL files, parity SQL, Deno handlers, test harnesses and operations docs were inventoried. Static source supports selected flows. Live settings and exhaustive downstream policy effects remain open. See [architecture, stack and capability inventory](SUPABASE_ARCHITECTURE_ANALYSIS.md), [database and service security findings](SUPABASE_SECURITY_REVIEW.md), and the [source registry](SOURCE_EVIDENCE.md).

The canonical skill had no initial commit. An isolated file snapshot served as the baseline. It contained both integrated frontend profiles, existing backend selection and combined guidance, neutral examples, validation scripts, and 18 rules. The project-specific structure and business logic stayed in the reference.

## Knowledge and deliverables

| Area | Staged result |
| --- | --- |
| Shared engineering | Typed SDK feature boundaries, precise authorization ownership, optional backend selection, migration and data lifecycle documentation |
| Database | [Schema, RLS, type generation and migrations](../web-engineering/references/supabase/database.md), including relational integrity, upgrade and recovery |
| Identity | [Auth and authorization](../web-engineering/references/supabase/identity.md), including ownership, app roles, effective grants and elevated calls |
| Storage, Realtime, Edge | [Optional services](../web-engineering/references/supabase/services.md), including file ownership, channel lifecycle and logic placement |
| React, Next.js, combined | [Application profiles](../web-engineering/references/supabase/applications.md), including session/cache boundaries and shared migration ownership |
| Strategy and scenarios | [Backend comparison and A–H assessments](BACKEND_STRATEGY_COMPARISON.md), [selection workflow](../web-engineering/references/project-selection.md) and [compatibility matrix](../web-engineering/references/compatibility.md) |
| Workflows and documents | [19 grouped procedures](../web-engineering/references/supabase/workflows.md), [backend plan](../web-engineering/assets/supabase-plan.md) and [living documents](../web-engineering/references/project-documentation.md). The existing project, ADR, feature and route plans continue to apply. |
| Neutral examples | [Workspace notes](../web-engineering/assets/supabase-example/README.md) with schema, seed, RLS, object rules, invoker RPC, assertions, typed client, repository and upload |
| Audit and integration | [Coverage audit](PHASE_3_COVERAGE_AUDIT.md) and [merge plan](PHASE_3_MERGE_PLAN.md) |

### Rule inventory

| Group | IDs |
| --- | --- |
| Decisions and docs | WEB-DEC-001, WEB-DOC-001 |
| Composition | WEB-ARC-001, WEB-ARC-002, WEB-ARC-003 |
| Data, state and auth | WEB-API-001, WEB-STATE-001, WEB-AUTH-001 |
| UI | WEB-UI-001, WEB-UI-002, WEB-UI-003 |
| Forms and localization | WEB-FORM-001, WEB-I18N-001 |
| Testing and performance | WEB-QA-001, WEB-PERF-001 |
| Next.js | WEB-NEXT-001, WEB-NEXT-002, WEB-SEO-001 |
| Supabase additions | WEB-SUP-001, WEB-SUP-002 |

### Phase 1 gap reassessment

| Gap | Evidence and stage decision |
| --- | --- |
| Multiple audiences | Staff portal and separate content/integration entry points show distinct needs. Independent releases and Next integration remain architectural guidance. PARTIAL. |
| Bulk operations | Quota and operational actions offer useful flow evidence. Add atomicity, authorization and partial-failure guidance. PARTIAL pending synthetic bulk verification. |
| Import/export | Source allocates begin/finish state, chunking, duplicate detection and filtered exports. Add contract, retry and audit guidance. PARTIAL pending neutral replay and tests for partial failure. |
| Dynamic fields | Feature forms exist. Reusable schema evolution and validation evidence is insufficient. PARTIAL. |
| Multi-step forms | First-login and password workflows show separate states. A general wizard with resumption, backward navigation and validation has insufficient evidence. PARTIAL. |
| Unsaved changes | Unload guards cover active uploads. Dirty forms and in-app navigation need separate evidence. PARTIAL. |

## Validation and limits

| Check | Actual result |
| --- | --- |
| Baseline and staged `python3 scripts/validate.py` and stable rule comparison | Metadata, links, evidence and rule references passed. 18 baseline, 20 staged. |
| Skill Creator `quick_validate.py` using isolated PyYAML | Passed for baseline and proposal. |
| `tsc --strict --target ES2022 --module NodeNext --moduleResolution NodeNext`, neutral assertions, React DOM smoke | Passed baseline and proposal with TypeScript 5.9.3. Simulated routing/session UI, RTL, filters and data states. |
| `next build --webpack`, `next start` and Node loopback assertions | Passed baseline and proposal with Next.js 16.2.4. Checked both locale routes, direction, canonicals, alternate language, unknown route 404, sitemap and robots. |
| `initdb`, `pg_ctl`, `psql -v ON_ERROR_STOP=1` with synthetic bootstrap, migration, seed and assertions | Passed final fixture twice on PostgreSQL 16.15. Unix socket only. Verified SQL role gates, membership changes, constraints, scoped RPC and Storage-style metadata policies. Sandbox initially blocked shared memory; the isolated rerun was approved. |
| Supabase SDK fixture TypeScript | Strict TypeScript 5.9.3 passed with dependency checks on, Supabase JS 2.107.0, Node 22 ambient declarations and schema types generated twice from the synthetic PostgreSQL catalog by upstream Supabase tooling. |
| Supabase local stack and exact generated types | Project-local CLI 3.4.0 initialized successfully. The standard stack and CLI type path require a compatible container engine, which was absent. The experimental native path still requires additional disk and isolation. Auth, Storage transport, Realtime, Edge and framework integration were not exercised. |
| Privacy and portability | Staged files checked for source paths, private endpoints, token patterns and build/dependency artifacts. A private evidence map enables owner traceability without adding source material to the skill. |

The PostgreSQL test does not emulate token validation, API gateway grants, actual storage semantics or production policy state. Historical replay, schema drift, upgrade from a previous release, accessibility/browser hydration, cross-app auth, and restore verification remain open. Forward behavioral skill validation has not been performed independently.

## Owner decisions and consolidation

Review the two proposed new rule IDs and the scope of Supabase as an optional profile. Approve access to a disposable container-capable environment and, if exact reference policy conclusions are needed, a sanitized and reproducible schema baseline. Review whether full-stack fixture and representative replay evidence are required before merging. Backend selection, provisioning, destructive migration, production execution and canonical integration each remain subject to applicable owner approval. The [merge plan](PHASE_3_MERGE_PLAN.md) inventories files, regressions and prerequisites. Phase 4 awaits the outcome of owner review and the unresolved validation.
