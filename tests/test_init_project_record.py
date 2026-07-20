from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/project-allrounder/scripts/init_project_record.py"


class InitProjectRecordTest(unittest.TestCase):
    def test_creates_complete_record_without_overwriting(self):
        with TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo"
            subprocess.run(["python3", str(SCRIPT), str(target)], check=True)

            expected = [
                f"{i:02d}-{name}"
                for i, name in enumerate(
                    [
                        "source",
                        "requirements",
                        "proposal",
                        "baseline",
                        "plan",
                        "execution",
                        "deliverables",
                        "progress",
                        "finance",
                        "changes-risks",
                        "acceptance",
                        "closeout",
                    ]
                )
            ]
            actual = sorted(path.name for path in target.iterdir() if path.is_dir())
            self.assertEqual(expected, actual)

            marker = target / "01-requirements/requirements-matrix.md"
            marker.write_text("keep", encoding="utf-8")
            subprocess.run(["python3", str(SCRIPT), str(target)], check=True)
            self.assertEqual("keep", marker.read_text(encoding="utf-8"))

    def test_rejects_target_that_is_an_existing_file(self):
        with TemporaryDirectory() as tmp:
            target = Path(tmp) / "not-a-directory"
            target.write_text("content", encoding="utf-8")
            result = subprocess.run(
                ["python3", str(SCRIPT), str(target)],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn("directory", result.stderr.lower())


if __name__ == "__main__":
    unittest.main()
