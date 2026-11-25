# Skill architecture and portability

Package the entire `web-engineering/` directory as one skill. Keep its folder name. The entry point, references and neutral assets form the distributable runtime. Repository README and roadmap serve owners. Reports and evidence history serve maintainers. Root scripts are development validation infrastructure. Keep private provenance and recovery archives external.

1. **Activation** uses the name and description.
2. **Core** loads the entry point, then the relevant task row.
3. **Profile** selects an existing or approved frontend and adds an API, combined or Supabase profile only as needed.
4. **Task** loads relevant rule sections, workflow and optional templates or examples.
5. **Verification** uses scenario checks and supporting evidence where needed. Routine changes can complete without extraction reports.

Direct routes from the entry point and task table keep loading shallow. Profile documents are optional indexes once the correct task reference is known. Cross-links are lookups, with no recursive reading requirement.

## Consumer assessment

Reviewed on 2026-11-25. Specification checks cover matching folder/name, YAML frontmatter, bounded description and self-contained references. Installation guidance describes expected locations. Discoverability, activation, reference selection and workflow execution require separate consumer-level tests. [Agent Skills specification](https://agentskills.io/specification)

- Codex repository distribution can place the folder under `.agents/skills/` where supported by the installed client. Check the client’s current discovery scope and available skill list. [OpenAI skills documentation](https://developers.openai.com/codex/skills)
- Claude Code project distribution can place the folder under `.claude/skills/`. Check discovery and invocation in a neutral workspace. [Claude Code skills documentation](https://code.claude.com/docs/en/skills)

The skill uses shared frontmatter fields and relative paths. Installation, real activation and execution are Phase 5 test objectives for each consumer. License choice remains with the owner.

## Version-sensitive knowledge

| Area | Evidence and validation | Target applicability |
| --- | --- | --- |
| React and SPA libraries | React 19.2.4 DOM fixture. Phase 1 records the observed Vite, Router, Query and form stack. | Respect the target lockfile and verify router guards, query lifecycle and build conventions. |
| Next.js | 16.2.4 observed and built on Node 22.23.2. | Proxy, async route inputs and cache options need version matching. [Next.js App Router docs](https://nextjs.org/docs/app) |
| TypeScript | 5.9.3 strict fixture checks. | Respect the target compiler, module resolution and SDK declaration support. |
| Supabase | JS 2.107.0 compiled and PostgreSQL 16 synthetic fixture rerun. CLI 3.4.0 reviewed in Phase 3. | Confirm CLI flags, generated types, SSR cookie adapter and runtime services with the target stack. [Supabase local development](https://supabase.com/docs/guides/local-development) |

Validation date for Phase 4 fixture checks is 2026-11-25. Reference stack observations remain source-specific.
