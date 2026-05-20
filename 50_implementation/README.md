---
title: 50_implementation 實作
status: draft
updated: 2026-05-20
tags: [implementation, overview]
---

# 50_implementation/

本資料夾收錄**實作**——程式碼、測試、依賴與環境設定。SOP 的第五階段。

## 內容

| 路徑 | 用途 |
|---|---|
| [src/](src/) | 主要程式碼 |
| [tests/](tests/) | 自動化測試 |
| [requirements.txt](requirements.txt) | Python 依賴 |
| [.env.example](.env.example) | 環境變數範例（實際 `.env` 不進版控） |

## 規則

- 實作必須對齊 [40_design/](../40_design/) 的設計；設計與實作有歧異時，先更新設計（或新增 ADR）再改實作。
- 對 schema 的引用以 [40_design/schema/](../40_design/schema/) 為單一事實來源，不要在 src/ 內重新定義。

## 快速開始

<!-- TODO: 此處填本地開發的快速開始步驟
     需涵蓋：
       - Python 版本需求
       - 建立虛擬環境的指令
       - 安裝依賴
       - 設定 .env
       - 跑測試
       - 跑最小範例
     參考 ../README.md 的「快速開始」段
     完成後將 status 從 draft 改為 in-review -->
