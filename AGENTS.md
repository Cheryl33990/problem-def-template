---
title: AI 協作規則
status: in-review
updated: 2026-11-16
owner: jenny890808
tags: [meta, ai-collaboration]
---

# AGENTS.md — AI 協作規則

## 0. 專案目標（一句話）

<!-- TODO：衍生專案填入目標；本模板維護目標為提供一致且可裁剪的問題解析工作流程。 -->

> `<PROJECT_GOAL>`

## 1. 重要慣例

### 1.1 檔名規則
- 階段資料夾以 `NN_snake_case/` 命名，編號代表 SOP 階段
  （主階段：10→20→30→40→50→60→99；中介階段：25→45→70）。
- 文件採 `snake_case.md`；探索筆記前綴 `NN_` 表示閱讀順序。
- ADR 採 `ADR-NNN-short-title.md`；實驗採 `EXP-NNN-short-title/`。

### 1.2 文件格式
- 所有 `.md` 開頭都要有 YAML frontmatter，欄位定義見 [99_meta/conventions.md](99_meta/conventions.md)。
- 完成 / 變更時更新 `status` 與 `updated`；不要靜默修改已封存文件。

### 1.3 術語表位置
- 統一見 [99_meta/glossary.md](99_meta/glossary.md)；新術語先寫進 glossary 再被引用。

## 2. 動手前必讀清單

先讀 [WORKFLOW.md](WORKFLOW.md)、[REVIEW.md](REVIEW.md) 與 [work_log](99_meta/work_log.md)。本檔是 AI 規則唯一來源，CLAUDE.md 只作引用入口。


先依 [START_HERE.md](START_HERE.md) 選擇精簡或完整流程。工具名稱是候選，使用前確認當前環境；不依賴特定 AI 產品。

> **重要原則：編號是分類、不是執行順序。**
> 真實流程通常是「資料盤點 → 初版 PRD → 探索 → 用發現挑戰 PRD → 修 PRD → ...」的迴圈。
> 對問題不熟時，先做 `20_discovery/` 的一輪資料盤點，再回頭寫 `10_problem/PRD.md` 是合理的。
> 不確定走哪條路徑時看 [SOP_ROADMAP.html](SOP_ROADMAP.html)。

在開始任何實作或設計變更前，請依序閱讀：

1. [10_problem/PRD.md](10_problem/PRD.md) — 目前的問題定義與成功指標（**活文件**，見 §4 與 PRD §8 修訂紀錄）
2. [10_problem/acceptance.md](10_problem/acceptance.md) — 可驗證的 DoD（什麼算「做完」）
3. [10_problem/non_goals.md](10_problem/non_goals.md) — 範圍邊界（什麼「不要做」）
4. [30_decisions/](30_decisions/) 內**與本次工作相關、status 為 approved** 的 ADR
5. [40_design/tech_spec.md](40_design/tech_spec.md) — 當前的技術設計
6. [99_meta/conventions.md](99_meta/conventions.md) — 慣例與 frontmatter 規範
7. [99_meta/glossary.md](99_meta/glossary.md) — 術語表
8. [99_meta/traceability.md](99_meta/traceability.md) — 追溯矩陣（看清楚動到一個東西會牽動到哪）

文件可依精簡模式合併；未用範本與不適用欄位可裁剪，須記理由。平台設定檔依平台格式；實際路徑以 work log 對照為準。

## 3. 禁止事項

- ❌ **不要直接改 `30_decisions/` 內已封存（status: approved / archived）的 ADR**。
  - 要修正請新增一份 ADR，將舊 ADR 的 status 改為 `deprecated`，並用 `related` 互相連結。
- ❌ **不要繞過 frontmatter**。新增任何 `.md` 都必須有完整 frontmatter。
- ❌ **不要把原始素材 / 大型輸入檔加進 git**（建議放在 `.gitignore` 排除的路徑下）。
- ❌ **不要從 memory 引入未在當前對話討論過的概念**。memory 是輔助、不是事實來源。
- ❌ **不要刪除 TODO 註解**，除非該 TODO 對應的內容已完成，或已明確記錄不適用／裁剪理由。

