---
title: 40_design/schema 資料結構
status: draft
updated: 2026-05-20
tags: [design, schema]
---

# 40_design/schema/

本資料夾收錄**資料結構定義**——本系統處理的領域物件（梁、柱、配筋表等）的 schema。

## 角色定位

- **契約**：schema 是各模組間的契約；變動需要走 ADR。
- **單一事實來源**：實作、prompts、文件中描述的欄位都必須以本處的 schema 為準。

## 內容

<!-- TODO: 此處列出本資料夾將有的 schema 檔案
     建議檔名規則：
       - beam.schema.json（梁）
       - rebar.schema.json（鋼筋）
       - drawing.schema.json（圖紙層級）
     參考 [[../../20_discovery/04_data_model_study]] 對梁配筋的分析
     完成後將 status 從 draft 改為 in-review -->

## 維護規則

<!-- TODO: 此處填 schema 維護規則
     建議涵蓋：
       - 新增欄位 / 改型 / 刪欄位 各自需要什麼層級的審閱
       - 版本管理（schema 內是否有 version 欄位）
       - 向後相容性策略 -->
