"""Check the documentation contracts this template can verify mechanically.

Standard library only.

    python tools/validate.py

Checks:
  1. every relative link / image in tracked Markdown points to an existing path
     (fenced code blocks and HTML comments are skipped; anchors are not checked);
  2. every Markdown file except the READMEs starts with YAML frontmatter that has
     title, status and updated, and status is one of the allowed values;
  3. generated diagrams are up to date (skipped when docs/about/ was removed).

Exit code is the number of failed checks (0 = all passed).
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
STATUSES = {"draft", "in-review", "approved", "archived", "deprecated"}
FRONTMATTER_EXEMPT = {"README.md", "README.zh-TW.md"}  # GitHub renders YAML frontmatter as a table

LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HTML_RE = re.compile(r"""(?:src|srcset|href)\s*=\s*["']([^"']+)["']""")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


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


def check_links(files: list[Path]) -> list[str]:
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
                errors.append(f"{md.relative_to(ROOT).as_posix()}: broken link -> {t}")
    return errors


def check_frontmatter(files: list[Path]) -> list[str]:
    errors = []
    for md in files:
        rel = md.relative_to(ROOT).as_posix()
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
