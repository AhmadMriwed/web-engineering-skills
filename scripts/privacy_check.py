"""Flag potential private data in candidate files without printing matches."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

# Split sensitive path markers so the audit source can be safely scanned too.
PATTERNS = {
    "machine path": r"/(?:User" + r"s/|private/" + r"tmp/|home/)[^\s<>`]+",
    "private key": r"-----BEGIN (?:[A-Z ]+ )?PRIVATE" + " KEY-----",
    "credential URL": r"(?:https?|postgres(?:ql)?)://[^\s/:@]+:[^\s/@]+@",
    "managed project hostname": r"https?://[a-z0-9]{20}\.supabase\.(?:co|in)\b",
    "token": r"\b(?:gh[pousr]_[a-zA-Z0-9]{30,}|sk_live_[a-zA-Z0-9]{20,}|eyJ[a-zA-Z0-9_-]{15,}\.[a-zA-Z0-9_-]{15,}\.[a-zA-Z0-9_-]{15,})\b",
    "private source host": r"(?i)gitlab\." + "futxtech" + r"\.com",
    "private source slug": r"(?i)net-" + r"esim",
}


def main():
    paths = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT
    ).decode().split("\0")
    findings = []
    scanned = set()
    for name in sorted(set(paths) - {""}):
        path = ROOT / name
        if path.is_symlink():
            findings.append(f"{name}: symlink")
        elif path.is_file():
            scanned.add(name)
            try:
                body = path.read_text()
            except UnicodeDecodeError:
                findings.append(f"{name}: binary file needs review")
                continue
            for label, pattern in PATTERNS.items():
                if re.search(pattern, body):
                    findings.append(f"{name}: {label}")
    if findings:
        raise SystemExit("\n".join(findings))
    print(f"Targeted privacy scan passed for {len(scanned)} candidate files.")


if __name__ == "__main__":
    main()
