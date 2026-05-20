---
title: 40_design 技術設計
status: draft
updated: 2026-05-20
tags: [design, overview]
---

# 40_design/

本資料夾收錄**技術設計**階段的文件。SOP 的第四階段，把 ADR 中的決策具體化為可實作的設計。

## 內容

| 檔案 / 資料夾 | 用途 |
|---|---|
| [tech_spec.md](tech_spec.md) | 整體技術規格：架構圖、模組劃分、資料流 |
| [schema/](schema/) | 資料結構定義（領域物件的 schema） |
| [pipeline/](pipeline/) | 處理管線設計（輸入 → 結構化資料的各階段） |
| [prompts/](prompts/) | 生產用 prompt 的最終版（與 60_experiments/ 內探索性 prompt 區分） |

## 設計原則

<!-- TODO: 此處填本資料夾的設計原則
     建議涵蓋：
       - 設計變更應由 ADR 觸發，不應直接動 tech_spec.md
       - schema 為設計的「契約」，變動要慎重
       - prompts/ 內為已 freeze 的生產 prompt；實驗中的版本留在 60_experiments/
     完成後將 status 從 draft 改為 in-review -->
