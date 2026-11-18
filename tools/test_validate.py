"""Tests for tools/validate.py. Standard library only.

    python -m unittest discover -s tools -p "test_*.py"
"""

from __future__ import annotations

import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate  # noqa: E402


class Repo:
    """A throwaway directory of Markdown files."""

    def __init__(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def write(self, rel: str, text: str) -> Path:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(text).lstrip("\n"), encoding="utf-8")
        return path

    def files(self) -> list[Path]:
        return sorted(self.root.rglob("*.md"))

    def close(self) -> None:
        self._tmp.cleanup()


class RepoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = Repo()

    def tearDown(self) -> None:
        self.repo.close()


class SlugTest(unittest.TestCase):
    def test_github_style_slugs(self) -> None:
        self.assertEqual(validate.slugify("1．建立或整合專案"), "1建立或整合專案")
        self.assertEqual(validate.slugify("實際用到哪些範本"), "實際用到哪些範本")
        self.assertEqual(validate.slugify("AC-01: Login works"), "ac-01-login-works")
        self.assertEqual(validate.slugify("Use `validate.py` now"), "use-validatepy-now")


class AnchorTest(RepoTest):
    def test_existing_heading_and_html_id_pass(self) -> None:
        self.repo.write("a.md", """
            # Title
            ## 實際用到哪些範本
            <a id="method-map"></a>
            """)
        self.repo.write("b.md", "[x](a.md#實際用到哪些範本) [y](a.md#method-map) [z](#local)\n\n## Local\n")
        self.assertEqual(validate.check_anchors(self.repo.files(), self.repo.root), [])

    def test_missing_anchor_is_reported(self) -> None:
        self.repo.write("a.md", "# Title\n")
        self.repo.write("b.md", "[x](a.md#nope) [y](#also-nope)\n")
        errors = validate.check_anchors(self.repo.files(), self.repo.root)
        self.assertEqual(len(errors), 2)
        self.assertIn("a.md#nope", errors[0])

    def test_duplicate_headings_get_numbered(self) -> None:
        self.repo.write("a.md", "## Notes\n## Notes\n[x](#notes-1)\n")
        self.assertEqual(validate.check_anchors(self.repo.files(), self.repo.root), [])

    def test_code_blocks_are_ignored(self) -> None:
        self.repo.write("a.md", "```\n[x](#nope)\n## Fake\n```\n[y](#fake)\n")
        errors = validate.check_anchors(self.repo.files(), self.repo.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("#fake", errors[0])

    def test_frontmatter_comments_are_not_headings(self) -> None:
        self.repo.write("a.md", "---\ntitle: t\n# owner: me\n---\n\n[x](#owner-me)\n")
        self.assertEqual(len(validate.check_anchors(self.repo.files(), self.repo.root)), 1)

    def test_non_markdown_targets_and_missing_files_are_skipped(self) -> None:
        # Missing files are the link check's job; anchors into non-Markdown are not checked.
        self.repo.write("a.md", "[x](gone.md#a) [y](tool.py#L3)\n")
        self.assertEqual(validate.check_anchors(self.repo.files(), self.repo.root), [])


class MaturityTest(RepoTest):
    TABLE = """
        | 項目 | 內容 | 成熟度 | 確認人與日期 |
        |---|---|---|---|
        | 問題 | X | {maturity} | {confirm} |
        """

    def check(self, rel: str, maturity: str, confirm: str) -> list[str]:
        self.repo.write(rel, self.TABLE.format(maturity=maturity, confirm=confirm))
        return validate.check_maturity(self.repo.files(), self.repo.root)

    def test_confirmed_with_date_passes(self) -> None:
        self.assertEqual(self.check("docs/project/brief.md", "已確認", "使用者 2026-11-16"), [])

    def test_confirmed_without_date_fails(self) -> None:
        errors = self.check("docs/project/brief.md", "已確認", "使用者")
        self.assertEqual(len(errors), 1)
        self.assertIn("docs/project/brief.md", errors[0])

    def test_tentative_without_date_passes(self) -> None:
        self.assertEqual(self.check("docs/project/brief.md", "暫定", "待補"), [])

    def test_merged_maturity_and_confirmation_column(self) -> None:
        self.repo.write("docs/project/brief.md", """
            | AC ID | 成熟度／依據與確認 |
            |---|---|
            | AC-01 | 已確認；使用者 2026-11-16 |
            | AC-02 | 已確認 |
            """)
        errors = validate.check_maturity(self.repo.files(), self.repo.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("AC-02", errors[0])

    def test_date_in_maturity_cell_counts_even_without_confirm_header(self) -> None:
        # Real case: header '成熟度／來源', cell '已確認；使用者 2026-11-17 本輪第 1 點'.
        self.repo.write("docs/project/brief.md", """
            | 方向 | 成熟度／來源 |
            |---|---|
            | 可換教材 | 已確認；使用者 2026-11-17 本輪第 1 點 |
            | 多種補強 | 已確認方向；使用者同日第 2 點 |
            """)
        errors = validate.check_maturity(self.repo.files(), self.repo.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("多種補強", errors[0])

    def test_files_outside_project_records_are_ignored(self) -> None:
        self.assertEqual(self.check("docs/workflow/templates/x.md", "已確認", ""), [])


class ValidationRecordTest(RepoTest):
    PATH = "docs/project/validation/2026-11-18-login.md"

    def record(self, **fields: str) -> str:
        lines = [f"- {k}：{v}" for k, v in fields.items()]
        return "---\ntitle: t\nstatus: draft\nupdated: 2026-11-18\n---\n\n" + "\n".join(lines) + "\n"

    def check(self, text: str) -> list[str]:
        self.repo.write(self.PATH, text)
        return validate.check_validation_records(self.repo.files(), self.repo.root)

    def test_passed_with_full_evidence(self) -> None:
        text = self.record(**{"被測分支與 commit": "main @ 9d2f6b7", "實際命令或人工步驟": "pytest",
                              "實際結果、輸出與證據位置": "12 passed", "判定": "通過"})
        self.assertEqual(self.check(text), [])

    def test_template_label_is_accepted(self) -> None:
        text = self.record(**{"被測分支與 commit（工作目錄有未提交變更也記錄）": "main @ 9d2f6b7",
                              "實際命令或人工步驟": "pytest", "實際結果、輸出與證據位置": "ok",
                              "判定：通過／失敗／未跑／不適用（附理由）": "通過"})
        self.assertEqual(self.check(text), [])

    def test_missing_verdict_fails(self) -> None:
        self.assertTrue(self.check(self.record(**{"實際命令或人工步驟": "pytest"})))

    def test_empty_verdict_fails(self) -> None:
        self.assertTrue(self.check(self.record(**{"判定": ""})))

    def test_unknown_verdict_fails(self) -> None:
        self.assertTrue(self.check(self.record(**{"判定": "大致OK"})))

    def test_passed_without_commit_fails(self) -> None:
        text = self.record(**{"被測分支與 commit": "main", "實際命令或人工步驟": "pytest",
                              "實際結果、輸出與證據位置": "ok", "判定": "通過"})
        errors = self.check(text)
        self.assertEqual(len(errors), 1)
        self.assertIn("commit", errors[0])

    def test_passed_without_command_or_result_fails(self) -> None:
        text = self.record(**{"被測分支與 commit": "abc1234", "判定": "通過"})
        self.assertEqual(len(self.check(text)), 2)

    def test_not_run_needs_no_commit(self) -> None:
        self.assertEqual(self.check(self.record(**{"判定": "未跑，環境未就緒"})), [])

    def test_one_verdict_per_ac(self) -> None:
        text = self.record(**{"被測分支與 commit": "abc1234", "實際命令或人工步驟": "pytest",
                              "實際結果、輸出與證據位置": "ok", "判定": "通過"}) + "- 判定：待定\n"
        self.assertEqual(len(self.check(text)), 1)

    def test_readme_in_validation_dir_is_ignored(self) -> None:
        self.repo.write("docs/project/validation/README.md", "# Index\n")
        self.assertEqual(validate.check_validation_records(self.repo.files(), self.repo.root), [])


if __name__ == "__main__":
    unittest.main()
