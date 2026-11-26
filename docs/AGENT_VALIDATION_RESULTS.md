# Independent validation results

The project requests, clarification script, acceptance rubric, CLI JSONL traces, test outputs, and generated projects are stored in the durable evaluation workspace. Discovery is assessed separately from implementation. A skill read never substitutes for application acceptance.

| Project | Discovery and architecture | Behavior verified and remaining boundary |
| --- | --- | --- |
| A. Inventory dashboard | Enabled run selected React/TypeScript and existing REST, identified role/token handoff and asked for approval. Control also respected the API and asked about handoff. | See independent project checks below. Synthetic credentials are valid only in this fixture. |
| B. Multilingual service guide | Enabled run proposed static Next.js with monthly rebuilds, localized URLs and explicit approval. | Build generated both locales and four detail pages. Independent loopback export checks and Chrome smoke passed. This verifies metadata and links, with crawler indexing outside the test. |
| C. Team tasks | Enabled run compared React/Supabase, Next.js and a dedicated API, then requested approval for the stack, storage and access model. | Discovery only. Managed Auth, RLS, tenant and Storage interfaces require a disposable Supabase runtime. |
| D. Course bookings | Enabled run chose one Next.js app with Supabase and explained an independently deployed admin alternative. | Discovery only. Cookie refresh, private caching, direct authorization and bookings transactional behavior remain unresolved. |
| E. Combined system | Enabled run compared separately deployed React and Next.js apps with a single Next.js app and requested scope and identity details. | A separate approved implementation trial was launched. See project checks below. |
| F. Existing React app | Enabled and control retained React, CommonJS and the supplied fixture conventions. | Enabled output implemented close/Escape focus restoration and filter reset. Control implemented close focus restoration and reset. The test suites cover different cases. |
| G. Static landing | Enabled run compared dependency-free static delivery with Next.js and waited for approval. The evaluator approved static files. | Independent Node assertions and Chrome smoke passed topic filtering and responsive markup. CTA uses synthetic mailto. No backend was added. |

## Routing and clarification

The focused Codex routing run visibly read the task table and returned routes and completion checks for all 29 named rows. Ticket 30 described localization/RTL, which the run routed through an existing profile workflow. The Phase 4 validator counts the table separator, creating the reported 30-row discrepancy. This was an actual read-only routing exercise rather than 29 independent implementation tests.

A asked about unspecified bearer role transport and update scope. B distinguished SEO from app search and asked for canonical and content decisions. C requested file limit and actor decisions. D and E discussed trust and deployment boundaries before implementation. G asked for an email and approval. F proceeded directly within the approved existing framework. Some questions bundled optional product choices. The discovery-only prompts also explicitly constrained side effects, so avoidance of writes does not independently prove an intrinsic approval gate.

## Browser and security scope

Headless Chrome and Playwright ran against the neutral Next.js fixture and independently generated B/G outputs. Checks covered desktop/mobile widths, heading, RTL, locale link, keyboard disclosure/filter and overflow. This was a focused automated smoke. Screen readers, full dialog interactions, a broad accessibility scan and actual crawler indexing remain untested. Direct REST fixture checks exercised expired token 401, denied viewer write 403, invalid quantity 400, allowed manager write and readback. Neutral PostgreSQL authorization assertions exercised synthetic actor predicates. Managed Supabase endpoints and source deployments remain separate.

## Six-domain reassessment

Multiple audiences has positive evidence from discovery and the dashboard viewer/manager path. Bulk actions, import/export, conditional fields, multistep forms and dirty navigation require focused end-to-end evidence. The advanced fixture trial was launched separately. Retain V-01 through V-06 unless the corresponding acceptance criteria are met.

## Independently rerun project checks

| Project | Command or artifact | Actual result |
| --- | --- | --- |
| A | `npm test`, `A-tests.log`, `A-browser.log` | Seven tests passed. Chrome read inventory as viewer, exposed no edit action, switched to manager, saved quantity and observed it through a live REST read. The UI offers an ID sort that the evaluator API rejects with 400. The contract did not specify allowed keys, so this remains a contract gap. |
| B | `python3 checks/export.py --http`, `B-export-http.log`, `generated-browser.log` | Passed. Direct localized routes, canonical/alternate URLs, contact, sitemap, robots and 404s verified. |
| E | `combined-advanced-browser.log` | Both generated entry points ran against the live fixture. The public page showed aggregate data without token strings in HTML. The private staff entry rejected unauthenticated navigation at its UI boundary and loaded live inventory after selecting a synthetic viewer. Real identity and cross-deployment skew remain open. |
| F | `npm test`, `F-tests.log`, `F-isolated-tests.log`, `F-control-tests.log` | Three tests passed on each enabled run and two on control. Enabled tests include Escape behavior. These are DOM tests. |
| G | `node --test tests/planner.test.cjs`, `G-tests.log`, `generated-browser.log` | Two Node assertions passed. Chrome verified topic-filter activation by keyboard and responsive overflow. |
| Advanced | `npm test`, `advanced-tests.log` | Eight tests passed. They cover domain actor checks, filtered bulk partial failure and retry, CSV previews/validation/escaping, conditional lot code, wizard gating, history navigation and save recovery. The generated app is an in-memory fixture. |

The advanced fixture exposes gaps beyond the passing tests. It archives immediately after selection, so destructive confirmation remains unverified. CSV import is preview-only. The fixture models roles and data checks in process, and does not demonstrate a real tenant-authenticated API. Step validation and in-session recovery passed in jsdom. Persisted draft resume and native unload behavior still require their own tests.

A, B, E, G and the advanced fixture provide project profiles. F updated the existing feature document. Checks and scope limitations are recorded at differing levels of detail. This is evidence of documentation usage in the sample, with no general guarantee of coverage.

## Failure classifications

- **TEST_INFRASTRUCTURE_FAILURE**. The first enabled launch failed before Codex execution because the host Bash treats an empty array as unbound with nounset. The retry used a nonempty argument array and preserved logs from both attempts.
- **ENVIRONMENT_LIMITATION**. The default Homebrew Node could not load a shared library in maintenance commands. Node 22 passed. Apps connector startup and model refresh intermittently timed out. Fresh isolated retries disabled the Apps connector. Managed Supabase services and Claude Code could not run.
- **EVALUATION_LIMITATION**. The provider does not expose exact reference injection or model configuration per run. Several runtime assertions used available dependency trees. Paired trials are observational.
- **IMPLEMENTATION_FAILURE / contract gap**. A exposes an unsupported sort option. The synthetic REST fixture and agent interpretation disagree, and the evaluator brief did not constrain keys.
- **MISSING_ENGINEERING_GUIDANCE** was not established for any behavioral failure. The route-count mismatch is a validator defect in the frozen distribution. It is tracked for review.

The advanced Chrome retest passed a real CSV download, validation preview, required conditional lot code, transition to step two and cancellation of the unsaved navigation confirmation at mobile width. An earlier browser probe used an exact label selector that did not match the generated select and timed out. The retest used the rendered form control directly; it did not change the agent implementation. Native unload and persistent draft resume remain open.
