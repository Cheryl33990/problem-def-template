---
title: 追溯矩陣（Traceability Matrix）
status: draft
updated: 2026-11-16
tags: [meta, traceability]
# related: [PRD, acceptance] 
---

# 追溯矩陣（Traceability Matrix）

> **範本庫文件**：需要時才複製到專案紀錄區。本檔連結供瀏覽範本；複製後須改為實際專案文件，未建立的依賴標待建立或連到 brief。做法見 [使用指南](../../guide.md)。

本文件把跨資料夾的工件**串成一條線**——從問題到驗證，每一條成功指標都能被追溯到實作與測試。

> 沒有這張表，各資料夾是孤島；有了這張表，砍掉一個東西、加一個東西，都能立刻看到牽動到哪。

---

## 1. 主表：PRD 成功指標 → 全鏈追溯

| PRD 指標 # | 指標摘要 | AC ID | 對應 ADR | 對應方法 | 對應 EXP | 對應實作模組 | 對應驗收測試 | 狀態 |
|---|---|---|---|---|---|---|---|---|
| 1 | <!-- 摘要 --> | <!-- AC-01 --> | <!-- ADR-NNN --> | <!-- approach 內方法名 --> | <!-- EXP-NNN --> | <!-- src/X --> | <!-- docs/project/testing/acceptance_tests/AC-01.md --> | <!-- spec / impl / passing --> |
| 2 | <!-- TODO --> | <!-- AC-02 --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |
| 3 | <!-- TODO --> | <!-- AC-03 --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

<!-- TODO: 此表每加一條 PRD 指標或一條 ADR 就要更新
     原則：
       - 任何一欄空白都是「斷鏈」——表示這條指標還沒有對應的實作或驗證
       - 結案時適用欄位都應有對應；ADR、EXP、實作不適用時填 N/A 並說明理由，且狀態為 passing
     完成後將 status 從 draft 改為 in-review -->

---

## 2. 反向索引：ADR → 影響範圍

| ADR | 標題 | 影響的 PRD 指標 | 影響的設計模組 | 影響的測試 |
|---|---|---|---|---|
| <!-- ADR-001 --> | <!-- TODO --> | <!-- 1, 2 --> | <!-- docs/project/design/schema/X --> | <!-- TODO --> |
| <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

> 用途：當某個 ADR 要被取代或修改時，本表能立刻指出「會牽動到什麼」。

---

## 3. 反向索引：EXP → 結論影響

| EXP | 標題 | 驗證的假設 | 結論 | 影響的 ADR / PRD |
|---|---|---|---|---|
| <!-- EXP-001 --> | <!-- TODO --> | <!-- TODO --> | <!-- 證實 / 推翻 / 部分 --> | <!-- ADR-NNN / PRD §X --> |
| <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

> 用途：實驗結論對後續決策的影響應在此體現。若結論支持維持現況，記錄無需變動的理由即可。

---

## 4. 維護規則

- **何時更新**：
  - 新增 / 修改 PRD §4 成功指標 → 更新主表
  - 新增 / 修改 ADR → 更新 §1 與 §2
  - 新增 / 結束 EXP → 更新 §3
  - 新增 acceptance test → 更新主表狀態欄
- **檢查時機**：
  - 每次 PR 合入大改動時，作者應確認本表一致
  - 結案前（docs/project/closure/done_checklist.md §9）強制檢查
- **斷鏈處理**：
  - 主表有任何空白欄位都是「斷鏈警示」
  - 斷鏈可接受的情境：指標尚未開工、ADR 仍 in-review；不可接受的情境：已宣告完成但仍斷鏈

## 5. 與其他文件的關係

- **`PRD.md` §4** — 主表第一欄的來源
- **`docs/project/decisions/`** — 主表的「對應 ADR」欄與 §2 的來源
- **`docs/project/experiments/`** — §3 的來源
- **`docs/project/testing/acceptance_tests/`** — 主表狀態欄的來源
- **`docs/project/closure/done_checklist.md` §9** — 結案前強制檢查本表


## 6. 當次驗證證據

每條 AC 連結測試規格與 [validation](../../guide.md) 的實際結果；同一測試可覆蓋多個 AC，仍須逐條判定。記錄版本與日期，未跑就填未跑，不能僅憑過去 passing 判斷目前版本。

| AC ID | 測試規格 | 當次結果／版本 | 判定／限制 |
|---|---|---|---|
| AC-01 | 待填 | 待填 | 未跑 |
