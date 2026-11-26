# Initial version readiness assessment

The owner approved publication of v0.1.0 under Apache-2.0 with the documented verification scope. The candidate retains framework preferences, security boundaries, progressive disclosure and all 20 stable rules.

| Capability | Codex CLI | Claude Code | Other agents |
| --- | --- | --- | --- |
| Shared Agent Skills specification | Frontmatter and portable folder checked | Same format is documented | Portable format only |
| Installation documentation | Project-local path documented | Project-local path documented | Consult consumer instructions |
| Actual installation and discovery | Frozen package installed; project-local reads observed | Unverified | Unverified |
| Explicit invocation | CLI trace observed | Unverified | Unverified |
| Automatic activation | Ordinary requests led to skill reads in tested sessions; per-session metadata events unavailable | Unverified | Unverified |
| Reference loading | Direct tool traces | Unverified | Unverified |
| Independent implementation | Selected Phase 5 fixtures built and tested | Unverified | Unverified |

See [activation evidence](AGENT_ACTIVATION_REPORT.md) and [skill architecture](SKILL_ARCHITECTURE.md). Package the `web-engineering/` directory. Root reports, validator tooling, evaluation logs and proprietary provenance stay outside the package. Recheck installation on supported clients and scope claims to the verified consumer.

Packaging and confirmed validator issues have bounded checks. No evidence established a material defect in runtime security guidance. The candidate does not certify hosted systems. Managed Auth, Storage, Realtime, Edge, frontend integration, service session behavior, cache isolation, deployed authorization, migration replay and production security remain unverified. A disposable Supabase service stack needs a working supported container engine or authorized native runtime, adequate disk/memory, access to service images or archives, local binding and synthetic identities. Reference replay additionally needs a sanitized and ordered baseline. See [Phase 3 prerequisites](PHASE_3_VALIDATION_COMPLETION.md) and the [validation backlog](VALIDATION_BACKLOG.md).

Apache-2.0 licensing is approved. Preserve the frozen commit and evidence before any subsequent packaging or release work.

Phase 6 adds a reproducible distribution procedure and publication gates. See [distribution](DISTRIBUTION.md), the [public evidence summary](PUBLIC_VALIDATION.md) and the [publication checklist](RELEASE_CHECKLIST.md). The approved holder is Ahmad Mriwed.
