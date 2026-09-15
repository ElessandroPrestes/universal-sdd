import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC_TEMPLATE = ROOT / "templates" / "SPEC_TEMPLATE.md"
VERIFICATION_WORKFLOW = ROOT / "workflows" / "verification.md"
QUALITY_GATES = ROOT / "standards" / "quality-gates.md"
FEATURE_WORKFLOW = ROOT / "workflows" / "feature.md"


class StructuredAcceptanceVerificationTests(unittest.TestCase):
    def test_canonical_template_has_required_yaml_contract_fields(self):
        content = SPEC_TEMPLATE.read_text(encoding="utf-8")
        for field in ("id: AC-001", "preconditions:", "action:", "expected_result:", "evidence_type:"):
            with self.subTest(field=field):
                self.assertIn(field, content)

    def test_qa_verifier_lists_inputs_divergence_and_review_order(self):
        content = VERIFICATION_WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("## Inputs", content)
        self.assertIn("## Comparison", content)
        self.assertIn("## Output", content)
        self.assertIn("missing", content)
        self.assertIn("unmapped", content)
        self.assertIn("failed", content)
        self.assertIn("ambiguous", content)
        self.assertIn("before Code Review", content)

    def test_open_verifier_findings_block_code_review(self):
        gates = QUALITY_GATES.read_text(encoding="utf-8")
        workflow = FEATURE_WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("block Code Review", gates)
        self.assertIn("before independent\nreviews", workflow)
        self.assertIn("blocking Gate 3 finding", VERIFICATION_WORKFLOW.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
