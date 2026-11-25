# Neutral Next.js library example

The localized item page reads a synthetic catalog through a server-only module. It generates localized metadata, canonical links and alternates, composes a client disclosure and returns a 404 for an unknown item. The sitemap demonstrates shared route inputs. The robots policy disallows crawling for the fixture.

Copy this directory's app and catalog sources into an isolated Next.js 16.2.4 app with React 19.2.4, TypeScript, React and Node types, and the server-only package. Run a strict type check and production build. Start locally and inspect both localized item URLs, a missing item, robots and sitemap. Replace the reserved hostname and dummy catalog only for a real deployment. Test client interaction separately in a browser.
