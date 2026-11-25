# Task routing

Read only the row and linked sections relevant to the request. These are task-specific rules in addition to applicable owner approval and documentation requirements. React and Next workflows remain implementation-specific, and Supabase workflows apply only to an approved backend. Start with the narrower row when several apply. Add other rows only for changed boundaries.

| Task | Required context and profile | Rules and workflow | Output, validation and docs |
| --- | --- | --- | --- |
| New project initialization | Goals, audience, constraints and approved stack | WEB-DEC-001, [discovery](project-selection.md), then selected profile workflow | Profile, runnable slice, build/smoke, architecture and setup docs |
| Existing project analysis | Current dependencies, routes, conventions and infrastructure | WEB-ARC-002, [discovery](project-selection.md) | Current-state map, verify traced entry points, update architecture if stale |
| Architecture planning | Options, costs, boundaries and approval | WEB-DEC-001, WEB-ARC-001, [compatibility](compatibility.md) | Recommendation and ADR with verification and rollback |
| Requirements clarification | Known facts and consequential unknowns | WEB-DEC-001, [discovery](project-selection.md) | Targeted questions and recorded decisions |
| New feature implementation | Actor, contract, existing entry point | WEB-ARC-002, WEB-QA-001, selected [workflow](index.md) | Verified vertical slice, affected feature/API docs |
| UI implementation | Existing design, component, devices | WEB-UI-001, [UI patterns](react/interface.md) | Focus, responsive and state checks, design docs if contract changes |
| Dashboard implementation | Roles, metrics, definitions and data | WEB-UI-002, WEB-AUTH-001, [dashboard workflow](react/workflows.md) | Verified calculation, filters and access, feature docs |
| Public website implementation | Content, locale, route and render policy | WEB-NEXT-001, WEB-SEO-001, [Next workflows](next/workflows.md) | Rendered routes, metadata and responsive checks, feature docs |
| Landing-page implementation | Approved assets, verified copy and CTA | WEB-UI-001, [public UI](next/public-ui.md) | Working CTA and mobile/keyboard checks, content or design docs |
| Design-system creation | Brand, primitives and accessibility | WEB-UI-001, [design system](react/interface.md) | Tokens and states, theme/reflow checks, design-system docs |
| API integration | Versioned contract, origins and identity | WEB-API-001, WEB-AUTH-001, [API](external-api.md) | Typed adapter and contract tests, API docs |
| Authentication implementation | Actor, session model and trust boundary | WEB-AUTH-001, selected [adapter](index.md) | Session flows, expired and anonymous tests, authentication docs |
| Authorization implementation | Resource, actor, role, tenant | WEB-AUTH-001, WEB-SUP-002 if applicable, [Supabase identity](supabase/identity.md) or selected API adapter | Permission matrix, denied actor cases and access docs |
| Database schema changes | Current catalog, data and release window | Existing migration workflow. For Supabase, WEB-SUP-001 and the [database workflow](supabase/database.md) | Replayable migration, fresh and upgrade checks, database docs |
| Supabase integration | Approved backend, target SDK and local environment | WEB-SUP-001, WEB-SUP-002, [Supabase workflow](supabase/workflows.md) | Typed boundary, actor checks, backend and environment docs |
| Storage implementation | Object ownership, sizes and retrieval scope | WEB-AUTH-001, [services](supabase/services.md) for Supabase or [external API](external-api.md) | Verified upload/download/delete and denial, storage docs |
| Realtime implementation | Event owner, scope, reconnection | WEB-STATE-001 and the existing event adapter. For Supabase, WEB-SUP-002 and [services](supabase/services.md) | Subscribe and cleanup checks, authorization and freshness docs |
| Form implementation | Defaults, payload, validation and failure | WEB-FORM-001, [feature contracts](advanced-features.md) for complex forms | Accessible form, server error and retry tests, feature/API docs |
| Bug fixing | Reproduction and affected entry point | WEB-QA-001, [standards](standards.md) | Scoped fix, regression check, relevant behavior docs |
| Refactoring | Existing behavior and contract | WEB-ARC-003, WEB-QA-001, selected workflow | Preserved callers and regression result, structure docs if changed |
| Performance optimization | Baseline, bottleneck and budget | WEB-PERF-001, selected delivery workflow | Measured comparison and performance record |
| Accessibility improvement | Affected journey and existing semantics | WEB-UI-001, WEB-UI-003, [UI patterns](react/interface.md) | Keyboard, focus, names and reduced motion checks, design docs |
| SEO improvement | Indexed routes, locale and canonical policy | WEB-SEO-001, [public UI](next/public-ui.md) | HTTP, metadata and crawl checks, route plan |
| Security review | Threat boundaries and authorized scope | WEB-AUTH-001, WEB-SUP-002 when applicable, selected data workflow | Findings, defensive checks and scoped security documentation |
| Testing | Behavior, environment and failure cases | WEB-QA-001, selected workflow | Reproducible checks and stated limitations, testing docs |
| Deployment preparation | Host, runtime, artifacts and rollback | WEB-QA-001, selected workflow | Build and safe smoke checks, deployment notes |
| Documentation updates | Actual behavior and approved decisions | WEB-DOC-001, [documentation](project-documentation.md) | Updated affected topics, check links and claims |
| Code review | Diff, callers and rules for the affected boundary | WEB-QA-001, [standards](standards.md) | Actionable findings tied to risk and evidence, identify documentation gaps |
| Project maintenance | Existing conventions, affected feature or debt | WEB-ARC-002, WEB-DOC-001, [discovery](project-selection.md) | Scoped verified change and relevant history update |

For UI-only work, the framework profile index may already be enough to select one UI section. For database backends other than Supabase, use the existing platform's migration and policy tooling. Supabase-specific commands are conditional.
