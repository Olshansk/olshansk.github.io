from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUOTE_SCRIPT = ROOT / "scripts" / "add_quote.py"
TIX_SCRIPT = ROOT / "scripts" / "add_tix.py"
MARKER = "<!-- captures:start -->"
END_MARKER = "<!-- captures:end -->"
HEADER = '<div class="year-header">\n  <h2 class="year-title">{date}</h2>\n</div>'


class CaptureScriptsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.path = Path(self.temporary.name) / "capture.md"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_script(self, script: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), *arguments, "--path", str(self.path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_adds_attributed_quote_to_new_date(self) -> None:
        self.path.write_text(
            f"Intro\n\n{MARKER}\n\n{END_MARKER}\n\n> \"Legacy.\"\n", encoding="utf-8"
        )
        result = self.run_script(
            QUOTE_SCRIPT,
            "--text", '“Simplicity is prerequisite for reliability.”',
            "--author", "Edsger W. Dijkstra",
            "--date", "2026-08-11",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        content = self.path.read_text(encoding="utf-8")
        self.assertIn(HEADER.format(date="08/11/2026"), content)
        self.assertIn('> "Simplicity is prerequisite for reliability."\n\n— _Edsger W. Dijkstra_', content)
        self.assertLess(content.index("08/11/2026"), content.index("Legacy"))

        second = self.run_script(
            QUOTE_SCRIPT, "--text", "Second quote.", "--date", "2026-08-11"
        )
        self.assertEqual(second.returncode, 0, second.stderr)
        content = self.path.read_text(encoding="utf-8")
        self.assertLess(content.index("Second quote"), content.index(END_MARKER))
        self.assertLess(content.index(END_MARKER), content.index("Legacy"))

    def test_adds_unattributed_multiline_quote(self) -> None:
        self.path.write_text(f"Intro\n\n{MARKER}\n", encoding="utf-8")
        result = self.run_script(
            QUOTE_SCRIPT, "--text", "First line\nsecond line", "--date", "2026-08-11"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('> "First line\n> second line"', self.path.read_text(encoding="utf-8"))

    def test_reuses_existing_date_and_stays_before_legacy_header(self) -> None:
        self.path.write_text(
            f"Intro\n\n{MARKER}\n\n{HEADER.format(date='06/30/2025')}\n\nOld idea.\n\n"
            '<div class="year-header">\n  <h2 class="year-title">Before June 2025</h2>\n</div>\n\nLegacy.\n',
            encoding="utf-8",
        )
        result = self.run_script(TIX_SCRIPT, "--text", "New idea.", "--date", "2025-06-30")
        self.assertEqual(result.returncode, 0, result.stderr)
        content = self.path.read_text(encoding="utf-8")
        self.assertEqual(content.count("06/30/2025"), 1)
        self.assertLess(content.index("New idea."), content.index("Before June 2025"))

    def test_inserts_titled_tix_in_reverse_date_order(self) -> None:
        self.path.write_text(
            f"Intro\n\n{MARKER}\n\n{HEADER.format(date='08/12/2025')}\n\nNewest.\n\n"
            f"{HEADER.format(date='06/30/2025')}\n\nOldest.\n",
            encoding="utf-8",
        )
        result = self.run_script(
            TIX_SCRIPT, "--title", "Middle", "--text", "Middle idea.", "--date", "2025-07-17"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        content = self.path.read_text(encoding="utf-8")
        self.assertLess(content.index("08/12/2025"), content.index("07/17/2025"))
        self.assertLess(content.index("07/17/2025"), content.index("06/30/2025"))
        self.assertIn("### Middle\n\nMiddle idea.", content)

    def test_duplicate_and_invalid_date_leave_file_unchanged(self) -> None:
        original = f"Intro\n\n{MARKER}\n\n> “Same quote.”\n"
        self.path.write_text(original, encoding="utf-8")
        duplicate = self.run_script(QUOTE_SCRIPT, "--text", "Same quote.", "--date", "2026-08-11")
        self.assertNotEqual(duplicate.returncode, 0)
        self.assertEqual(self.path.read_text(encoding="utf-8"), original)

        invalid = self.run_script(TIX_SCRIPT, "--text", "Different.", "--date", "not-a-date")
        self.assertNotEqual(invalid.returncode, 0)
        self.assertEqual(self.path.read_text(encoding="utf-8"), original)

    def test_missing_marker_leaves_file_unchanged(self) -> None:
        original = "Intro only.\n"
        self.path.write_text(original, encoding="utf-8")
        result = self.run_script(TIX_SCRIPT, "--text", "Idea.", "--date", "2026-08-11")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.path.read_text(encoding="utf-8"), original)

    def test_short_capture_is_not_rejected_as_a_substring(self) -> None:
        self.path.write_text(
            f"Intro\n\n{MARKER}\n\nA longer observation about AI systems.\n", encoding="utf-8"
        )
        result = self.run_script(TIX_SCRIPT, "--text", "AI", "--date", "2026-08-11")
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
