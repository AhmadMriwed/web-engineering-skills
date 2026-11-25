# Supabase security review

Scope covers checked-in SQL, representative web and function callers, and observable intent. Production grants, secrets, redirect settings, rate limits, logs, buckets and data were outside the inspection. Treat observations as review leads where effective cumulative policy is unknown.

| Resource and evidence | Intended access | Static assessment and verification required |
| --- | --- | --- |
| Identity/profile and role assignments, S02/S04 | Self profile plus authorized managers, tightly scoped role changes | Snapshot has broad table grants and row rules. Later employee hardening revokes table-wide access and grants a column projection. Reconcile both and test protected columns and function paths under current roles. |
| Organizational lookups and roles, S04 | Authenticated active lookups, administrator writes | Snapshot policy predicates distinguish active lookups and manager/admin writes. Verify effective cumulative grants and checks on updated rows. |
| Suspensions and detailed view, S04 | Self, scoped managers, privileged audit | Snapshot RLS is actor- and department-aware. Inspect view ownership, invoker settings and exposed grants separately before relying on base-table policy. |
| Settings, S04 | Controlled function path | Snapshot expresses direct deny. Audit execute privileges and function inputs independently. |
| Posts, categories, attachments, category links, interactions, S04 | Scoped parent records and associated interactions | Snapshot has narrower parent policies and wider child SELECT predicates. A later attachment read overlay exists. Verify direct child reads remain aligned with current parent visibility. |
| Conversations, messages, preferences and audit, S07 | Participants and own preferences; explicit audit operation | Participant and self predicates and direct audit deny appear in the chat migration. Writes use RPC. Test revoked membership, direct writes, RPC grants and actual subscription payload boundaries. |
| Document records, folders and access metadata, S03/S06 | Scoped organization access and approved shares, administrative maintenance | RPC checks and Storage predicate overlays are separate. Validate copy/replacement, expired shares, same-unit vs other-unit and post-revocation access independently. |
| Object namespaces and public media, S06 | Public-facing media vs private documents | Review public URL paths and storage metadata policies separately. Signed URLs should be treated as bearer credentials with bounded lifetime. Check cleanup errors and metadata divergence. |
| Integration and public data Edge handlers, S08 | Surface-specific public, signed-in or provider callers | Server secrets appear in source as env lookups. Confirm every elevated operation's credential and permission gate, input contract, redaction, timeouts and rate limits. No deployed verification. |
| Other feature schema overlays, S05 | Per-feature contracts | Effective table/function ledger and actor matrix remain open. Require disposable replay plus catalogs before a project-wide verdict. |

## Findings to carry forward

- Snapshot and migration overlays can encode different effective privileges. A policy listing alone does not establish authority. Capture grants, policies and function execution from an approved isolated replay.
- Row policies govern rows. Use explicit grants to protect columns and check views or child tables individually.
- Browser-persisted sessions are accessible to same-origin JavaScript. Review CSP, script trust and token-safe logs. Move Supabase calls out of async auth event callbacks, avoid duplicate subscriptions, and cancel or ignore stale in-flight profile requests across identity changes.
- Keep service credentials server-only. Review function owner, fixed search path and intended EXECUTE audience. Use verified identity and current resource checks before privileged writes.
- Validate at trusted boundaries, use safe parameterization, and enforce rate limits on auth, uploads and cost-bearing endpoints. Consider cookie CSRF, exact redirect origins, separate application and database authorization, and an auditable retention policy.
- PostgreSQL fixture outcomes cover synthetic owner, peer, scoped admin, other workspace, revoked membership, anonymous, ownership checks, title constraints and object path policy. Storage/Auth service behavior and reference policy correctness remain unverified.

See the [reusable security practice](../web-engineering/references/supabase/identity.md) and [optional services profile](../web-engineering/references/supabase/services.md).

## Ordered authorization audit

S12 provides a per-relation private index with RLS markers, operation, role, mode, USING and WITH CHECK predicates, and direct and schema-wide ACL events. It also indexes function declarations and grants, explicit drops and privilege changes. Evaluating privileges requires composing grants for inherited roles and PUBLIC with policies per operation, checking permissive OR and restrictive AND, checking table and view ownership or bypass, and checking function-level authorization independently. Many protected tables are intended for RPC-only use. A missing direct policy does not establish that an elevated RPC cannot operate on them.

The final top-level projection contains 98 policy declarations, of which 45 target Storage. The 144 explicit RLS markers and eight remaining relation cases are source projections. For 775 elevated function candidates, review execute ACL, verified actor checks, current tenant/resource predicates, and search-path writability. Ten lack declaration-level search-path settings. External role definitions, defaults, schema exposure and 453 procedural blocks constrain conclusions. This review did not establish exploitable behavior or a clean effective catalog. See the [completion report](PHASE_3_VALIDATION_COMPLETION.md).
