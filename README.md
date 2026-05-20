---
title: <PROJECT_NAME>
status: draft
updated: 2026-05-20
---

# `<PROJECT_NAME>`

> **這是從 [problem-def-template](https://github.com/Cheryl33990/problem-def-template) 衍生的專案。**
> 使用方式見 [USAGE.md](USAGE.md)；新建後請把本段與 `<PROJECT_NAME>` placeholder 換成你的專案名。

`<PROJECT_GOAL — 一句話描述本專案要解的問題>`

---

## 專案目標

<!-- TODO: 此處用 3-5 句話展開專案目標。
     需回答：要解什麼問題？目標使用者是誰？成功的樣子是什麼？
     詳細需求與成功指標見 [10_problem/PRD.md](10_problem/PRD.md)。
     完成後將 status 從 draft 改為 in-review -->

---

## 目錄導覽

本專案依「問題定義 → 探索 → 方法 → 決策 → 設計 → 測試規畫 → 實作 → 實驗 → 結案」的 SOP 編排：

| 目錄 | 用途 |
|---|---|
| [10_problem/](10_problem/) | 問題定義：PRD、stakeholders、non_goals、acceptance |
| [20_discovery/](20_discovery/) | 探索筆記：依本專案的問題定義展開 |
| [25_approach/](25_approach/) | 候選方法比較：options、tradeoffs |
| [30_decisions/](30_decisions/) | ADR（Architecture Decision Records） |
| [40_design/](40_design/) | 技術設計：tech_spec、schema、pipeline、prompts |
| [45_test_plan/](45_test_plan/) | 測試規畫：strategy、fixtures、acceptance_tests |
| [50_implementation/](50_implementation/) | 實作：src、tests、依賴與環境 |
| [60_experiments/](60_experiments/) | 實驗紀錄：每個實驗一個資料夾 |
| [70_closure/](70_closure/) | 結案與復盤：done_checklist、retrospective |
| [99_meta/](99_meta/) | 慣例、術語、prompt log、traceability |

> 文件慣例與 frontmatter 格式見 [99_meta/conventions.md](99_meta/conventions.md)。
> 給 AI session 的工作規則見 [CLAUDE.md](CLAUDE.md)。
> **第一次使用？** 看 [SOP_ROADMAP.html](SOP_ROADMAP.html) — 依熟悉度判斷該走哪條路徑、每條路徑前 1-2 週的具體動作。

---

## 快速開始

<!-- TODO: 此處待 50_implementation/ 有實際程式碼後補上
     需包含：環境需求（Python 版本）、安裝步驟、最小執行範例
     參考 50_implementation/README.md
     完成後將 status 從 draft 改為 in-review -->

```bash
# 安裝
# cd 50_implementation
# pip install -r requirements.txt

# 執行（範例）
# python -m src.main <input.pdf>
```

---

## 變更紀錄

見 [CHANGELOG.md](CHANGELOG.md)。
