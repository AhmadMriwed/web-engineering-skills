# Knowledge routing audit

The [task table](../web-engineering/references/tasks.md) provides 29 named routes. An agent reads the entry point then relevant rows and sections. Whole-file estimates below use UTF-8 bytes divided by four, rounded up. They exclude the user's task, tool output and repository source. These estimates do not measure model token usage. All paths omit extraction reports, unrelated profiles and unrelated examples. Open standards and living docs sections selectively when implementation changes a boundary.

| Task | Required references after entry point and task row | Conditional reads | Potential overlap or ambiguity |
| --- | --- | --- | --- |
| React button styling | react/interface.md | Design docs, component contract | Read design system section and local component only |
| Dashboard CRUD | react/workflows.md, react/interface.md | react/data-and-identity.md, advanced-features.md | Use data reference only when contract changes |
| Next landing section | next/public-ui.md | Motion or locale section | Framework profile overview can be skipped |
| Next metadata | next/public-ui.md | next/rendering.md, route plan | Load rendering if metadata depends on request data |
| Supabase migration | supabase/database.md | supabase/workflows.md, backend plan | Prefer migration row and database section |
| RLS | supabase/identity.md | supabase/workflows.md, SQL assertions | Add service policies only when relevant |
| File upload | supabase/services.md for Supabase, external-api.md otherwise | Web UI upload states and backend plan | Choose the storage owner before reading adapters |
| Combined system | project-selection.md, compatibility.md | Approved profile docs and discovery template | Read proposed profiles only after options are identified |
| Existing architecture review | project-selection.md, shared-core.md | One profile and boundary reference | Follow actual stack and dependencies |
| New project with incomplete requirements | project-selection.md | Discovery worksheet and compatibility | Stop material scaffolding until approved |

The React, Next.js and Supabase workflow tables preserve framework-specific verification and documentation. Shared planning, implementation and reporting now live in standards and selection. Review of the 19 Supabase paths retained them for their distinct inputs and security surfaces.

| Path | Full files, bytes | Estimated tokens |
| --- | ---: | ---: |
| Button | 20,000 | 5,000 |
| CRUD | 24,514 | 6,129 |
| Landing | 11,701 | 2,926 |
| Metadata | 11,701 | 2,926 |
| Migration | 13,648 | 3,412 |
| RLS | 11,218 | 2,805 |
| Upload | 11,926 | 2,982 |
| Combined | 18,150 | 4,538 |
| Existing review | 15,690 | 3,923 |
| Greenfield discovery | 13,206 | 3,302 |
