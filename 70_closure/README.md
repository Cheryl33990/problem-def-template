---
title: 70_closure 結案與復盤
status: draft
updated: 2026-11-16
tags: [closure, overview]
---

# 70_closure/

本資料夾收錄**結案與復盤**——SOP 的最後一階段，讓專案能「乾淨關閉」並留下可復盤的紀錄。

> 沒有這層，專案常常「自然消失」而非「完成」——下一個專案無法繼承經驗，做對的事和踩到的雷都會被忘記。

本輪適用範圍與未完成項目先對齊；復盤完成後才簽最終結案。

## 內容

| 檔案 | 用途 |
|---|---|
| [done_checklist.md](done_checklist.md) | Definition of Done 檢查清單，全勾才算完成 |
| [retrospective.md](retrospective.md) | 事後復盤：做對的、卡住的、假設驗證、下次想換的 |

## 何時進入本資料夾

只有當 [10_problem/acceptance.md](../10_problem/acceptance.md) §4「結案閘門」全部勾選後，
才開始填本資料夾。否則 retrospective 會變成「半路心得」而非「結案復盤」。

## 與其他資料夾的關係

- 上游：所有資料夾都會被本資料夾盤點（done_checklist 是整個 SOP 的最終檢查）
- 下游：給「下一個專案」或「下一階段」當作前車之鑑——可能直接催生新的 PRD

## 寫作原則

<!-- TODO: 此處填本資料夾的寫作慣例
     建議內容：
       - 復盤要在記憶還新時寫（最終簽署前）
       - 誠實記錄失誤；目的是讓下一個專案少踩雷，不是究責
       - 對未來決策有用的洞察應抽出來進 99_meta/ 或新 ADR
     完成後將 status 從 draft 改為 in-review -->

## 完成本資料夾後

- 確認本輪適用文件已審閱；未用範本與 N/A 不需升為 approved
- 在 CHANGELOG.md 加上「結案」條目
- 若這個專案的方法論值得沉澱，把可重用的部分抽到 template repo
