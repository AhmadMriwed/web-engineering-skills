# Phase 2 integration report

**PHASE_2_INTEGRATED** on 2026-11-25.

The owner-approved Next.js profile is in the canonical skill. The [extraction](PHASE_2.md), [coverage audit](PHASE_2_COVERAGE_AUDIT.md), [comparison](REACT_NEXTJS_COMPARISON.md) and [merge plan](PHASE_2_MERGE_PLAN.md) document the evidence and approval path.

## Baseline and merge

The local repository had an unborn `master` branch, no remotes, and 25 untracked files. A local archive outside the repository captured all 25 files before integration. The complete staging comparison showed the expected Phase 2 proposal and no unrelated file differences. The integration applied the approved files, added an index and roadmap, and clarified deployment and environment ownership. No merge conflicts arose. The staging workspace was retained. Repository files remain untracked, and no commit, push or publication occurred.

## Integration audit

Reviewed the staged guidance against the [Phase 2 coverage audit](PHASE_2_COVERAGE_AUDIT.md). Architecture and rendering guidance covers native routes, feature placement, boundaries, initial and request rendering, and caching choices. API, forms and identity guidance distinguishes server services, optional browser state, authorization and validation. Public UI and SEO guidance covers responsive composition, shared primitives, motion, localization, metadata and crawl artifacts. Workflow tables identify placement, preconditions, rules, documentation updates and verification. Added explicit deployment steps for choosing runtime or static delivery, separating build/runtime configuration, smoking the deployed routes and documenting rollback. Added per-app environment and documentation ownership to combined compatibility guidance.

| Inventory | Canonical location and scope |
| --- | --- |
| Shared standards | [Shared core](../web-engineering/references/shared-core.md), [standards](../web-engineering/references/standards.md), discovery, documentation and compatibility. Covers contracts, composition, state, security, UI, forms, localization and quality. |
| React | [Dashboard profile](../web-engineering/references/react-dashboard.md), architecture, data/identity, interface, delivery and workflows. Preserves SPA-specific alternatives and fixtures. |
| Next.js | [App Router profile](../web-engineering/references/next/profile.md), rendering, public UI/SEO, data/forms/security and workflows. |
| Workflows | [React](../web-engineering/references/react/workflows.md) and [Next.js](../web-engineering/references/next/workflows.md) cover initialization, architecture, features, API, auth, UI, locale, optimization and validation. Next.js additionally covers rendering, SEO, static or server delivery and crawl artifacts. |
| Templates | Project profile, feature plan, architecture decision and Next.js route plan. See the [skill index](../web-engineering/references/index.md). |
| Examples | [React inventory API and list state](../web-engineering/assets/examples/README.md) and a [localized neutral Next.js catalog](../web-engineering/assets/next-example/README.md). |
| Evidence | [Source registry](SOURCE_EVIDENCE.md) maps 16 React and nine Next.js implementation evidence groups. Private provenance remains external. |
| Living docs | [Project documentation](../web-engineering/references/project-documentation.md) defines baseline and conditional documents, affected updates and ADRs. Covers known limitations and change history, plus Next.js rendering, cache, SEO and deployment details and combined ownership. |

## Complete rule inventory

| Rules | Scope |
| --- | --- |
| WEB-DEC-001, WEB-DOC-001 | Technology approval, project documentation |
| WEB-ARC-001, WEB-ARC-002, WEB-ARC-003 | Composition, feature structure and extraction |
| WEB-API-001, WEB-STATE-001, WEB-AUTH-001 | Data contract, state ownership and authorization |
| WEB-UI-001, WEB-UI-002, WEB-UI-003 | Shared primitives, data views and motion |
| WEB-FORM-001, WEB-I18N-001 | Forms and localization |
| WEB-QA-001, WEB-PERF-001 | Verification and performance |
| WEB-NEXT-001, WEB-NEXT-002, WEB-SEO-001 | Native route boundaries, rendering/cache policy and canonical web discovery |

The entry point links both profiles and the [skill index](../web-engineering/references/index.md). All 15 Phase 1 definitions and three approved additions retain their IDs.

## Project selection scenarios

Manually traced each scenario through the [selection workflow](../web-engineering/references/project-selection.md) and [compatibility matrix](../web-engineering/references/compatibility.md). Each recommendation remains subject to user approval and is recorded in the project profile. The exercise assesses guidance.

