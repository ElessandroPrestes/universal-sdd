import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IDS_GUIDE = ROOT / "docs" / "ids-and-traceability.md"
QUALITY_GATES = ROOT / "standards" / "quality-gates.md"
CHANGE_REQUEST_TEMPLATE = ROOT / "templates" / "CHANGE_REQUEST_TEMPLATE.md"


class SpecAmendmentProtocolTests(unittest.TestCase):
    def test_ids_guide_preserves_versioned_predecessors_and_approvals(self):
        content = IDS_GUIDE.read_text(encoding="utf-8")
        self.assertIn("## SPEC amendment lifecycle", content)
        self.assertIn("`SPEC-NNN-vN`", content)
        self.assertIn("never overwrites the approved predecessor", content)
        self.assertIn("new applicable human approval cycle", content)

    def test_change_request_template_contains_both_explicit_paths(self):
        content = CHANGE_REQUEST_TEMPLATE.read_text(encoding="utf-8")
        self.assertIn("## Lightweight clarification path", content)
        self.assertIn("## Scope change path", content)
        self.assertIn("Select exactly one path", content)
        self.assertIn("Durable approval reference", content)
        self.assertIn("New amended SPEC ID: SPEC-NNN-vN", content)

    def test_quality_gate_blocks_ambiguous_or_material_changes(self):
        content = QUALITY_GATES.read_text(encoding="utf-8")
        self.assertIn("## SPEC amendment classification", content)
        self.assertIn("false or unknown", content)
        self.assertIn("is a blocking gate", content)
        self.assertIn("No agent may classify uncertainty as a clarification", content)


if __name__ == "__main__":
    unittest.main()
