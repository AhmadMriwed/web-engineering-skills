# Profile compatibility and combined systems

Choose the full combination before scaffolding. See [React](react-dashboard.md), [Next.js](next/profile.md), [shared rules](shared-core.md) and [project selection](project-selection.md). All combinations also apply WEB-DEC-001 and WEB-DOC-001.

For landing pages use WEB-NEXT-002 and WEB-SEO-001, with minimal client state and static export only when every feature supports it. Export remains unverified. For authenticated Next.js routes apply WEB-AUTH-001 and use request-scoped private data and upstream checks. For React dashboards combine WEB-UI-002 with the applicable backend boundary below.

## Combined deployment

Separate apps when ownership, release cadence, traffic, or security boundaries justify separation. A monorepo can provide coordinated dependency and contract changes, shared tests and tooling. Separate repositories can support independent ownership and release control. Publish versioned types and tokens as neutral packages where both sides use them. Share validation-compatible contracts and design values before sharing framework-dependent components.

Choose a single Next.js app with public and authenticated route groups when one team, identity boundary, host and release cadence make separation costly. For combined deployments, map domains and cross-app links, allowed origins and cookie scope. Prefer narrow cookies and explicit identity handoff where needed. Document CSRF and CORS at the API boundary, cross-app redirects, shared contract change policy, evidence of independent deploys and who owns rollback. Verify direct navigation, session transitions, version skew and data isolation. See the backend-specific combinations below.

Assign ownership for shared API contracts and environment variables per deployment. Keep server credentials in the application that uses them. Put approved browser configuration in each app's own environment and verify dev, preview and production origins and backend compatibility independently. Record owners for shared documentation and per-app deployment runbooks.

## Backend combinations

All rows apply WEB-DEC-001 and WEB-DOC-001. Supabase rows also apply WEB-SUP-001, WEB-SUP-002 and WEB-AUTH-001.

| Combination and rules | Profile and workflows | Rendering and state | Data, identity, authorization and storage | Deployment, limits and evidence |
| --- | --- | --- | --- | --- |
| React without backend, WEB-ARC-001 | [React workflows](react/workflows.md) | SPA, URL and local state | Authored data, no backend boundary | Static host with route fallback. Neutral React smoke. |
| React with API, WEB-API-001 | [React workflows](react/workflows.md) | SPA, query cache | Existing contract and API authorizer. API owns data and files | Static host with API and CORS. Source and neutral seam evidence. |
| React with Supabase, WEB-STATE-001 | [Supabase workflows](supabase/workflows.md) and [frontend integration](supabase/applications.md) | SPA, scoped client query cache | Browser identity with grants/RLS and optional Storage | Static host and backend release. Source plus neutral DB evidence. Managed integration unverified. |
| Next without backend, WEB-NEXT-002, WEB-SEO-001 | [Next.js workflows](next/workflows.md) | Static/public render and locale routes | Authored data and no backend session | Static when host/features permit. Neutral Node build and HTTP. |
| Next with API, WEB-API-001, WEB-NEXT-002 | [Next.js workflows](next/workflows.md) | Server reads and client islands | Server session and upstream authz; upstream owns data/files | Node if dynamic. Static evidence for upstream integration. |
| Next with Supabase, WEB-NEXT-001, WEB-NEXT-002 | [Supabase workflows](supabase/workflows.md) and [frontend integration](supabase/applications.md) | Request-scoped private data, isolated public cache | SSR cookie clients with RLS, reauthorize mutations, private file access | SSR host plus backend. Official guidance, integration unverified. |
| React and Next with API, WEB-API-001 | [React](react/workflows.md) and [Next.js](next/workflows.md) | SPA paired with App Router; separate caches | Shared DTO and API grants, explicit identity handoff | Separate or coordinated releases. Architecture assessment. |
| React and Next with Supabase, WEB-NEXT-002 | [Supabase workflows](supabase/workflows.md) and [frontend integration](supabase/applications.md) | SPA and SSR, disjoint session/cache owners | Shared schema, separate app permissions and file scopes | Separate releases plus one migration owner. Architecture assessment. |
| Dedicated backend or hybrid, WEB-API-001, WEB-QA-001 | [Selection](project-selection.md) and chosen frontend workflows | Framework-appropriate with explicit job state | Dedicated backend or approved managed CRUD. Backend owns persistence, files and permissions. Workers use explicit service identities. | Additional queue/worker and failure recovery. Architecture assessment. |
