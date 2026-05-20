---
title: Claude Code 專案規則
status: approved
updated: 2026-05-20
owner: jenny890808
tags: [meta, ai-collaboration]
---

# CLAUDE.md — 給未來 Claude Code session 看的專案規則

## 0. 專案目標（一句話）

> 從 PDF 鋼筋圖紙自動讀取結構配筋資訊的系統。

## 1. 重要慣例

### 1.1 檔名規則
- 階段資料夾以 `NN_kebab-name/` 命名，編號代表 SOP 階段（10→20→30→…）。
- 文件採 `snake_case.md`；探索筆記前綴 `NN_` 表示閱讀順序。
- ADR 採 `ADR-NNN-short-title.md`；實驗採 `EXP-NNN-short-title/`。

### 1.2 文件格式
- 所有 `.md` 開頭都要有 YAML frontmatter，欄位定義見 [99_meta/conventions.md](99_meta/conventions.md)。
- 完成 / 變更時更新 `status` 與 `updated`；不要靜默修改已封存文件。

### 1.3 術語表位置
- 統一見 [99_meta/glossary.md](99_meta/glossary.md)；新術語先寫進 glossary 再被引用。

## 2. 動手前必讀清單

在開始任何實作或設計變更前，請依序閱讀：

1. [10_problem/PRD.md](10_problem/PRD.md) — 目前的問題定義與成功指標
2. [30_decisions/](30_decisions/) 內**最新且 status 為 approved** 的 ADR
3. [40_design/tech_spec.md](40_design/tech_spec.md) — 當前的技術設計
4. [99_meta/conventions.md](99_meta/conventions.md) — 慣例與 frontmatter 規範
5. [99_meta/glossary.md](99_meta/glossary.md) — 術語表

## 3. 禁止事項

- ❌ **不要直接改 `30_decisions/` 內已封存（status: approved / archived）的 ADR**。
  - 要修正請新增一份 ADR，將舊 ADR 的 status 改為 `deprecated`，並用 `related` 互相連結。
- ❌ **不要動 `00_reference/` 內的既有資料夾**（這些是原始案件 PDF，唯讀）。
  - 只能讀取、不可改名、不可移動。
- ❌ **不要繞過 frontmatter**。新增任何 `.md` 都必須有完整 frontmatter。
- ❌ **不要把 `00_reference/` 加進 git**（已在 `.gitignore`）。
- ❌ **不要從 memory 引入未在當前對話討論過的概念**。memory 是輔助、不是事實來源。
- ❌ **不要刪除 TODO 註解**，除非該 TODO 對應的內容真的已完成。

## 4. 工作流程提醒

- 動手前先列計畫，等使用者確認再執行。
- 多步任務用 TodoWrite 追蹤進度。
- 變更檔案後更新該檔案的 `updated:` 欄位為今日日期。
- 任何 prompt 嘗試與結果記錄到 [99_meta/prompt_log.md](99_meta/prompt_log.md)。
