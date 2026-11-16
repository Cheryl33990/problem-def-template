---
title: 30_decisions ADR
status: draft
updated: 2026-11-16
tags: [decisions, overview]
---

# 30_decisions/

本資料夾收錄 **Architecture Decision Records (ADR)**。SOP 的第三階段，每一個重要技術或產品決策都應在此留下紀錄。

## 內容

| 檔案 | 用途 |
|---|---|
| [TEMPLATE.md](TEMPLATE.md) | ADR 標準範本，新增 ADR 時複製此檔 |

## 命名與流程

- 檔名格式：`ADR-NNN-short-title.md`（NNN 為三位數流水號，從 001 開始）
- status 流轉：`draft` → `in-review` → `approved`；被新版取代時改為 `deprecated`
- **已 `approved` 或 `archived` 的 ADR 不可直接修改**；要更動請新增一份 ADR 並用 `related` 互相連結（見 [AGENTS.md §3](../AGENTS.md)）

## 何時新增 ADR

<!-- TODO: 此處填觸發新增 ADR 的時機
     建議涵蓋：
       - 技術路徑選擇（OCR / Vision LLM / 規則式）
       - 重大依賴的選用
       - 資料 schema 的重大變更
       - 跨資料夾流程的變動
     參考 [[20_discovery/03_tech_feasibility]] 完成後應產出第一份 ADR
     完成後將 status 從 draft 改為 in-review -->

## 列表（依編號）

<!-- TODO: 此處維護 ADR 一覽，新增 ADR 後更新此列表
     格式：
       - ADR-001 — <標題> — `approved`
       - ADR-002 — <標題> — `in-review` -->
