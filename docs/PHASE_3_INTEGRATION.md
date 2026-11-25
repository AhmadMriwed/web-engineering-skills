# Phase 3 canonical integration

The owner conditionally approved the reusable Supabase engineering profile. Two earlier execution attempts were interrupted deliberately, first after checkpoint creation and then after candidate edits. The repository had no initial commit. The recovery checkpoint matched the unchanged canonical tree before integration.

## Scope and inventory

- [Shared engineering standards](../web-engineering/references/shared-core.md) retain shared architectural, validation, authorization, state and documentation conventions. Existing external API guidance remains available.
- [React](../web-engineering/references/react-dashboard.md) and [Next.js](../web-engineering/references/next/profile.md) retain their existing frontend profiles and workflows.
- The optional [Supabase profile](../web-engineering/references/supabase/profile.md) adds database design, migrations, typed repositories, identity, authorization, Storage, Realtime, Edge Functions and application integration.
- The [compatibility matrix](../web-engineering/references/compatibility.md) covers nine backend and frontend configurations. Overlapping baseline rows were consolidated while retaining landing page, dashboard and authenticated-rendering guidance.
- [Backend selection](BACKEND_STRATEGY_COMPARISON.md) retains the eight architecture assessments and requires approval of material choices.
- The [Supabase workflow matrix](../web-engineering/references/supabase/workflows.md) retains 19 workflows. Existing React and Next.js workflows remain in place.
- Templates cover the project profile, architecture decision, feature plan, Next.js route and Supabase implementation. Neutral examples cover React/API state, a localized Next.js site and a Supabase-backed notes schema with typed queries and policies.
- The [validation backlog](VALIDATION_BACKLOG.md) records the six partial React domains, remaining reusable verification and separate reference evidence tasks.

## Rules

| Area | Rule IDs |
| --- | --- |
| Decisions and docs | WEB-DEC-001, WEB-DOC-001 |
| Composition | WEB-ARC-001, WEB-ARC-002, WEB-ARC-003 |
| Data, state and authorization | WEB-API-001, WEB-STATE-001, WEB-AUTH-001 |
| UI | WEB-UI-001, WEB-UI-002, WEB-UI-003 |
| Forms and localization | WEB-FORM-001, WEB-I18N-001 |
| Quality and performance | WEB-QA-001, WEB-PERF-001 |
| Next.js | WEB-NEXT-001, WEB-NEXT-002, WEB-SEO-001 |
| Supabase | WEB-SUP-001, WEB-SUP-002 |

## Conditions and remaining work

Knowledge is **COMPLETE**, source evidence is **PARTIAL**, and runtime verification is **PARTIALLY_VERIFIED**. The ordered static analysis of the reference snapshot and 206 migration files establishes a source inventory. Effective deployed permissions and the historical starting schema remain unresolved. No reference migration was executed. Full-stack Auth, Storage API, Realtime, Edge Functions, React and Next.js Supabase service integration, and deployment security remain unverified. Full-stack synthetic validation is deferred to Phase 5. See the [completion audit](PHASE_3_VALIDATION_COMPLETION.md) and [test matrix](SUPABASE_VALIDATION_MATRIX.md).

Phase 4 is pending separate authorization. The recovery checkpoint and staging workspaces are retained outside the repository. No commit, push, publication or release is authorized.

## Final repository structure and file inventory

Each entry gives its path from the repository root. The Git directory is omitted.

