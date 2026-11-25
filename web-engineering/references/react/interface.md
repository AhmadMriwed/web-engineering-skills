# Dashboard interface engineering

### WEB-UI-001 — Centralize interface primitives and feedback

**CONDITIONAL** within the rule’s applicable scope.

Define semantic tokens for surfaces, text, border, focus, statuses, spacing, radii and typography. Map light and dark themes to the same roles. Build primitives from native elements or accessible headless controls, expose intentional size and state variants, and compose feature-level patterns around them. Keep focus indication, loading announcements, and label associations in primitive contracts. Audit contrast, zoom, forced colors where applicable, keyboard operation and long labels. Use a token for a reusable visual choice and feature-local CSS for a one-off layout.

Build a shell with a single main landmark, stable navigation, a usable collapsed or modal menu, and predictable content overflow. Move focus into an opened modal menu and restore it on close. Test narrow screens, desktop resizing, touch and route changes. The source separates a generic shell from feature navigation and header actions. Verify these accessibility expectations in the target project. See WEB-SRC-001 E05/E07/E08 and WEB-SRC-002 G05/G09.

### WEB-UI-002 — Design the complete data-view interaction

**CONDITIONAL** within the rule’s applicable scope.

Use a semantic table when comparing columns is central. On narrow screens, prefer scroll if column relationships remain important, or cards when each item can stand alone. Use a real link or button for row actions, stable keys for records, and descriptive labels for sorting, filters and page controls. Share table structure and state affordances. Keep column meaning, status interpretation, mobile cards and permissions with the feature.

Distinguish initial loading, background refresh, unfiltered empty, filtered empty, fatal load error and stale data after a refresh failure. Preserve useful rows during background refresh. Show a retry when recovery is possible and a clear-filters action for zero matches. Preserve table structure in skeletons and announce status without stealing focus. Use pagination metadata from the backend for remote lists and avoid paginating an already paged response again.

For example, an empty inventory with a query suggests clearing filters. An inventory with no data and no query may offer a create action when permitted. See [neutral state selection](../../assets/examples/list-state.ts). Verify all states at both breakpoints, keyboard access to row actions, and stable pagination after updates. See WEB-SRC-001 E02/E08/E09 and WEB-SRC-002 G05/G08.

### WEB-FORM-001 — Separate user-facing form state from API payloads

**CONDITIONAL** within the rule’s applicable scope.

Keep field arrangement and submit feedback in the feature form. Keep schema and input-to-request mapping near it, with generic inputs and error primitives in shared UI. React Hook Form with a schema resolver is useful for multi-field validation and touched state. A native form and simple validation can be enough for a small interaction. Normalize correctly typed values before submission and apply backend validation. Map known server errors to fields, use a readable form-level message for other failures, and retain values after rejection. Disable duplicate submits where appropriate. Clear or navigate only after confirmed success.

For example, a quantity field can display text as the user types and produce a bounded integer for the service. Test labels and descriptions, Enter submission, malformed values, backend field errors, repeated submits and focus on failure. See WEB-SRC-001 E05 and WEB-SRC-002 G01/G04/G08.

### WEB-I18N-001 — Localize text and presentation at the correct boundary

**CONDITIONAL** within the rule’s applicable scope.

Use shared and feature catalogs, a declared fallback locale, and one registration or loading mechanism. Use locale-aware date, number and currency formatting, with interpolation and plural forms configured in messages. Set document language and direction at startup and on change using the resolved locale. Use logical CSS properties, verify direction-sensitive icons and isolate mixed-direction data when needed. Confirm registered namespaces and key coverage across all supported locales. Treat English fallbacks as resilience and measure missing keys separately.

For example, use a common pagination label, a feature-specific empty message, and locale-aware inventory counts. Avoid concatenating phrases and applying a direction by exact match against a single spelling of a language tag. Test RTL and LTR navigation, menu placement, validation and long translations. See WEB-SRC-001 E05/E10 and WEB-SRC-002 G06.

### WEB-UI-003 — Match motion to interaction and accessibility

**CONDITIONAL** within the rule’s applicable scope.

Keep animation near its primitive or feature. Use transitions for distinct interactions such as opening a sheet or revealing a status change. Keep controls immediately operable, preserve focus, and provide a reduced-motion path including for repeated motion. Prefer transform and opacity for suitable transitions and measure costly layout changes before optimizing. Avoid decorative motion in dense tables or when it delays task completion.

For example, a mobile sidebar can transition using a shared sheet primitive with reduced-motion styling and identical open/close semantics. Verify rapid toggling, keyboard dismissal, reduced-motion settings and slow devices. Animation utilities are observed. The reduced-motion requirement is corrective guidance. See WEB-SRC-001 E08/E11.

## Establish a project-owned design system

