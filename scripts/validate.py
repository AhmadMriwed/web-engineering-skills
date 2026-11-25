"""Validate the draft skill and its local documentation links."""
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "web-engineering" / "SKILL.md"
RULE_ID = r"WEB-(?!SRC-)[A-Z][A-Z0-9]*-\d{3}"


def main():
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
    if not tasks.is_file():
        errors.append("Missing task routing table")
    else:
        rows = [line for line in tasks.read_text().splitlines() if line.startswith("| ")][1:]
        if len(rows) != 30:
            errors.append(f"Expected 30 task routes, found {len(rows)}")

    for rule in sorted(citations - definitions.keys()):
        errors.append(f"Undefined evidence rule {rule}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated skill metadata, local links, audit evidence IDs and {len(definitions)} rule IDs.")


if __name__ == "__main__":
    main()
