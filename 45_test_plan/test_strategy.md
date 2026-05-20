---
title: 測試策略
status: draft
updated: 2026-05-20
tags: [test, strategy]
# related: [acceptance, tech_spec]
---

# 測試策略

本文件規範本專案的**測試金字塔、覆蓋目標、工具選擇**。

---

## 1. 測試金字塔

本專案採以下分層（依需求調整）：

| 層級 | 測什麼 | 數量級 | 跑頻率 |
|---|---|---|---|
| Unit | 單一函式 / 類別的邏輯 | 多（每個函式 1+） | 每次 commit |
| Integration | 多模組組裝後的行為 | 中（每條 pipeline 1+） | 每次 PR |
| Acceptance / E2E | 端到端的驗收條件 | 少（對應 PRD §4 每條指標） | 釋出前 |

<!-- TODO: 此處依本專案實際情境調整層級
     原則：
       - 層越上、執行越慢，數量應該越少（典型 7:2:1 比例）
       - 若是研究型專案，可加「資料驗證測試」一層
     完成後將 status 從 draft 改為 in-review -->

---

## 2. 覆蓋目標

<!-- TODO: 此處設定具體覆蓋指標
     原則：
       - 不追求 100%，追求「關鍵路徑必覆蓋」
       - 行覆蓋率（line coverage）不是唯一指標，分支覆蓋率（branch coverage）更重要
     範例：
       - 核心邏輯模組（src/core/）行覆蓋率 ≥ 90%
       - 工具函式（src/utils/）行覆蓋率 ≥ 70%
       - I/O 邊界（讀寫檔、外部 API）100% 走 integration test -->

| 模組 | 行覆蓋率目標 | 分支覆蓋率目標 | 備註 |
|---|---|---|---|
| <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

---

## 3. 工具與環境

<!-- TODO: 此處列實際使用的測試工具與環境
     需涵蓋：
       - 測試框架（如 pytest）
       - 斷言庫
       - mock / stub 工具
       - 覆蓋率工具（如 coverage.py）
       - CI 跑測試的指令
     參考 50_implementation/README.md 的快速開始 -->

| 工具 | 用途 | 指令 |
|---|---|---|
| <!-- 例：pytest --> | <!-- 跑單元與整合測試 --> | <!-- pytest 50_implementation/tests --> |
| <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

---

## 4. 成功指標 ↔ 測試層級對應

> 每條 PRD §4 成功指標應對應到「至少一個層級」的測試。本表確保沒有指標被遺漏。

<!-- TODO: 此處從 acceptance.md §2 對應表展開
     原則：每條指標都要說「在哪一層測」與「為什麼是這層」 -->

| PRD 指標 # | 主要測試層級 | 為何是這層 | 對應檔案 |
|---|---|---|---|
| 1 | <!-- 例：Acceptance --> | <!-- 例：是端到端的正確率，必須走完整 pipeline --> | <!-- acceptance_tests/test_*.py --> |
| 2 | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |
| 3 | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

---

## 5. 不測什麼（Anti-coverage）

<!-- TODO: 此處明確列「不打算測」的部分與原因
     原則：
       - 第三方套件不重複測（信任套件本身的測試）
       - 純展示層（如純 print）通常不測
       - 一次性腳本不測
     注意：每條都要有理由，避免變成「懶得測」的擋箭牌 -->

---

## 6. 測試的失敗處理

<!-- TODO: 此處說明測試失敗時的標準流程
     建議內容：
       - 不允許 commit 跑紅測試（除非標註 expected failure 並有 issue）
       - flaky test 的處理（重跑 N 次仍紅就降為 quarantine）
       - 何時可以刪除 / 跳過測試（必須有 PR 與 reviewer 同意） -->
