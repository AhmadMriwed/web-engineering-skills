# Publication checklist

The owner approved the repository, version, visibility, Apache-2.0 licensing and all publication operations. The commands below are the planning record. The final release includes the archive, checksums and release manifest.

- [x] Approve repository name, skill identifier, version and public visibility.
- [x] Confirm Apache-2.0 and the approved attribution, Copyright (c) 2026 Ahmad Mriwed.
- [ ] Recheck all files staged for public distribution and enable a private security channel if desired.
- [ ] Approve final artifacts, checksums, installation evidence and compatibility wording.
- [x] Authorize final commit, remote creation, push, tag, release and asset publication.

## Proposed metadata

Name `web-engineering-skills`, skill `web-engineering`, default branch `main`, initial version `v0.1.0`. Homepage unset until an owner-approved URL exists. About text and social preview copy: “Engineering workflows for AI coding agents building with React, Next.js, external APIs and optional Supabase.”

Suggested topics: `agent-skills`, `ai-agents`, `codex`, `claude-code`, `react`, `nextjs`, `typescript`, `supabase`, `web-development`, `software-engineering`, `software-architecture`, `design-system`, `developer-tools`. Claude Code indicates documented installation guidance.

## Proposed commands

Run only after those approvals. Substitute the approved GitHub namespace and artifact directory. Inspect the staged diff and approved license first. The release command below publishes; use the draft option if approved only to stage a release.

```sh
git diff --cached --check
git commit -m "Prepare Web Engineering Skills v0.1.0"
gh repo create OWNER/web-engineering-skills --public --source=. --remote=origin
git push -u origin main
git tag -a v0.1.0 -m "Web Engineering Skills v0.1.0"
git push origin refs/tags/v0.1.0
gh release create v0.1.0 --verify-tag --title "Web Engineering Skills v0.1.0" \
  --notes-file docs/RELEASE_NOTES_v0.1.0.md \
  "$ARTIFACT_DIR/web-engineering-v0.1.0.zip" "$ARTIFACT_DIR/SHA256SUMS" \
  "$ARTIFACT_DIR/runtime.sha256" "$ARTIFACT_DIR/INSTALLATION.md"
```
