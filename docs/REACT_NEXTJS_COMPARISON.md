# React and Next.js knowledge comparison

These proposals preserve the 15 stable Phase 1 IDs. Evidence refers to [source traces](SOURCE_EVIDENCE.md). Confidence concerns the observed static pattern and proposed application separately from runtime correctness.

| Existing rule or topic | New evidence | Classification and proposal | Profiles and compatibility | Risk, confidence and validation |
| --- | --- | --- | --- | --- |
| WEB-ARC-001 | N01/N02 | CREATE_NEW_PROFILE. Native route segments and layouts compose Next routes. | Next. Keep SPA router for React. | High static confidence. Check route manifest and nested direct links. |
| WEB-ARC-002 | N02 | REJECT_REGRESSION. Extract shared route view or loader when two routes reuse a page. | Both. Avoid route-entry dependency. | Sampled page reuse can couple metadata. Check detail canonical and route boundaries. |
| WEB-ARC-003 | N06/N07 | IMPROVE_EXISTING. Add render ownership to component extraction decisions. | Both. Next client graph is an additional constraint. | High for directive presence. Inspect bundles and hydration. |
| WEB-API-001 | N04/N07 | MERGE_PATTERNS. Share typed transport and contracts. Preserve Axios/query and Fetch/server as alternatives. | Both, no new required dependency. | High for observed adapters. Check cancellation, response shape and scopes. |
| WEB-STATE-001 | N02/N07 | ADD_ALTERNATIVE. Initial server result and URL state with optional browser cache. | Next, React ownership stays intact. | High static confidence. Check stale navigation and identity switch. |
| WEB-AUTH-001 | N08/N09 | KEEP_EXISTING. Require authorization at the operation, with Next adapters for server entry points. | Both. Public source cannot validate authenticated compatibility. | High principle confidence. Test more than one principal on target. |
| WEB-UI-001/002 | N06/N07 | MERGE_PATTERNS. Share semantic tokens, UI states and conventions. Keep public sections and dashboard primitives scoped. | Both. Branding stays app-local. | Visual and keyboard behavior unverified. Run viewport and keyboard checks. |
| WEB-UI-003 | N06 | IMPROVE_EXISTING. Pair CSS reduced motion with JS motion-library handling. | Both as applicable. | Source contains selective handling. Verify each animation and keyboard state. |
| Brand and 3D | N06 | KEEP_PROJECT_SPECIFIC. Treat media style, tokens and 3D rendering as optional choices. | Any app with measured need. | Confirm asset ownership, bundle/interaction cost and motion preferences. |
| WEB-FORM-001 | N08 | KEEP_EXISTING. Preserve schema and backend validation. Add native or Server Action workflow as a conditional option. | Both. React Hook Form optional. | Source uses local pending and guards. Test fields and backend validation. |
| WEB-I18N-001 | N01/N03/N07 | IMPROVE_EXISTING. Coordinate localized URLs, catalogs, server document direction and metadata. | Next, public multilingual React can reuse contract principle. | High static confidence. Check locale parity, switcher and metadata reciprocity. |
| Rendering | N02/N04/N09 | ADD_NEW_SKILL. Define explicit route and cache policy and keep client boundary narrow. | Next, adds WEB-NEXT-001 and WEB-NEXT-002. | Do not assume cached results. Verify version, actual build and cross-user isolation. |
| SEO | N03/N05 | ADD_NEW_SKILL. Establish one canonical route contract for metadata and crawl artifacts. | Next profile adds WEB-SEO-001. | Query detail metadata and sitemap dates need review. Check HTML, XML and status. |
| WEB-QA-001/PERF-001 | N09 | IMPROVE_EXISTING. Combine baseline gates with route manifest, server and HTTP checks. | Both. Browser and deployed gates remain target-specific. | Infrastructure and live vitals unverified. Keep actual outcomes separate. |
| WEB-DEC-001/DOC-001 | N01/N04/N09 | ADD_ALTERNATIVE. Compare split and single app, document rendering and integration boundaries. | Both and combined. | Compatibility proposed from architectural analysis. Validate deployment and version skew. |
| Six Phase 1 partial domains | N01/N07/N08/N09 | REQUIRE_MORE_EVIDENCE. Keep gaps at their current status. | React baseline retained. | Public routes and forms do not establish admin audiences, bulk operations, import/export, dynamic fields, multi-step forms or unsaved changes. |
