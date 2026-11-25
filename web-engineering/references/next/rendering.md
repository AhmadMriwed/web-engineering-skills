# App Router architecture and rendering

### WEB-NEXT-001 — Preserve native route and component boundaries

**CONDITIONAL** within the rule’s applicable scope.

Place route entries in `app/` and long-lived shell composition in `layout.tsx`. Use bracketed segments for URL parameters, route groups for layouts without new path segments, and private folders or ordinary colocated modules for implementation details. Keep Pages Router projects on their router pending approved migration. Await Next.js 16 asynchronous route inputs. Validate IDs and locales before lookups. Use `notFound()` for missing resources and intentional redirects for aliases. Share a view or feature loader between pages instead of importing another page entry.

Keep components server-side unless they need browser events, state, effects, browser APIs or a client-only library. Mark the smallest viable interactive boundary with `"use client"`. Pass serializable, minimal props and keep server-only dependencies out of the client graph. A client provider can accept server-rendered children passed by the layout. Scope providers and translated messages to consumers where practical. Keep public config separate from secrets, follow project naming, align aliases in TypeScript and tooling, and review both import directions.

Place `loading.tsx` at a segment for navigation feedback, use Suspense around separately slow features, and use client `error.tsx` boundaries for unexpected render failures with recovery. Give known errors and genuine empty values explicit states. Proxy in Next.js 16 can normalize locale and perform lightweight redirects. Use file conventions for the installed major. See WEB-SRC-003 N01/N02/N09 and the [Next.js 16 upgrade guide](https://nextjs.org/docs/app/guides/upgrading/version-16).

### WEB-NEXT-002 — Choose rendering and cache scope together

**CONDITIONAL** within the rule’s applicable scope.

| Need | Choose | Validate |
| --- | --- | --- |
| Known public content | Static rendering and `generateStaticParams` for known segment values where appropriate | Build route output, direct links, unknown segment handling |
| Public content that changes | Explicit time or event invalidation, then verify staleness and failure recovery | Cold cache, TTL, invalidation, published and unpublished states |
| Identity or request-specific data | Request-time server rendering, explicit private/no-store behavior | Two users or tenants, logout, intermediaries and no shared data leakage |
| Interaction after initial render | Small client island and client fetch where justified | Hydration, empty/error/loading, cancellation and bundle cost |
| Slow independent server read | Parallelize independent reads and use a nearby Suspense fallback | Early shell, fallback, failure and final result |

For Next.js 16 with Cache Components off, default Fetch behavior is not a persistent-cache guarantee, and a static route can still fetch during prerender. Set fetch/cache and render policy intentionally. On opting into Cache Components, review its different runtime data and Suspense rules and use `use cache`, cache life and tags as applicable. Keep request memoization, persistent data cache, rendered route output and client navigation cache distinct. Invalidate the scope affected by a committed write. Use `updateTag` in a Server Action for read-your-writes where appropriate, `revalidateTag` with an appropriate profile for tagged freshness, and `revalidatePath` for affected route output. Treat each as version-sensitive. Never use a shared public cache for authenticated reads without a verified isolation model.

Source explicitly forces request rendering in a catalog route and enumerates homepage locales. It does not establish the production render classification of every route. ISR, explicit invalidation and streaming have no confirmed source example. Verify the production manifest rather than inferring behavior from a single export. See WEB-SRC-003 N02/N04/N09 and [Fetch behavior](https://nextjs.org/docs/app/api-reference/functions/fetch), [Cache Components](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents), and [Fetching Data](https://nextjs.org/docs/app/getting-started/fetching-data).
