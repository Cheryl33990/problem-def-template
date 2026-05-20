---
title: 專案慣例
status: in-review
updated: 2026-05-20
tags: [meta, conventions]
---

# 專案慣例

本文件規範本專案的命名、文件格式、與工作流程慣例。
**「frontmatter 規範」一節已是當前最新版本可直接套用；其他章節為骨架，待補。**

---

## 1. YAML Frontmatter 規範（已定版）

所有 `.md` 檔案開頭必須有 frontmatter，欄位分**必填**與**選填**兩組。

### 1.1 必填三欄

```yaml
---
title: <檔案標題>
status: draft        # 狀態值見 1.3
updated: YYYY-MM-DD  # 最近一次內容變動的日期
---
```

### 1.2 選填三欄（視需要加）

```yaml
owner: <負責人>                       # 該文件目前的負責人
tags: [requirements, beam]            # 主題標籤，便於檢索
related: [ADR-001, EXP-003]           # 相關文件 ID（ADR、EXP、其他 .md）
```

### 1.3 status 五個值

| status | 意義 | 何時用 |
|---|---|---|
| `draft` | 草稿 | 剛建立、內容未完整 |
| `in-review` | 審閱中 | 內容完整、等待 review 或交叉檢核 |
| `approved` | 已採用 | 通過審閱、作為當前事實來源 |
| `archived` | 已歸檔 | 仍正確但不再活躍維護（例如已結案的實驗） |
| `deprecated` | 已棄用 | 被新版取代或被判定為不正確；應在 `related` 指向取代者 |

### 1.4 完整範例

```yaml
---
title: <核心領域物件>資料模型
status: in-review
updated: 2026-05-20
owner: <name>
tags: [design, schema]
related: [ADR-002, EXP-001]
---
```

---

## 2. 檔名規則

<!-- TODO: 此處填具體命名規則
     需包含：
       - 階段資料夾命名（NN_name/）
       - 探索筆記排序前綴（NN_）
       - ADR 命名（ADR-NNN-short.md）
       - 實驗命名（EXP-NNN-short/）
       - snake_case vs kebab-case 的使用時機
     參考 CLAUDE.md §1.1 已列的初稿
     完成後將 status 從 in-review 改為 approved -->

---

## 3. 文件結構慣例

<!-- TODO: 此處填各類文件的標準章節結構
     需包含：
       - PRD 章節（背景 / 使用者 / 需求 / 成功指標 / 非目標）
       - 探索筆記章節（問題 / 方法 / 發現 / 對下一階段的影響）
       - ADR 章節（已有 30_decisions/TEMPLATE.md，本處引用即可）
     參考 30_decisions/TEMPLATE.md
     完成後將相關範例補進對應檔案 -->

---

## 4. 術語使用

<!-- TODO: 此處說明術語管理流程
     需包含：
       - 新術語先寫進 99_meta/glossary.md 再被引用
       - 文件內首次出現中英對照
       - 縮寫的展開規則
     參考 99_meta/glossary.md -->

---

## 5. 變更與版本

<!-- TODO: 此處填變更管理規則
     需包含：
       - 何時更新 CHANGELOG.md
       - 何時 bump 版本號
       - 已 approved 文件如何修訂（新增 ADR、原文 deprecate）
     參考 CHANGELOG.md、30_decisions/TEMPLATE.md -->
