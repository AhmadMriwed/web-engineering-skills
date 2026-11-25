# Phase 2 Next.js extraction report

The staged recommendation below records the extraction outcome. The owner approved it and it was integrated. See the [integration report](PHASE_2_INTEGRATION.md) for the canonical validation.

**Recommendation — READY_FOR_OWNER_APPROVAL**

The staged proposal extends the approved React foundation into one Web Engineering Skill with a Next.js App Router profile, framework-neutral engineering guidance and conditional combined-project support. It adds three rules and preserves all 15 Phase 1 rule definitions. Review the [coverage audit](PHASE_2_COVERAGE_AUDIT.md), [React and Next.js comparison](REACT_NEXTJS_COMPARISON.md) and [merge plan](PHASE_2_MERGE_PLAN.md).

## Acquisition and scope

WEB-SRC-003 was acquired in the external reference workspace through authorized Git HTTPS. The default and analyzed branch was `main`. The exact revision and source location are in the private evidence record. The lockfile pins Next.js 16.2.4. The review inventoried 215 tracked paths and examined routing, composition, configuration, API flow, UI, localization, assets, styling, tests and repository documentation. Generated artifacts and sensitive values were excluded. Git tree and blob reads preserved the source. No source build or deployment was executed.

| Concern | Observed |
| --- | --- |
| Framework | Next.js 16.2.4 App Router, React and React DOM 19.2.4, strict TypeScript 5.9.3 |
| Styling and localization | Tailwind 4.3.1, next-intl 4.13.0, CSS variables, locale routing and Framer Motion |
| Integration | Native Fetch, typed envelopes, locale-aware requests and public endpoints |
| Forms and state | Local state and pending guards on traced public forms, React Hook Form 7.80.0 and Zod 4.4.3 in the lockfile |
| Tooling | npm lockfile, Next development/build scripts, ESLint and a Node test source for public API behavior |

## Extracted knowledge inventory

| Area | What the source demonstrates and how the skill uses it |
| --- | --- |
| Routing and architecture | A dynamic locale segment provides a root layout, provider, header and footer. Proxy handles localization. Catalog details delegate to another page, which motivates extracting a reusable view and explicit metadata. Route groups, private folders and protected handlers remain conditional guidance. |
| Rendering and cache | Locale static-parameter generation and an explicitly request-rendered catalog route show different choices. Some client components fetch after mount. Explicit ISR, streaming and invalidation lack evidence. The version-specific reference explains cache and render policy and tests to perform. |
| SEO | A shared builder produces localized titles, canonical URLs, alternates and Open Graph. Sitemap, robots and JSON-LD exist. A reused catalog metadata function warrants checking detail canonical intent. A generated current date is a weak modification signal. Actual crawl outcomes remain unverified. |
| Public UI | Header, mobile navigation, footer, hero, content sections, product discovery, FAQs, support and lead forms compose the site. Theme variables and project assets coexist with inline visual values and motion/3D islands. Shared guidance favors semantic tokens, narrow client boundaries and reduced-motion checks. |
| API | Typed native Fetch helpers parse envelopes, normalize HTTP errors, paginate and pass locale. Catalog and footer combine independent server reads. The sampled error/response handling lacks a runtime schema guarantee. Some client effects suppress stale writes without aborting network work. |
| State | URL filters control navigable selection. Component hooks own interactive inputs, pending state and fetched client results. A locale provider shares messages. No application import of a general global store, Axios or TanStack Query was found in the inspected product paths. |
| Security and forms | Public contact and partner paths submit to the external backend. A CMS sanitization seam and configured response headers appear in source. Authenticated reads, session renewal, roles, Server Actions and Route Handlers need target evidence before adoption. |
| Localization | Two locale trees, namespace registration, switcher, locale-specific metadata and document direction are in source. Validate parity, locale resolution, formatting and keyboard behavior in the target. |
| Quality and delivery | Static inspection found strict types, lint and build commands, and a public API test. Documentation differs by revision, including a description of hardcoded screens now wired to APIs. Deployment infrastructure and monitoring remain unverified. |

