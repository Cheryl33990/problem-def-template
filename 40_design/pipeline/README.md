---
title: 40_design/pipeline 處理管線
status: draft
updated: 2026-05-20
tags: [design, pipeline]
---

# 40_design/pipeline/

本資料夾收錄**處理管線**設計——從輸入素材到結構化輸出之間，每個階段的職責、介面、與順序。

## 角色定位

- 描述「資料怎麼流」的層次；具體模組實作放在 [50_implementation/src/](../../50_implementation/src/)。
- 與 [40_design/schema/](../schema/) 的關係：pipeline 各階段的輸入輸出格式必須對齊 schema。

## 內容

<!-- TODO: 此處列出本資料夾將有的設計文件
     建議結構：
       - 00_overview.md — 整條管線的階段圖
       - 01_pre_processing.md — 輸入前處理（依領域定義：如格式轉換、切分、降噪）
       - 02_extraction.md — 抽取階段
       - 03_postprocess.md — 後處理（正規化、驗證）
     參考 [[../tech_spec]] §3 §4
     完成後將 status 從 draft 改為 in-review -->

## 設計原則

<!-- TODO: 此處填管線設計原則
     建議涵蓋：
       - 每一階段應可獨立測試（明確的輸入輸出）
       - 失敗 / 中斷時的中繼產物保留策略
       - 重跑 / 部分重跑的支援 -->
