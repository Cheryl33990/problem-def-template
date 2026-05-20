---
title: Slot Contracts — 各 SOP 文件的填補契約
status: draft
updated: 2026-05-20
tags: [meta, contracts, slots]
---

# Slot Contracts

> 本檔是**索引**：把散落在各階段 README 與檔案內 TODO 註解中的「該被填成什麼樣」契約集中起來，供 skill / agent / 本 session 統一參考。
> 任何 skill 產出的內容，不論來源，都必須通過此處列出的驗收標準。
>
> 對應的可用 skill 見 [skill_registry.md](skill_registry.md)；路由規則見 [CLAUDE.md §5](../CLAUDE.md)。

---

## 0. 共通驗收（所有 slot 必過）

| 項 | 規則 | 參考 |
|---|---|---|
| frontmatter | 必填三欄（`title` / `status` / `updated`），值合法 | [conventions.md §1.1](conventions.md) |
| status 值 | 限 draft / in-review / approved / archived / deprecated | [conventions.md §1.3](conventions.md) |
| updated | 每次內容變動同步更新為當日日期 | [conventions.md §1.1](conventions.md) |
| 術語 | 使用 [glossary.md](glossary.md) 既有術語；新術語先補進 glossary | [conventions.md §4](conventions.md) |
| TODO 註解 | 內容真填上後才能刪該 TODO；未完成不可靜默移除 | [CLAUDE.md §3](../CLAUDE.md) |

---

## 1. `10_problem/` — 問題定義

### 1.1 `PRD.md`

| 欄位/段落 | 必填? | 內容契約 |
|---|---|---|
| §1 背景 | ✅ | 痛點 + 現況 + 為什麼現在做（3-5 句） |
| §2 目標使用者 | ✅ | 具體角色 + 介入時點；對應 `stakeholders.md` |
| §3 需求 | ⚠️ 可分批 | 至少先有 MUST 一組；SHOULD/MAY 可延後 |
| §4 成功指標 | ✅ | 至少 3 條、可量化；每條編號（被 acceptance / traceability 引用） |
| §5 非目標 | ✅ | 3-5 條摘要；完整版見 `non_goals.md` |
| §6 約束 | ✅ | 至少列出已知的硬性約束（時程/預算/技術/法規） |
| §7 開放問題 | ✅ | 未知數列出 + 指到預計回答的 discovery / experiment |
| §8 修訂紀錄 | ✅ | 至少 v0.1 一列；之後每次修訂 append（含觸發來源） |

**驗收**：能回答「現在 PRD 是 v 幾？最近一次被誰挑戰過？」這兩問。

### 1.2 `acceptance.md`

| 規則 |
|---|
| 每條驗收條件用 `AC-NN` 編號 |
| 每條對應 PRD §4 的指標編號（多對一 / 一對多皆可） |
| 每條為**二元可判定**（可寫成 pytest assert / 人工 checklist） |

### 1.3 `non_goals.md`

| 規則 |
|---|
| 至少分四類：範圍外 / 延後 / 明確拒絕 / 責任邊界 |
| 每條附「為什麼是 non-goal」一句話 |

### 1.4 `stakeholders.md`

| 規則 |
|---|
| 至少 3 個關鍵角色；含「角色名 / 對本專案的關注點 / 何時介入」三欄 |

---

## 2. `20_discovery/` — 探索筆記

### 2.1 `NN_<topic>.md`

| 段落 | 必填? | 內容契約 |
|---|---|---|
| 問題 | ✅ | 這份筆記要釐清什麼具體疑問 |
| 方法 | ✅ | 用什麼方式找答案（看資料、訪談、實驗、文獻） |
| 發現 | ✅ | 至少 3 條具體發現；**禁止把假設當結論**寫 |
| 對下一階段的影響 | ✅ | 用 「→ 改 PRD §X」「→ 開 ADR」「→ 排實驗」格式條列 |

**驗收**：能回答「這份筆記改變了 PRD / approach / decision 的什麼？」若答不出，要嘛筆記沒寫完、要嘛上游沒被更新。

---

## 3. `25_approach/` — 候選方法

### 3.1 `options.md`

| 規則 |
|---|
| 至少 2 個候選（只有 1 個不是「選擇」） |
| 每個候選含「核心想法 / 優點 / 限制 / 不確定性」四段 |

