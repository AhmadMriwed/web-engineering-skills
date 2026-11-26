# Contributing

Keep agent-facing changes in `web-engineering/`. Keep evaluation history and development tooling outside it. Put one rule definition at its owning reference and preserve stable IDs. Record applicability, prerequisites, expected outcomes, failure handling and verification. Update task routes when a reader needs a different entry point. Keep route names unique and targets package-local. Add workflows with narrow loading paths, neutral examples and no project-specific secrets or source.

Describe the evidence supporting a change, the validated framework and tool versions, conflicts addressed, and remaining limitations. Update affected references, project documentation and examples together. For new patterns, tie the claim to evidence with the scope and verification level. Review work against [knowledge maintenance](docs/KNOWLEDGE_MAINTENANCE.md).

Run `python3 scripts/validate.py` and `python3 -B -m unittest discover -s scripts`. Run applicable fixture checks and follow [distribution](docs/DISTRIBUTION.md) for package verification. Runtime changes require an approved new manifest and appropriate retesting. PRs should summarize impact, evidence, actual tests, privacy and compatibility effects.

The repository is distributed under [Apache-2.0](LICENSE). Submit only material you have the right to contribute.
