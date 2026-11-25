# Phase 3 validation completion and readiness audit

**READY_FOR_CONDITIONAL_OWNER_APPROVAL**

| Assessment | Status | Basis |
| --- | --- | --- |
| Knowledge readiness | COMPLETE | Schema, migration, types, Auth, RLS, Storage, Realtime, Edge, both frontend profiles, combined apps, selection, testing, operations, recovery and documentation have actionable guidance. CLI v3 incompatibilities discovered during audit were corrected. |
| Source evidence readiness | PARTIAL | Complete top-level grammar inventory and ordered static authorization projection. Historical starting schema, dynamic SQL semantics, actual managed grants, effective policies and applied production configuration remain unestablished. |
| Runtime verification readiness | PARTIALLY_VERIFIED | PostgreSQL fixture, strict SDK compilation and framework regressions passed at their stated boundaries. Reference replay and managed Supabase integration remain blocked on infrastructure and replay prerequisites. |

Conditional approval is for the reusable knowledge and fixture. The condition is to retain the explicit verification labels and keep reference authorization, replayability and managed-service integration open. The proposal supplies no project-wide security attestation.

## Blocker classification

| Category | Disposition |
| --- | --- |
| Missing engineering knowledge | No additional rule or workflow was needed. Optional Supabase capabilities have implementation decisions, security boundaries and validation procedures. |
| Missing source evidence | The release ledger and current snapshot do not establish the historical starting schema or deployed configuration. The procedural SQL and inherited role state limit the static projection. |
| Missing validation infrastructure | A project-local CLI is operational. Full-stack execution needs an approved engine or enabled native runner, disk space and service download access. |
| Unverified runtime behavior | Reference replay and catalog, actual service authorization and frontend integration, release upgrade and recovery remain open. |
| Engineering defects | The staged instructions used unsupported CLI v3 flags. Corrected after inspecting local help. The negative fixture checks also omitted peer update, administrator delete and anonymous RPC denial. Expanded and rerun. Reference security leads remain unverified. |

## Environment and exact outstanding prerequisites

macOS 26.5.2 on Apple silicon, Node 22.23.2, npm 10.9.8, pnpm available, PostgreSQL/psql 16.15, and 18 GiB physical RAM. Available disk fell from approximately 1.5 GiB to under 1 GiB during audit. No Docker CLI, daemon sockets, Docker Desktop, OrbStack, Colima or Podman were found in the checked locations. The earlier disposable PostgreSQL cluster was accessible through a private Unix socket with no TCP listener when approved. It was stopped after testing.

A project-local npm install of Supabase CLI 3.4.0 succeeded with approved package network access. `SUPABASE_HOME` redirected CLI state into staging. `supabase --version` and `supabase init` succeeded. CLI initialization produced JSONC. The package registry and parser download were reachable under approval. Registry access for all container images or native service archives was not tested. No system installation or persistent service activation was performed.

For the supported container route, use an approved host with a functioning Docker-compatible engine and capacity for the selected stack. Supabase recommends at least 7 GB of RAM for all services. For this audit, allow at least 15 GiB free as a planning buffer for image downloads, unpacking and database volumes. This is a working estimate rather than a vendor minimum. Docker Desktop for Apple silicon can be installed from Docker's signed distribution once the owner approves the system change. On macOS, open the signed installer with `open Docker.dmg`, drag Docker into Applications and start it with `open -a Docker`. The owner can also provide an already provisioned disposable runner. The experimental native runtime documented for Apple silicon removes the engine dependency where enabled in the installed version. It still downloads and runs service archives, needs working disk, network and process permissions, and is suitable for the neutral fixture only within an approved isolation boundary. [Supabase local development](https://supabase.com/docs/guides/local-development) · [CLI resource guidance](https://supabase.com/docs/reference/cli/supabase-config) · [Docker and native runtimes](https://supabase.com/docs/guides/local-development/docker-and-native-runtimes) · [Docker Desktop for macOS](https://docs.docker.com/desktop/setup/install/mac-install/)

Once the owner has provided adequate capacity and activated the engine, verify the server and a test image before creating any fixture stack. Commands assume execution from a fresh staging-only directory with an approved local Docker context.

```sh
docker version
docker info
docker run --rm hello-world
npm init -y
npm install --save-dev --save-exact supabase@3.4.0
export SUPABASE_HOME="$PWD/.supabase-cli"
npx supabase --version
npx supabase init
npx supabase gen types --help
```

Before startup, copy only the reviewed neutral migration and seed from the [fixture](../web-engineering/assets/supabase-example/README.md). Configure unique project identity and local ports. Use the CLI's supported loopback binding or a dedicated Docker network with host binding set to 127.0.0.1. Verify published ports and fixture identity before resetting. The reset command defaults to local on v3.

