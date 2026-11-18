"""Check the documentation contracts this template can verify mechanically.

Standard library only.

    python tools/validate.py

Checks:
  1. every relative link / image in tracked Markdown points to an existing path
     (fenced code blocks and HTML comments are skipped);
  2. every Markdown file except the READMEs starts with YAML frontmatter that has
     title, status and updated, and status is one of the allowed values;
  3. every #anchor in a link to a Markdown file matches a heading (GitHub slug)
     or an HTML id in that file;
  4. in project records (docs/project/), a table row whose maturity column says
     已確認 has a confirmation date (YYYY-MM-DD) in that cell or a column about 確認;
  5. every validation record (docs/project/validation/*.md) has a 判定 that is
     通過／失敗／未跑／不適用, and a 通過 also records the tested commit hash, the
     command or steps, and the result;
  6. generated diagrams are up to date (skipped when docs/about/ was removed).

Not checked: external URLs, whether a recorded commit still exists (squash merges
and other repositories make that unreliable), and whether the content is true.
These checks catch missing evidence fields, not wrong evidence.

Exit code is the number of failed checks (0 = all passed).
"""

from __future__ import annotations

import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
STATUSES = {"draft", "in-review", "approved", "archived", "deprecated"}
FRONTMATTER_EXEMPT = {"README.md", "README.zh-TW.md"}  # GitHub renders YAML frontmatter as a table

LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HTML_RE = re.compile(r"""(?:src|srcset|href)\s*=\s*["']([^"']+)["']""")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$")
HTML_ID_RE = re.compile(r"""<[^>]*\b(?:id|name)\s*=\s*["']([^"']+)["']""")
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
HASH_RE = re.compile(r"\b[0-9a-f]{7,40}\b")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
VERDICTS = ("通過", "失敗", "未跑", "不適用")
PLACEHOLDERS = {"", "待填", "待補"}
PROJECT_DIR = "docs/project/"
VALIDATION_DIR = "docs/project/validation/"
# Labels of the validation template fields; a label may keep the template's （hint）.
FIELDS = {
    "verdict": ("判定：通過／失敗／未跑／不適用（附理由）", "判定"),
    "commit": ("被測分支與 commit",),
    "command": ("實際命令或人工步驟",),
    "result": ("實際結果、輸出與證據位置", "實際結果"),
}


def tracked_markdown() -> list[Path]:
    try:
        out = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout
        files = [ROOT / line for line in out.splitlines() if line]
    except (OSError, subprocess.CalledProcessError):
        files = list(ROOT.rglob("*.md"))
    return sorted(p for p in files if p.exists())


def strip_code(text: str) -> str:
    text = COMMENT_RE.sub("", text)
    keep, fenced = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            fenced = not fenced
            continue
        if not fenced:
            keep.append(re.sub(r"`[^`]*`", "", line))
    return "\n".join(keep)


def is_external(target: str) -> bool:
    return bool(re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I)) or target.startswith("#")


def check_links(files: list[Path], root: Path = ROOT) -> list[str]:
    errors = []
    for md in files:
        body = strip_code(md.read_text(encoding="utf-8"))
        targets = LINK_RE.findall(body)
        for raw in HTML_RE.findall(body):
            targets.extend(part.strip().split(" ")[0] for part in raw.split(","))
        for t in targets:
            if not t or is_external(t):
                continue
            path = unquote(t.split("#", 1)[0].split("?", 1)[0])
            if not path:
                continue
            dest = (md.parent / path).resolve()
            if not dest.exists():
                errors.append(f"{md.relative_to(root).as_posix()}: broken link -> {t}")
    return errors


def check_frontmatter(files: list[Path], root: Path = ROOT) -> list[str]:
    errors = []
    for md in files:
        rel = md.relative_to(root).as_posix()
        if rel in FRONTMATTER_EXEMPT:
            continue
        lines = md.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != "---":
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        try:
            end = lines.index("---", 1)
        except ValueError:
            errors.append(f"{rel}: frontmatter is not closed")
            continue
        fields = dict(
            (k.strip(), v.strip()) for k, _, v in (l.partition(":") for l in lines[1:end]) if k.strip())
        for key in ("title", "status", "updated"):
            if not fields.get(key):
                errors.append(f"{rel}: frontmatter missing '{key}'")
        status = fields.get("status")
        if status and status not in STATUSES:
            errors.append(f"{rel}: status '{status}' not in {sorted(STATUSES)}")
    return errors


def outside_fences(text: str) -> list[tuple[int, str]]:
    """(line number, line) pairs that are not inside fenced code blocks."""
    keep, fenced = [], False
    for no, line in enumerate(text.splitlines(), 1):
        if FENCE_RE.match(line):
            fenced = not fenced
            continue
        if not fenced:
            keep.append((no, line))
    return keep


