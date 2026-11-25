# Phase 3 coverage audit

Coverage refers to actionable staged guidance. Source presence and runtime verification are separate fields. COMPLETE indicates the listed guidance covers decisions, implementation and acceptance criteria. PARTIAL indicates a specific missing implementation or evidence seam. MISSING marks absent deliverables. NOT_APPLICABLE applies to source environments with no corresponding capability. NOT_PRESENT_IN_SOURCE marks capabilities searched for without representative implementation. REQUIRES_MORE_EVIDENCE applies when static code cannot settle the question.

Read the [plan template](../web-engineering/assets/supabase-plan.md), [workflow matrix](../web-engineering/references/supabase/workflows.md), [example](../web-engineering/assets/supabase-example/README.md) and [evidence](SUPABASE_ARCHITECTURE_ANALYSIS.md) together.

| Domain | Guidance | Rule and reference | Workflow / template / example | Evidence and verification |
| --- | --- | --- | --- | --- |
| Selection, costs, portability | COMPLETE | WEB-DEC-001, project selection | Selection / profile and ADR / strategy cases | S01 S05 S10, manual A–H |
| CLI initialization and hosted environments | COMPLETE | WEB-SUP-001, database | Initialize/connect / backend plan / neutral setup | S05 partial, managed runtime unverified |
| Architecture and typed client boundaries | COMPLETE | WEB-ARC-002, Supabase profile | Feature / backend plan / browser and repository | S01 S03 S09, strict compile with generated catalog contract |
| Relational design, constraints, relationships, indexing | COMPLETE | WEB-SUP-001, database | Design and review performance / backend plan / migration and seed | S04, isolated SQL execution |
| Views, materialized views, triggers, audit | COMPLETE | WEB-SUP-002, database | SQL RPC/trigger / backend plan / no separate view example | S04 views/triggers, materialized view NOT_PRESENT_IN_SOURCE |
| Migrations, upgrades, drift, regeneration | PARTIAL | WEB-SUP-001, database | Design and regenerate / backend plan / first migration | S05, fresh replay only. Upstream catalog generation passed; prior-release upgrade and CLI regeneration unverified |
| CRUD, pagination, sorting, retry and query state | COMPLETE | WEB-API-001, database | CRUD and search / feature plan / notes repository | S03 S11, strict SDK and dependency compilation with generated catalog contract |
| Bulk work and import/export | PARTIAL | WEB-API-001, database | CRUD/bulk / feature plan / no neutral importer | S11, representative trace only |
| PostgreSQL functions and concurrency | PARTIAL | WEB-SUP-002, database | SQL RPC / backend plan / invoker rename | S03 S04, SQL execution; concurrent/serialization tests open |
| Password, Auth state and profile | COMPLETE | WEB-AUTH-001, identity | Authentication / backend plan / no live fixture | S01 S02, managed Auth unverified |
| OAuth, magic links, MFA, SSR | PARTIAL | WEB-AUTH-001, identity and applications | Authentication / backend and route plans / no live SSR fixture | NOT_PRESENT_IN_SOURCE, docs only |
| Ownership, admin, anonymous and tenant RLS | COMPLETE | WEB-SUP-002, identity | RLS / backend plan / policies and assertions | S04 S06 S07, synthetic DB roles passed; effective reference policies REQUIRES_MORE_EVIDENCE |
| Storage restrictions, lifecycle and files | PARTIAL | WEB-SUP-002, services | Storage / backend plan / policy and upload | S06, object SQL passed with stand-in; managed API, limits and URLs unverified |
| Postgres Changes, Broadcast, Presence | PARTIAL | WEB-STATE-001, services | Realtime / backend plan / no subscriber fixture | S07; Broadcast/Presence NOT_PRESENT_IN_SOURCE, official docs |
| Edge Functions and webhooks | PARTIAL | WEB-AUTH-001, services | Edge Functions / backend plan / no handler fixture | S08, static only; gateway, idempotency and limits require runtime evidence |
| React integration | PARTIAL | WEB-STATE-001, applications | React / feature plan / typed SDK seams | S01 S02 S03, canonical DOM regression, no Supabase SPA smoke |
| Next.js integration | PARTIAL | WEB-NEXT-002, applications | Next.js / route plan / canonical example | NOT_APPLICABLE to reference. Official guidance, canonical HTTP smoke only |
| Combined and hybrid applications | COMPLETE | WEB-DEC-001, applications and compatibility | Combined / ADR / strategy cases | Design assessment only |
| Security and least privilege | COMPLETE | WEB-AUTH-001, WEB-SUP-002, identity | Security review / actor matrix / grant+policy checks | S02 S04 S06 S07 S08, neutral SQL only |
| CI, deploy, monitoring, backups and recovery | PARTIAL | WEB-QA-001, services and workflows | Deploy/recovery / backend plan / neutral scope | S10 static. Upgrade, production and restore verification open |
| Living docs | COMPLETE | WEB-DOC-001, project documentation | All rows / profile, feature, ADR and backend plans | Packaging check and manual review |
| Full local Supabase services validation | MISSING | WEB-QA-001, workflows | Security and release / backend plan / script instructions | Project-local CLI installed; runtime engine and disk blocker |

The [completion audit](PHASE_3_VALIDATION_COMPLETION.md) finds the reusable engineering guidance complete for conditional review. PARTIAL and MISSING rows in this historical coverage matrix denote missing test seams, reference evidence or executable validation where stated. The [validation matrix](SUPABASE_VALIDATION_MATRIX.md) tracks those distinctions.
