# React dashboard profile

Use this profile for interactive, client-rendered applications, especially authenticated dashboards. Check [project selection](project-selection.md) when server rendering, public indexing, or independent deployment changes the decision. Use simpler local state and static fixtures when a dashboard has no remote data.

| Concern | Observed assembly in WEB-SRC-001 | Adoption condition |
| --- | --- | --- |
| App and routing | React 19, TypeScript 5.9, Vite 8, React Router 7 | Host can serve client routes and the deployment runtime can build the selected Vite version |
| Data | TanStack Query 5, Axios 1, Zustand 5 | Query owns remote state. Axios and a cross-route store are optional |
| UI and forms | Tailwind CSS 4, Radix primitives, React Hook Form 7, Zod 4 | Pick component and schema tools that fit the existing design and validation contracts |
| Localization | i18next 26 and react-i18next | Use when the product supports multiple locales. Verify direction and format per locale |

This assembly was observed through source inspection. Verify installed versions, peer dependencies, build runtime, routing, and browser behavior in the target project.

- Read [architecture](react/architecture.md) for directories, dependency direction, routing and extraction decisions.
- Read [data and identity](react/data-and-identity.md) for API integration, query state, URLs and session handling.
- Read [interface engineering](react/interface.md) for the shell, design system, data tables, forms and localization.
- Read [delivery and validation](react/delivery.md) to bootstrap an app, deliver a feature, or verify a deployment.
- Read [implementation workflows](react/workflows.md) for task entry points, file placement, documentation and verification.

For an approved Supabase backend, see the [React integration profile](supabase/applications.md).
