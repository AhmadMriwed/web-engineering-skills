# Phase 1 engineering coverage audit

This audit measures whether the skill gives an agent enough guidance to implement and verify each capability in a target React application. **COMPLETE** means actionable guidance is present. It does not certify source runtime behavior. **PARTIAL** and **MISSING** describe the previous skill. **NOT_PRESENT_IN_SOURCE** means no implementation was found in the inspected tree for that capability. **REQUIRES_MORE_EVIDENCE** means the implementation or behavior could not be established from the inspected source. **NOT_APPLICABLE** is reserved for domains outside scope. Conditional capabilities have implementation guidance and apply only when the target project needs them.

Reference and workflow keys link each row to file placement, decisions and checks. Evidence IDs refer to the [source registry](SOURCE_EVIDENCE.md). G IDs refer to the [guide reconciliation](REACT_GUIDE_RECONCILIATION.md).

| Key | Skill reference | Workflow | Neutral example |
| --- | --- | --- | --- |
| ARC | [Architecture](../web-engineering/references/react/architecture.md) | Initialize, analyze, create page or layout, extract component/hook | Inventory structure in portability walkthrough |
| DATA | [Data and identity](../web-engineering/references/react/data-and-identity.md) | API, table and security | [Inventory service](../web-engineering/assets/examples/inventory-api.ts), [list state](../web-engineering/assets/examples/list-state.ts) |
| UI | [Interface](../web-engineering/references/react/interface.md) | Dashboard, table, CRUD, design system and localization | [Form and query sketches](../web-engineering/assets/examples/README.md), inventory walkthrough |
| QA | [Delivery](../web-engineering/references/react/delivery.md) | Initialize, review performance and validate | [Example assertions](../scripts/validate_examples.cjs) |

All workflow names below refer to the [workflow reference](../web-engineering/references/react/workflows.md). The examples show selected seams. For other rows the linked workflow and walkthrough supply implementation context.

### A. Project Architecture

| Domain | Previous skill | Final skill | Source status | Reference and rule | Workflow and example key | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Project initialization. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Feature-first architecture. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Application shell. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Folder and file responsibilities. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Dependency direction. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Feature boundaries. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Shared-layer boundaries. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Cross-feature communication. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Multiple application audiences. | MISSING | PARTIAL | REQUIRES_MORE_EVIDENCE | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Naming conventions. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Path aliases. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Configuration management. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Component extraction. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-003 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Hook extraction. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Service extraction. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Utility extraction. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Appropriate abstraction. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |
| Scalability and maintainability. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-002 | Initialize, analyze or refactor, ARC | E01, E07, E16/G02–G04 |

### B. React Engineering

| Domain | Previous skill | Final skill | Source status | Reference and rule | Workflow and example key | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| React component composition. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| TypeScript conventions. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| Props and component interfaces. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| Application providers. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| Routing. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| Route constants. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| Nested layouts. | COMPLETE | COMPLETE | Observed in scope | ARC, WEB-ARC-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| Protected routes. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| Local state. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-STATE-001 | Create page, API or review performance, DATA | E01, E03, E04, E09/G03–G08 |
| URL state. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-STATE-001 | Create page, API or review performance, DATA | E01, E03, E04, E09/G03–G08 |
| Global state when justified. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-STATE-001 | Create page, API or review performance, DATA | E01, E03, E04, E09/G03–G08 |
| Server state. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-STATE-001 | Create page, API or review performance, DATA | E01, E03, E04, E09/G03–G08 |
| TanStack Query. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-API-001 | Create page, API or review performance, DATA | E01, E03, E04, E09/G03–G08 |
| Query keys. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-API-001 | Create page, API or review performance, DATA | E01, E03, E04, E09/G03–G08 |
| Mutations. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Create page, API or review performance, DATA | E01, E03, E04, E09/G03–G08 |
| Cache invalidation. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-API-001 | Create page, API or review performance, DATA | E01, E03, E04, E09/G03–G08 |
| Error boundaries. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| Component lifecycle. | PARTIAL | COMPLETE | Observed in scope | ARC, WEB-ARC-001 | Create page, API or review performance, ARC | E01, E03, E04, E09/G03–G08 |
| Rendering performance. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | QA, WEB-PERF-001 | Create page, API or review performance, QA | E01, E03, E04, E09/G03–G08 |

### C. UI Engineering and Design Systems

| Domain | Previous skill | Final skill | Source status | Reference and rule | Workflow and example key | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Design tokens. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Semantic colors. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Typography. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Font management. | MISSING | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Spacing. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Border radius. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Shadows. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Branding configuration. | MISSING | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Logo management. | MISSING | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Assets. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Icons. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Theme configuration. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Dark and light modes. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Responsive layouts. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Breakpoints. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Component variants. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Shared component interfaces. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Buttons. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Inputs. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Selects. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Checkboxes. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Cards. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Dialogs. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Drawers. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Dropdowns. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Tooltips. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Toasts. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Navigation. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Sidebars. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Headers. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Page headers. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Tables. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Pagination. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-UI-002 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Filters. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Search. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Charts. | MISSING | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Statistics. | MISSING | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Loading indicators. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Skeletons. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Empty states. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Error states. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Animations. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-003 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Transitions. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-003 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Micro-interactions. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-UI-003 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Accessibility. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Keyboard navigation. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| Focus management. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |
| RTL/LTR. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-UI-001 | Configure design system or build dashboard, UI | E05, E07, E08, E12/G05, G09 |