```text
modified README.md
modified ROADMAP.md
new      docs/BACKEND_STRATEGY_COMPARISON.md
retained docs/KNOWLEDGE_MAINTENANCE.md
retained docs/PHASE_1.md
retained docs/PHASE_1_COVERAGE_AUDIT.md
retained docs/PHASE_2.md
retained docs/PHASE_2_COVERAGE_AUDIT.md
retained docs/PHASE_2_INTEGRATION.md
retained docs/PHASE_2_MERGE_PLAN.md
new      docs/PHASE_3.md
new      docs/PHASE_3_COVERAGE_AUDIT.md
new      docs/PHASE_3_INTEGRATION.md
new      docs/PHASE_3_MERGE_PLAN.md
new      docs/PHASE_3_VALIDATION_COMPLETION.md
retained docs/REACT_GUIDE_RECONCILIATION.md
retained docs/REACT_NEXTJS_COMPARISON.md
modified docs/SOURCE_EVIDENCE.md
new      docs/SUPABASE_ARCHITECTURE_ANALYSIS.md
new      docs/SUPABASE_SECURITY_REVIEW.md
new      docs/SUPABASE_VALIDATION_MATRIX.md
new      docs/VALIDATION_BACKLOG.md
retained scripts/smoke_react.cjs
modified scripts/validate.py
retained scripts/validate_examples.cjs
modified web-engineering/SKILL.md
retained web-engineering/assets/architecture-decision.md
retained web-engineering/assets/examples/README.md
retained web-engineering/assets/examples/inventory-api.ts
retained web-engineering/assets/examples/list-state.ts
retained web-engineering/assets/feature-plan.md
retained web-engineering/assets/next-example/README.md
retained web-engineering/assets/next-example/app/[locale]/items/[slug]/Details.tsx
retained web-engineering/assets/next-example/app/[locale]/items/[slug]/page.tsx
retained web-engineering/assets/next-example/app/[locale]/layout.tsx
retained web-engineering/assets/next-example/app/robots.ts
retained web-engineering/assets/next-example/app/sitemap.ts
retained web-engineering/assets/next-example/catalog.ts
retained web-engineering/assets/next-route-plan.md
modified web-engineering/assets/project-profile.md
new      web-engineering/assets/supabase-example/README.md
new      web-engineering/assets/supabase-example/checks/policy-assertions.sql
new      web-engineering/assets/supabase-example/src/browser.ts
new      web-engineering/assets/supabase-example/src/database.generated.ts
new      web-engineering/assets/supabase-example/src/files.ts
new      web-engineering/assets/supabase-example/src/notes.ts
new      web-engineering/assets/supabase-example/supabase/migrations/20261125000000_notes.sql
new      web-engineering/assets/supabase-example/supabase/seed.sql
new      web-engineering/assets/supabase-plan.md
modified web-engineering/references/compatibility.md
modified web-engineering/references/index.md
retained web-engineering/references/next/data.md
modified web-engineering/references/next/profile.md
retained web-engineering/references/next/public-ui.md
retained web-engineering/references/next/rendering.md
retained web-engineering/references/next/workflows.md
modified web-engineering/references/project-documentation.md
modified web-engineering/references/project-selection.md
retained web-engineering/references/react/architecture.md
retained web-engineering/references/react/data-and-identity.md
retained web-engineering/references/react/delivery.md
retained web-engineering/references/react/interface.md
retained web-engineering/references/react/workflows.md
modified web-engineering/references/react-dashboard.md
modified web-engineering/references/shared-core.md
retained web-engineering/references/standards.md
new      web-engineering/references/supabase/applications.md
new      web-engineering/references/supabase/database.md
new      web-engineering/references/supabase/identity.md
new      web-engineering/references/supabase/profile.md
new      web-engineering/references/supabase/services.md
new      web-engineering/references/supabase/workflows.md
```

## Validation

| Check and command | Candidate result |
| --- | --- |
| `python3 scripts/validate.py` and Skill Creator `quick_validate.py web-engineering` | Skill metadata, rules, links and evidence references passed. |
| Exact rule comparison, compatibility and workflow counts, template and privacy review | 18 original rule IDs and two Supabase IDs, 19 Supabase workflows, nine compatibility configurations, eight scenario assessments and 20 backlog items. No removed files, private paths, common secret signatures, symlinks or dependency/build directories detected. |
| Strict TypeScript and `node scripts/validate_examples.cjs`, then `node scripts/smoke_react.cjs` | Neutral assertions and React DOM smoke passed. |
| `tsc --strict --types node --noEmit --target ES2022 --module NodeNext --moduleResolution NodeNext` | Synthetic catalog types and positive/negative fixtures passed with Supabase JS 2.107.0 and dependency declaration checks enabled. |
| `next build --webpack` and `next start -H 127.0.0.1` with loopback assertions | Next.js 16.2.4 passed production build and locale, direction, canonical, alternate locale, 404, sitemap and robots checks. |
| `createdb` and `psql -X -v ON_ERROR_STOP=1` using the disposable socket | Synthetic migration, seed and positive/negative authorization assertions passed on two fresh PostgreSQL 16.15 databases. Auth and Storage were represented at the SQL boundary. |

## Final canonical result

**PHASE_3_INTEGRATED_CONDITIONALLY**

The full validation suite passed again from canonical content. The final canonical working tree matches the validated candidate byte for byte, excluding the Git directory. The integration added 25 files and modified 13, with 34 baseline files unchanged. The existing branch is unborn and all 72 working-tree files are untracked. The external recovery checkpoint remains intact.

The reference checkout has advanced since the recorded evidence snapshot and currently has a clean working tree. This integration used the previously approved evidence and left the reference tree untouched. The reference results remain scoped to the recorded revision. No production infrastructure was accessed.
