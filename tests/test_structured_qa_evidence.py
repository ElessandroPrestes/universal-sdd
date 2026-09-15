import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA_EVIDENCE_TEMPLATE = ROOT / "templates" / "QA_EVIDENCE_TEMPLATE.md"
VERIFICATION_REPORT_TEMPLATE = ROOT / "templates" / "VERIFICATION_REPORT_TEMPLATE.md"
VERIFICATION_WORKFLOW = ROOT / "workflows" / "verification.md"
TESTING_STANDARD = ROOT / "standards" / "testing.md"


class StructuredQAEvidenceTests(unittest.TestCase):
    def test_canonical_qa_evidence_template_has_required_yaml_fields(self):
        content = QA_EVIDENCE_TEMPLATE.read_text(encoding="utf-8")
        expected_fields = [
            "criterion_id: AC-001",
            "status: passed",
            "execution_type:",
            "execution_date:",
            "verified_by:",
            "preconditions_met:",
            "action_taken:",
            "observable_result:",
            "reproducible_evidence:",
            "command:",
            "log_or_artifact:",
            "details:",
            "exception_ref:",
        ]
        for field in expected_fields:
            with self.subTest(field=field):
                self.assertIn(field, content)

    def test_verification_report_template_structures_comparison_and_gate_decision(self):
        content = VERIFICATION_REPORT_TEMPLATE.read_text(encoding="utf-8")
        self.assertIn("## Comparison results", content)
        self.assertIn("verified:", content)
        self.assertIn("missing:", content)
        self.assertIn("unmapped:", content)
        self.assertIn("failed:", content)
        self.assertIn("ambiguous:", content)
        self.assertIn("## Unresolved findings", content)
        self.assertIn("## Gate 3 decision", content)
        self.assertIn("Gate status:", content)

    def test_verification_workflow_and_testing_standard_reference_evidence_contract(self):
        workflow = VERIFICATION_WORKFLOW.read_text(encoding="utf-8")
        standard = TESTING_STANDARD.read_text(encoding="utf-8")

        self.assertIn("templates/QA_EVIDENCE_TEMPLATE.md", workflow)
        self.assertIn("templates/VERIFICATION_REPORT_TEMPLATE.md", workflow)
        self.assertIn("is operational", workflow)
        self.assertIn("templates/QA_EVIDENCE_TEMPLATE.md", standard)


if __name__ == "__main__":
    unittest.main()