def slugify(heading: str) -> str:
    """GitHub's heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # [text](url) -> text
    text = re.sub(r"<[^>]+>", "", text).lower()
    kept = "".join(ch for ch in text
                   if ch in " -" or unicodedata.category(ch)[0] in "LMN" or unicodedata.category(ch) == "Pc")
    return kept.replace(" ", "-")


def anchors_of(md: Path, cache: dict[Path, set[str]]) -> set[str]:
    if md not in cache:
        found: set[str] = set()
        seen: dict[str, int] = {}
        text = md.read_text(encoding="utf-8")
        if text.startswith("---\n"):  # YAML frontmatter comments are not headings
            end = text.find("\n---", 4)
            text = text[end + 4:] if end != -1 else text
        for _, line in outside_fences(COMMENT_RE.sub("", text)):
            m = HEADING_RE.match(line)
            if m:
                slug = slugify(m.group(1))
                n = seen.get(slug, 0)
                seen[slug] = n + 1
                found.add(slug if n == 0 else f"{slug}-{n}")
            found.update(a.lower() for a in HTML_ID_RE.findall(line))
        cache[md] = found
    return cache[md]


def check_anchors(files: list[Path], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    cache: dict[Path, set[str]] = {}
    for md in files:
        for t in LINK_RE.findall(strip_code(md.read_text(encoding="utf-8"))):
            if "#" not in t or re.match(r"^[a-z][a-z0-9+.-]*:", t, re.I):
                continue
            path, anchor = t.split("#", 1)
            path = unquote(path.split("?", 1)[0])
            dest = (md.parent / path).resolve() if path else md
            if dest.suffix.lower() != ".md" or not dest.is_file() or not anchor:
                continue  # missing files are reported by the link check
            if unquote(anchor).lower() not in anchors_of(dest, cache):
                errors.append(f"{md.relative_to(root).as_posix()}: missing anchor -> {t}")
    return errors


def split_row(line: str) -> list[str]:
    cells = line.strip()
    if cells.startswith("|"):
        cells = cells[1:]
    if cells.endswith("|"):
        cells = cells[:-1]
    return [c.strip() for c in cells.split("|")]


def check_maturity(files: list[Path], root: Path = ROOT) -> list[str]:
    errors = []
    for md in files:
        rel = md.relative_to(root).as_posix()
        if not rel.startswith(PROJECT_DIR):
            continue
        lines = outside_fences(md.read_text(encoding="utf-8"))
        header: list[str] | None = None
        for i, (no, line) in enumerate(lines):
            if not line.strip().startswith("|"):
                header = None
                continue
            if i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1][1]):
                header = split_row(line)
                continue
            if header is None or TABLE_SEP_RE.match(line):
                continue
            row = split_row(line)
            maturity = [c for h, c in zip(header, row) if "成熟度" in h]
            if not any("已確認" in c for c in maturity):
                continue
            confirmations = [c for h, c in zip(header, row) if "確認" in h or "成熟度" in h]
            if not any(DATE_RE.search(c) for c in confirmations):
                errors.append(f"{rel}:{no}: '{row[0]}' is 已確認 but has no confirmation date (YYYY-MM-DD)")
    return errors


def field_value(content: str, labels: tuple[str, ...]) -> str | None:
    """Value of a 'label：value' list item, or None if the item is another field."""
    for label in labels:
        if not content.startswith(label):
            continue
        rest = content[len(label):]
        if rest.startswith("（") and "）" in rest:
            rest = rest[rest.find("）") + 1:]
        if rest[:1] in ("：", ":"):
            return rest[1:].strip()
    return None


def check_validation_records(files: list[Path], root: Path = ROOT) -> list[str]:
    errors = []
    for md in files:
        rel = md.relative_to(root).as_posix()
        if not rel.startswith(VALIDATION_DIR) or md.name.upper().startswith("README"):
            continue
        values: dict[str, list[str]] = {k: [] for k in FIELDS}
        for _, line in outside_fences(COMMENT_RE.sub("", md.read_text(encoding="utf-8"))):
            content = line.strip()
            if not content.startswith("- "):
                continue
            for key, labels in FIELDS.items():
                value = field_value(content[2:].strip(), labels)
                if value is not None:
                    values[key].append(value)
                    break
        if not values["verdict"]:
            errors.append(f"{rel}: missing 判定")
        for verdict in values["verdict"]:
            if not verdict.startswith(VERDICTS):
                errors.append(f"{rel}: 判定 '{verdict}' must start with {'／'.join(VERDICTS)}")
        if not any(v.startswith("通過") for v in values["verdict"]):
            continue
        if not any(HASH_RE.search(v) for v in values["commit"]):
            errors.append(f"{rel}: 判定 is 通過 but 被測分支與 commit has no commit hash")
        if not any(v not in PLACEHOLDERS for v in values["command"]):
            errors.append(f"{rel}: 判定 is 通過 but 實際命令或人工步驟 is empty")
        if not any(v not in PLACEHOLDERS for v in values["result"]):
            errors.append(f"{rel}: 判定 is 通過 but 實際結果 is empty")
    return errors


def check_diagrams() -> list[str]:
    if not (ROOT / "docs" / "about").exists() or not (ROOT / "tools" / "render_diagrams.py").exists():
        return []
    sys.path.insert(0, str(ROOT / "tools"))
    import render_diagrams  # noqa: E402

    stale = [p for p, svg in render_diagrams.expected().items()
             if not p.exists() or p.read_text(encoding="utf-8") != svg]
    return [f"{p.relative_to(ROOT).as_posix()}: stale, run python tools/render_diagrams.py"
            for p in stale]


def main() -> int:
    files = tracked_markdown()
    checks = [
        ("links", lambda: check_links(files)),
        ("frontmatter", lambda: check_frontmatter(files)),
        ("anchors", lambda: check_anchors(files)),
        ("maturity", lambda: check_maturity(files)),
        ("validation records", lambda: check_validation_records(files)),
        ("diagrams", check_diagrams),
    ]
    failed = 0
    for name, fn in checks:
        errors = fn()
        print(f"[{'FAIL' if errors else 'ok'}] {name} ({len(files)} markdown files)" if name != "diagrams"
              else f"[{'FAIL' if errors else 'ok'}] {name}")
        for e in errors:
            print(f"    {e}")
        failed += bool(errors)
    return failed


if __name__ == "__main__":
    sys.exit(main())
