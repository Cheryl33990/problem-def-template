---
title: 驗收測試索引
status: draft
updated: 2026-11-16
tags: [test, acceptance]
# related: [acceptance, test_strategy]
---

# 驗收測試索引

本資料夾的角色是「**從驗收條件對應到實際測試**」的索引。
真正的測試程式碼放在 [../../50_implementation/tests/](../../50_implementation/tests/) 的 acceptance 子目錄（實作時建立）（或對應位置），
本資料夾僅維護**對應關係**與**測試規格**（先於程式碼存在）。

> TDD 的精神：先在這裡寫「測什麼、預期什麼」（spec），再到 50_implementation/ 寫測試與程式。

---

## 1. 驗收條件 → 測試對應

| AC ID | 測試名稱 | 測試類型 | 對應檔案 | 狀態 |
|---|---|---|---|---|
| <!-- AC-01 --> | <!-- test_<name> --> | <!-- E2E --> | <!-- ../../50_implementation/tests/acceptance/test_*.py --> | <!-- spec / impl / passing --> |
| <!-- AC-02 --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

<!-- TODO: 完成上表後，將 status 從 draft 改為 in-review
     原則：每條 acceptance.md 的驗收條件至少要有一個對應測試 -->

## 2. 測試規格檔案

> 每條驗收條件各建一份規格，包含前置條件、步驟、期望結果、通過條件與驗證證據。人工驗證也適用。
> 命名：`AC-NN.md`

<!-- TODO: 規格檔案列表
     - AC-01.md
     - AC-02.md -->

## 3. 狀態定義

| 狀態 | 意義 |
|---|---|
| `spec` | 測試規格已寫，但程式碼尚未實作 |
| `impl` | 測試已實作但尚未跑通（紅燈或被 skip） |
| `passing` | 測試已通過 |
| `flaky` | 偶爾失敗，待調查 |

## 4. 寫作原則

<!-- TODO: 此處填本資料夾的寫作慣例
     建議內容：
       - 規格用「Given / When / Then」結構
       - 每條規格都要對應到 acceptance.md 內某條的編號
       - 避免在規格中寫實作細節（保留給程式碼）
     完成後將 status 從 draft 改為 in-review -->
