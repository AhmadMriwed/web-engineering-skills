"""Build and validate the frozen runtime ZIP using only the Python standard library."""
import argparse
import json
from hashlib import sha256
from io import BytesIO
from pathlib import Path, PurePosixPath
import re
from urllib.parse import unquote
from zipfile import ZIP_STORED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILL = "web-engineering"


def digest(data):
    return sha256(data).hexdigest()


def runtime_files():
    manifest = {}
    for line in (ROOT / "scripts/runtime.sha256").read_text().splitlines():
        checksum, name = line.split("  ", 1)
        rel = PurePosixPath(name)
        if (not re.fullmatch(r"[0-9a-f]{64}", checksum)
                or rel.parts[:1] != (SKILL,) or len(rel.parts) < 2
                or any(part.startswith(".") or part in {"node_modules", "__pycache__"}
                       for part in rel.parts)
                or name in manifest):
            raise ValueError(f"Invalid runtime manifest entry: {name}")
        manifest[name] = checksum
    directory = ROOT / SKILL
    paths = list(directory.rglob("*"))
    if directory.is_symlink() or any(path.is_symlink() for path in paths):
        raise ValueError("Runtime contains a symlink")
    actual = {path.relative_to(ROOT).as_posix() for path in paths if path.is_file()}
    if actual != manifest.keys() or len(actual) != 52:
        raise ValueError(f"Runtime inventory differs: {sorted(actual ^ manifest.keys())}")
    files = {name: (ROOT / name).read_bytes() for name in sorted(manifest)}
    for name, data in files.items():
        if digest(data) != manifest[name]:
            raise ValueError(f"Runtime hash mismatch: {name}")
    return files


def check_links(files):
    for name, content in files.items():
        if not name.endswith(".md"):
            continue
        for target in re.findall(r"\]\(([^)]+)\)", content.decode()):
            if re.match(r"^[a-z][a-z+.-]*:", target, re.I):
                continue
            resource = unquote(target.partition("#")[0])
            if not resource:
                continue
            destination = (ROOT / name).parent / resource
            resolved = destination.resolve()
            if not resolved.is_relative_to(ROOT) or resolved.relative_to(ROOT).as_posix() not in files:
                raise ValueError(f"Broken or nonportable link in {name}: {target}")


def build(files):
    buffer = BytesIO()
    with ZipFile(buffer, "w", compression=ZIP_STORED) as archive:
        for name, data in files.items():
            entry = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data)
    return buffer.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Directory outside the repository")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(ROOT):
        parser.error("Use an output directory outside the repository")
    try:
        files = runtime_files()
        distribution = dict(sorted({**files, **{f"{SKILL}/{name}": (ROOT / name).read_bytes() for name in ("LICENSE", "NOTICE")}}.items()))
        payload = build(distribution)
        with ZipFile(BytesIO(payload)) as archive:
            if archive.testzip() or archive.namelist() != list(distribution):
                raise ValueError("Archive integrity check failed")
            unpacked = {name: archive.read(name) for name in archive.namelist()}
        if unpacked != distribution:
            raise ValueError("Archive contents differ from source")
        check_links(unpacked)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")

    output.mkdir(parents=True, exist_ok=True)
    filename = "web-engineering-v0.1.0.zip"
    artifacts = {
        filename: payload,
        "release-manifest.json": (json.dumps({
            "version": "v0.1.0",
            "license": "Apache-2.0",
            "copyright": "Copyright (c) 2026 Ahmad Mriwed",
            "archive": {"name": filename, "bytes": len(payload), "sha256": digest(payload)},
            "runtime_files": len(files),
            "release_files": {name: digest(data) for name, data in distribution.items() if name not in files},
        }, indent=2) + "\n").encode(),
        "runtime.sha256": (ROOT / "scripts/runtime.sha256").read_bytes(),
        "INSTALLATION.md": (ROOT / "docs/INSTALLATION.md").read_bytes(),
        "RELEASE_NOTES_v0.1.0.md": (ROOT / "docs/RELEASE_NOTES_v0.1.0.md").read_bytes(),
    }
    artifacts["SHA256SUMS"] = "".join(
        f"{digest(data)}  {name}\n" for name, data in artifacts.items()
    ).encode()
    for name, data in artifacts.items():
        (output / name).write_bytes(data)
    print(f"Verified {len(files)} runtime files. Wrote {output / filename}")


if __name__ == "__main__":
    main()
