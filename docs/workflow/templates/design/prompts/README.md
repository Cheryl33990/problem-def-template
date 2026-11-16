---
title: docs/project/design/prompts 生產用 prompt
status: in-review
updated: 2026-11-16
tags: [design, prompts]
---

# docs/project/design/prompts/ 

> **範本庫文件**：需要時才複製到專案紀錄區。本檔連結供瀏覽範本；複製後須改為實際專案文件，未建立的依賴標待建立或連到 brief。做法見 [使用指南](../../../guide.md)。

這是生產 prompt 的組織與契約範本；複製到實際專案後才保存正式版本。探索 prompt 依已授權疑問、資源邊界與完成條件建立，不要求先有產品 AC。與 [docs/project/experiments/](../../experiments) 內仍在實驗的 prompt 區分。

## 角色定位

- 本資料夾的 prompt 是「目前正式版」；任何被本專案實作引用的 prompt 都應出自此處。
- 實驗性、迭代中的版本留在 `docs/project/experiments/EXP-NNN/prompt.md`；通過驗證後才搬入此處並更新 status。

---

## 1. Prompt 檔案契約（必填）

> **核心原則**：每個 prompt 檔的 frontmatter 必須能回答這四個問題：
> 1. 它要達成 acceptance 的哪幾條？（目的）
> 2. 它的設計來自哪份 discovery 的什麼發現？（依據）
> 3. 它的輸入輸出 schema 在哪？（介面）
> 4. 已知會失敗的情境是哪些？（防呆）
>
> 生產用途須能回答適用的契約問題；證據可來自 brief 或獨立探索紀錄，確實不適用的欄位說明理由，不建立空文件充數。未知不能冒充不適用。

### 1.1 必填 frontmatter

```yaml
---
title: <prompt 用途簡稱>          # 例：beam_extract
status: draft                     # draft / in-review / approved / deprecated
updated: YYYY-MM-DD
version: v0.1                     # prompt 自身的版本號（每次重大改動 bump）

# === Prompt 契約（必填五欄）===
serves_acceptance:                # 它要達成哪幾條 acceptance（編號對應 docs/project/problem/acceptance.md）
  - AC-03
  - AC-07
informed_by_discovery:            # 它的設計來自哪些 discovery 發現
  - docs/project/discovery/02_data_model.md#3-結構特徵
  - docs/project/discovery/03_tech_feasibility.md#4-限制
input_schema: docs/project/design/schema/input.md#user-utterance
output_schema: docs/project/design/schema/output.md#extracted-fields
known_failure_modes:              # 已知會失敗的情境（來自 discovery / experiment）
  - 長文截斷（>2000 tokens 時尾段被忽略）
  - 中英混排時欄位錯位
  - 缺乏明確日期時 LLM 會幻覺出近期日期

# === 選填 ===
related:                          # 對應的 ADR / EXP
  - ADR-002
  - EXP-003
tags: [prompt, extraction]
---
```

### 1.2 欄位語意

| 欄位 | 為什麼存在 |
|---|---|
| `serves_acceptance` | 沒有對應的 acceptance 條目，這個 prompt 就沒有「正確」的定義。任何 review 都無從下手。 |
| `informed_by_discovery` | 強迫 prompt 設計者證明「我看過資料才寫的」，而不是憑感覺。 |
| `input_schema` / `output_schema` | prompt 是 schema 的實現，不是相反。schema 變了 prompt 必須跟著動。 |
| `known_failure_modes` | 這份名單應該來自 discovery 與 experiment，會隨時間長。沒寫＝你還沒測過。 |
| `version` | 同檔內變動追蹤；重大版本變動同步在 [docs/project/meta/prompt_log.md](../../meta/prompt_log.md) 留紀錄。 |

### 1.3 何時 bump version

- patch（v0.1 → v0.1.1）：純文字微調、不改行為
- minor（v0.1 → v0.2）：加 few-shot 範例、改指令語氣、調 output schema 但向後相容
- major（v0.1 → v1.0、v1.0 → v2.0）：重大邏輯重寫、output schema breaking change
- 重大版本應附帶 `docs/project/experiments/EXP-NNN/` 的驗證紀錄

---

## 2. Prompt 檔案內容結構

frontmatter 之後依序：

```markdown
## 1. 目的（1-3 句）
本 prompt 要做什麼、為誰而做、達成 AC-XX 的什麼面向。

## 2. System
（角色設定 / 全域規則 / 輸出格式約束）

## 3. User template
（含變數占位符，例：{{user_query}}、{{context_chunks}}）

## 4. 範例輸入輸出
至少 1 組正例 + 1 組來自 known_failure_modes 的反例。

## 5. 已知限制與後處理
此 prompt 解不掉、需要外部後處理的部分（指向 `src/` 的處理函式）。
```

---

## 3. 命名規則

- 檔案：`<用途>.prompt.md`（例：`beam_extract.prompt.md`、`drawing_classify.prompt.md`）
- 用途名用 `snake_case`、動詞優先（extract / classify / summarize / validate）
- 範本檔以底線開頭：`_example.prompt.md`（被 implementation 忽略，僅供參考）

---

## 4. 維護規則

- **修改前確認契約仍成立**：改 prompt 內容前先回看 frontmatter 五欄是否仍正確。若 `serves_acceptance` 變了，可能是新的 prompt 而不是修改現有的。
- **重大版本變動須有實驗支撐**：major bump 必須在 `related:` 指到至少一個 `EXP-NNN`，否則拒收。
- **重大 schema 變更走 ADR**：破壞相容或重大介面變更先記 ADR；相容修正同步 prompt 與測試。
- **deprecated prompt 不刪**：保留檔案、status 改 `deprecated`、`related:` 指到取代它的新 prompt。
- 每次重大修改在專案 progress 留紀錄；需要詳細重現資料時才依 [prompt log 範本](../../meta/prompt_log.md) 另建紀錄。

---

## 5. 範例

見 [_example.prompt.md](_example.prompt.md)——完整契約 + 內容結構的最小可參考樣板。
