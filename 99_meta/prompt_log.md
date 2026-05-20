---
title: Prompt 歷史日誌
status: draft
updated: 2026-05-20
tags: [meta, prompt-log]
---

# Prompt 歷史日誌

本檔記錄專案中所有「值得復盤的 prompt 嘗試」——含 Claude Code session、實驗中的模型 prompt、以及對人類的指示。
目的是讓未來的人或 AI 在類似情境下不必從零摸索。

## 記錄時機

<!-- TODO: 此處明確列出「什麼樣的 prompt 應該被記錄」
     建議：
       - 任何新嘗試的 prompt 結構（不論成功與否）
       - 失敗樣態與其推測原因
       - 對既有 prompt 的修改與結果
     不需要記錄：日常重複性、結果可預期的 prompt -->

---

## 記錄格式

每筆紀錄使用以下三段：

```
### YYYY-MM-DD — <一句話標題>

**情境**：…
**Prompt 重點**：…
**結果 / 觀察**：…
**對之後的啟示**：…
**關聯**：[[EXP-NNN]] / [[ADR-NNN]] / 對應的檔案
```

---

## 紀錄

<!-- TODO: 此處依時序新增紀錄。最新的放最上方。
     完成首筆紀錄後將 status 從 draft 改為 in-review。 -->

### 2026-05-20 — 專案骨架建立

**情境**：第一次與 Claude Code 協作建立 REBAR_READER 專案的文件骨架。
**Prompt 重點**：使用「問題定義 → 探索 → 決策 → 設計 → 實作」的 SOP；要求「人機皆好復盤、未來容易維護回溯」；明確區分完整寫 / 骨架寫 / 空檔三層。
**結果 / 觀察**：建立了 11 個資料夾與本套文件骨架；frontmatter 規範統一為必填三欄 + 選填三欄。
**對之後的啟示**：「動手前先列計畫等使用者確認」這個迴圈值得保留；TODO 註解明確化（要填什麼 / 參考哪裡 / 完成後改 status）對日後接手非常有幫助。
**關聯**：[CLAUDE.md](../CLAUDE.md)、[99_meta/conventions.md](conventions.md)
