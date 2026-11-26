"""Validate the draft skill and its local documentation links."""
from pathlib import Path
import argparse
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "web-engineering" / "SKILL.md"
RULE_ID = r"WEB-(?!SRC-)[A-Z][A-Z0-9]*-\d{3}"


TASK_HEADER = ("Task", "Required context and profile", "Rules and workflow",
               "Output, validation and docs")


def parse_task_routes(source, path, package_root):
    """Validate the named rows of the canonical task table."""
    routes, errors = [], []
    seen = set()
    found_header = found_separator = False
    for number, line in enumerate(source.splitlines(), 1):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = tuple(cell.strip() for cell in re.split(r"(?<!\\)\|", line[1:].removesuffix("|")))
        if not any(cells):
            continue
        where = f"{path.name}:{number}"
        if cells == TASK_HEADER:
            if found_header:
                errors.append(f"{where}: duplicate task header")
            found_header = True
            continue
        if len(cells) == len(TASK_HEADER) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            if not found_header or found_separator:
                errors.append(f"{where}: unexpected task separator")
            found_separator = True
            continue
        if not found_separator or len(cells) != len(TASK_HEADER) or not all(cells):
            errors.append(f"{where}: malformed task entry")
            continue
        name = cells[0]
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 -]*", name):
            errors.append(f"{where}: invalid task name: {name}")
            continue
        identifier = re.sub(r"[-\s]+", "-", name.casefold())
        if identifier in seen:
            errors.append(f"{where}: duplicate task route: {name}")
            continue
        seen.add(identifier)
        routes.append(name)
        for target in re.findall(r"\]\(([^)]+)\)", line):
            resource = unquote(target.partition("#")[0])
            destination = (path.parent / resource).resolve()
            if not resource or not destination.is_relative_to(package_root) or not destination.is_file():
                errors.append(f"{where}: invalid task reference: {target}")
    if not found_header or not found_separator:
        errors.append(f"{path.name}: missing task table header or separator")
    return routes, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list-routes", action="store_true")
    options = parser.parse_args()
    errors = []
    if not SKILL.is_file():
        errors.append("Missing skill entry point")
    elif not re.match(
        r"\A---\nname: web-engineering\ndescription: [^\n]+\n---\n",
        SKILL.read_text(),
    ):
        errors.append("Invalid skill entry-point metadata")

    definitions = {}
    citations = set()
    for directory in (ROOT, ROOT / "docs", ROOT / "web-engineering"):
        files = directory.rglob("*.md") if directory != ROOT else directory.glob("*.md")
        for file in files:
            body = file.read_text()
            for rule in re.findall(rf"^### ({RULE_ID}) ", body, re.M):
                if rule in definitions:
                    errors.append(f"Duplicate rule {rule} in {file.relative_to(ROOT)}")
                definitions[rule] = file
            citations.update(re.findall(RULE_ID, body))
            for target in re.findall(r"\]\(([^)]+)\)", body):
                if re.match(r"^[a-z][a-z+.-]*:", target, re.I):
                    continue
                path = unquote(target.partition("#")[0])
                if not path:
                    continue
                destination = (file.parent / path).resolve()
                if not destination.is_relative_to(ROOT) or not destination.is_file():
                    errors.append(f"Invalid local link in {file.relative_to(ROOT)}: {target}")

    evidence_registry = (ROOT / "docs" / "SOURCE_EVIDENCE.md").read_text()
    guide_registry = (ROOT / "docs" / "REACT_GUIDE_RECONCILIATION.md").read_text()
    audit = (ROOT / "docs" / "PHASE_1_COVERAGE_AUDIT.md").read_text()
    evidence_ids = set(re.findall(r"^\| (E\d{2}) \|", evidence_registry, re.M))
    guide_ids = set(re.findall(r"^\| (G\d{2}) \|", guide_registry, re.M))
    for item in sorted(set(re.findall(r"\b[EG]\d{2}\b", audit)) - evidence_ids - guide_ids):
        errors.append(f"Undefined audit evidence {item}")

    next_ids = set(re.findall(r"^\| (N\d{2}) \|", evidence_registry, re.M))
    for name in ("PHASE_2_COVERAGE_AUDIT.md", "REACT_NEXTJS_COMPARISON.md"):
        content = (ROOT / "docs" / name).read_text()
        for item in sorted(set(re.findall(r"\bN\d{2}\b", content)) - next_ids):
            errors.append(f"Undefined Next.js evidence {item} in {name}")

    phase3_evidence = set(re.findall(r"^\| (S\d{2}) \|", evidence_registry, re.M))
    phase3_docs = [
        "PHASE_3.md", "PHASE_3_COVERAGE_AUDIT.md", "PHASE_3_MERGE_PLAN.md",
        "SUPABASE_ARCHITECTURE_ANALYSIS.md", "SUPABASE_SECURITY_REVIEW.md",
        "BACKEND_STRATEGY_COMPARISON.md", "PHASE_3_VALIDATION_COMPLETION.md",
        "SUPABASE_VALIDATION_MATRIX.md",
    ]
    for name in phase3_docs:
        content = (ROOT / "docs" / name).read_text()
        citations.update(re.findall(RULE_ID, content))
        for item in sorted(set(re.findall(r"\bS\d{2}\b", content)) - phase3_evidence):
            errors.append(f"Undefined Supabase evidence {item} in {name}")

    unified_audit = (ROOT / "docs" / "UNIFIED_COVERAGE_AUDIT.md").read_text()
    known_evidence = evidence_ids | guide_ids | next_ids | phase3_evidence
    unified_ids = set(re.findall(r"\b[EGNS]\d{2}\b", unified_audit))
    for item in sorted(unified_ids - known_evidence):
        errors.append(f"Undefined unified coverage evidence {item}")

    if len(definitions) != 20:
        errors.append(f"Expected 20 stable rules, found {len(definitions)}")
    tasks = SKILL.parent / "references" / "tasks.md"
    routes = []
    if not tasks.is_file():
        errors.append("Missing task routing table")
    else:
        routes, route_errors = parse_task_routes(tasks.read_text(), tasks, SKILL.parent.resolve())
        errors.extend(route_errors)
        if len(routes) != 29:
            errors.append(f"Expected 29 named task routes, found {len(routes)}")

    for rule in sorted(citations - definitions.keys()):
        errors.append(f"Undefined evidence rule {rule}")
    if errors:
        raise SystemExit("\n".join(errors))
    if options.list_routes:
        print("\n".join(routes))
    else:
        print(f"Validated skill metadata, links, evidence, {len(definitions)} rules and {len(routes)} task routes.")


if __name__ == "__main__":
    main()