| Scenario | Result |
| --- | --- |
| A. Internal admin and REST API | Recommend React and the existing external API. Evaluate interaction, browser transport and API authorization. |
| B. Public multilingual site with SEO | Recommend Next.js and localized public routes, with route-specific metadata and render policy. |
| C. Public site and admin | Compare Next.js plus React with one Next.js app. Weigh owners, deployment cadence, shared contracts, identity and operational cost. |
| D. Static landing with no account or persistence | Prefer Next.js for public delivery. Use static content and confirm host fit. No backend capability is required by the scenario. |
| E. Existing React feature | Retain the current stack and implement through the existing project profile. |
| F. New app with identity and persistence | Identify backend requirements. Compare framework-native server support backed by appropriate persistence, managed backend or dedicated service. Supabase remains a conditional candidate pending Phase 3. |

## Validation

| Command or check | Result |
| --- | --- |
| `python3 scripts/validate.py` | Passed metadata, local links, rule citations and audit evidence references. |
| Skill-creator `quick_validate.py web-engineering` with isolated PyYAML | Passed. |
| Strict TypeScript 5.9.3 compilation and `node scripts/validate_examples.cjs <compiled>` | Passed for both standalone React-profile modules and their assertions. |
| `node scripts/smoke_react.cjs <compiled>` with React 19 and jsdom | Passed simulated session boundary, URL filters, state transitions and RTL metadata. |
| Isolated `tsc --noEmit` and `next build --webpack` with Next.js 16.2.4 and Node 22 | Passed on sources copied from the canonical example. Both localized detail routes were prerendered. |
| `next start` and loopback Fetch assertions | Passed localized HTML, canonicals, language alternates, direction, initial disclosure markup, unknown route 404s, sitemap and robots. |
| Rule preservation, privacy and artifact scan | Exact set of 18 expected IDs. Phase 1 files outside the reviewed changes remained byte-identical. No known source URL, path, revision, branding or dependency on the staging workspace was found. No build artifacts or package installs were added. |

These checks verify neutral fixtures and package structure. Real browser hydration, keyboard and focus, accessibility, actual auth enforcement, cache invalidation, reference runtime, SEO ranking and deployment remain unverified.

## Files and repository structure

Paths are relative to the repository root.

```text
modified README.md
new      ROADMAP.md
baseline docs/KNOWLEDGE_MAINTENANCE.md
baseline docs/PHASE_1.md
baseline docs/PHASE_1_COVERAGE_AUDIT.md
new      docs/PHASE_2.md
new      docs/PHASE_2_COVERAGE_AUDIT.md
new      docs/PHASE_2_INTEGRATION.md
new      docs/PHASE_2_MERGE_PLAN.md
baseline docs/REACT_GUIDE_RECONCILIATION.md
new      docs/REACT_NEXTJS_COMPARISON.md
modified docs/SOURCE_EVIDENCE.md
baseline scripts/smoke_react.cjs
modified scripts/validate.py
baseline scripts/validate_examples.cjs
modified web-engineering/SKILL.md
baseline web-engineering/assets/architecture-decision.md
baseline web-engineering/assets/examples/README.md
baseline web-engineering/assets/examples/inventory-api.ts
baseline web-engineering/assets/examples/list-state.ts
baseline web-engineering/assets/feature-plan.md
new      web-engineering/assets/next-example/README.md
new      web-engineering/assets/next-example/app/[locale]/items/[slug]/Details.tsx
new      web-engineering/assets/next-example/app/[locale]/items/[slug]/page.tsx
new      web-engineering/assets/next-example/app/[locale]/layout.tsx
new      web-engineering/assets/next-example/app/robots.ts
new      web-engineering/assets/next-example/app/sitemap.ts
new      web-engineering/assets/next-example/catalog.ts
new      web-engineering/assets/next-route-plan.md
modified web-engineering/assets/project-profile.md
new      web-engineering/references/compatibility.md
new      web-engineering/references/index.md
new      web-engineering/references/next/data.md
new      web-engineering/references/next/profile.md
new      web-engineering/references/next/public-ui.md
new      web-engineering/references/next/rendering.md
new      web-engineering/references/next/workflows.md
modified web-engineering/references/project-documentation.md
modified web-engineering/references/project-selection.md
baseline web-engineering/references/react/architecture.md
baseline web-engineering/references/react/data-and-identity.md
baseline web-engineering/references/react/delivery.md
baseline web-engineering/references/react/interface.md
baseline web-engineering/references/react/workflows.md
baseline web-engineering/references/react-dashboard.md
new      web-engineering/references/shared-core.md
baseline web-engineering/references/standards.md
```

## Remaining gaps and next phase

The six partial React domains remain open. They are multiple application audiences, bulk operations, import and export, dynamic fields, multi-step forms, and unsaved changes. The integrated skill is ready to receive the next evidence source. Supabase extraction awaits the repository and separate owner authorization. See the [roadmap](../ROADMAP.md).
