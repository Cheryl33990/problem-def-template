---
title: 變更紀錄
status: approved
updated: 2026-11-16
---

# Changelog

本文件採 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/) 格式，
版本號遵循 [Semantic Versioning](https://semver.org/lang/zh-TW/)。

## [Unreleased]

### 專案流程架構與使用指南
- 新增 WORKFLOW、REVIEW、進度接手與風險追蹤，重寫 USAGE 與測試策略。
- 新增 AC 規格、當次驗證紀錄及 GitHub PR 填寫範本。
- AI 規則集中到 AGENTS，CLAUDE 保留相容入口；補文件慣例與問題拆解。
- 實例試跑延後；未安裝自動化、CI 或部署。


### 2026-11-16 文件一致性與首次使用
- 統一 AC-NN、驗收規格命名及實驗三件組，拆開驗收與最終結案。
- 工具清單改為待確認候選；補資料盤點入口與 N/A 理由規則。
- 重寫模板首頁，加入 START_HERE、合成示例、PILOT 與改善進度。
- 真實案例成效待驗證，未新增應用程式或自動化。


### Added
- [40_design/prompts/_example.prompt.md](40_design/prompts/_example.prompt.md) — prompt 契約樣板（dummy），示範 frontmatter 五欄契約與內容結構五段。
- [10_problem/PRD.md](10_problem/PRD.md) §8 修訂紀錄 — 把 PRD 從「一次寫死」改成可追溯的活文件。
- [99_meta/skill_registry.md](99_meta/skill_registry.md) — SOP 階段 ↔ 外部 skill / agent 對照表。Template 提供初始通用候選；衍生 repo 後依該環境裁剪。
- [99_meta/slot_contracts.md](99_meta/slot_contracts.md) — 各 SOP 文件的填補契約集中索引。任何 skill 產出都需通過此處驗收。

### Changed
- [40_design/prompts/README.md](40_design/prompts/README.md) 完整改寫：明確訂出 prompt 檔的五欄必填契約（serves_acceptance / informed_by_discovery / input_schema / output_schema / known_failure_modes）、版本 bump 規則、命名規則、維護規則。
- [CLAUDE.md](CLAUDE.md) §2 增加「編號是分類、不是執行順序」說明；§4 工作流程提醒新增「PRD 是活文件」與「寫 prompt 前先填契約」兩條原則；新增 §5 Skill 路由原則（template-as-glue 模式）。
- [99_meta/README.md](99_meta/README.md) 內容表加入 skill_registry 與 slot_contracts 兩項。

### Notes
- 本次強化的核心張力：PRD 不該被資料挑戰後默默忽略；prompt 不該在問題與資料尚未收斂時就動筆寫。
- 新增 template-as-glue 模式：template 提供 SOP slots，外部 skill / agent 作為外掛；不假設特定 skill 存在，由衍生 repo 的環境決定。

## [0.2.0] - 2026-05-20

### Added
- 新增三個中介階段資料夾，補強 SOP 的完整性：
  - [25_approach/](25_approach/) — 候選方法比較（`options.md`、`tradeoffs.md`），承接 20_discovery 與 30_decisions 之間「為什麼選 A 不選 B」的過程紀錄
  - [45_test_plan/](45_test_plan/) — 測試規畫（`test_strategy.md`、`fixtures.md`、`acceptance_tests/`），把驗收條件翻成可執行的測試規格，是 TDD 的源頭
  - [70_closure/](70_closure/) — 結案與復盤（`done_checklist.md`、`retrospective.md`），讓專案能「乾淨關閉」並留下可復盤紀錄
- 強化問題定義階段（10_problem/）：
  - [10_problem/non_goals.md](10_problem/non_goals.md) — 非目標完整版（分類視角：範圍外 / 延後 / 明確拒絕 / 責任邊界）；PRD §5 改為摘要
  - [10_problem/acceptance.md](10_problem/acceptance.md) — 把 PRD §4 成功指標翻成可驗證二元條件（Definition of Done）
- 新增 [99_meta/traceability.md](99_meta/traceability.md) — 追溯矩陣，把 PRD 指標 → ADR → EXP → 實作 → 驗收測試串成一張表

### Changed
- [10_problem/PRD.md](10_problem/PRD.md) §4 與 §5 改為「摘要 + 連結到深入版」
- [CLAUDE.md](CLAUDE.md) §1.1 階段編號規則涵蓋中介階段（25/45/70）；§2 必讀清單擴充至 8 項
- [USAGE.md](USAGE.md) §2 初始化清單與 §4 結構速查同步更新
- [README.md](README.md) 目錄導覽加入新資料夾
- [99_meta/glossary.md](99_meta/glossary.md) 補上 DoD、TDD、非目標、驗收條件、測試金字塔、追溯矩陣等術語

### Notes
- 完整 SOP 流程：**10 → 20 → 25 → 30 → 40 → 45 → 50 → 60（穿插）→ 70**；99 為跨階段共用。
- 所有新檔維持「skeleton + TODO 註解」原則，衍生者複製後依實際情境填入。

## [0.1.0] - 2026-05-20

### Added
- Template 初版發布：問題定義 → 探索 → 決策 → 設計 → 實作 SOP 的完整文件骨架
- 13 個資料夾（10_problem / 20_discovery / 30_decisions / 40_design / 50_implementation / 60_experiments / 99_meta 及子目錄）
- 兩份範本：[30_decisions/TEMPLATE.md](30_decisions/TEMPLATE.md)（ADR）、[60_experiments/EXP_TEMPLATE/](60_experiments/EXP_TEMPLATE/)（實驗三件組）
- 一份探索筆記範本：[20_discovery/NN_template.md](20_discovery/NN_template.md)
- Frontmatter 規範：3 必填欄（title / status / updated）+ 3 選填欄（owner / tags / related）；status 五值（draft / in-review / approved / archived / deprecated）
- [USAGE.md](USAGE.md) — 衍生新專案後的初始化清單
- [CLAUDE.md](CLAUDE.md) — 給 AI session 的工作規則（含「動手前必讀」與「禁止事項」）

### Notes
- 所有骨架檔的 TODO 都明確標示「該填什麼 / 參考哪裡 / 完成後改 status」，方便人機接手。
