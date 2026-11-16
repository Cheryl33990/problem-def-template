---
title: docs/project/design/schema 資料結構
status: draft
updated: 2026-11-16
tags: [design, schema]
---

# docs/project/design/schema/ 

> **範本庫文件**：需要時才複製到專案紀錄區。本檔連結供瀏覽範本；複製後須改為實際專案文件，未建立的依賴標待建立或連到 brief。做法見 [使用指南](../../../guide.md)。

本資料夾收錄**資料結構定義**——本系統處理的領域物件的 schema。

## 角色定位

- **契約**：schema 是各模組間的契約；變動需要走 ADR。
- **單一事實來源**：實作、prompts、文件中描述的欄位都必須以本處的 schema 為準。

## 內容

<!-- TODO: 此處列出本資料夾將有的 schema 檔案
     建議檔名規則：
       - <object>.schema.json（每個核心領域物件一份）
       - <container>.schema.json（容器 / 上層集合）
     參考 docs/project/discovery/ 內對核心領域物件的分析
     完成後將 status 從 draft 改為 in-review -->

## 維護規則

<!-- TODO: 此處填 schema 維護規則
     建議涵蓋：
       - 新增欄位 / 改型 / 刪欄位 各自需要什麼層級的審閱
       - 版本管理（schema 內是否有 version 欄位）
       - 向後相容性策略 -->
