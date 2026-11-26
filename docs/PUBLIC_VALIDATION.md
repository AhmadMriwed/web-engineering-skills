# Public validation summary

Frozen runtime `8699a0ff508f665dd2731858f2d93595000e29f0` contains 52 files, 20 stable engineering rules and 29 named task routes. [Phase 5 evidence](PHASE_5.md) · [Remediation](PHASE_5_1.md)

| Capability | Observed scope |
| --- | --- |
| Agent Skills format | YAML metadata, package shape, portable relative references and byte integrity checked locally. |
| Codex CLI | Project-local installation, explicit invocation, automatic use in tested scenarios, reference reads and independent implementation traces. |
| Claude Code | Official installation/invocation guidance reviewed. Installation, discovery, activation, references and implementation remain unverified. |
| Other consumers | Shared specification only. Installation and runtime behavior remain unverified. |
| React and Next.js | Selected fixture suites, strict TypeScript, React DOM, Next.js production build and HTTP smoke. |
| External REST and combined apps | Local browser and API interactions against synthetic data, including selected denied requests. |
| Supabase | Architecture proposals, SDK compilation, generated types and synthetic PostgreSQL checks. Managed services and deployed authorization remain unverified. |

Seven independent project scenarios ran. Five produced implementation evidence within their tested scopes. Two evaluated Supabase discovery and architecture selection. A focused routing intake exercised the named route catalog, with no claim of 29 independent implementations. Comparisons were small observational trials.

Browser checks covered selected keyboard, focus, responsive and RTL paths. Supplemental checks used synthetic identities, in-memory server import storage and browser-local draft recovery. The six advanced domains remain partially verified. Browser tests do not establish comprehensive accessibility. Reference migration replay and production deployment evidence are separately outstanding. See the [backlog](VALIDATION_BACKLOG.md).
