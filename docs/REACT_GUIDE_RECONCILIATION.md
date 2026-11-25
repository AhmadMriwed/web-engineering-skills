# Dashboard guide reconciliation

The guide is WEB-SRC-002. Each row records a guide section and its comparison with WEB-SRC-001. Confidence refers to inspection of the named source areas and representative paths.

| Guide evidence | Section | Source comparison and disposition |
| --- | --- | --- |
| G01 | Tech stack | Dependencies and representative uses confirm the stated React, routing, query, transport, form, UI and locale assembly. Zustand owns persisted auth, which the guide's client-state row omits. |
| G02 | Top-level layout | App, configuration, features, locale resources and shared layers match broadly. A scoped API adapter under shared imports a feature store. Move that composition out of generic shared infrastructure in new work. |
| G03 | Anatomy and data flow | Orders and a second list trace show page → hook → service → client. Layout, search and auth have specialized shapes. Keep optional folders proportional to responsibilities. |
| G04 | Layer responsibilities | Pages coordinate inputs and toasts. The orders hook unwraps the envelope and owns conditional polling, detail cache writes and invalidation. Typed envelopes establish compile-time assumptions. Representative calls lack runtime response decoding. The shared table and feature cards substantiate extraction guidance. |
| G05 | Shared layer | HTTP is a configurable factory with a scoped instance. The instance wires a 401 callback with a login exception and full navigation. Regular logout clears the query client explicitly. The URL helper normalizes on write and handles basic page coercion. Incoming filters still need validation. Several features use the generic responsive table. |
| G06 | Internationalization | Central registration, feature catalogs, fallback locale, and DOM language/direction are observed. Six locale trees invalidate a two-file checklist. RTL detection checks a single language code, which warrants testing resolved dialect tags. |
| G07 | Routing and navigation | A declarative sidebar and nested guarded layout are present. Literal paths exist in route declarations and auth redirects. Sidebar role filtering is a presentation choice. Backend permission behavior is outside reviewed source. |
| G08 | Error and loading | Table skeleton, empty and retry patterns and a root error boundary exist. The table can fall through to empty when error details are omitted. The generic clickable-row path uses a click handler without a row keyboard handler. Prefer native interactive elements. |
| G09 | Naming and style | Aliases, hook and service conventions, class merging and theme tokens are visible. Mixed shared input casing makes the naming description a convention. Accessibility expectations need interaction checks. |
| G10 | Feature recipe and known gaps | Use the vertical slice recipe with all configured locales, a contract check and explicit workflow tests. No conventional tracked tests, boundary lint rules, or tracked support feature were found. Git trees cannot establish the existence of an empty local directory. A generic table already shares major data states. Multi-audience reuse remains unverified. |

Additional findings include an SPA static-host fallback, eager route imports, conditional order polling and local UI transitions. The React references explain their scope and mark improvements such as measured splitting and reduced-motion support as target guidance. See the [source and evidence registry](SOURCE_EVIDENCE.md).
