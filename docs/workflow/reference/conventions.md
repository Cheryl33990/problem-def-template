---
title: 專案文件慣例
status: in-review
updated: 2026-11-16
---

# 專案文件慣例

## 文件與任務狀態

Markdown frontmatter 必填 title、status、updated（YYYY-MM-DD）；owner、tags、related 可選。GitHub 提供的設定格式若不支援 frontmatter，依平台格式，不硬塞 YAML。
文件狀態：draft 草擬／in-review 待審／approved 已採用／archived 封存／deprecated 被取代。狀態不是大小排序，不使用「≥ in-review」作判斷。
範本可保留 draft 與 TODO，說明文件可為 in-review；不要將未使用範本視為交付缺失。任務進度另見 work log，測試結果另見 validation。

## 命名與連結

專案紀錄按用途放 docs/project，按需建立，不使用根目錄數字階段；普通文件 snake_case.md，ADR-NNN-short-title.md，EXP-NNN-short-title/，驗收規格 AC-NN.md，驗證結果 YYYY-MM-DD-short-name.md。
文件互相使用相對連結；外部資料記版本、來源與存取條件。AC、ADR、EXP 編號不可重用；一個測試可涵蓋多條 AC，但規格須逐條可追溯。

## 內容與術語

PRD 定義問題，AC 定義完成標準，測試規格定義測法，validation 記實際結果。完整流程見 [WORKFLOW](workflow.md)；單份文件契約見 [slot_contracts](slot_contracts.md)。
新術語先在 brief 說明，需要獨立管理時才建立 glossary，首次出現說明縮寫。事實附來源，假設明確標示，不足證據寫未知。

## 變更管理

一般 approved 活文件可以修訂，更新日期並保留必要修訂記錄；修改 PRD 需求、指標或範圍時記觸發來源。
已接受 ADR 的決策正文不重寫；改決策新增 ADR，舊文件只更新 deprecated 與取代連結。歷史驗證結果不覆寫，重跑新增紀錄。
模板變更記 docs/template-maintenance/CHANGELOG.md；衍生專案維護自己的變更紀錄；尚未發布的版本放 Unreleased，不把 commit 或 PR 合併冒充正式發布。
衍生專案記模板來源 commit，後續透過獨立 PR 手動挑選改進；模板沒有自動同步機制。

## 裁剪與衝突

精簡模式可合併文件，但保留問題、AC、證據與決策鏈。N/A 填理由與確認人；適用但未做的工作標未完成。
流程以 WORKFLOW 為準、review 以 REVIEW 為準、內容以 slot_contracts 為準，guide 是操作入口。發現衝突先列出差異並修文件，不靜默挑有利條款。使用者已明確授權的範圍優先。
