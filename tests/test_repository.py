from pathlib import Path
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAMES = (
    "project-allrounder",
    "writing-project-proposals",
    "building-project-presentations",
)


class RepositoryTest(unittest.TestCase):
    def test_expected_skills_and_pass_branding_exist(self):
        self.assertTrue((ROOT / "docs/assets/pass-logo.svg").is_file())

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        readme_en = (ROOT / "README_EN.md").read_text(encoding="utf-8")
        for content in (readme, readme_en):
            self.assertIn("Project Allrounder Skill Suite", content)
            self.assertIn("docs/assets/pass-logo.svg", content)
            self.assertNotIn("$ equip project-allrounder", content)

        self.assertNotIn("## 优秀本子与优秀 PPT", readme)
        self.assertNotIn("案例对照是必经步骤", readme)
        self.assertNotIn("## Successful Proposals and Reference Decks", readme_en)
        self.assertNotIn("Example comparison is a required step", readme_en)

        for name in SKILL_NAMES:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file())

    def test_pass_logo_is_valid_green_cyan_svg(self):
        logo = ROOT / "docs/assets/pass-logo.svg"
        ET.parse(logo)
        svg = logo.read_text(encoding="utf-8").lower()
        for color in ("#a7f070", "#63e6a9", "#3dd9c2", "#42c9f5"):
            self.assertIn(color, svg)
        self.assertIn("project allrounder skill suite", svg)


if __name__ == "__main__":
    unittest.main()
