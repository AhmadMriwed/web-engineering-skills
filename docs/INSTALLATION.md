# Install Web Engineering Skills

Download the [versioned ZIP](https://github.com/AhmadMriwed/web-engineering-skills/releases/tag/v0.1.0) or clone the public repository with `git clone https://github.com/AhmadMriwed/web-engineering-skills.git`. The ZIP includes the Apache-2.0 license and notice. Verify any provided checksum with `shasum -a 256 -c SHA256SUMS` from the artifact directory. Extract the ZIP into a scratch directory first. Confirm the result has `web-engineering/SKILL.md` and its sibling `references/` and `assets/` directories. For a source checkout, use its existing `web-engineering/` folder.

## Choose a destination

| Consumer | Project scope | User scope | Explicit invocation |
| --- | --- | --- | --- |
| Codex CLI | `.agents/skills/web-engineering/` | `~/.agents/skills/web-engineering/` | `$web-engineering` |
| Claude Code | `.claude/skills/web-engineering/` | `~/.claude/skills/web-engineering/` | `/web-engineering` |

Create the chosen parent directory and place the entire folder inside it. For example, from the target project root:

```sh
source_skill="/path/to/extracted/web-engineering"
skills_dir=".agents/skills"
test -f "$source_skill/SKILL.md" &&
mkdir -p "$skills_dir" &&
test ! -e "$skills_dir/web-engineering" &&
test ! -L "$skills_dir/web-engineering" &&
cp -R "$source_skill" "$skills_dir/"
```

Substitute the Claude or user-scope destination as appropriate. Use one scope initially to avoid duplicate-name resolution. Inspect existing installations before replacing anything.

Start a fresh agent session in the target project. Look for the skill in the consumer's selector if available, then invoke it and request a discovery or review task. Confirm it can report the selected task route or workflow. Natural language can trigger skill use when the client judges it relevant. If that does not happen, invoke it explicitly. If discovery fails, check the launch directory, folder depth, exact filename, client permissions and duplicate installations.

To update, verify and extract the newer package, move the known installed folder to a backup location outside skill discovery paths, then copy the replacement. Restore the backup if verification fails. To uninstall, move or remove only the installed `web-engineering` folder after checking the path. Start a fresh session and confirm discovery has stopped. Keep local modifications in your backup.

Other consumers need their own documented discovery and invocation mechanisms. Claude Code and other consumers have no independent runtime verification in this project. [Agent Skills specification](https://agentskills.io/specification) · [Codex skills](https://developers.openai.com/codex/skills) · [Claude Code skills](https://code.claude.com/docs/en/skills)
