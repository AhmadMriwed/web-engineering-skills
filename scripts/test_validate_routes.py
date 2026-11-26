from pathlib import Path
import tempfile
import unittest

from validate import ROOT, parse_task_routes


HEADER = """| Task | Required context and profile | Rules and workflow | Output, validation and docs |
| :--- | --- | ---: | --- |
"""


class TaskRouteTests(unittest.TestCase):
    def test_named_routes_exclude_header_separator_and_blank_rows(self):
        text = HEADER + "| | | | |\n| Bug fixing | Scope | Rule | Check |\n"
        routes, errors = parse_task_routes(text, ROOT / "tasks.md", ROOT)
        self.assertEqual(routes, ["Bug fixing"])
        self.assertEqual(errors, [])

    def test_reports_duplicate_and_malformed_rows(self):
        text = HEADER + (
            "| Bug fixing | Scope | Rule | Check |\n"
            "| bug-fixing | Scope | Rule | Check |\n"
            "| incomplete | Scope | Rule |\n"
            "| Missing context | | Rule | Check |\n"
        )
        routes, errors = parse_task_routes(text, ROOT / "tasks.md", ROOT)
        self.assertEqual(routes, ["Bug fixing"])
        self.assertEqual(len(errors), 3)
        self.assertIn("duplicate", errors[0])
        self.assertTrue(all("malformed" in error for error in errors[1:]))

    def test_requires_portable_existing_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "valid.md").touch()
            text = HEADER + (
                "| Good | Context | [workflow](valid.md) | Check |\n"
                "| Bad | Context | [workflow](missing.md) | Check |\n"
                "| Escape | Context | [workflow](../valid.md) | Check |\n"
            )
            _, errors = parse_task_routes(text, root / "tasks.md", root)
            self.assertEqual(len(errors), 2)
            self.assertTrue(all("invalid task reference" in error for error in errors))

    def test_frozen_shape_has_29_unique_routes(self):
        root = ROOT / "web-engineering"
        path = root / "references" / "tasks.md"
        routes, errors = parse_task_routes(path.read_text(), path, root)
        self.assertEqual(errors, [])
        self.assertEqual(len(routes), 29)


if __name__ == "__main__":
    unittest.main()
