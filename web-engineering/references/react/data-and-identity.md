# Data, state and identity

### WEB-API-001 — Trace data through a typed feature boundary

**REQUIRED** within the rule’s applicable scope.

A page calls a feature hook, the hook calls a service, and the service uses a configured transport. Give transport configuration ownership of base URL, credentials, cancellation and error classification. A service owns request mapping and response decoding. Treat response data as unknown at consequential trust boundaries. Validate required shape, then adapt envelopes into feature-facing data. Keep services usable without React.

Use normalized list inputs and identity scope in cache keys where the client can serve multiple identities. Separate list, detail and aggregate key families. On mutation success, update exact authoritative cache entries or invalidate affected families. After a known rejection, show contextual feedback. Retry transient reads with a bound. Retry writes only under a supported idempotency contract. Forward cancellation where route or filter changes can obsolete requests. Add conditional polling only while a server state warrants it and stop on terminal state or unmount.

For example, a stock adjustment can update the detail from its authoritative response and invalidate filtered inventory lists whose membership or sort order may change. Check malformed responses, transport failure, overlapping mutations, cancellation, retry and affected keys. See WEB-SRC-001 E02/E03/E09 and WEB-SRC-002 G03–G05.

### WEB-STATE-001 — Assign one owner per kind of state

**REQUIRED** within the rule’s applicable scope.

| State | Owner | Examples |
| --- | --- | --- |
| Shareable navigation state | Router and URL codec | Search, filters, sort and page |
| Remote data and freshness | Query cache | Lists, details, mutations and aggregates |
| Transient interaction | Component or form | Dialog open, pending text, draft edits |
| Cross-route local state | Scoped provider or client store | Theme preference, session metadata |

Keep uncommitted search text local when typing is frequent. Apply it on submit or debounce a replace navigation, then derive request inputs from the URL. Validate incoming and outgoing values with the same codec, reset page atomically on a filter change, and preserve unrelated parameters. Clamp the page against backend pagination after deletion or a scope change. Keep private inputs out of URLs. Shareable filters add little value to a transient selector.

Test initial loading, back/forward, stale requests and a filter change while on a later page. For the parser and state precedence see [neutral TypeScript examples](../../assets/examples/list-state.ts). See WEB-SRC-001 E03/E08 and WEB-SRC-002 G05.

### WEB-AUTH-001 — Enforce permissions at the backend boundary

**REQUIRED** within the rule’s applicable scope.

Model session initialization, signed-out, signed-in and expired states. Let route guards and navigation reflect access for UX. Require backend enforcement for every protected operation and resource, including direct requests. Give 401 expiry handling and 403 permission feedback separate paths. Choose credential storage and renewal for the backend and deployment. Browser-readable credentials need exposure review. Cookie sessions require appropriate attributes and CSRF protection for relevant operations.

Keep credential access and expiry callbacks in session composition. On logout or account change, cancel or isolate in-flight private data, clear private cache and persisted session state, and replace protected history as appropriate. Handle expiry once per session and avoid redirect loops on sign-in requests. For example, an inventory viewer may see a read-only route while the API independently rejects stock updates. Test direct links, backend permissions, account switch, expiration, and late requests. See WEB-SRC-001 E04/E09 and WEB-SRC-002 G05/G07.

## External API principles and adapters

Document base URL, version, auth, timeouts, envelope, error shapes, pagination and write semantics in the API integration document. Configure one client per trust or protocol boundary and restrict where credentials are attached. Middleware for auth, locale and correlation belongs at the transport layer. Endpoint models and mapping belong to the feature. With Axios use a scoped instance and configured interceptors. With Fetch use an equivalent injected function and explicitly handle HTTP errors. TanStack Query is a React lifecycle adapter around these capabilities.

For uploads, let the browser compute the multipart boundary, validate file size and type with the server, and surface progress if the workflow needs it. For downloads, verify access, content type and safe names, and revoke temporary object URLs. Keep running requests scoped by identity and normalized input. Cancel obsolete reads, ignore superseded results where cancellation cannot be enforced, and serialize conflicting writes or use version preconditions. Treat cancellation separately from failure. Choose bounded retries based on operation semantics, response status and server hints.

If refresh is supported by the backend, coordinate concurrent expiry events through one refresh attempt, replay eligible requests at most once, and terminate the session on failure. Its presence and security properties require an explicit backend contract. See WEB-SRC-001 E09/E14/E16.

## Security review at trust boundaries

Keep secrets server-side and restrict deployment credentials to the necessary environment. Redact identifiers, tokens, personal data and raw bodies from client logs and error reports. Give users recovery instructions and retain diagnostic detail in authorized monitoring. Rely on framework text escaping, validate untrusted URLs, and avoid rendering untrusted HTML. Where rich content is required use an approved sanitization policy. Use server-side authorization and input validation regardless of UI guards. Enforce CSRF controls with cookie-authenticated mutations and explicitly allow only the origins required by the API. CORS governs browser access and is separate from authentication and authorization. Verify permission changes, session expiry, retry limits and safe user-facing errors. These are security requirements for the target project. Source review covers browser-side controls and cannot establish backend policy. See WEB-SRC-001 E04/E09/E16.
