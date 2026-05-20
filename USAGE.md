---
title: USAGE — 如何使用本 Template
status: approved
updated: 2026-05-20
tags: [meta, template-usage]
---

# 如何使用本 Template

本 repo 是一個 **GitHub Template**，提供「問題定義 → 探索 → 決策 → 設計 → 實作」SOP 的文件骨架。
適用於需要把研究、探索、決策過程留下可復盤紀錄的專案——不限於工程，也適合資料分析、產品探索、學術專案。

---

## 1. 衍生新專案

### 1.1 從 GitHub 衍生
在 GitHub 本 repo 頁面點 **「Use this template」 → 「Create a new repository」**，填入新 repo 名稱（建議公開度設為 Private 直到專案有具體成果）。

### 1.2 本機 clone
```bash
gh repo clone <YOUR_ORG>/<YOUR_PROJECT>
cd <YOUR_PROJECT>
```

---

## 2. 衍生後的初始化清單

按順序處理，每完成一項把該檔的 `status` 從 `draft` 改為 `in-review`（或 `approved`）。

### 2.1 替換 placeholder
全文搜尋並替換以下標記：
- `<PROJECT_NAME>` — 你的專案名（一兩個字的代號，例如 `rebar_reader`）
- `<PROJECT_GOAL>` — 一句話描述要解的問題

建議先用：
```bash
grep -rn "<PROJECT_NAME>" --include="*.md"
grep -rn "<PROJECT_GOAL>" --include="*.md"
```

### 2.2 更新門面三檔
- [README.md](README.md) — 改標題、把開頭「本 template 衍生」那段刪掉
- [CLAUDE.md](CLAUDE.md) — §0 專案目標一句話
- [CHANGELOG.md](CHANGELOG.md) — 加上你的 `## [0.1.0] - YYYY-MM-DD` 與初始 commit 摘要

### 2.3 填入問題定義
- [10_problem/PRD.md](10_problem/PRD.md) — 至少完成 §1 背景、§2 目標使用者、§4 成功指標
- [10_problem/stakeholders.md](10_problem/stakeholders.md) — 至少列出 3 個關鍵角色
- [10_problem/non_goals.md](10_problem/non_goals.md) — 列出範圍邊界（PRD §5 為摘要）
- [10_problem/acceptance.md](10_problem/acceptance.md) — 把 PRD §4 成功指標翻成可驗證條件

### 2.4 規劃探索筆記
進入 [20_discovery/](20_discovery/)：複製 `NN_template.md` 為 `01_<topic>.md`、`02_<topic>.md` 等，依本專案實際探索主題命名。同時更新 `20_discovery/README.md` 的內容表。

### 2.5 補上術語表
[99_meta/glossary.md](99_meta/glossary.md) — 把你領域的核心術語先放幾個進去，避免文件內名詞不一致。

### 2.6 完成本檔
本 USAGE.md 本身可以刪除（你不再需要使用說明），或保留作為新成員 onboarding。

---

## 3. 工作流程提醒（沿用 CLAUDE.md §4）

- 動手前先列計畫，與 stakeholder 確認再執行
- 多步任務用 task tracker 追蹤
- 變更檔案後更新 `updated:` 為今日日期
- ADR 採「新增不修改」原則：要改舊決策請新增一份 ADR、把舊 ADR 標 `deprecated`

---

## 4. 結構速查

```
10_problem/        問題定義（PRD、stakeholders、non_goals、acceptance）
20_discovery/      探索筆記（一份一個主題）
25_approach/       候選方法比較（options、tradeoffs）
30_decisions/      ADR
40_design/         技術設計（tech_spec + schema/pipeline/prompts 子目錄）
45_test_plan/      測試規畫（strategy、fixtures、acceptance_tests）
50_implementation/ 程式碼、測試
60_experiments/    實驗紀錄（一個實驗一個資料夾）
70_closure/        結案與復盤（done_checklist、retrospective）
99_meta/           慣例、術語、prompt log、traceability
```

每個資料夾的 README.md 都有更詳細的角色定位。

SOP 流程：**10 → 20 → 25 → 30 → 40 → 45 → 50 → 60（穿插）→ 70**；99 為跨階段共用。

---

## 5. 回饋與貢獻

對本 template 結構有改進建議，歡迎回到 [problem-def-template](https://github.com/Cheryl33990/problem-def-template) 開 issue 或 PR。