### D. Dashboard Engineering

| Domain | Previous skill | Final skill | Source status | Reference and rule | Workflow and example key | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Application layout. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Navigation configuration. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Dashboard overview. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| KPI cards. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Data visualization. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Responsive data tables. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Mobile table alternatives. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| CRUD operations. | MISSING | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Detail pages. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Create and edit pages. | MISSING | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Search. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Filtering. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| URL-persisted filters. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Pagination. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Sorting. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Confirmation dialogs. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Destructive actions. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Permission-aware UI. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Bulk operations. | MISSING | PARTIAL | NOT_PRESENT_IN_SOURCE | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Import and export. | MISSING | PARTIAL | Export link observed. Import NOT_PRESENT_IN_SOURCE | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |
| Loading, error, and empty states. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-UI-002 | Build dashboard, table or CRUD, UI | E02, E08, E13, E14/G05, G08 |

### E. API Integration

| Domain | Previous skill | Final skill | Source status | Reference and rule | Workflow and example key | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Centralized HTTP client. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| API configuration. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Domain-scoped clients. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Services. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Typed request and response models. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| API envelopes. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Request interceptors. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Response interceptors. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Authentication headers. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Session expiration. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Token refresh. | MISSING | COMPLETE | NOT_PRESENT_IN_SOURCE | DATA, WEB-AUTH-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Error normalization. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Pagination metadata. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Search and filtering. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Uploads and downloads. | MISSING | COMPLETE | Upload observed. Download behavior REQUIRES_MORE_EVIDENCE | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Request cancellation. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Retry policies. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Concurrent requests. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Race conditions. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Runtime response validation. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Mutation handling. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |
| Cache invalidation. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-API-001 | Integrate API, DATA | E02, E03, E09, E14, E16/G03–G05 |

### F. Forms and Validation

| Domain | Previous skill | Final skill | Source status | Reference and rule | Workflow and example key | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| React Hook Form. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Zod. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Schema organization. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Form types. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Default values. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Reusable form components. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Create and edit forms. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Client validation. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Server validation errors. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Submission states. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Duplicate submission prevention. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Conditional fields. | MISSING | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Dynamic fields. | MISSING | PARTIAL | NOT_PRESENT_IN_SOURCE | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Form reset. | MISSING | COMPLETE | REQUIRES_MORE_EVIDENCE | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| File attachments. | MISSING | COMPLETE | Observed in scope | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Multi-step forms. | MISSING | PARTIAL | NOT_PRESENT_IN_SOURCE | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |
| Unsaved changes. | MISSING | PARTIAL | NOT_PRESENT_IN_SOURCE | UI, WEB-FORM-001 | CRUD and validated forms, UI | E05, E14/G01, G04, G08 |

### G. Authentication and Security

| Domain | Previous skill | Final skill | Source status | Reference and rule | Workflow and example key | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Authentication architecture. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Session management. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Token storage. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Logout. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Protected routes. | COMPLETE | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Authorization. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Roles. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Permissions. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Backend authorization boundaries. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Sensitive data handling. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Environment variables. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Secret management. | MISSING | COMPLETE | REQUIRES_MORE_EVIDENCE | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| XSS. | MISSING | COMPLETE | REQUIRES_MORE_EVIDENCE | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| CSRF. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| CORS. | MISSING | COMPLETE | REQUIRES_MORE_EVIDENCE | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Input validation. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Error messages. | PARTIAL | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |
| Logging. | MISSING | COMPLETE | Observed in scope | DATA, WEB-AUTH-001 | Authentication and security, DATA | E04, E09, E14, E16/G05, G07 |

### H. Localization

| Domain | Previous skill | Final skill | Source status | Reference and rule | Workflow and example key | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Translation file structure. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Feature namespaces. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Shared translations. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Translation registration. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Language switching. | MISSING | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Locale persistence. | MISSING | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| RTL/LTR. | COMPLETE | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Direction-aware layouts. | PARTIAL | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Currency formatting. | MISSING | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Date formatting. | MISSING | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Number formatting. | MISSING | COMPLETE | Observed in scope | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Missing translation detection. | MISSING | COMPLETE | NOT_PRESENT_IN_SOURCE | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |
| Translation completeness validation. | MISSING | COMPLETE | NOT_PRESENT_IN_SOURCE | UI, WEB-I18N-001 | Implement localization and RTL, UI | E05, E10, E15/G06 |

### I. Quality, Performance, and Testing

