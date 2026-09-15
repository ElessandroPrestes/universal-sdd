import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_traceability.py"
HOOK = ROOT / "templates" / "hooks" / "commit-msg"


class TraceabilityGeneratorTests(unittest.TestCase):
    def test_generates_links_commits_and_gaps(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            fixture = Path(temporary_directory)
            (fixture / "specs").mkdir()
            (fixture / "tasks").mkdir()
            (fixture / "reviews").mkdir()
            (fixture / "docs").mkdir()
            (fixture / "specs" / "SPEC-042-example.md").write_text(
                "| ID | SPEC-042 |\n| Status | Approved |\n", encoding="utf-8"
            )
            (fixture / "tasks" / "TASK-042-01-example.md").write_text(
                "| ID | TASK-042-01 |\n| Status | Done |\n| Refs: | SPEC: SPEC-042 |\n",
                encoding="utf-8",
            )
            (fixture / "reviews" / "qa.md").write_text(
                "| Status | Passed |\nSpec-Ref: SPEC-042\nTask-Ref: TASK-042-01\n",
                encoding="utf-8",
            )
            (fixture / "reviews" / "README.md").write_text("Review index\n", encoding="utf-8")
            self.run_git(fixture, "init", "-q")
            self.run_git(fixture, "config", "user.email", "tests@example.invalid")
            self.run_git(fixture, "config", "user.name", "Traceability Tests")
            self.run_git(fixture, "add", ".")
            self.run_git(
                fixture,
                "commit",
                "-qm",
                "Add fixture\n\nSpec-Ref: SPEC-042\nTask-Ref: TASK-042-01",
            )

            completed = subprocess.run(
                [sys.executable, str(GENERATOR), "--repo-root", str(fixture)],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr)
            matrix = (fixture / "docs" / "traceability-matrix.md").read_text(encoding="utf-8")
            self.assertIn("SPEC-042", matrix)
            self.assertIn("TASK-042-01", matrix)
            self.assertIn("Add fixture", matrix)
            self.assertIn("qa.md", matrix)
            self.assertIn("None detected", matrix)

    def test_hook_rejects_partial_or_malformed_trailers(self):
        cases = [
            ("Update docs\n\nSpec-Ref: SPEC-042\n", 1),
            ("Update docs\n\nSpec-Ref: SPEC-42\nTask-Ref: TASK-042-01\n", 1),
            ("Update docs\n\nSpec-Ref: SPEC-042\nTask-Ref: TASK-042-01\n", 0),
            ("Update docs\n", 0),
        ]
        with tempfile.TemporaryDirectory() as temporary_directory:
            message_file = Path(temporary_directory) / "message"
            for message, expected_code in cases:
                message_file.write_text(message, encoding="utf-8")
                completed = subprocess.run(["sh", str(HOOK), str(message_file)], check=False)
                self.assertEqual(completed.returncode, expected_code, message)

    def run_git(self, directory, *arguments):
        completed = subprocess.run(
            ["git", "-C", str(directory), *arguments], capture_output=True, text=True, check=False
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)


if __name__ == "__main__":
    unittest.main()
