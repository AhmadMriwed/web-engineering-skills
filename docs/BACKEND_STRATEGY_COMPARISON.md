# Backend strategy comparison

| Candidate | Fit and strengths | Work and trade-offs |
| --- | --- | --- |
| No backend | Public authored or generated content, no accounts or persistence | Static delivery and simple recovery. Add a backend only for a concrete requirement. |
| Existing or in-flight API | Current system of record, team owns a contract or is delivering one | Preserve ownership and sessions. Use fixtures for in-flight contracts and verify CORS, versioning and service guarantees. |
| Next.js server capabilities | UI-connected server reads and mutations, SSR identity or callback handling | Choose persistence and file services separately. Keep private cache isolated and verify runtime/host limitations. |
| Dedicated backend | Rich domain orchestration, strict hosting or compliance control, long-lived workloads | Greater operational ownership of DB, identity, messaging, deployment and availability. |
| Supabase | Managed relational CRUD, identity, private file access and selective Realtime | Use migrations, RLS and verification. Plan limits, data residency, egress, compute, Auth email delivery and restore. PostgreSQL schema transfers more readily than Auth sessions, object metadata, Realtime and function infrastructure. |
| Hybrid | Bounded CRUD plus external systems or durable jobs | Assign source of truth, explicit service identities, retries, queue visibility and clear release responsibility. |

Use the [selection workflow](../web-engineering/references/project-selection.md). Ask for explicit approval of material frontend and backend choices and of provisioning, then record the boundary and alternatives in PROJECT_PROFILE and an ADR. The cases below were traced manually through the staged workflow.

| Case | Recommendation and alternatives | Boundary and dependency check |
| --- | --- | --- |
| A. Dashboard, existing REST | React and current API. Compare Next.js only if server rendering or mediation matters. | Current API owns data/authorization. Preserve client contracts and approved origins. |
| B. Multilingual SEO, no persistence | Next.js public locale routes, prerender where feasible. Compare simpler static tooling. | Public content, no session or database dependency. Verify localized canonicals. |
| C. Dashboard needs login, DB and files | React plus Supabase if managed-region/cost fit. Compare dedicated backend and file service. | Owner-approved provisioning. RLS, Auth and private object boundaries. |
| D. Next.js account app | Next.js with approved persistence and identity, Supabase SSR if selected. Compare separate identity/backend. | Request-bound auth, permission checks and private caches. |
| E. React plus Next shared backend | Split app deploys if ownership/cadence need them. Compare one Next.js app. | One migration owner, separate app permissions, no implied shared cookies. |
| F. Working dedicated backend | Retain React and the existing backend. Compare migration only when supported by a concrete requirement. | Current server controls operations; no new SDK dependency. |
| G. Complex and long-running | Dedicated worker/backend or hybrid with managed CRUD. Compare managed runtime limits. | Durable queue and idempotent jobs, service identities and recovery ownership. |
| H. Strict tenant isolation | Compare shared Postgres with tested RLS and tenant-consistent FKs, dedicated schemas or isolated projects according to policy. | Include Storage, Realtime, elevated operations and incident containment. Approval before choosing isolation model. |
