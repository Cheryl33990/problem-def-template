---
title: 99_meta
status: draft
updated: 2026-05-20
tags: [meta, overview]
---

# 99_meta/

本資料夾收錄**跨階段共用**的後設資訊：慣例、術語、prompt 歷史。

## 內容

| 檔案 | 用途 |
|---|---|
| [conventions.md](conventions.md) | 專案慣例（命名、frontmatter、文件結構） |
| [glossary.md](glossary.md) | 術語表 |
| [prompt_log.md](prompt_log.md) | Prompt 歷史日誌（給人與 AI 復盤用） |
| [traceability.md](traceability.md) | 追溯矩陣：PRD 指標 → ADR → EXP → 實作 → 驗收測試 |
| [skill_registry.md](skill_registry.md) | Skill / agent 對照表：SOP 階段 ↔ 環境中可用的外部 skill |
| [slot_contracts.md](slot_contracts.md) | 各 SOP 文件的填補契約集中索引（任何 skill 產出都依此驗收） |

## 角色定位

- 本資料夾是「跨階段一致性的守門人」。其他資料夾的內容如有衝突，以本處為準（特別是 conventions 與 glossary）。

## 維護規則

<!-- TODO: 此處填本資料夾的維護規則
     建議涵蓋：
       - conventions 變更需經過審閱（影響全專案）
       - glossary 新增條目的流程
       - prompt_log 的記錄時機（每次嘗試新 prompt 都應記下）
     完成後將 status 從 draft 改為 in-review -->
