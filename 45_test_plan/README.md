---
title: 45_test_plan 測試規畫
status: draft
updated: 2026-11-16
tags: [test, overview]
---

# 45_test_plan/

本資料夾收錄**測試規畫**——在進入 `50_implementation/` 寫程式之前，
先把「要測什麼、怎麼測、用什麼資料測」想清楚。SOP 的第 4.5 階段。

> 本資料夾是 `10_problem/acceptance.md`（驗收條件）與 `50_implementation/tests/`（測試實作）之間的橋。
> 沒有這層，TDD 容易變成「想到什麼測什麼」。

## 內容

| 檔案 / 資料夾 | 用途 |
|---|---|
| [test_strategy.md](test_strategy.md) | 測試金字塔、覆蓋目標、工具選擇 |
| [fixtures.md](fixtures.md) | 測試資料來源、邊界 case、假資料與真實資料的使用界線 |
| [acceptance_tests/](acceptance_tests/) | 從 `10_problem/acceptance.md` 對應出來的具體測試清單 |

## 與其他資料夾的關係

- 上游：
  - `10_problem/acceptance.md` — 驗收條件（要測什麼的源頭）
  - `40_design/` — 系統設計（決定測試切點）
- 下游：
  - `50_implementation/tests/` — 真正的測試程式碼，依本資料夾的規畫實作

## 寫作原則

<!-- TODO: 此處填本資料夾的寫作慣例
     建議內容：
       - 先有 acceptance_tests/ 再有實作（test-first 的核心）
       - test_strategy.md 不要寫成書本理論，要對齊本專案實際需求
       - fixtures 要分「合成」與「真實」，不要混用
     完成後將 status 從 draft 改為 in-review -->

## 何時更新

- PRD 或 acceptance.md 變更 → acceptance_tests/ 必須跟著更新
- 新增 ADR 改變技術路徑 → test_strategy.md 可能需要調整
- 發現新的邊界 case → 寫進 fixtures.md（並補對應測試）


先用 [acceptance_tests/TEMPLATE.md](acceptance_tests/TEMPLATE.md) 定義測法，再用 [validation/](validation/README.md) 記實際執行結果；流程與工具選擇見 [test_strategy.md](test_strategy.md)。
