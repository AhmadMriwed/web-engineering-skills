# Public website UI, SEO and localization

### WEB-SEO-001 — Derive metadata and crawl artifacts from the public route contract

**CONDITIONAL** within the rule’s applicable scope.

Use layout metadata for defaults and page metadata for route-specific title, description, canonical and Open Graph or social images. Use `generateMetadata` for locale or entity-dependent values and reuse verified server data. Treat metadata inheritance as shallow for nested metadata objects. Decide whether a query variant is an indexable page or consolidates to a canonical page. A standalone item needs its own route contract and canonical if it merits discovery. Keep canonical, alternate language links, sitemap and internal links consistent. Emit equivalent locale variants only when pages exist and link back to each other.

Use `sitemap.ts` for indexable canonical URLs. Use content-backed modification dates where available. Set `robots.ts` and route-level indexing policy explicitly by deployment environment, including previews. Robots directives guide crawlers. Keep private content behind access controls. Generate JSON-LD for eligible visible content, encode JSON safely for script context, and validate structured data. Check direct HTTP status, HTML metadata, headings, links, hreflang, crawl files and noindex behavior. Treat indexing and ranking as external outcomes. See WEB-SRC-003 N03/N05 and [Metadata API](https://nextjs.org/docs/app/api-reference/functions/generate-metadata).

## Public interface composition

Keep header, mobile navigation, footer and locale control in the public layout. Compose hero, product, pricing, feature, FAQ, support and CTA sections from typed content. Author a clear main heading and use semantic sections and links. Build detail or content routes when users need a distinct direct URL. Keep interactive menus, filters, search, accordion or forms in small client components. Use keyboard-operable native elements and manage focus when menus and dialogs open or close. Check viewport reflow, long translations, pointer and keyboard, reduced motion, focus and no JavaScript for essential reading.

Use [shared UI principles](../shared-core.md). Component variants should own intent, size and interaction state. App configuration owns brand assets. Shared theme CSS owns semantic colors, type, spacing, radius, elevation and theme mappings. Keep icons and brand assets replaceable and give responsive images dimensions or a stable container and a sizes policy. Use Next Image where the host supports its optimizer and manage remote allowlists. Choose local fonts or build-approved font delivery, include script subsets and verify layout shift. Evaluate 3D and animation against user value, bundle size and reduced-motion behavior. See WEB-SRC-003 N06/N07.

Use a single typed locale registry for route parsing, switcher URLs, catalogs, metadata and direction. Set root `lang` and `dir` on the server, keep an equivalent path and supported query keys when switching, and use logical CSS offsets. Load server messages and scope client catalogs to consumers. Test missing keys and parity, language switch persistence, RTL navigation, date/number/currency formats and canonical equivalence. Unsupported locales need a deliberate 404 or redirect. See WEB-SRC-003 N01/N03/N06.

For conversion-oriented pages, map the primary journey and call to action first. Instrument only agreed events and gate optional analytics according to the applicable consent requirements. Test the consent-denied and JavaScript-disabled reading paths where relevant. Preserve approved brand and verified claims.
