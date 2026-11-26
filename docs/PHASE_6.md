# Phase 6 release preparation

**PHASE_6_COMPLETE_WITH_EXPLICIT_LIMITATIONS**

The proposed v0.1.0 candidate packages the validated Web Engineering Skill as an installable folder archive. Packaging preserves the frozen baseline at `8699a0ff508f665dd2731858f2d93595000e29f0`. The archive contains 52 runtime files, 20 stable rule IDs and 29 named task routes. Runtime files added, removed or modified: zero.

## Release content

- [README](../README.md) introduces the profiles, selection workflow and progressive disclosure.
- [Installation](INSTALLATION.md), [requests](USAGE.md), [compatibility](PUBLIC_VALIDATION.md) and [distribution](DISTRIBUTION.md) support the independently installable folder.
- [Changelog](../CHANGELOG.md), [contribution guide](../CONTRIBUTING.md), [security policy](../SECURITY.md) and [roadmap](../ROADMAP.md) prepare repository maintenance.
- [Draft release notes](RELEASE_NOTES_v0.1.0.md) and [publication checklist](RELEASE_CHECKLIST.md) contain proposed metadata, owner decisions and publication commands. The skill and repository names stay as proposed. No public URL exists.
- GitHub issue forms and a PR template are local drafts. The GitHub workflow uses read-only repository permissions, no production secrets and a mandatory lightweight package job. GitHub-hosted execution remains unverified.

## Packaging and agent smoke

The approved manifest contains SHA-256 for every runtime path. The Python packager fixes entry order, timestamp, permissions and storage format, validates membership, bytes and internal links, and writes artifacts outside the repository. Two separate output directories matched byte for byte. Extraction into a clean project-local Codex skills directory preserved all 52 hashes and passed the skill-creator metadata validator.

Two fresh Codex CLI sessions ran against the extracted ZIP with Apps disabled and a read-only sandbox. The explicit request read the installed entry point, task routes, discovery, compatibility and standards, then selected the architecture planning route for React with REST. The natural-language request read the installed entry point, Next.js profile and workflow, then selected Next.js localized routing and asked about publishing and update cadence. Both completed. Recorded file reads provide evidence of discovery and real usage. This smoke did not regenerate applications or run Claude Code.

## License and attribution review

The preliminary license proposal was superseded by the owner-approved Apache-2.0 license. See the repository license and notice.

The 52 files are guidance, templates and neutral examples. The review found no vendored dependency source or external assets in the package. Imports and documented installation dependencies remain subject to their own licenses. References to official sources remain linked. The review is not an ownership determination or a full dependency-license audit of future consumer apps. The preliminary license draft was excluded from the distribution.

## Repository and distribution layout

```text
.github/                         issue forms, PR template and validation workflow
README.md, CHANGELOG.md          public overview and version history
CONTRIBUTING.md, SECURITY.md     participation and private reporting guidance
ROADMAP.md                       phases and future verification
docs/                            public guides and sanitized development history
scripts/                         validators, checks, manifest and packager
web-engineering/                 sole ZIP root
  SKILL.md                       validated entry point
  references/                    shared and profile rules and workflows
    react/, next/, supabase/      profile-specific guidance
  assets/                        templates and independent examples
    examples/                    React/TypeScript fixtures
    next-example/                localized App Router fixture
    supabase-example/            typed client and synthetic SQL fixture
```

This phase added the public guides, release docs, CI, templates, ignore rules, manifest, packager and privacy checker. It updated README, roadmap and release readiness. Existing Phase 5 and 5.1 working-tree edits were preserved. The full file inventories, checksums and recovery checkpoint are external and supplied in the handoff. Git remains on `main` at the frozen commit, with uncommitted release preparation and prior evaluation edits.

## Publication gates

Confirm version, license, holder, attribution, publication scope and final artifacts. Separately authorize the final commit, remote creation, push, tag, release and asset publication. No such actions were taken. Managed Supabase, Claude Code, reference replay, production security and broad accessibility remain documented verification limits.

## Executed checks

| Check | Result |
| --- | --- |
| Repository validator, named route inventory and parser unit tests | Passed. 20 rule IDs, 29 routes, local links and evidence references, and all four parser tests. An initial run caught the README linking to this report before it existed. The final run passed after the report was added. |
| Packaging, repeated builds, ZIP test, extraction and per-file SHA-256 | Passed. Byte-identical artifacts and 52 verified runtime paths. |
| Skill-creator YAML metadata validator | Passed against the extracted package. |
| Strict TypeScript compile, example assertions and React DOM smoke | Passed using the installed TypeScript 5.9.3 and Node 22. |
| Next production build and HTTP smoke | Passed with Next.js 16.2.4 and Webpack. Checked Arabic RTL, canonical, sitemap, robots and missing-item status on loopback. |
| Supabase SDK compile and PostgreSQL migration and actor assertions | Passed with the existing SDK environment and a fresh private PostgreSQL 16 cluster. These are synthetic checks. |
| Local Chrome import and draft regression | Passed against the Phase 5.1 synthetic fixture. |
| Privacy and portability | Targeted scan and review found no known private source host, project links, credential patterns or machine paths in candidate files. Archive membership and local link boundaries passed. A pattern scan cannot establish provenance or guarantee absence of every secret. |
| GitHub workflow and issue forms | Local YAML parsing and required structure checks passed. GitHub execution remains open. |

The ZIP is 151,707 bytes. Its SHA-256 is `0a5c8961288df610b6eab8120aed58793bc37775c32a21461fce37aba59c288a`. The companion checksum file covers the ZIP, runtime manifest, installation instructions and draft release notes.

The two README diagrams use GitHub's documented fenced Mermaid flowchart syntax and were reviewed locally against their node and edge definitions. The pinned Mermaid dependency installation and standalone bundle download timed out, so a Mermaid parser and GitHub-rendered preview were not verified. [GitHub diagram documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
