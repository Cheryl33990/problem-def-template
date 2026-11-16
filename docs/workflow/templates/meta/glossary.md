---
title: 術語表
status: draft
updated: 2026-11-16
tags: [meta, glossary]
---

# 術語表 

> **範本庫文件**：需要時才複製到專案紀錄區。本檔連結供瀏覽範本；複製後須改為實際專案文件，未建立的依賴標待建立或連到 brief。做法見 [使用指南](../../guide.md)。

本表收錄本專案使用的**領域術語**與**專案術語**。新增任何文件時若引入新術語，先在此處登錄再被引用。

## 使用規則

- 文件內首次出現某術語時，使用「中文（English / 縮寫）」格式。
- 縮寫的展開以本表為準。
- 若某術語有多種譯名，本表訂出「採用譯名」與「不採用譯名」。

---

## 1. 領域術語

<!-- TODO: 此處依本專案所處的領域填入專有名詞。
     原則：
       - 只列「會在文件中出現且需要對齊定義」的詞
       - 每個詞給「中文 / 英文 / 一句話定義」三欄
       - 模糊或有爭議的譯名放到 §4 待釐清
     參考：docs/project/discovery/ 內各筆記分析時遇到的詞彙 -->

| 術語 | 英文 | 定義 | 備註 |
|---|---|---|---|
| `<領域術語 1>` | `<EN>` | `<一句話定義>` | |

## 2. 專案術語

<!-- TODO: 此處填本系統自己定義的概念（模組名、階段名、輸出格式名）。
     原則：所有專案內部命名都應登錄於此，避免同一概念被多個名字稱呼。
     參考：docs/project/design/tech_spec.md 對齊系統元件名 -->

| 術語 | 定義 | 備註 |
|---|---|---|
| `<模組名 / 階段名>` | `<一句話定義>` | |
| 非目標（Non-Goals） | 本專案明確「不做」的事，分為範圍外 / 延後 / 明確拒絕 / 責任邊界四類 | 見 docs/project/problem/non_goals.md |
| 驗收條件（Acceptance Criteria） | PRD 成功指標的可驗證二元條件（達 / 未達） | 見 docs/project/problem/acceptance.md |
| 測試金字塔（Test Pyramid） | 將測試依「單元 → 整合 → 端對端」分層，數量由下而上遞減的策略 | 見 docs/project/testing/test_strategy.md |
| 追溯矩陣（Traceability Matrix） | 把 PRD 指標 → ADR → EXP → 實作 → 驗收測試 串成可追溯的一張表 | 見 docs/project/meta/traceability.md |

## 3. 縮寫

| 縮寫 | 全寫 | 中文 | 備註 |
|---|---|---|---|
| ADR | Architecture Decision Record | 架構決策紀錄 | 用於 docs/project/decisions/ |
| PRD | Product Requirements Document | 產品需求文件 | 見 docs/project/problem/PRD.md |
| EXP | Experiment | 實驗 | 用於 docs/project/experiments/ |
| DoD | Definition of Done | 完成定義 | 見 docs/project/problem/acceptance.md |
| TDD | Test-Driven Development | 測試驅動開發 | 對應 docs/project/testing/ 與 tests/ |
<!-- TODO: 後續新增的縮寫補在此處 -->

## 4. 待釐清

<!-- TODO: 此處列尚未有共識的術語與待解的命名爭議
     格式：
       - <候選名> vs <候選名> — 用於 xxx，待 ADR-NNN 決定 -->
