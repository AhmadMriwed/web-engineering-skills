# Phase 5 independent real-agent validation

**PHASE_5_COMPLETE_WITH_EXPLICIT_LIMITATIONS**

Independent Codex CLI trials used an immutable copy of the Web Engineering Skill. Explicit invocation and automatic use were observed in CLI file-read traces. Real builds and selected browser/API flows passed for generated fixtures. None of these results establishes managed Supabase behavior, Claude Code activation or production readiness.

## Frozen baseline

Commit `8699a0ff508f665dd2731858f2d93595000e29f0` on `main` is the single authorized commit. It contains 83 files, including 52 files in the frozen skill. The pre-commit recovery archive checksum matched and the initial commit passed the repository metadata/link/rule validator and skill-creator validator. The baseline had no ignore file. Staging used the reviewed repository roots and excluded private source, dependencies and build outputs. The frozen manifest and hashes were verified again after the trials.

The durable evaluation directory holds the isolated projects, CLI traces, fixture sources, rubric, file manifests, and browser and runtime artifacts. The canonical skill content remains identical to the commit. Only Phase 5 reports, backlog and roadmap changes are in the working tree. The workspace and checkpoint paths are supplied in the handoff rather than packaged.

## Environment and scope

| Capability | Result |
| --- | --- |
| Host and toolchain | macOS 26.5.2 arm64, Node 22.23.2, npm, pnpm, Git. Available disk was about 14 GiB at preflight; process isolation restricted the direct RAM probe. |
| Codex and Claude | Codex CLI 0.171.0-alpha.13 logged in with ChatGPT. Fresh CLI sessions used project-local skill folders and recorded JSONL. Claude CLI was unavailable on PATH. |
| Browser | Installed Chrome with Playwright. Desktop/mobile, locale, keyboard and focus tests ran locally. |
| Database | PostgreSQL 16.15, private socket, synthetic compatibility schemas and actors. Supabase CLI 3.4.0 runs with local CLI state redirected. |
| Managed stack | No Docker-compatible engine or available socket was found. No pre-existing native disposable stack was available. No system software or service images were installed. |

For a future full-stack run, use an approved disposable runner and functioning container engine with storage and memory for the selected stack. Verify the engine first with `docker version`. In a disposable project with the pinned CLI, use `supabase init`, `supabase start`, `supabase db reset`, and `supabase stop` according to its version and binding options. Confirm fixture identity and local binding before reset. The Phase 3 record details the starting-schema requirement and prior capacity guidance. [Phase 3 limitations](PHASE_3_VALIDATION_COMPLETION.md)

## Evidence and review

- [Activation report](AGENT_ACTIVATION_REPORT.md) records installation, metadata limits, explicit usage and automatic discovery traces.
- [Project results](AGENT_VALIDATION_RESULTS.md) covers scenarios A–G, focused route selection, clarification, implementation and documentation observations, the six gap tests, and browser and security limits.
- [Comparative evaluation](COMPARATIVE_EVALUATION.md) records paired observations, discovery scores and measured cumulative session usage.
- [Improvement plan](PHASE_5_IMPROVEMENT_PLAN.md) proposes fixes and retests. The frozen baseline was retained.
- [Backlog](VALIDATION_BACKLOG.md) reconciles all 17 reusable and three reference-specific items.

## Regression results

`baseline-regression.log` records passing repository and YAML validation, all 20 stable rule IDs, local links, strict TypeScript examples, React assertions and DOM smoke, Supabase JS strict compilation, Next.js 16.2.4 Webpack production build and HTTP smoke, and a clean disposable synthetic PostgreSQL migration and role assertion run. The detached installed copy was read by independent Codex sessions. Project A exercised real HTTP requests against a synthetic REST server, and selected independent browser checks ran against the generated applications. The evaluation did not access real customer data or deployed infrastructure.

## Release assessment

Measured evidence supports Codex installation and use in this environment and selected neutral project behavior. Managed Supabase capabilities, production authorization, Claude Code activation, and broad accessibility and deployment checks remain unverified. Reference-specific replay needs a sanitized starting schema, ordered evidence and a disposable service stack. The frozen route-table count defect and evaluation-harness improvements are available for review. No release, tag, push, licensing decision or Phase 6 work occurred.
