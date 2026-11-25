# Storage, Realtime and Edge Functions

## Storage

Use public buckets for deliberately public assets and private buckets for user or tenant material. Public URL reads bypass object read authorization. Grant each required operation on `storage.objects` by bucket, trusted identity and namespace. Treat path input as untrusted and validate ownership or membership against the target resource. Use random stable object identifiers and sanitize display names. Check MIME/size at bucket and trusted service boundaries. A supplied MIME label is insufficient for security-sensitive files. For large uploads choose resumable transfer and record progress/cancellation per object. Signed URLs are bearer capabilities until expiration, so choose short TTL and redact them from logs. Validate list, read, upload, delete, copy and replacement independently. Update metadata and object state via retryable staged operations and compensating cleanup because SQL and Storage cannot commit together. Reconcile orphan candidates after a grace period with dry-run, retention checks and an explicit deletion decision. Use the Storage API for physical deletion.

## Realtime

Start with fetch or bounded polling when latency allows. Postgres Changes fits narrowly filtered updates with tested authorization and manageable subscriber volume. Check publication, event payload and replica identity behavior for the exact operations and versions. Use private Broadcast for scoped events and Presence for ephemeral collaboration. Configure channel admission and send/receive policies on `realtime.messages`. Treat topics and filters as routing hints. On scope change and unmount remove channels, coalesce redundant events, reconcile from authoritative reads after reconnect and test duplicate/out-of-order delivery. Invalidate query keys when ordering, counts or pagination can change. Patch cache only when a full, ordered, versioned payload makes it safe. Measure fanout, database/WAL impact, quotas and missed-event recovery.

## Server-side placement

| Seam | Use when | Boundary |
| --- | --- | --- |
| SDK | Single user-scoped read/write | PostgreSQL grants and RLS |
| SQL/RPC | Atomic relational work or invariant requiring database locality | Grants and caller/resource checks |
| Trigger | Invariant must apply to every writer | Transactional, bounded work and controlled side effects |
| Edge Function | Shared HTTP operation, external API secret or webhook across apps | Verified caller or signed webhook, validation and explicit authorization |
| Next.js Action | Form mutation coupled to App Router UI and revalidation | Validate request, authorize per invocation |
| Next.js Handler | HTTP callback or independent browser/integration API | Auth, content/method limits and scoped responses |
| Worker or dedicated service | Long-running jobs, durable delivery, heavy compute or network needs | Queue acknowledgment, retries, dead-letter and idempotency |

Place functions in `supabase/functions/<operation>/index.ts`. Share only stable request, error and observability helpers. Define allowed methods/origins, body limits, stable error codes and timeout budget. Follow environment/version-specific token verification guidance and verify principal before using elevated clients. Webhooks need provider-specific signature and freshness checks on the raw body and persistent deduplication. Keep request IDs and redact credentials and payloads. Keep secrets server-side. Retry only known transient failures within budget. Serve locally with synthetic secrets and validate unauthorized, permitted and duplicate requests before approved deploy. CI should check database reset, type drift, policy tests and application builds. Deployment plans should include runtime health, query latency, storage growth, Realtime quotas, cost, backups and timed restore drills.