## 3.1 模糊需求的協助規則

- 使用者只描述目標或困擾就能開始；先讀 [WORKFLOW](WORKFLOW.md) 的釐清流程，不把定義範圍與成功標準的工作全部交回使用者。
- 先回述與利用現有資料，每輪最多 1–3 個關鍵問題；問題要能用生活情境或例子回答，不重問已知資訊。
- 主動提出邊界與成功標準候選，附理由、取捨與證據。無依據的數字不填，未知可保留；將「好用」轉為可觀察任務與判準，不強迫用百分比。
- 在 PRD §0 與 AC 確認表逐項記未知／暫定／已確認；這不是 frontmatter 狀態。不得自行把 AI 草案、使用者沉默或文件 approved 當同意。
- 使用者回答不知道時，提出可授權的限量探索及其完成條件，不能反覆要求先給產品 AC。探索獲授權後持續完成，結果回饋提案。
- 正式實作只依本輪已確認的範圍、AC 與必要決策；確認可以沿用明確的先前指示，不重複索取相同授權。其餘未知留待後續。

## 4. 工作流程提醒

- 模糊目標先協助釐清；正式實作前依 WORKFLOW 確認本輪範圍、AC 與重大決策；已授權範圍內的可逆工作持續執行，依 WORKFLOW.md 處理需要確認的變更。
- 多步任務使用目前環境可用的工作清單追蹤進度。
- 變更檔案後更新該檔案的 `updated:` 欄位為今日日期。
- 影響產出或決策的 prompt 嘗試與結果記錄到 [99_meta/prompt_log.md](99_meta/prompt_log.md)。
- **PRD 是活文件**：當 `20_discovery/` 或 `60_experiments/` 的發現與 PRD（特別是 §3 需求 / §4 成功指標）衝突時，**提出 PRD 修訂及影響，確認範圍或 AC 的變更後再採用**，並在 PRD §8 修訂紀錄留一筆，不要默默忽略發現也不要靜默改 PRD。
- **寫 prompt 前先填契約**：`40_design/prompts/` 內每個 prompt 檔的 frontmatter 必須能指明它服務哪幾條 acceptance、來自哪份 discovery 的發現、輸入輸出 schema 在哪。填不出來代表上游還沒收斂，回上游補完再寫 prompt。

## 5. Skill 路由（template-as-glue 模式）

本 template 採「SOP 提供 slots、外部 skill / agent 作為外掛」的模式。
當使用者用自然語言描述某個 SOP 階段的動作（例：「分析這份資料」「寫個 PRD」「列方法比較」），依下列順序處理：

1. **查 [99_meta/skill_registry.md](99_meta/skill_registry.md)** 看該階段的目標 slot 有無對應 skill / agent
2. **優先用最具體的 skill**（領域專用 > 通用）；多個候選時挑「適用範圍」最匹配的
3. **沒匹配時** fallback 到 general-purpose agent 或本 session 直接處理
4. **不論誰產出**，落地檔案都必須通過 [99_meta/slot_contracts.md](99_meta/slot_contracts.md) 的驗收（§0 共通驗收 + 該 slot 的內容契約）
5. **觸發但結果不適用時**，在 [99_meta/prompt_log.md](99_meta/prompt_log.md) 留一筆「skill X 對 slot Y 不適用，原因 Z」，並把 registry 該列的安裝狀態改為 ❌ 或加備註
6. **跨 SOP 影響時**（例：discovery 的發現挑戰 PRD），按 §4 的「PRD 是活文件」規則同步更新上游，不要靜默吞掉

> Skill 由人裝、由 description 觸發；template 不假設特定 skill 存在。衍生新 repo 後請依該 repo 的實際環境裁剪 [skill_registry.md](99_meta/skill_registry.md)。
