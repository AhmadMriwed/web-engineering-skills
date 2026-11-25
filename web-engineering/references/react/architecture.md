# React application architecture

### WEB-ARC-001 — Compose routes and providers at the application boundary

**RECOMMENDED** within the rule’s applicable scope.

Use an application composition root for the router, query client, theme, locale initialization and error boundaries. Register public routes separately from the authenticated route group. Mount the sidebar and top bar once around nested page content. Keep navigation labels and visibility rules declarative. Use route builders for links and redirects, and verify that their output matches registered patterns. Pages compose the screen, state and interactions.

An authenticated inventory dashboard might register a signed-in shell with a list and detail route, leaving sign-in outside the shell. A single-screen tool may only need a root component. Add providers when a tree actually consumes the capability. For deployed SPAs, direct-refresh a nested route and verify browser back, unknown routes, focus after navigation and redirects. See WEB-SRC-001 E01, E07 and WEB-SRC-002 G02/G07.

### WEB-ARC-002 — Organize source by feature and dependency direction

**RECOMMENDED** within the rule’s applicable scope.

| Location | Responsibility |
| --- | --- |
| `app/` | Startup, providers, route table, application policy |
| `features/<feature>/pages/` | Route composition, transient screen decisions and workflow feedback |
| `features/<feature>/components/` | Feature views and intentional controller components |
| `features/<feature>/api/` | Endpoint calls, request/response adapters |
| `features/<feature>/hooks/` | Query and mutation lifecycle, reusable React coordination |
| `features/<feature>/types/`, `config/`, `lib/` | Domain contracts, declarative settings and pure helpers |
| `shared/` | Feature-independent UI, transport factories and stable utilities |
| `locales/` | Shared catalog namespaces and feature resources when multilingual |

Create folders as a feature needs them. Keep strict TypeScript and align import aliases across compiler, bundler and tests. Follow the project's casing and suffix conventions. In a new project, use recognizable PascalCase component files and consistent kebab-case service and hook files. Export supported feature entry points selectively. Let the app integrate feature APIs when features collaborate. Compose domain-scoped infrastructure at the feature or app boundary and inject credentials into generic transport. Enforce import direction with a lint restriction when recurring violations justify it.

Example: a product list owns display mapping and filtering. A generic dialog belongs in shared UI. A route shell can call a public sign-out function from the auth feature. Check new shared modules for feature imports and new feature imports for private implementation dependencies. See WEB-SRC-001 E01/E07 and WEB-SRC-002 G02–G05.

### WEB-ARC-003 — Extract components around stable responsibilities

**RECOMMENDED** within the rule’s applicable scope.

Keep short row, card or section helpers beside their caller. Extract a feature-private file when it has an independent responsibility, interactions worth testing, or a body that obscures its parent. Promote to shared UI when the contract is feature-neutral and reuse is real or deliberate. Repeated styling alone can call for a token or variant. Keep feature language and actions in the caller. Avoid configuration props that make shared components mirror several unrelated screens.

Example: keep an inventory mobile card with its list. Expose a shared table's column renderers and row key, and let the inventory feature supply labels, links and status mapping. Verify that API calls, feature-specific translation keys and permission decisions stay in their owning layer. See WEB-SRC-001 E08 and WEB-SRC-002 G04/G05.

## Startup configuration and composition

Put public runtime settings in `app/config/` or a neutral shared config module. Parse required values once at startup, fail with a safe and actionable message, and document defaults and per-environment overrides. Build-time browser variables and public runtime configuration are visible to users. Keep secrets in server or deployment infrastructure. Use theme settings and brand assets through a typed composition input where more than one audience warrants it.

Use typed props for controlled values, events and view data. Prefer named domain events over exposing store setters. Choose one owner for open state and document controlled versus uncontrolled behavior. Keep derived values in render. Extract a hook for reusable stateful behavior or an isolated lifecycle, a service for external I/O, and a pure utility for deterministic logic. Keep one-off logic nearby until the boundary clarifies ownership or tests. Use effects for subscriptions and external synchronization. Clean listeners, timers and obsolete requests on dependency changes or unmount, and verify behavior under Strict Mode.

For a second audience, compare distinct routes and permissions inside one app with separately deployed shells. Share neutral primitives and stable contracts. Keep audience navigation, permissions, branding and release boundaries explicit. Avoid creating an audience framework before the second audience has concrete requirements. The pinned source has one audience. Verify cross-audience links, direct access, and shared dependency boundaries in the target. See WEB-SRC-001 E01/E07/E16 and WEB-SRC-002 G02/G10.
