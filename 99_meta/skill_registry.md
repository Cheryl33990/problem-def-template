---
title: Skill Registry — SOP 階段 ↔ 外部 skill 對照
status: draft
updated: 2026-11-16
tags: [meta, skills, routing]
---

# Skill Registry

> 本檔列出**本專案環境中可用的 skill / agent**，以及它們對應到哪些 SOP 階段的 slot。
> 給未來 Claude session 用：當使用者用自然語言描述某階段動作時，先查本檔挑最具體的 skill；沒匹配再 fallback 到 general-purpose agent 或本 session 直接處理。
>
> 路由規則見 [AGENTS.md §5](../AGENTS.md)；slot 契約見 [slot_contracts.md](slot_contracts.md)。

---

## 1. 怎麼讀這張表

| 欄位 | 意義 |
|---|---|
| SOP 階段 | 對應的資料夾編號 |
| 目標 slot | 該 skill 預計填補的文件（路徑、片段、或 slot id） |
| Skill / Agent | skill 的完整名稱（含 plugin 前綴）或 agent 類型 |
| 觸發語句範例 | 使用者用什麼話會自然觸發；用來檢查 skill 的 description 是否夠精準 |
| 安裝狀態 | 待確認 / 🔌 已安裝 / 📦 已知但未裝 / ❌ 不適用 |
| 適用範圍 / 備註 | 限制條件、誰先誰後、已知坑 |

---

## 2. Skill 對照表

> **使用方式**：衍生新 repo 後，依你的環境刪去不適用列、補上你實際安裝的 skill。
> 本表列出的工具均為候選，不代表目前環境已安裝或可用；實際使用前確認名稱、權限與能力。確認後記錄環境與日期。
> 本表初始保留**通用候選**，不針對特定領域。

### 2.1 `20_discovery/` — 資料盤點與探索

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `20_discovery/NN_*.md` | general-purpose agent | 「分析這份資料」「盤點 data」 | 待確認 | fallback；任何格式 |
| `20_discovery/NN_*.md`（Excel/CSV） | `financial-analysis:clean-data-xls` | 「clean this data」「normalize this sheet」 | 待確認 | 限試算表；偏資料清整非結構盤點 |
| `20_discovery/NN_*.md`（Excel 稽核） | `financial-analysis:audit-xls` | 「audit this sheet」「sanity check」 | 待確認 | 限試算表 |

### 2.2 `10_problem/` — 問題定義

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `10_problem/PRD.md` v0.1 | （無專用 skill；本 session 直接寫） | 「從模糊需求寫 PRD」 | — | 候選自建 skill：`prd-draft` |
| `10_problem/PRD.md` §8 修訂 | （無專用 skill；本 session 直接改） | 「discovery 挑戰了 PRD」「更新 PRD」 | — | 候選自建 skill：`prd-revise` |
| `10_problem/acceptance.md` | （無專用 skill；本 session 直接寫） | 「把成功指標翻成驗收條件」 | — | 候選自建 skill：`acceptance-derive` |
| `10_problem/non_goals.md` | （無專用 skill；本 session 直接寫） | 「列出 non-goals」 | — | — |

### 2.3 `25_approach/` — 候選方法比較

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `25_approach/options.md` | general-purpose agent | 「列方法比較」「列出候選方案」 | 待確認 | — |
| `25_approach/tradeoffs.md` | （本 session 直接寫） | 「做 trade-off 矩陣」 | — | 候選自建 skill：`approach-compare` |

### 2.4 `30_decisions/` — ADR

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `30_decisions/ADR-NNN-*.md` | （本 session 依 TEMPLATE 寫） | 「開 ADR」「記錄這個決定」 | — | 候選自建 skill：`adr-draft` |

### 2.5 `40_design/` — 技術設計

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `40_design/tech_spec.md` | （本 session 直接寫） | 「寫技術設計」 | — | — |
| `40_design/prompts/*.prompt.md` | （本 session 依契約寫） | 「建立 prompt 檔」「新增 prompt」 | — | 必填 [_example.prompt.md](../40_design/prompts/_example.prompt.md) 契約欄位 |
| `40_design/schema/*.md` | （本 session 直接寫） | 「定 input/output schema」 | — | — |

### 2.6 `45_test_plan/` — 測試規畫

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `45_test_plan/test_strategy.md` | （本 session 直接寫） | 「規畫測試策略」 | — | — |
| `45_test_plan/acceptance_tests/*` | `verify`（候選） | 「驗證這個 PR」「manually test 一下」 | 待確認 | 用於跑驗收測試而非寫測試 |

### 2.7 `50_implementation/` — 實作

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `50_implementation/src/**` | （本 session 編輯） | 「實作 X」 | — | — |
| `50_implementation/src/**`（review） | `review`、`security-review`、`simplify`（候選） | 「review 一下」「security review」 | 待確認 | code 寫完後跑 |

### 2.8 `60_experiments/` — 實驗

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `60_experiments/EXP-NNN/` | （本 session 依 EXP_TEMPLATE 建） | 「開個實驗」「建 EXP-NNN」 | — | — |

### 2.9 `70_closure/` — 結案

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `70_closure/done_checklist.md` | （本 session 對照） | 「跑結案 checklist」 | — | — |
| `70_closure/retrospective.md` | （本 session 主持） | 「做 retrospective」 | — | — |

### 2.10 `99_meta/` — 跨階段

| 目標 slot | Skill / Agent | 觸發語句範例 | 安裝狀態 | 適用範圍 / 備註 |
|---|---|---|---|---|
| `99_meta/traceability.md` | （本 session 掃 repo 重生） | 「更新追溯矩陣」 | — | 候選自建 skill：`traceability-update` |
| `99_meta/prompt_log.md` | （本 session 追加） | （每次 prompt 嘗試自動追加） | — | — |

---

## 3. 候選自建 skill（未來考慮）

> 跑過幾次真實案例、確定卡點之後再考慮自建。**不要在實際痛點出現前先寫**。

- `data-inventory` — 標準化 discovery 筆記
- `prd-draft` / `prd-revise` — PRD 的初版與迭代
- `acceptance-derive` — PRD §4 → acceptance.md
- `approach-compare` — options + tradeoffs
- `adr-draft` — ADR 草稿
- `prompt-contract` — 含契約 frontmatter 的 prompt 檔
- `traceability-update` — 自動重建追溯矩陣

---

## 4. 維護規則

- **新增一列**：當你發現某個 skill / agent 適合補某個 slot，append 一列；附上「為什麼選這個、什麼時候不適用」。
- **改安裝狀態**：環境有變動（裝了新 plugin、移除某個）就同步本表。
- **發現 skill 不適用**：在 [prompt_log.md](prompt_log.md) 記一筆「skill X 對 slot Y 不適用，原因 Z」；同時把本表該列的安裝狀態改為 ❌ 或加上備註。
- **跨 repo 同步**：本檔是 template 的一部分；衍生新 repo 後依該 repo 的環境裁剪。若發現「跨多個衍生 repo 都需要」的 skill，建議回 template 補上。