See the [source registry](SOURCE_EVIDENCE.md) for the nine evidence groups and the [comparison](REACT_NEXTJS_COMPARISON.md) for rationale, risks and validation.

## Proposed rules and shared changes

| Addition | Scope |
| --- | --- |
| WEB-NEXT-001 | Framework-native route structure, provider placement, component boundaries and failure conventions |
| WEB-NEXT-002 | Intentional render mode, data/cache scope and invalidation |
| WEB-SEO-001 | Canonical route contract, metadata, alternates and crawl artifacts |

Existing definitions and IDs are preserved. The [shared core](../web-engineering/references/shared-core.md) separates framework-neutral ownership, API, security, UI, localization and validation from framework mechanisms. The React SPA may retain Axios and React Query. Next.js can use Fetch, server data and small client boundaries. Project-specific assets, design values and business logic remain outside the proposal.

The [workflow reference](../web-engineering/references/next/workflows.md) covers initialization and review, feature/page/layout/component creation, public and detail routes, SEO, rendering, API, forms, authorization, localization, design system, motion, performance and validation. Each workflow links its decisions and docs. The template inventory includes the project profile, feature plan, architecture decision and new [Next.js route plan](../web-engineering/assets/next-route-plan.md). The [neutral library example](../web-engineering/assets/next-example/README.md) demonstrates localized static detail routes, server-only data, a client disclosure, canonical/alternate metadata, sitemap, robots and missing item handling. React examples remain available.

The [compatibility matrix](../web-engineering/references/compatibility.md) covers React SPA/dashboard, Next.js public/landing/authenticated, external API, no backend and combined options. The [selection workflow](../web-engineering/references/project-selection.md) evaluates the audience, rendering, backend state, identity, cost, team and host, then records the approved decision. Split deployments are conditional on ownership and release boundaries. A single Next.js app is also a candidate. Shared contracts and tokens can cross app boundaries without sharing runtime modules.

## Phase 1 gaps

Multiple audiences, bulk operations, import/export, dynamic fields, multi-step forms and unsaved changes retain their partial status. The localized public site and submission hooks did not supply adequate evidence for any of those domains. React packaging, examples and smoke tests remain available.

## Validation and limitations

| Check | Actual result |
| --- | --- |
| `python3 scripts/validate.py` and skill-creator `quick_validate.py web-engineering` | Phase 1 baseline passed with 15 IDs. Staging passed with 18 IDs, links and evidence references. |
| React examples, TypeScript 5.9.3 strict compile and `node scripts/validate_examples.cjs <compiled>` | Passed on baseline and staging. |
| `node scripts/smoke_react.cjs <compiled>` with React 19.2.4 and jsdom 26.1.0 | Passed on baseline and staging. |
| Neutral Next.js `tsc --noEmit` and `next build --webpack` on Node 22.23.2 | Passed. Both localized detail pages were prerendered and both crawl files generated. |
| Neutral Next.js `next start` on loopback and Node Fetch assertions | Passed localized HTML, direction, canonical and alternate presence, disclosure initial markup, 404 for unknown locale/item, sitemap and robots. |
| Privacy, staging and reference checks | Deliverable scan and revision verification passed. Comparison against the canonical baseline isolated the proposed changes. |

The default host Node executable failed due to a missing dynamic library. The checks used the installed Node 22 runtime. Loopback required escalated sandbox permissions. Source runtime, client hydration and accessibility, cache invalidation, real external API contracts, authenticated flows, ranking, Core Web Vitals and deployment correctness remain unverified.

## Staged file inventory

The listing shows paths relative to the staged root and their status against the approved baseline.

```text
modified README.md
baseline docs/KNOWLEDGE_MAINTENANCE.md
baseline docs/PHASE_1.md
baseline docs/PHASE_1_COVERAGE_AUDIT.md
new      docs/PHASE_2.md
new      docs/PHASE_2_COVERAGE_AUDIT.md
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

## Owner decisions and next phase readiness

Approve the three new rules, shared core, selection/compatibility scope and staged merge before applying the [merge plan](PHASE_2_MERGE_PLAN.md). The staged system supplies seams for a future backend profile. Supabase extraction requires its reference and separate authorization. Phase 3 remains pending.
