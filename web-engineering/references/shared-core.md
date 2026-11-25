# Shared engineering core

Apply these principles across profiles. Existing rule IDs remain defined in their original references. The React implementations there apply when using the React SPA profile.

| Principle | React SPA implementation | Next.js implementation |
| --- | --- | --- |
| WEB-ARC-001, WEB-ARC-002 and WEB-ARC-003. Compose once, respect ownership, extract stable contracts. | Router and application root compose feature screens. | App Router composes layouts and pages. Feature modules provide services and isolated interactive components. |
| WEB-API-001 and WEB-STATE-001. Explicit transport, validated inputs and outputs, clear data and cache ownership. | Feature service and query lifecycle adapter. | Server read model by default. Browser service and query cache when interactivity justifies them. |
| WEB-AUTH-001. Authorize at the resource and operation boundary. | Backend owns authorization. Client guards guide navigation. | Server services, Actions and Handlers enforce checks, and the upstream API independently authorizes requests. |
| WEB-UI-001, WEB-UI-002 and WEB-UI-003. Semantic tokens, explicit states, accessible controls and reduced motion. | Reusable dashboard primitives and app-wide styles. | Server-rendered public sections and small interactive islands. Use CSS media queries and motion-library settings for nonessential motion. |
| WEB-FORM-001 and WEB-I18N-001. Validate at the trust boundary and render usable localized feedback. | Localized schema form and feature mutation hooks. | Server or external validation and local interaction state. Locale URL and server metadata share a routing contract. |
| WEB-QA-001 and WEB-PERF-001. Verify real entry points and measure before tuning. | Static SPA hosting, browser flow and API tests. | Build route manifest, generated HTML, server and browser paths, cache scope and runtime behavior. |

Use typed presentation contracts and semantic CSS variables. Keep tokens, accessibility states and direction conventions reusable. Share libraries only when both runtimes can load them and two consumers benefit. A stable contract, design value or localization convention can be shared independently of runtime code.

With Supabase, apply WEB-API-001 through native SDK calls and typed feature contracts. Apply WEB-AUTH-001 through database grants and RLS for available user-facing data, with independent server authorization for elevated operations. See the [Supabase profile](supabase/profile.md).
