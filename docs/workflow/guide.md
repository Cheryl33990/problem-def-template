---
title: 從一個問題開始使用模板
status: in-review
updated: 2026-11-16
---

# 從一個問題開始使用模板

本頁是唯一使用入口。你只需用自然語言描述困擾，AI 協助釐清問題、範圍與成功條件。未知就保留未知，沒有資料時先做小型探索。

## 1．建立或整合專案

**新 repo**：在 GitHub 有 Use this template 時，用它建立新 repo；沒有此入口也可複製檔案到新 repo。衍生專案是獨立副本，不會自動取得模板更新。
初始只需 README、AGENTS、docs/project 兩份紀錄與本工作指南。src、tests 是空位置標記，沒有 Python 或其他語言依賴；開始實作時依框架建立實際結構，非程式專案可移除。

**既有 repo**：在工作分支加入 docs/workflow，並按需要加入 docs/project。不要覆蓋既有 README、AGENTS、CI、ADR 或程式目錄；將需要的規則整合進原 AGENTS，於 progress 記路徑對照。已有同用途文件就沿用，不再建立副本。

**移除模板維護材料**：docs/template-maintenance 只記模板的歷史、盤點與試跑計畫，不是新專案的成果。新專案可移除整個目錄；同時把根 README 改成自己的介紹，刪掉模板維護入口。指南、規則和空白範本不依賴該目錄。教學 examples 可選擇保留，不是專案待辦。

## 2．先用兩份文件開始

- [brief](../project/brief.md)：使用者原話、事實與假設、範圍、成功條件和確認紀錄。
- [progress](../project/progress.md)：目前做什麼、實際路徑、阻礙與下一步。

AI 先利用已有資料回述情境，每輪問 1–3 個最關鍵問題，再提候選方向與取捨。你可以接受、修正或回答不知道。
定義標未知／暫定／已確認。沒有基準時先量測，不編造門檻；成功條件也可採明確人工判準。
正式實作採用已確認範圍與 AC。探索可只先確認疑問、操作／資料、時間資源邊界及完成條件，不要求先有產品 AC。

## 3．什麼時候才新增文件

[範本庫](templates/README.md)提供可複製材料，**不要在範本原檔填你的專案內容，也不要一次複製全部**。

| 真的遇到的需求 | 建議新增位置（尚未預建） | 使用範本 |
|---|---|---|
| brief 已太長或多角色協作 | docs/project/problem/ | templates/problem |
| 需要查資料或分析 | docs/project/discovery/ | templates/discovery |
| 需要比較候選方案 | docs/project/approach/ | templates/approach |
| 重大或難以回頭的選擇 | docs/project/decisions/ADR-NNN-title.md | templates/decisions |
| 已確認方案需要詳細介面／設計 | docs/project/design/ | templates/design |
| 可證偽假設需要實驗 | docs/project/experiments/EXP-NNN-title/ | templates/experiments |
| 測法或案例已超過 brief 可容納程度 | docs/project/testing/ | templates/testing |
| 要保存本次測試證據 | docs/project/validation/YYYY-MM-DD-title.md | templates/testing/validation |
| 準備結案，需完整檢查與復盤 | docs/project/closure/ | templates/closure |
| 多來源、多假設或追溯關係變複雜 | docs/project/meta/ | templates/meta |

小型任務的比較、判準、結果與復盤可直接放 brief／progress；不強制獨立建檔。
需要拆分時，將原段落改成摘要＋新文件連結。原本已確認的 AC 編號和證據關係保留。

## 4．複製範本後必做的整理

1. 只取本輪需要的檔案，放到上表目的位置；改成實際名稱，例如 ADR-001-storage.md 或 AC-01.md。
2. 將 frontmatter 改 draft，更新標題、日期與內容；未使用欄位可寫 N/A 與理由。
3. **重新定位連結**：範本庫的相對連結用來瀏覽範本，不會因複製自動變成專案連結。把 Markdown、正文及 YAML 中的路徑都改到真實文件；尚未建立的依賴寫待建立，或連到 brief 的對應段落。
4. 在 progress 登記實際主來源；檢查新文件每個連結能開啟，且指向專案證據而非空白範本。
5. 契約只檢查本輪適用內容，不要求所有範本 TODO 清空。未知與不適用分開記。

例如 AC 規格複製到 docs/project/testing/acceptance_tests/AC-01.md；實際驗證紀錄放 docs/project/validation，程式測試則放 tests。三者互相連結，但用途不同。

## 5．每天怎麼進行

讀 brief、progress 及本輪相關文件 → 選一個小目標 → 在工作分支探索或實作 → 保存證據 → 開 PR → review → 合併後更新下一步。
Issue 可追待辦，PR 保存具體變更；小任務不強制重複填兩份。
實作前先定測法；資料、工具、環境與當次版本記進結果。未跑或失敗要明寫。測試命令依實際語言與框架設定，本模板沒有預裝工具或 CI。

## 6．驗證、Review 與收尾

- 假設驗證：方法是否值得繼續？記探索／實驗結果。
- 測試：實作是否符合已定義行為？測成功、失敗與重要邊界。
- Review：讀實際 diff 與證據，找遺漏、錯誤與剩餘風險；詳見 [review](reference/review.md)。
- 驗收：本輪已確認的 AC 是否達成？文件 approved 不等於測試通過。
- 結案：保存未完成與接受風險，復盤後才簽署；合併不代表部署或整個專案完成。

每次結束更新 progress；不用等專案結案。對已接受需求或門檻的變更先說明影響並確認，不能事後改到「通過」。

## 7．給 AI 的起手指令

> 請先讀 AGENTS.md、docs/workflow/guide.md 與 docs/project 的 brief、progress。我目前的困擾是……，還不知道範圍與成功標準。請利用已有資料，用白話回述情境，每輪問少量關鍵問題，再提出有理由的候選範圍與成功條件。未知保持未知，資訊不足時先提限量探索。不預建所有階段文件，依需要從範本庫取用。已有明確授權的可逆工作持續完成，重大範圍變更提出供我確認。

接手時請 AI 先讀 progress 與相關證據；review 時要求依 reference/review.md 檢查實際 diff、被測版本與限制。

## 8．深入參考與版本更新

[workflow](reference/workflow.md)保存完整釐清流程及階段條件；[conventions](reference/conventions.md)定義文件狀態；[slot contracts](reference/slot_contracts.md)規範需要展開的文件內容。日常從本頁和兩份專案紀錄開始即可。
記下採用的模板 commit；之後用獨立 PR 挑選方法改進，不整包覆蓋既有專案紀錄或程式。此流程尚未通過真實案例可用性驗證。
