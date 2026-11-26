# Distribution

The installable ZIP has one top-level `web-engineering/` folder with `SKILL.md` directly beneath it. It includes 52 frozen runtime files plus Apache-2.0 LICENSE and NOTICE. Repository history, dependencies, private evidence and validation outputs stay outside the archive. This is a portable folder archive. Check consumer-specific requirements before adapting it to another format.

From a reviewed checkout, build with Python 3.10+:

```sh
python3 scripts/validate.py
python3 -B -m unittest discover -s scripts
python3 scripts/privacy_check.py
artifact_dir="$(mktemp -d)"
python3 scripts/package_skill.py --output "$artifact_dir"
(cd "$artifact_dir" && shasum -a 256 -c SHA256SUMS)
```

The script checks `scripts/runtime.sha256` against every runtime path and byte, rejects symlinks and extras, then writes fixed-order, stored ZIP members with stable timestamps and permissions. It verifies archive integrity and checks relative Markdown links against the archive members. Rebuild into another fresh directory and compare ZIP bytes with `cmp`. After extraction, verify all file hashes with `shasum -a 256 -c runtime.sha256` from the directory containing the extracted skill folder.

The ZIP, runtime manifest, release manifest and checksums are the package artifacts. Keep the [installation guide](INSTALLATION.md) and [draft release notes](RELEASE_NOTES_v0.1.0.md) alongside them. The release manifest records archive and license hashes separately from the runtime inventory. No installer script is required.

## Repository boundary

Repository docs include onboarding, compatibility, release and maintenance material. Sanitized historical audits remain under `docs/`. Scripts and CI are development tools. The CI workflow checks packaging, privacy, references, route tests and neutral TypeScript. Live agent, browser and database exercises are separate local validation tasks requiring their respective tooling.
