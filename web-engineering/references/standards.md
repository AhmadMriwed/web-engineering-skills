# Engineering standards

### WEB-DEC-001 — Approve material technology choices

**REQUIRED** within the rule’s applicable scope.

Present trade-offs and obtain the owner's decision before implementing a material stack or architecture choice. Record the rationale in the project profile.

### WEB-DOC-001 — Update documentation with implementation

**REQUIRED** within the rule’s applicable scope.

Review the affected requirements, interfaces, decisions, and operational procedures whenever behavior changes. Update the relevant documentation as part of the implementation.

These initial standards come from the workspace brief.

## Instruction and rule precedence

Follow higher-priority agent instructions first. Within the approved task, enforce security, data integrity and framework constraints. Apply shared rules across profiles and use applicable framework guidance to decide implementation. Retain valid local conventions where they satisfy the rules. Use workflows and examples as implementation aids. Surface a conflict that needs owner approval and preserve security boundaries while awaiting a decision.

- **REQUIRED** applies to security, correctness, approved scope, documentation and verification obligations triggered by the task.
- **RECOMMENDED** is an engineering default that can yield to a documented local constraint.
- **CONDITIONAL** applies when the relevant technology or capability is selected.
- **OPTIONAL** applies to an enhancement with a demonstrated benefit.
- **ANTI_PATTERN** identifies a choice that violates a rule or introduces a known failure mode.

Use [task routing](tasks.md) to locate applicable rules. Examples illustrate one applicable configuration.

## Feature lifecycle and definition of done

Trace an existing entry point before changing it. Identify actors, authorization, data ownership, UI states, locale and accessibility constraints. For a small change, keep this inspection and verification local to the affected flow. For a cross-boundary change, record the contract, ownership, affected docs and rollout or recovery path before implementing. Deliver a working slice, validate failure paths, and repeat for the next slice.

Check the requested behavior, types, applicable rules and affected documentation in every change. Check focus, responsive behavior, localization and visible states when interaction changes. Verify negative actor cases for authorization changes, metadata and rendered output for SEO changes, and rollback or compatibility for changes to deployment or persisted data. Measure relevant performance when the change affects it. Report the observed results and limits, including failed mandatory checks. Scale reporting to the change.
