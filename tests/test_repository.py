from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAMES = (
    "project-allrounder",
    "writing-project-proposals",
    "building-project-presentations",
)
PASS_BANNER_START = """<p align="center">🟢　🟡　🔵</p>

<p align="center"><code>"""
PASS_BANNER_END = """</code></p>

<p align="center"><strong>🟩 Project Allrounder Skill Suite 🟦</strong></p>"""


class RepositoryTest(unittest.TestCase):
    def test_expected_skills_and_pass_branding_exist(self):
        self.assertFalse((ROOT / "docs/assets/pass-logo.svg").exists())

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        readme_en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for content in (readme, readme_en):
            self.assertIn(PASS_BANNER_START, content)
            self.assertIn(PASS_BANNER_END, content)
            self.assertIn("██████╗&nbsp;&nbsp;█████╗", content)
            self.assertIn("<br>", content)
            self.assertNotIn("<pre", content)
            self.assertNotIn("docs/assets/pass-logo.svg", content)
            self.assertNotIn("$ equip project-allrounder", content)
            self.assertNotIn("> [!NOTE]", content)

        self.assertNotIn("## 优秀本子与优秀 PPT", readme)
        self.assertNotIn("案例对照是必经步骤", readme)
        self.assertNotIn("## Successful Proposals and Reference Decks", readme_en)
        self.assertNotIn("Example comparison is a required step", readme_en)

        for name in SKILL_NAMES:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
