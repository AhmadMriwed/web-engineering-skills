# Phase 3 proposed merge

The proposal is based on a byte-for-byte file snapshot of the canonical working-tree files. No canonical Git baseline was available. Before any approved integration, compare current files against this snapshot and reconcile owner edits. Run baseline and proposed validation independently. Apply only the reviewed file delta, verify all 18 original rule IDs and rerun regression checks. Do not distribute private provenance. Obtain separate authorization for production activity and any commits or release actions.

## Evolution ledger

| Existing guidance | Evidence | Proposed guidance and classification | Applicability, regression and validation |
| --- | --- | --- | --- |
| Material stack approval | Existing skill and source deployment seams | KEEP_EXISTING. Keep approval and project profile. | All profiles. High confidence. Verify A–H. |
| Backend candidate only | S01 S03 S05 S06 S10 | CREATE_NEW_PROFILE. Stage an opt-in backend with explicit selection. | All frontend configurations. Avoid implicit dependency. High confidence in routing. Full local stack needed. |
| Typed external API boundary | S03 S09 | MERGE_PATTERNS. Preserve typed trust boundary for native SDK. | React and Next. Existing external clients untouched. Medium confidence for generated type integration. Compile exact generated contract. |
| Backend authorization | S04 S06 S07 S08 | ADD_NEW_SKILL. Add provider-specific exposed-surface rule in the same unified skill. | RLS, storage, roles, RPC, Realtime. Avoid broad grants or promotion of route guards. High confidence in principles, neutral SQL proof only. |
| Documentation and QA | S05 S09 S10 | IMPROVE_EXISTING. Add migration reproducibility rule, regeneration and conditional operational docs. | All Supabase consumers. Avoid destructive CI commands outside isolation. High confidence. Replay and upgrade pending. |
| Next external identity | Official SSR and Proxy guidance | ADD_ALTERNATIVE. Add request-scoped cookie clients and isolated authenticated caches. | Next.js and split apps. Protect private data between sessions. Medium confidence pending runtime smoke. |
| Deploy and share contracts | S05 S09 and canonical combined architecture | IMPROVE_EXISTING. Assign schema ownership and a compatibility window across apps. | Combined. Release coordination may block deployment if consumers diverge. Test version skew. |
| Reference custom migration and typed client | S05 S09 | REJECT_REGRESSION. Avoid endorsing duplicate prefixes or unchecked handwritten SDK contracts. | Supabase. Existing history needs explicit reconciliation. Validate unique clean replay. |
| Reference feature workflows | S03 S06 S07 S08 S11 | KEEP_PROJECT_SPECIFIC. Keep proprietary roles, names and integration contracts out. | Example uses neutral actors and resources. High confidence. Privacy and portability scan. |
| Exact effective authorization and operations | S04 S05 S08 S10 | REQUIRE_MORE_EVIDENCE. Audit representative columns now and capture effective catalog after approved replay. | Reference assessment only. High impact if assumed. Reconcile grants, RPC and Storage before certifying. |

## Proposed file delta

Paths form a proposed tree overlay. All omitted baseline files retain their original bytes.

```text
modified  README.md
modified  ROADMAP.md
new       docs/BACKEND_STRATEGY_COMPARISON.md
new       docs/PHASE_3.md
new       docs/PHASE_3_COVERAGE_AUDIT.md
new       docs/PHASE_3_MERGE_PLAN.md
new       docs/PHASE_3_VALIDATION_COMPLETION.md
modified  docs/SOURCE_EVIDENCE.md
new       docs/SUPABASE_ARCHITECTURE_ANALYSIS.md
new       docs/SUPABASE_SECURITY_REVIEW.md
new       docs/SUPABASE_VALIDATION_MATRIX.md
modified  scripts/validate.py
modified  web-engineering/SKILL.md
new       web-engineering/assets/supabase-example/README.md
new       web-engineering/assets/supabase-example/checks/policy-assertions.sql
new       web-engineering/assets/supabase-example/src/browser.ts
new       web-engineering/assets/supabase-example/src/database.generated.ts
new       web-engineering/assets/supabase-example/src/files.ts
new       web-engineering/assets/supabase-example/src/notes.ts
new       web-engineering/assets/supabase-example/supabase/migrations/20261125000000_notes.sql
new       web-engineering/assets/supabase-example/supabase/seed.sql
new       web-engineering/assets/supabase-plan.md
modified  web-engineering/references/compatibility.md
modified  web-engineering/references/index.md
modified  web-engineering/references/next/profile.md
modified  web-engineering/references/project-documentation.md
modified  web-engineering/references/project-selection.md
modified  web-engineering/references/react-dashboard.md
modified  web-engineering/references/shared-core.md
new       web-engineering/references/supabase/applications.md
new       web-engineering/references/supabase/database.md
new       web-engineering/references/supabase/identity.md
new       web-engineering/references/supabase/profile.md
new       web-engineering/references/supabase/services.md
new       web-engineering/references/supabase/workflows.md
```

Review the [coverage and verification gaps](PHASE_3_COVERAGE_AUDIT.md) before approval. The greatest remaining risks are cumulative authorization drift, replayability, exact generated contracts and unverified Auth/SSR, Storage, Realtime and Edge endpoint behavior.

## Conditional recommendation

The reusable profile is ready for conditional owner approval. Adopt the readiness and verification labels with it. A source-specific authorization verdict and full-stack integration claim remain gated on a sanitized reference replay and a disposable Supabase runtime. CLI v3 command corrections, exact generated fixture types and the expanded negative assertions are part of the proposal. See the [completion report](PHASE_3_VALIDATION_COMPLETION.md).
