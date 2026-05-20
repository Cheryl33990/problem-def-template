---
title: REBAR_READER
status: draft
updated: 2026-05-20
---

# REBAR_READER

PDF 鋼筋圖紙自動讀取系統。

---

## 專案目標

從結構工程 PDF 圖紙中自動辨識並抽取鋼筋配筋資訊，產出可被下游工程作業使用的結構化資料。

> 詳細需求與成功指標見 [10_problem/PRD.md](10_problem/PRD.md)。

---

## 目錄導覽

本專案依「問題定義 → 探索 → 決策 → 設計 → 實作」的 SOP 編排：

| 目錄 | 用途 |
|---|---|
| [00_reference/](00_reference/) | 原始 PDF 案件參考資料（不進版控） |
| [10_problem/](10_problem/) | 問題定義：PRD、stakeholders |
| [20_discovery/](20_discovery/) | 探索筆記：PDF 樣態、技術可行性、資料模型 |
| [30_decisions/](30_decisions/) | ADR（Architecture Decision Records） |
| [40_design/](40_design/) | 技術設計：tech_spec、schema、pipeline、prompts |
| [50_implementation/](50_implementation/) | 實作：src、tests、依賴與環境 |
| [60_experiments/](60_experiments/) | 實驗紀錄：每個實驗一個資料夾 |
| [99_meta/](99_meta/) | 慣例、術語、prompt log |

> 文件慣例與 frontmatter 格式見 [99_meta/conventions.md](99_meta/conventions.md)。
> 給 AI session 的工作規則見 [CLAUDE.md](CLAUDE.md)。

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
