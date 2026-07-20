from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
SKILL_NAMES = (
    "project-allrounder",
    "writing-project-proposals",
    "building-project-presentations",
)


class SkillSuiteTest(unittest.TestCase):
    def test_skill_frontmatter_and_metadata(self):
        for name in SKILL_NAMES:
            with self.subTest(skill=name):
                folder = SKILLS_ROOT / name
                text = (folder / "SKILL.md").read_text(encoding="utf-8")
                self.assertRegex(text, rf"(?m)^name: {re.escape(name)}$")
                self.assertRegex(text, r"(?m)^description: Use when .+$")
                metadata = (folder / "agents/openai.yaml").read_text(encoding="utf-8")
                self.assertIn(f"${name}", metadata)
                self.assertFalse((folder / "README.md").exists())

    def test_all_relative_markdown_links_resolve(self):
        for markdown in SKILLS_ROOT.rglob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "#")):
                    continue
                clean_target = target.split("#", 1)[0]
                with self.subTest(file=markdown, target=clean_target):
                    self.assertTrue((markdown.parent / clean_target).resolve().exists())

    def test_cross_skill_contracts_are_explicit(self):
        orchestrator = (SKILLS_ROOT / "project-allrounder/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("writing-project-proposals", orchestrator)
        self.assertIn("building-project-presentations", orchestrator)

        proposals = (SKILLS_ROOT / "writing-project-proposals/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("case-comparison-matrix.md", proposals)
        self.assertIn("Never copy", proposals)

        presentations = (
            SKILLS_ROOT / "building-project-presentations/SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("actual `.pptx`", presentations)
        self.assertIn("Render every final slide", presentations)
        self.assertIn("full size", presentations)


if __name__ == "__main__":
    unittest.main()
