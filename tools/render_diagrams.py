"""Render the README diagrams as light/dark SVG pairs in English and Traditional Chinese.

Standard library only. The SVG files under docs/about/assets/ are generated;
edit this file and re-run instead of editing the SVGs by hand. Files are named
<diagram>-<lang>-<theme>.svg, for example method-loop-en-dark.svg.

    python tools/render_diagrams.py          # write all diagrams
    python tools/render_diagrams.py --check  # exit 1 if any SVG is stale or orphaned
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "docs" / "about" / "assets"

FONT = ("-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans TC', "
        "'PingFang TC', 'Microsoft JhengHei', Helvetica, Arial, sans-serif")

THEMES = {
    "light": {
        "bg": "#ffffff", "frame": "#d0d7de", "ink": "#1f2328", "muted": "#59636e",
        "label_bg": "#ffffff",
        "blue": ("#0969da", "#ddf4ff"), "green": ("#1a7f37", "#dafbe1"),
        "purple": ("#8250df", "#fbefff"), "amber": ("#9a6700", "#fff8c5"),
        "red": ("#cf222e", "#ffebe9"), "gray": ("#8c959f", "#f6f8fa"),
    },
    "dark": {
        "bg": "#0d1117", "frame": "#30363d", "ink": "#e6edf3", "muted": "#9198a1",
        "label_bg": "#0d1117",
        "blue": ("#4493f8", "#0d2140"), "green": ("#3fb950", "#0f2a1a"),
        "purple": ("#ab7df8", "#241a3a"), "amber": ("#d29922", "#2e2208"),
        "red": ("#f85149", "#3a1416"), "gray": ("#6e7681", "#161b22"),
    },
}


def text_width(s: str, size: float) -> float:
    """Rough rendered width: CJK and full-width glyphs ~1em, others ~0.56em."""
    w = 0.0
    for ch in s:
        w += size if ord(ch) > 0x2E7F else size * 0.56
    return w


class Svg:
    def __init__(self, width: int, height: int, theme: str, title: str, subtitle: str):
        self.w, self.h, self.t = width, height, THEMES[theme]
        self.title = title
        self.parts: list[str] = []
        self.markers: set[str] = set()
        self.parts.append(
            f'<rect width="{width}" height="{height}" rx="14" fill="{self.t["bg"]}" '
            f'stroke="{self.t["frame"]}"/>')
        self.text(28, 38, title, 18, weight=700)
        self.text(28, 60, subtitle, 13, color=self.t["muted"])

    def color(self, name: str) -> tuple[str, str]:
        return self.t[name]

    def text(self, x, y, s, size=13, weight=400, color=None, anchor="start", max_width=None):
        if max_width is not None and text_width(s, size) > max_width:
            raise ValueError(f"text too wide for {max_width}px: {s!r}")
        color = color or self.t["ink"]
        self.parts.append(
            f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(s)}</text>')

    def box(self, x, y, w, h, title, lines=(), color="blue", title_size=15, line_size=12,
            align="middle", tag=None):
        stroke, fill = self.color(color)
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="1.5"/>')
        pad = 14
        tx = x + w / 2 if align == "middle" else x + pad
        rows: list[tuple[str, float, int, str]] = []
        if tag:
            rows.append((tag, 11, 700, stroke))
        rows.append((title, title_size, 600, self.t["ink"]))
        rows.extend((line, line_size, 400, self.t["muted"]) for line in lines)
        heights = [size * 1.45 for _, size, _, _ in rows]
        cy = y + (h - sum(heights)) / 2
        for (s, size, weight, col), rh in zip(rows, heights):
            cy += rh
            self.text(round(tx, 1), round(cy - rh * 0.3, 1), s, size, weight, col,
                      anchor=align, max_width=w - 2 * pad + 2)

    def _marker(self, stroke: str) -> str:
        mid = "head-" + stroke.lstrip("#")
        self.markers.add(stroke)
        return mid

    def arrow(self, points, color="blue", dashed=False, label=None, label_at=None,
              label_anchor="middle", label_color=None):
        stroke = self.color(color)[0]
        mid = self._marker(stroke)
        d = "M" + " L".join(f"{x},{y}" for x, y in points)
        dash = ' stroke-dasharray="6 5"' if dashed else ""
        self.parts.append(
            f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="1.6"{dash} '
            f'marker-end="url(#{mid})"/>')
        if label:
            lx, ly = label_at
            w = text_width(label, 12) + 10
            rx = lx - w / 2 if label_anchor == "middle" else (lx - 5 if label_anchor == "start" else lx - w + 5)
            self.parts.append(
                f'<rect x="{round(rx, 1)}" y="{ly - 13}" width="{round(w, 1)}" height="18" rx="4" '
                f'fill="{self.t["label_bg"]}"/>')
            self.text(lx, ly, label, 12, color=label_color or stroke, anchor=label_anchor)

    def pill(self, x, y, s, color="gray", size=12, min_width=0):
        stroke, fill = self.color(color)
        w = max(text_width(s, size) + 22, min_width)
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{round(w, 1)}" height="26" rx="13" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="1.2"/>')
        self.text(round(x + w / 2, 1), y + 17.5, s, size, 600, self.t["ink"], anchor="middle")
        return w

    def render(self) -> str:
        defs = "".join(
            f'<marker id="head-{c.lstrip("#")}" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
            for c in sorted(self.markers))
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" role="img" aria-label="{escape(self.title)}">'
            f'<title>{escape(self.title)}</title><defs>{defs}</defs>'
            + "".join(self.parts) + "</svg>\n")


# ---------------------------------------------------------------- strings

LANGS = ("en", "zh-TW")

TEXT = {
    "method_title": {
        "en": "The method: reduce uncertainty with evidence",
        "zh-TW": "方法論全圖：用證據逐步降低不確定性"},
    "method_sub": {
        "en": "Stages are problems being solved, not documents to fill in. Any stage can go back to exploration.",
        "zh-TW": "階段是正在解決的問題，不是要填完的文件；任何階段發現未知都可以回到探索。"},
    "stages": {
        "en": [("Start", "state the pain"), ("Define", "scope + AC"), ("Choose", "compare options"),
               ("Design & tests", "plan the tests"), ("Implement", "small batches"),
               ("Review & ship", "review · accept"), ("Close", "retro, next")],
        "zh-TW": [("起始", "描述困擾"), ("定義", "問題 · 範圍 · AC"), ("選擇", "候選 · 取捨"),
                  ("設計與測試規劃", "怎麼做 · 怎麼測"), ("實作", "小批 · 跑測試"),
                  ("審查與交付", "review · 驗收"), ("收尾", "復盤 · 下一輪")]},
    "explore": {"en": ("Explore", "gather evidence"), "zh-TW": ("探索", "蒐集證據 · 驗證假設")},
    "def_explore": {"en": "define ⇄ explore", "zh-TW": "定義 ⇄ 探索"},
    "enough": {"en": "enough evidence → choose", "zh-TW": "證據足夠 → 選擇"},
    "not_enough": {"en": "not enough → explore", "zh-TW": "證據不足 → 探索"},
    "untested": {"en": "untested assumption", "zh-TW": "假設待驗證"},
    "tests_fail": {"en": "tests fail", "zh-TW": "測試未通過"},
    "fix": {"en": "fix, re-verify", "zh-TW": "修正與重驗"},
    "wrong_req": {"en": "wrong requirement → re-confirm", "zh-TW": "需求不符，重新確認"},
    "new_goal": {"en": "new goal → next round", "zh-TW": "新目標，開下一輪"},
    "forward": {"en": "forward", "zh-TW": "前進"},
    "go_back": {"en": "go back (original result kept)", "zh-TW": "返回修正（保留原結果）"},
    "method_ref": {
        "en": "Minimum output and exit criteria for each stage: docs/workflow/guide.md",
        "zh-TW": "每個階段的最小產出與前進條件：docs/workflow/guide.md"},

    "map_title": {
        "en": "Framework map: start with two records, expand only when needed",
        "zh-TW": "框架地圖：從兩份紀錄開始，需要時才展開"},
    "map_sub": {
        "en": "One AGENTS.md for every AI tool. Templates are reference material, not a to-do list.",
        "zh-TW": "所有 AI 工具共用同一份 AGENTS.md；範本是參考材料，不是待辦清單。"},
    "layers": {
        "en": [
            ("Entry", "One rule set for every AI tool; the user only has to describe the problem"),
            ("Project records", "The only files created up front: single source of goals and AC; current stage and evidence"),
            ("Templates", "problem · discovery · approach · decisions · design · experiments · testing · closure · meta"),
            ("Reference", "workflow (clarifying) · review (checklist) · conventions (format) · slot_contracts (content)"),
            ("Checks", "Links & anchors · frontmatter · confirmed dates · validation evidence · diagram freshness · init-smoke\nPRs must state the tested commit and what was not verified"),
        ],
        "zh-TW": [
            ("入口", "所有 AI 工具共用一份規則；使用者只需描述困擾"),
            ("專案紀錄", "唯一預先建立的紀錄：目標與 AC 的單一來源、目前階段與證據"),
            ("按需範本", "problem · discovery · approach · decisions · design · experiments · testing · closure · meta"),
            ("規則參考", "workflow（釐清流程）· review（審查）· conventions（格式）· slot_contracts（內容契約）"),
            ("檢查", "連結與錨點 · frontmatter · 已確認須有日期 · validation 證據欄位 · 圖表是否最新 · init-smoke\nPR 須寫被測版本與未驗證項目"),
        ]},
    "map_foot": {
        "en": "Derived projects can delete docs/about and docs/template-maintenance; nothing else depends on them.",
        "zh-TW": "衍生專案可刪除 docs/about 與 docs/template-maintenance；其餘不依賴它們。"},

    "axes_title": {
        "en": "Four kinds of state, recorded separately; none implies another",
        "zh-TW": "四種狀態分開記錄，互不推導"},
    "axes_sub": {
        "en": "The most common AI mistake is reading one as another: a draft as agreement, an approved doc as passing tests, a merge as delivery.",
        "zh-TW": "AI 最常見的錯誤，是把其中一種狀態當成另一種：草案當共識、文件 approved 當測試通過、合併當交付。"},
    "axes": {
        "en": [
            ("Definition maturity", "Has the user confirmed it?", ["Unknown", "Tentative", "Confirmed"], "with source, who and when"),
            ("Document status", "Has the doc been reviewed?", ["draft", "in-review", "approved"], "says nothing about results"),
            ("Test result", "Does this commit pass now?", ["Not run", "Failed", "Passed @ commit"], "an old pass is not a pass now"),
            ("Delivery", "How far has it gone?", ["Ready for review", "Mergeable", "Deployable", "Accepted", "Closed"],
             "merged ≠ deployed ≠ accepted"),
        ],
        "zh-TW": [
            ("定義成熟度", "這個需求被確認了嗎？", ["未知", "暫定", "已確認"], "附來源、確認人與日期"),
            ("文件 status", "這份文件審過了嗎？", ["draft", "in-review", "approved"], "不代表需求或結果"),
            ("測試結果", "這個版本現在通過嗎？", ["未跑", "失敗", "通過 @ commit"], "歷史 passing 不算現在"),
            ("交付", "走到哪一步了？", ["可送審", "可合併", "可部署", "已驗收", "已結案"], "合併不自動滿足後面各步"),
        ]},
    "axes_foot": {
        "en": "Rule sources: AGENTS.md §2, §4; docs/workflow/reference/workflow.md (definition maturity) and conventions.md.",
        "zh-TW": "規則來源：AGENTS.md §2、§4；docs/workflow/reference/workflow.md「定義成熟度」與 conventions.md。"},

    "case_title": {
        "en": "Real case: ipas-learning-hub (2026-11-16 → 11-18, 21 PRs)",
        "zh-TW": "真實案例：ipas-learning-hub（2026-11-16 → 11-18，21 個 PR）"},
    "case_sub": {
        "en": "It began with “searching the textbook with Ctrl+F is exhausting”. Each step was decided by the evidence before it, not by a finished PRD.",
        "zh-TW": "從一句「Ctrl+F 查教材很累」開始；每一步都靠前一步的證據決定，而不是先寫完 PRD。"},
    "case_nodes": {
        "en": [
            ("Start", "Describe the pain", ["Unsure which answer is right;", "searches the PDF with Ctrl+F"]),
            ("Explore 1", "Evidence for 50 questions", ["In textbook: 26, not found: 24", "(AI-filled, marked unreviewed)"]),
            ("Explore 2", "Keyword vs vector", ["Top-5 hits on 26: 21 vs 24", "— too few to conclude"]),
            ("Build v1", "Prototype + baseline", ["8 questions: 5/8 for all three;", "no success claimed, diagnose"]),
            ("Explore", "Eval v2: a new lens", ["90 support-scope labels;", "the v1 result is kept as is"]),
            ("Build", "PR #4 – #18", ["local LLM, cited sentences,", "pgvector, generic PDF"]),
            ("Accept", "243 held-out questions", ["Hybrid 87.2%, +5.3 pp vs BM25", "(95% CI +1.7 to +9.0)"]),
            ("Review", "Manual sample of 20", ["Reasoning correct 20/20;", "citations fully support 18/20"]),
        ],
        "zh-TW": [
            ("起始", "描述困擾", ["看到題目不會選，", "用 Ctrl+F 逐頁查教材"]),
            ("探索一", "50 題找依據", ["教材有依據 26 題、找不到 24 題", "（AI 代填，標明未複核）"]),
            ("探索二", "關鍵字 vs 向量", ["26 題前 5 命中 21 vs 24：", "樣本太小，不下結論"]),
            ("實作 v1", "檢索原型 + 8 題基準", ["三種檢索各 5/8：", "不宣稱成功，先診斷未命中"]),
            ("探索", "評估 v2：換評估視角", ["支持範圍標註 90 筆，", "原 v1 結果保留不改"]),
            ("實作", "PR #4 – #18", ["本機 LLM、逐句引用、", "pgvector、通用 PDF"]),
            ("驗收", "保留題 243 題", ["混合 87.2%，比 BM25 +5.3 pp", "（95% CI +1.7 ~ +9.0）"]),
            ("審查", "人工抽樣 20 題", ["理由正確 20/20、", "引用完全支持 18/20"]),
        ]},
    "case_loop": {"en": "not good enough → explore", "zh-TW": "結果不夠 → 回到探索"},
    "case_foot1": {
        "en": "Numbers and caveats: docs/about/case-study-ipas.md; sources are pinned to an ipas-learning-hub commit.",
        "zh-TW": "所有數字與判讀限制見 docs/about/case-study-ipas.md；原始紀錄在 ipas-learning-hub 的固定 commit。"},
    "case_foot2": {
        "en": "One solo developer working with AI; it does not show that the method works for teams or other domains.",
        "zh-TW": "這是單人＋AI 的一個案例，不代表多人團隊或其他領域已驗證。"},
}


def tr(lang: str):
    return lambda key: TEXT[key][lang]


# ---------------------------------------------------------------- diagrams

def method_loop(theme: str, lang: str) -> str:
    T = tr(lang)
    s = Svg(1150, 530, theme, T("method_title"), T("method_sub"))
    colors = ["gray", "blue", "blue", "blue", "blue", "blue", "green"]
    stages = T("stages")
    w, gap, x0, y, h = 136, 22, 33, 200, 72
    cx = [x0 + w / 2 + i * (w + gap) for i in range(len(stages))]
    for i, ((name, sub), col) in enumerate(zip(stages, colors)):
        s.box(x0 + i * (w + gap), y, w, h, name, [sub], col, title_size=14)
    for i in range(len(stages) - 1):
        s.arrow([(x0 + i * (w + gap) + w, y + h / 2), (x0 + (i + 1) * (w + gap) - 2, y + h / 2)])

    # Explore sits under Define / Choose
    ex, ey, ew, eh = 258, 380, 160, 72
    s.box(ex, ey, ew, eh, T("explore")[0], [T("explore")[1]], "purple")
    s.arrow([(285, y + h), (285, ey - 2)], "purple")
    s.arrow([(305, ey), (305, y + h + 2)], "purple")
    s.text(277, 330, T("def_explore"), 12, color=s.color("purple")[0], anchor="end")
    s.arrow([(375, ey), (375, y + h + 2)], "purple")
    s.arrow([(395, y + h), (395, ey - 2)], "amber", dashed=True)
    s.text(404, 322, T("enough"), 12, color=s.color("purple")[0])
    s.text(404, 342, T("not_enough"), 12, color=s.color("amber")[0])
    s.arrow([(cx[3], y + h), (cx[3], 416), (ex + ew + 2, 416)], "amber", dashed=True,
            label=T("untested"), label_at=(cx[3] - 78, 411))

    # return paths above the row
    def back(src, dst, level, label):
        a, b = cx[src] - 10, cx[dst] + 10
        s.arrow([(a, y), (a, level), (b, level), (b, y - 2)], "amber", dashed=True,
                label=label, label_at=((a + b) / 2, level + 4))
    back(4, 3, 170, T("tests_fail"))
    back(5, 4, 170, T("fix"))
    s.arrow([(cx[5] + 10, y), (cx[5] + 10, 132), (cx[1] + 10, 132), (cx[1] + 10, y - 2)],
            "amber", dashed=True, label=T("wrong_req"), label_at=(575, 136))
    s.arrow([(cx[6], y), (cx[6], 100), (cx[1] - 10, 100), (cx[1] - 10, y - 2)],
            "green", dashed=True, label=T("new_goal"), label_at=(654, 104))

    # legend
    ly, lx = 494, 33
    s.arrow([(lx, ly), (lx + 40, ly)])
    s.text(lx + 48, ly + 4, T("forward"), 12, color=s.t["muted"])
    lx += 48 + round(text_width(T("forward"), 12)) + 24
    s.arrow([(lx, ly), (lx + 40, ly)], "amber", dashed=True)
    s.text(lx + 48, ly + 4, T("go_back"), 12, color=s.t["muted"])
    s.text(1117, ly + 4, T("method_ref"), 12, color=s.t["muted"], anchor="end")
    return s.render()


def framework_map(theme: str, lang: str) -> str:
    T = tr(lang)
    s = Svg(1150, 540, theme, T("map_title"), T("map_sub"))
    where = ["README · AGENTS.md · docs/workflow/guide.md", "docs/project/brief.md · progress.md",
             "docs/workflow/templates/", "docs/workflow/reference/", "tools/validate.py · tools/test_validate.py · .github/"]
    colors = ["blue", "green", "purple", "gray", "amber"]
    y0, bh, gap = 92, 70, 12
    for i, ((name, what), path, col) in enumerate(zip(T("layers"), where, colors)):
        y = y0 + i * (bh + gap)
        stroke, fill = s.color(col)
        s.parts.append(
            f'<rect x="28" y="{y}" width="1094" height="{bh}" rx="10" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="1.2" stroke-opacity="0.55"/>')
        s.box(40, y + 10, 170, bh - 20, name, (), col, title_size=15)
        lines = what.split("\n")
        s.text(234, y + (20 if len(lines) > 1 else 30), path, 14, 600, max_width=870)
        for j, line in enumerate(lines):
            s.text(234, y + (39 + j * 18 if len(lines) > 1 else 52), line, 13,
                   color=s.t["muted"], max_width=870)
    s.text(28, 518, T("map_foot"), 12, color=s.t["muted"])
    return s.render()


def status_axes(theme: str, lang: str) -> str:
    T = tr(lang)
    s = Svg(1150, 470, theme, T("axes_title"), T("axes_sub"))
    col_colors = ["blue", "purple", "amber", "green"]
    state_colors = [["gray", "amber", "green"], ["gray", "amber", "green"], ["gray", "red", "green"],
                    ["gray", "gray", "gray", "gray", "green"]]
    cw, gap, x0, top = 256, 20, 28, 92
    for i, ((name, q, states, note), col, scs) in enumerate(zip(T("axes"), col_colors, state_colors)):
        x = x0 + i * (cw + gap)
        stroke, fill = s.color(col)
        s.parts.append(
            f'<rect x="{x}" y="{top}" width="{cw}" height="330" rx="12" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="1.5"/>')
        s.text(x + cw / 2, top + 32, name, 16, 700, anchor="middle", max_width=cw - 20)
        s.text(x + cw / 2, top + 54, q, 12, color=s.t["muted"], anchor="middle", max_width=cw - 20)
        step = 44 if len(states) > 3 else 64
        py = top + 76
        for j, (st, sc) in enumerate(zip(states, scs)):
            pw = 160
            s.pill(x + (cw - pw) / 2, py, st, sc, size=13, min_width=pw)
            if j < len(states) - 1:
                s.arrow([(x + cw / 2, py + 26), (x + cw / 2, py + step - 2)], col)
            py += step
        s.text(x + cw / 2, top + 314, note, 12, color=stroke, anchor="middle", max_width=cw - 20)
    s.text(28, 448, T("axes_foot"), 12, color=s.t["muted"])
    return s.render()


def case_ipas(theme: str, lang: str) -> str:
    T = tr(lang)
    s = Svg(1150, 560, theme, T("case_title"), T("case_sub"))
    colors = ["gray", "purple", "purple", "blue", "purple", "blue", "green", "green"]
    w, h, gap, x0 = 248, 116, 34, 28
    rows_y = [100, 330]
    pos = []
    for i, ((tag, title, lines), col) in enumerate(zip(T("case_nodes"), colors)):
        r, c = divmod(i, 4)
        if r == 1:
            c = 3 - c  # snake: second row runs right-to-left
        x, y = x0 + c * (w + gap), rows_y[r]
        pos.append((x, y))
        s.box(x, y, w, h, title, lines, col, title_size=15, line_size=12.5, tag=tag)
    for i in range(len(pos) - 1):
        (x1, y1), (x2, y2) = pos[i], pos[i + 1]
        if y1 == y2:
            if x2 > x1:
                s.arrow([(x1 + w, y1 + h / 2), (x2 - 2, y2 + h / 2)])
            else:
                s.arrow([(x1, y1 + h / 2), (x2 + w + 2, y2 + h / 2)])
        else:
            s.arrow([(x1 + w / 2, y1 + h), (x2 + w / 2, y2 - 2)])
    s.text(x0 + 3 * (w + gap) + w / 2 - 12, 278, T("case_loop"), 12, color=s.color("amber")[0],
           anchor="end")
    s.text(28, 492, T("case_foot1"), 12, color=s.t["muted"])
    s.text(28, 514, T("case_foot2"), 12, color=s.t["muted"])
    return s.render()


DIAGRAMS = {
    "method-loop": method_loop,
    "framework-map": framework_map,
    "status-axes": status_axes,
    "case-ipas": case_ipas,
}


def expected() -> dict[Path, str]:
    return {OUT_DIR / f"{name}-{lang}-{theme}.svg": fn(theme, lang)
            for name, fn in DIAGRAMS.items() for lang in LANGS for theme in THEMES}


def orphans(files: dict[Path, str]) -> list[Path]:
    return [p for p in OUT_DIR.glob("*.svg") if p not in files] if OUT_DIR.exists() else []


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if any SVG is missing, stale or orphaned")
    args = ap.parse_args(argv)
    files = expected()
    extra = orphans(files)
    if args.check:
        stale = [p for p, svg in files.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != svg]
        for p in stale:
            print(f"stale diagram: {p.relative_to(ROOT).as_posix()}")
        for p in extra:
            print(f"orphan diagram: {p.relative_to(ROOT).as_posix()}")
        return 1 if stale or extra else 0
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for p in extra:
        p.unlink()
        print(f"removed {p.relative_to(ROOT).as_posix()}")
    for p, svg in files.items():
        p.write_text(svg, encoding="utf-8", newline="\n")
        print(f"wrote {p.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
