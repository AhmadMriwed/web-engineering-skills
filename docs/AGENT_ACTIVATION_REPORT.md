# Phase 5 agent activation

The frozen package was copied into each enabled Codex workspace at `.agents/skills/web-engineering/`. An explicit `$web-engineering` run loaded the installed SKILL.md, task routing, project-selection and standards references and the discovery worksheet in shell tool traces. The response applied the discovery flow to localized search. Automatic runs received ordinary project requests without a skill mention. A, B, C and G completed with logged reads from the installed package. D, E and F also produced skill-read traces, independently of whether the project turn completed.

An explicit mention and a successful file read establish use of the installed skill. The CLI trace does not expose a separate metadata or activation event for every run. Reference and template reads were recorded when present. A file read provides evidence of access. It does not alone establish that all guidance was applied.

Control workspaces omitted the installed package and enabled the CLI's skip-host-skill-discovery flag. The traces reviewed contained no reads of the frozen skill in controls. Consumer and model-service behavior outside the visible traces remains uncontrolled. The workspaces share the same host and credentials; their project files and sessions were separate.

Codex CLI 0.171.0-alpha.13 ran these local tests. Claude Code was unavailable on PATH, so its installation, discovery and activation remain untested. [Codex skill documentation](https://developers.openai.com/codex/skills) · [Claude Code skill documentation](https://code.claude.com/docs/en/skills)
