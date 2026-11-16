---
title: _example — prompt 契約樣板（dummy）
status: draft
updated: 2026-11-16
version: v0.1

# === Prompt 契約（必填五欄）=== 
serves_acceptance:
  - AC-01    # （示意）使用者描述需求時，系統能擷取出核心動詞 + 受詞
  - AC-04    # （示意）擷取結果為合法 JSON、欄位齊全
informed_by_discovery:
  - docs/project/discovery/01_input_data_analysis.md#3-語言特徵
  - docs/project/discovery/02_data_model.md#2-核心欄位
input_schema: docs/project/design/schema/input.md#user-utterance
output_schema: docs/project/design/schema/output.md#extracted-intent
known_failure_modes:
  - 中英混排時動詞被誤判為英文 verb（discovery #01 §3.2）
  - 使用者句子過短（<5 字）時 LLM 會幻覺受詞
  - 含有否定語氣（「不是要 X 而是 Y」）時容易抓錯主受詞

# === 選填 ===
related:
  - ADR-001
  - EXP-001
tags: [prompt, extraction, example]
---

# `_example.prompt.md`

> **範本庫文件**：需要時才複製到專案紀錄區。本檔連結供瀏覽範本；複製後須改為實際專案文件，未建立的依賴標待建立或連到 brief。做法見 [使用指南](../../../guide.md)。

> 本檔是 **dummy 範例**，不被 `src/` 引用。
> 用途：示範 [README.md §1 prompt 契約](README.md) 在實際 prompt 檔內如何呈現。
> 建立真實 prompt 時複製本檔、改名為 `<用途>.prompt.md`、把 frontmatter 與內文都換成你的內容。

---

## 1. 目的

從使用者的單句敘述中擷取「動作」與「對象」兩個欄位，輸出合法 JSON。
服務 [AC-01](../../problem/acceptance.md#ac-01)（擷取核心動詞 + 受詞）與 [AC-04](../../problem/acceptance.md#ac-04)（輸出格式合法）。

---

## 2. System

```
你是一個結構化擷取助手。你的任務是從使用者的單句敘述中找出「動作（action）」與「對象（object）」。

規則：
- 輸出必須是合法 JSON，符合 schema：{"action": string, "object": string, "confidence": float}
- confidence ∈ [0, 1]，反映你對擷取結果的把握。若句子過短或語意不清，confidence < 0.5。
- 中英混排時，動作與對象用原文呈現，不要翻譯。
- 含否定語氣（「不是 X 而是 Y」）時，以否定後的肯定描述為主。
- 若無法明確擷取，回傳 {"action": null, "object": null, "confidence": 0.0}，不要亂猜。
```

---

## 3. User template

```
請從以下敘述擷取動作與對象：

「{{user_utterance}}」

只輸出 JSON，不要附加說明。
```

---

## 4. 範例輸入輸出

### 4.1 正例

**輸入**：`「幫我把上週的會議錄音轉成逐字稿」`
**輸出**：
```json
{"action": "轉成逐字稿", "object": "上週的會議錄音", "confidence": 0.95}
```

### 4.2 反例（對應 known_failure_modes #3：否定語氣）

**輸入**：`「我不是要刪檔，而是想把它移到備份資料夾」`
**期望輸出**：
```json
{"action": "移到備份資料夾", "object": "檔案", "confidence": 0.7}
```
**常見錯誤**：模型會抓到「刪檔」當 action。本 prompt 的「否定語氣規則」就是為了防這個。

### 4.3 反例（對應 known_failure_modes #2：句子過短）

**輸入**：`「處理一下」`
**期望輸出**：
```json
{"action": null, "object": null, "confidence": 0.1}
```

---

## 5. 已知限制與後處理

- **複合句子**（含多個動作）目前只擷取第一個動作。複合句處理由 `src/postprocess.py::split_compound_utterance` 在 prompt 之前先拆句。
- **代名詞解析**（「把『它』移到備份」中的「它」）本 prompt 不負責。需要上游補上 context 後再呼叫。
- **JSON 解析失敗**時 implementation 端應重試一次，仍失敗則記入 `docs/project/meta/prompt_log.md`。
