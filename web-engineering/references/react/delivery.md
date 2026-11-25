# React delivery and validation

## Start a dashboard

1. Read [project selection](../project-selection.md). Approve the stack and profile, including runtime, hosting, API contract and identity boundaries. Fill in the [project profile](../../assets/project-profile.md).
2. Scaffold the approved React TypeScript toolchain, strict compiler, aliases, lint and lockfile. Add router, query and theme providers as needs justify them.
3. Build a shell and one vertical slice with neutral fixture data or an agreed API. Exercise direct routing, list states, keyboard operation, session boundaries where applicable, and narrow and wide layouts.
4. Wire production static serving, configuration injection and verification. Record startup, build and deploy commands in the project documentation.

## Deliver a feature

1. Use the [feature plan](../../assets/feature-plan.md) to identify route, permissions, inputs, API contract, query keys and user-facing states.
2. Build service and query contracts with a pure adapter or URL codec where needed. Compose a page from feature UI and shared primitives. Register navigation and locales where applicable.
3. Verify success, failure and boundary cases with the checks below. Update the affected project documentation alongside the implementation.

### WEB-QA-001 — Verify the dashboard through its normal entry points

**REQUIRED** within the rule’s applicable scope.

| Check | Primary coverage |
| --- | --- |
| Type check, lint and build | Imports, types, hook rules and production packaging |
| Unit | URL round trips, data decoders, form schemas and pure state decisions |
| Component and integration | Accessible interactions, query and mutation lifecycle, responsive states, session transitions with mocked transport |
| Browser | Deep links, history, role visibility, expiry, keyboard, RTL and production serving |
| Deployed API | Independent authorization, error contract and backend pagination |

Verify direct refresh on a nested route and that a missing asset returns an error rather than the app shell. Inspect project scripts and run with an approved environment. Keep development and test requests on approved fixtures or endpoints. Source inspection found build and lint scripts. Automated interaction coverage is a proposed improvement. See WEB-SRC-001 E06/E11 and WEB-SRC-002 G10.

### WEB-PERF-001 — Measure route and data costs before optimizing

**CONDITIONAL** within the rule’s applicable scope.

Start with a production build and baseline route transfer, interaction latency and repeated request behavior. Split expensive or infrequently visited routes if the measurement supports it. Add a loading and recovery path for chunk failures. For lists, establish backend page size and cache freshness before considering virtualization. Keep polling conditional and follow [data ownership](data-and-identity.md) for cancellation and retries. Avoid optimizing a small static view through blanket memoization or route splitting.

For example, isolate a heavy reporting route and measure cold navigation and cached navigation before and after. Verify responsiveness, data freshness, failure recovery and scroll or focus behavior. Source uses eager routes and conditional polling. Route splitting is guidance pending target measurements. See WEB-SRC-001 E01/E09/E11.

## Quality and delivery gates

Pin supported runtime versions and commit the dependency lockfile. Run the frozen install, type checking, lint, configured formatting checks, tests and production build in CI, then deploy the resulting artifact with environment-specific settings. Keep credentials in deployment configuration and run smoke checks against the deployed routes. Check error monitoring on a controlled failure, with redaction and release attribution. Keep deployment rollback and required environment variables documented.

Assess derived-state duplication, unnecessary effects and unstable boundaries before adding memoization. Profile representative interactions and inspect cache freshness, serial requests and unnecessary refetches. Validate an optimization against a baseline and a changed deployment build. In source, lint, package locking, container builds and CI deployment are visible. A formatter gate and automated tests are target guidance. See WEB-SRC-001 E11/E16.