| Domain | Previous skill | Final skill | Source status | Reference and rule | Workflow and example key | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| TypeScript strictness. | COMPLETE | COMPLETE | Observed in scope | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Linting. | PARTIAL | COMPLETE | Observed in scope | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Formatting. | MISSING | COMPLETE | NOT_PRESENT_IN_SOURCE | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Import boundaries. | PARTIAL | COMPLETE | Observed in scope | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Dependency management. | MISSING | COMPLETE | Observed in scope | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Bundle optimization. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | QA, WEB-PERF-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Code splitting. | PARTIAL | COMPLETE | NOT_PRESENT_IN_SOURCE | QA, WEB-PERF-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Lazy loading. | PARTIAL | COMPLETE | NOT_PRESENT_IN_SOURCE | QA, WEB-PERF-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Rendering performance. | PARTIAL | COMPLETE | REQUIRES_MORE_EVIDENCE | QA, WEB-PERF-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Network efficiency. | PARTIAL | COMPLETE | Observed in scope | QA, WEB-PERF-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Caching. | PARTIAL | COMPLETE | Observed in scope | QA, WEB-PERF-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Error monitoring. | MISSING | COMPLETE | REQUIRES_MORE_EVIDENCE | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Unit testing. | PARTIAL | COMPLETE | NOT_PRESENT_IN_SOURCE | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Component testing. | PARTIAL | COMPLETE | NOT_PRESENT_IN_SOURCE | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Integration testing. | PARTIAL | COMPLETE | NOT_PRESENT_IN_SOURCE | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| End-to-end testing. | PARTIAL | COMPLETE | NOT_PRESENT_IN_SOURCE | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Build validation. | COMPLETE | COMPLETE | Observed in scope | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| Deployment configuration. | PARTIAL | COMPLETE | Observed in scope | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
| CI/CD. | MISSING | COMPLETE | Observed in scope | QA, WEB-QA-001 | Performance and validation, QA | E01, E06, E11, E16/G09, G10 |
## Practical portability walkthrough

| Build step | Independent implementation path | Assessment |
| --- | --- | --- |
| Initialize and document | Approve React SPA and a fixture transport. Fill project profile, requirements, structure and verification docs. Keep dependency and runtime versions pinned. | The workflow provides decisions and file locations. |
| Application shell and branding | Compose public sign-in and protected nested inventory routes, header, responsive sidebar and language selector. Define a neutral brand and tokenized light and dark roles. | Covered by architecture and interface references. Browser layout and focus require target tests. |
| Overview and navigation | Compose inventory totals and availability metrics from typed read models. Add an accessible summary and navigate to inventory through a registered route. | Covered by dashboard patterns. Chart rendering remains a target check. |
| Paginated inventory | Put service and query binding inside the feature, validate the envelope, and derive the list key from identity and the URL. Render loading, empty, error and ready states. | The neutral modules are independent of the reference. React DOM smoke covers a seeded table, URL filter/page reset and three feedback branches. |
| Create and edit | Use a feature schema with explicit defaults, map the payload, show field errors, and reconcile list and detail keys. Use dialogs for short forms or routes for complex forms. | Documented. The React smoke only submits a search form. |
| Identity and localization | Guard the frontend and require a verified API permission contract for writes. Register catalogs, set root direction and test language switching. | React DOM smoke covers a simulated signed-out boundary and root RTL metadata. Backend enforcement, real catalog switching and visual RTL remain target checks. |
| Review and deliver | Run static, component, integration and browser checks for actual user journeys. Record outcomes in the living docs and validate production routing/configuration. | Target project workflow is complete. The smoke does not cover deployment. |

Use this walkthrough to implement the flow with fixtures before connecting a backend. No source repository or private configuration is needed. Maintain one URL and API contract per feature. Apply project approval gates before introducing material dependencies.

## Knowledge scope

| Scope | Rule and reference ownership |
| --- | --- |
| Framework-neutral | WEB-DEC-001, WEB-DOC-001. Validation gates, input trust, authorization, data contract and token principles are portable. |
| React-specific | WEB-ARC-001/002/003, WEB-STATE-001, WEB-FORM-001, WEB-QA-001 and WEB-PERF-001 carry React placement and lifecycle guidance. |
| Dashboard-specific | WEB-UI-001/002/003 and dashboard sections of the profile cover dense shell, table, KPI and overlay interactions. WEB-I18N-001 applies direction and formatting to this UI. |
| External API integration | WEB-API-001 and WEB-AUTH-001 cover contracts, scoped transport, identity and backend boundaries. Axios and query integration are replaceable adapters. |
| Project-specific | Branding, exact tokens, library preferences, source business entities and credential persistence are evidence or target-project decisions. |
| Provisional shared | Extracted data, UI, rendering and deployment practices that may generalize stay in this profile pending Next.js comparison. |

## Remaining gaps and disposition

Multiple audiences, bulk and import operations, dynamic fields, multi-step forms and unsaved changes have conditional guidance. The source does not establish a production implementation for these cases. Backend security, real refresh behavior, full browser accessibility and RTL, chart correctness, integration tests, production performance and deployment behavior require a target environment. The guidance is ready for owner approval for the scoped React profile. These gaps remain documented as target validation or future profile work.