1. Start with contrast, target devices, type scale and density. Define primitive values, then semantic roles for canvas, panels, text, muted text, borders, focus, accent and feedback. Set typography, spacing, radius and elevation scales. Apply the same roles in light and dark mode and test each state in both.
2. Keep token and theme definitions in shared styles. Put brand name, logo variants and asset references in app configuration. Keep original assets under the project's assets directory with known licensing. Give meaningful logos an appropriate accessible name. Treat decorative art and icons as hidden when adjacent text identifies the action. Choose font weights and subsets for supported scripts, set fallbacks, and test rendering with delayed or blocked fonts.
3. Design primitives around semantic elements and explicit size, tone, disabled and pending variants. Document which props are controlled, which slots accept content, and how focus and accessible labels are provided. Keep feature-specific labels and behavior outside a primitive.
4. Choose breakpoints by content overflow and layout needs. Define which controls collapse or move and protect reading and focus order. Use the same tokens for overlays, headers, sidebars and page layouts. Test narrow, wide, zoomed, RTL, dark and keyboard-only use.

| Primitive | Contract and verification |
| --- | --- |
| Button, icon action | Use a button for actions and a link for navigation. Declare submit intent, accessible names, focus, disabled and pending behavior. |
| Input, select, checkbox | Use visible labels and descriptions, clear option and selection semantics, and associated errors. Verify keyboard entry and selection. |
| Card, page header | Provide a consistent heading hierarchy and slots for actions or metadata. Keep nested controls reachable. |
| Dialog, drawer | Use a labelled modal for blocking decisions, move and contain focus, support dismissal when safe, and restore focus on close. |
| Dropdown, tooltip | Distinguish action menus from field choices. Verify focus and escape behavior. A tooltip supplements a label and is available by keyboard. |
| Toast, spinner, skeleton | Announce transient updates politely. Keep recoverable errors near the affected controls. Preserve layout with skeletons and expose loading text where needed. |
| Sidebar, navigation, header | Mark current navigation, hide only links that permissions disallow, and expose menu state. Verify landmarks, route changes and mobile dismissal. |

Source evidence confirms token and primitive seams and role-specific shell composition. Brand configuration contracts, keyboard and focus acceptance checks are recommended guidance. See WEB-SRC-001 E05/E07/E08/E12.

## Compose dashboards and entity management

Keep KPI definitions, units, date range, time zone and comparison period in the feature. Compose a summary grid, chart and recent activity from typed read models. Keep chart axes and tooltips formatted consistently, distinguish zero from missing measurements, and offer a text summary or source table where a plot carries meaning. Use responsive dimensions and avoid color-only distinctions.

Organize entity routes around list, detail, create and edit when independent links or a complex workflow justify pages. A small edit can use a dialog with a stable record ID. Keep mutation and permission decisions in feature hooks and views. For deletion, name the target and consequence, require confirmation when warranted, and reconcile selection, current page and caches after success. On failure, retain context and give a recovery path. Permission-aware controls reflect capabilities supplied by the session, while the API independently authorizes the operation.

For server sorting, allowlist supported keys and include order in the URL, request and query key. For bulk actions, distinguish selected IDs from all matching records and report partial results. For import, validate and preview before writes where the workflow allows. For export, preserve scope and format and use an authorized endpoint or short-lived download. Source implements a CRUD dialog pattern, dashboards and an export link. The sorting, bulk and import workflows are conditional guidance. See WEB-SRC-001 E13/E14.

## Handle complex form lifecycles when needed

Keep a schema beside the feature form. Infer input and output types separately for transforming schemas. Supply explicit defaults. When switching record or opening an edit form, reset against a known snapshot without overwriting dirty changes during background refresh. Clear stale errors when the relevant inputs change. Conditional fields need schema and payload rules for hidden values. Dynamic lists need stable item keys and indexed error rendering. For file inputs validate size and type client-side for feedback and server-side for enforcement. For multi-step forms, define per-step validation and final submission against the full schema. Add an unsaved-change guard only for meaningful drafts and verify normal navigation after save.

## Verify locale changes and formatting

Keep the language selector in the shell and persist the resolved preference for later visits. Document precedence between user preference, browser locale and default. Compare flattened catalog keys in CI, accounting for approved plural variants, and verify runtime fallback behavior separately. Use locale-aware formatters for currency, dates and numbers, with explicit currencies and time zones where the domain requires them. For example, format a price with `Intl.NumberFormat(locale, { style: "currency", currency })` and test currencies with differing fraction digits. Check catalog completeness, number formatting, LTR/RTL icon orientation and modal placement together. See WEB-SRC-001 E10/E15.

For shared primitives, validate radio groups as one named choice, tabs with consistent keyboard focus, breadcrumb current-page semantics and chart summaries usable without color. Size controls for touch and establish grid, density and breakpoints from the approved brand and content. Check upload controls for operable file selection, file restrictions and accessible progress. For role shells, bulk and import/export flows, see [advanced feature contracts](../advanced-features.md).
