import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "PROJECT.md"
CONTEXT_BUDGET = ROOT / "docs" / "context-budget.md"
KNOWLEDGE_INDEX = ROOT / "knowledge" / "INDEX.md"
AGENTS = ROOT / "AGENTS.md"

MODULES = (
    "knowledge/modules/framework-overview.md",
    "knowledge/modules/governance-and-structure.md",
    "knowledge/modules/delivery-and-quality.md",
)


class ContextBudgetTests(unittest.TestCase):
    def test_context_budget_names_all_required_phases_and_boundaries(self):
        content = CONTEXT_BUDGET.read_text(encoding="utf-8")
        for phase in ("Discovery", "Architecture", "Implementation", "QA", "Review"):
            with self.subTest(phase=phase):
                section = content.split(f"## {phase}\n", maxsplit=1)[1]
                self.assertIn("**Must load:**", section)
                self.assertIn("**May load:**", section)
                self.assertIn("**Do not load:**", section)

    def test_project_index_and_knowledge_modules_support_selective_retrieval(self):
        self.assertLessEqual(len(PROJECT.read_text(encoding="utf-8").splitlines()), 75)
        index = KNOWLEDGE_INDEX.read_text(encoding="utf-8")
        project = PROJECT.read_text(encoding="utf-8")
        for module in MODULES:
            with self.subTest(module=module):
                self.assertTrue((ROOT / module).is_file())
                self.assertIn(module, index)
                self.assertIn(module, project)

    def test_agents_rule_restricts_knowledge_loading_to_referenced_modules(self):
        content = AGENTS.read_text(encoding="utf-8")
        self.assertIn("somente a SPEC aprovada", content)
        self.assertIn("módulos de `knowledge/` referenciados explicitamente pela SPEC", content)
        self.assertIn("Não carregue\na base de conhecimento completa", content)


if __name__ == "__main__":
    unittest.main()