### 3.2 `tradeoffs.md`

| 規則 |
|---|
| 用一致的評估維度（避免被偏見影響） |
| 「為什麼否決」要誠實，不要為了讓最終選擇看起來合理而美化 |

---

## 4. `30_decisions/` — ADR

### 4.1 `ADR-NNN-<short-title>.md`

| 規則 |
|---|
| 依 [TEMPLATE.md](../30_decisions/TEMPLATE.md) 結構：Status / Context / Decision / Consequences / Alternatives Considered |
| Decision 段若引用 `25_approach/`，該資料夾 status 須為 approved |
| 已 approved / archived 的 ADR **禁止直接改**——新增一份新 ADR、舊版 status 改 deprecated、雙向 `related` 連結 |

---

## 5. `40_design/` — 技術設計

### 5.1 `tech_spec.md`

| 規則 |
|---|
| 上游引用：至少指到一個 approved ADR |
| 下游連結：列出對應的 `schema/` 與 `prompts/` |

### 5.2 `prompts/<name>.prompt.md`

**契約見** [prompts/README.md §1](../40_design/prompts/README.md)。摘要：

| 必填 frontmatter 欄位 | 意義 |
|---|---|
| `serves_acceptance` | 對應 `acceptance.md` 的 AC-NN 編號（≥1） |
| `informed_by_discovery` | 對應 `20_discovery/` 的具體段落（≥1） |
| `input_schema` | 指到 `40_design/schema/` 的具體 anchor |
| `output_schema` | 指到 `40_design/schema/` 的具體 anchor |
| `known_failure_modes` | 已知失敗情境（來自 discovery / experiment） |

**驗收**：四欄都填得出來才動筆。填不出代表上游沒收斂。

### 5.3 `schema/*.md`

| 規則 |
|---|
| 每個 schema 用 anchor（`#user-utterance`、`#extracted-fields`）以便 prompt 引用 |
| schema 變動走 ADR（被 prompt 引用的 schema 是 breaking 點） |

---

## 6. `45_test_plan/` — 測試規畫

### 6.1 `test_strategy.md`

| 規則 |
|---|
| 對應 acceptance.md 的 AC-NN，列出每條的測試方式（unit / integration / 人工 / 線上監控） |

### 6.2 `acceptance_tests/<AC-NN>.md`

| 規則 |
|---|
| 一條 AC 對應一個檔案；含「前置條件 / 步驟 / 期望結果 / 通過條件」 |

---

## 7. `50_implementation/` — 實作

| 規則 |
|---|
| 程式碼變更若改變 acceptance 行為，需同步更新 `45_test_plan/` 與（必要時）PRD §3/§4 並在 PRD §8 留紀錄 |
| 依 [README.md](../50_implementation/README.md) 的環境與依賴規範 |

---

## 8. `60_experiments/` — 實驗

### 8.1 `EXP-NNN-<short>/`

| 規則 |
|---|
| 依 [EXP_TEMPLATE/](../60_experiments/EXP_TEMPLATE/) 三件組：`plan.md` / `run.md` / `result.md` |
| `result.md` 結論若挑戰 PRD，必須回頭改 PRD 並在 §8 留紀錄 |

---

## 9. `70_closure/` — 結案

### 9.1 `done_checklist.md`

| 規則 |
|---|
| acceptance.md 每條 AC 都標記 ✅ / ❌ / ⏭️（跳過原因） |

### 9.2 `retrospective.md`

| 規則 |
|---|
| 至少含「What went well / What didn't / What to change」三段 |

---

## 10. `99_meta/` — 跨階段

### 10.1 `traceability.md`

| 規則 |
|---|
| 每條 PRD §4 指標都能追到至少一個 ADR + 至少一個驗收測試 |
| 斷鏈處（指標→無 ADR、ADR→無實作）必須顯式標 ⚠️ 而不是省略 |

---

## 11. 驗收 checklist 用法

當 skill / session 完成一個 slot 後，自我檢核：

1. ☐ §0 共通驗收 5 項全過
2. ☐ 該 slot 在本檔的「內容契約」全部達成
3. ☐ 若觸發了上下游影響（例：discovery 改了 PRD），上下游也同步更新
4. ☐ 若有 skill 觸發失敗或結果不適用，在 [prompt_log.md](prompt_log.md) 留紀錄

任一項未過，回到對應段落補完再交付。
