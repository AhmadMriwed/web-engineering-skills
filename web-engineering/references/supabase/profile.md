# Supabase backend profile

Use after [backend selection](../project-selection.md). Keep the existing frontend profile and adopt only the backend capabilities the project needs. Start with the [workflow matrix](workflows.md), then read [database](database.md), [identity and authorization](identity.md), [optional services](services.md), or [frontend integration](applications.md) for the change.

### WEB-SUP-001 — Check in reproducible database change history

**CONDITIONAL** within the rule’s applicable scope.

Use uniquely versioned migrations for schema, grants, policies and functions. Reset a disposable environment from zero, verify upgrade from the previous release and regenerate types from the same schema before release. See [database engineering](database.md).

### WEB-SUP-002 — Test every exposed data surface as its actual caller

**CONDITIONAL** within the rule’s applicable scope.

Inventory grants, RLS, functions, views, storage and subscriptions. Test positive and negative access for each operation under actual anonymous, user, tenant and privileged contexts. Keep elevated connections server-only and separate from user sessions. See [identity and authorization](identity.md).

## Runtime boundaries

Browser components call feature hooks or explicit use cases. Put reusable Supabase setup under app infrastructure such as `src/lib/supabase/`, feature queries under `src/features/<feature>/repository.ts`, cache wiring in hooks and pure mapping next to domain models. A single small feature may keep a direct narrow query in its loader. Extract when callers share a contract, the operation has multiple steps, or boundary validation needs reuse. Infrastructure depends on generated schema contracts and configuration. Repositories depend on the typed client and map DB rows into stable application contracts. UI consumes those contracts. Keep SQL and Functions under `supabase/` owned by the backend release.

Use one browser client per app/project and one cookie-bound server client per request in SSR. Keep a distinct server-only administrative client with session persistence, automatic refresh and URL detection disabled. Avoid attaching incoming user JWTs to elevated client instances. Inject client instances at test seams. Validate startup config and keep browser settings limited to project URL and publishable key, or legacy anon key when required. Secrets belong in environment-specific secret stores. Document variable names and ownership, and commit placeholder values only. Use independently provisioned development, staging and production data and identities. Confirm region, network egress, version, extensions, limits and recovery targets before approving hosting.

Use the SDK for single authorized queries and simple writes. Share the external API profile's typed inputs and outputs, error normalization and cache decisions. Native PostgREST calls already implement transport. Use a feature adapter when mapping or composing inputs, without building another HTTP service merely to mirror SDK methods.
