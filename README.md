---
title: problem-def-template
status: in-review
updated: 2026-11-16
---

# problem-def-template

繁體中文的問題解析與探索模板：留下問題、證據、方案選擇、假設驗證與結果，讓自己或下一個協作者能接手。

**目前是文件模板，尚未完成真實案例可用性驗證。** 不需要安裝 Python 或啟動服務。

## 開始使用

**只要能描述困擾或期待就能開始。** AI 會協助釐清問題、範圍與成功條件；不知道時可先探索。使用者不必預先寫完整 PRD 或數字門檻。見 [WORKFLOW](WORKFLOW.md) 的模糊目標流程。


先看 [START_HERE.md](START_HERE.md)，用精簡流程處理一個問題；需要完整專案結構時再看 [USAGE.md](USAGE.md)。GitHub 衍生入口若未提供「Use this template」，可先複製檔案到新 repo；本文件不假設模板設定已啟用。

[合成示例](examples/meeting-notes.md)展示填寫方式，[PILOT.md](PILOT.md)定義真實試跑與紀錄方式。

完整操作：[USAGE](USAGE.md)；流程與階段條件：[WORKFLOW](WORKFLOW.md)；審查與合併：[REVIEW](REVIEW.md)。

本模板提供文件與 PR 填寫格式；尚未提供自動測試、CI、部署或自動驗收。工具需由衍生專案另外設定。

## 目錄

| 位置 | 用途 |
|---|---|
| 10_problem | PRD、角色、範圍、AC 驗收條件 |
| 20_discovery | 探索問題、方法、證據與影響 |
| 25_approach | 候選方案與比較 |
| 30_decisions | 重大決策 ADR |
| 40_design | 技術設計、介面與 prompt |
| 45_test_plan | AC 測試規格與驗證方式 |
| 50_implementation | 選用的程式與測試骨架，目前無可執行系統 |
| 60_experiments | 隨時穿插的假設驗證 |
| 70_closure | 完成清單與復盤 |
| 99_meta | 慣例、工具候選、契約、資料盤點與追溯 |

編號是分類，探索、PRD 與實驗會反覆修訂。不適用欄位填 N/A 與理由，不必為填滿文件創造工作。

## 維護入口

- [文件契約](99_meta/slot_contracts.md)、[慣例](99_meta/conventions.md)、[AI 工作規則](AGENTS.md)。
- [改善進度](IMPROVEMENT_PLAN.md)、[變更紀錄](CHANGELOG.md)。
- 本 repo 維護模板；衍生後依自己的問題改寫 PRD 與 AI 專案目標。
