# Living project documentation

Maintain the following under `docs/`. Create baseline documents during initialization or the first maintenance change that needs them. Create conditional documents when their capability is planned or implemented. Keep the index current and update affected documents in the implementation change. Use related sections in one file during early work if the project's approved documentation conventions allow that.

| Document | Requirement and update trigger |
| --- | --- |
| PROJECT_PROFILE.md | Mandatory. Record approved technologies, constraints, environments and decisions at setup and after material changes. Use the [project profile](../assets/project-profile.md). |
| REQUIREMENTS.md | Mandatory. Update when outcomes, scope, acceptance criteria or constraints change. |
| ARCHITECTURE.md | Mandatory. Explain runtime boundaries, data and identity flows, and integration decisions. Update on structural changes. |
| PROJECT_STRUCTURE.md | Mandatory. Record entry points, module ownership and conventions when these change. |
| DESIGN_SYSTEM.md | Conditional on shared UI. Record themes, tokens, brand assets, variants, responsive and accessibility contracts when introduced or changed. |
| API_INTEGRATION.md | Conditional on API use. Document scope, endpoints or contract location, request/response, errors, auth and retry behavior as they change. |
| AUTHENTICATION.md | Conditional on access control. Document session, credential handling, roles, permissions and enforcement boundaries. |
| DATABASE.md | Conditional on managed persisted data. Document schema, migrations, access policies and ownership. |
| FEATURES.md | Mandatory. Update maps of implemented user flows, permissions and limitations when behavior changes. Use the [feature plan](../assets/feature-plan.md) during design. |
| TESTING.md | Mandatory. Record how to run checks, environments, coverage and known gaps with meaningful changes. |
| DEPLOYMENT.md | Mandatory. Document build, environment names, deploy/rollback and post-deployment checks. Update when delivery changes. |
| CHANGELOG.md | Mandatory once implementation starts. Record meaningful changes and known limitations. |
| ADRs | Required for material choices affecting architecture, dependencies, security or deployment. Record context, options, choice, consequences and verification. |

Use the [decision record](../assets/architecture-decision.md) for ADRs. Omit empty documents and describe planned capabilities as planned.

For Next.js, record each route's render policy, runtime environment, SEO and metadata contract, cache scope and revalidation, locale routes and server/client ownership in architecture, API, deployment or feature docs as appropriate. Use the [route decision template](../assets/next-route-plan.md).

For combined deployments, document application responsibilities, shared contracts, domain and cookie boundaries, deployment relationships, compatibility policy and rollback ownership. Keep shared policy in one location and link it from each app's documentation.

For Supabase, DATABASE and MIGRATIONS are required when the project owns schema. Include version history, migration and recovery steps, generated-type regeneration and drift testing. AUTHENTICATION documents session and account lifecycle. AUTHORIZATION documents grants, policies, privilege checks and actor matrix when access is restricted. SECURITY records trust boundaries, risks and verified controls for exposed backends. STORAGE, REALTIME and EDGE_FUNCTIONS are conditional on use. Update schema, migrations, security, authorization and generated-type instructions with schema changes. For small projects group these capabilities in substantive sections with index links and review the [backend plan](../assets/supabase-plan.md).

Small projects may record the minimum sections in a concise docs index with profile, decisions, behavior, checks and delivery. Medium projects use the standard documents above for their implemented capabilities. Complex projects add owned runbooks and separate authorization, security or localization documents when their independent review justifies it. Use [document prompts](../assets/document-prompts.md) for recurring sections. Record each fact once and link to its owner.