```sh
docker network create -o com.docker.network.bridge.host_binding_ipv4=127.0.0.1 phase3-audit
npx supabase start --network-id phase3-audit
npx supabase status
npx supabase db reset
npx supabase gen types --lang typescript --schema public > database.generated.ts
npx supabase stop
```

Keep credentials from local status output in the local process context. Package and service downloads need approved egress. Reference replay needs a separate stack with runtime egress disabled, a sanitized pre-migration baseline, and the reviewed settings listed below.

## Reference migration history and effective authorization

A PostgreSQL parser processed the schema snapshot and every committed migration, retaining order and statement kind, including tables, columns and constraints, grants/revokes, defaults, indexes, functions, triggers, views, extensions, RLS and policy changes. The release ledger names 200 current files, with six unlisted. Simulations used snapshot plus ledger sequence plus six pending files, and snapshot plus filename order. There are 26 reused version prefixes and 49 order positions differ. The initial ledger batch is a historical inventory, so it cannot prove earlier execution order or that the tracked snapshot is a suitable empty replay baseline.

The two passes agree on tracked final top-level policy and function declarations. The static projection contains 152 relation candidates, 144 explicit RLS enable markers and eight unspecified cases. It contains 98 policy declarations after top-level removals, including 45 Storage policies. Counts by operation are 35 SELECT, 25 INSERT, 17 UPDATE, 18 DELETE and three ALL. The per-relation private index joins predicates, roles, WITH CHECK, policy mode, scope markers and ordered direct/schema-wide ACL statements. It preserves unknown ownership, external ACLs, inheritance and default privileges. The function inventory tracks names and signatures, declaration options, touched ACLs and recognized exact drops. There are 842 function declaration candidates, of which 775 are elevated by their latest parsed declaration. Ten of those have no declaration-level search path and most of the remaining declarations include the public schema. Review effective path and writability before establishing safety. Public schema presence is a review condition and does not establish an escalation.

The history includes 453 procedural blocks and dynamic operations outside the static projection. Lexically matching definitions across orderings provides no guarantee that a procedure, role grant, owner, default privilege, scoped view, or storage configuration reached the same end state. The [security review](SUPABASE_SECURITY_REVIEW.md) records boundary-specific findings. The [architecture analysis](SUPABASE_ARCHITECTURE_ANALYSIS.md) records replay hazards. No migration from the reference was executed. Zero reference migrations ran, succeeded or failed. There is no resulting reference catalog for drift or effective authorization comparison.

Before replay, classify all data payloads and procedural bodies, resolve legacy baseline and role expectations, and remove or stub external actions, scheduler jobs and foreign integrations in an approved sanitized replay. Preserve original source and record differences. Verify required Auth, Storage, Realtime and extension objects, then fail on first SQL error and capture the catalogs for RLS, table/column privileges, roles, policies, views, functions and Storage authorization. Repeat from a fresh baseline. Catalog checks and actor requests should be explicit separate results.

## Test results and changes

- Ran the PostgreSQL fixture on two fresh databases. Added explicit denied administrator deletion, denied peer update, and anonymous RPC rejection. Anonymous Storage reads may be refused by grants or return no rows under RLS. Both preserve the intended policy boundary.
- Installed Supabase JS 2.107.0 and Node 22 ambient types in staging. Strict TypeScript 5.9.3 checking passed with dependency declarations enabled, first against the stand-in and then against the actual public schema. The CLI path reported a missing container runtime. The upstream TypeScript generator, @supabase/typegen 0.2.2 with @supabase/postgrest-typegen 0.4.0, introspected the synthetic database through the private Unix socket and produced byte-identical output twice. The staged fixture includes the generated contract and typed RPC. Type assertions also confirmed that required insert fields and the RPC argument names reject incorrect calls. The earlier declaration failure remains specific to the different SDK and compiler combination previously exercised.
- Checked the existing React DOM and Next.js build/HTTP regressions separately from managed-service integration. See the [validation matrix](SUPABASE_VALIDATION_MATRIX.md) for results and outstanding tests across Auth, Storage, Realtime, Edge and the frontend integrations.
- Updated version-sensitive CLI guidance, fixture checks, evidence registry, coverage and merge guidance. Rule IDs, 19 workflows, scenarios and example scope survive.
- Kept exact migration paths, revision, parser outputs and replay triage in private staging. No canonical or reference changes, production access, publication or Phase 4 work occurred.

## Owner decision

Review the proposal with the three readiness labels above. Provide an approved disposable runtime with adequate disk and a sanitized, provenance-checked starting schema if reference reconstruction is needed. Require successful reference replay and managed-service tests before promoting those specific claims. Canonical integration requires separate approval.
