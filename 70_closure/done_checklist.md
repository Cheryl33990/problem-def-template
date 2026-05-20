---
title: Definition of Done 檢查清單
status: draft
updated: 2026-05-20
tags: [closure, dod, checklist]
# related: [acceptance]
---

# Definition of Done 檢查清單

本清單把 [10_problem/acceptance.md](../10_problem/acceptance.md) §4「結案閘門」展開為**逐項可勾選**的檢查表。
**全部勾選**才能宣告專案完成。

> 規則：每項勾選後填「驗證方式」欄（誰、何時、怎麼確認）。空白勾選等於沒勾。

---

## 1. 問題定義階段（10_problem/）

- [ ] `PRD.md` `status: approved`，所有 TODO 已清空 — 驗證：<!-- TODO -->
- [ ] `stakeholders.md` `status: approved`，角色清單完整 — 驗證：<!-- TODO -->
- [ ] `non_goals.md` `status: approved`，與 PRD §5 一致 — 驗證：<!-- TODO -->
- [ ] `acceptance.md` `status: approved`，每條 PRD §4 指標都有對應驗收條件 — 驗證：<!-- TODO -->

## 2. 探索階段（20_discovery/）

- [ ] 所有 `NN_*.md` 探索筆記 `status` ≥ `in-review` — 驗證：<!-- TODO -->
- [ ] 探索結論若被採用，已升級為 ADR — 驗證：<!-- TODO -->

## 3. 方法選擇階段（25_approach/）

- [ ] `options.md` 列出至少 2 個候選方法（若只有 1 個合理方法可豁免，但須於 ADR 註明）
- [ ] `tradeoffs.md` `status: approved`
- [ ] 被否決方案的「為什麼不選」已寫進對應 ADR

## 4. 決策階段（30_decisions/）

- [ ] 所有重大決策都有 ADR
- [ ] 所有 ADR `status` 為 `approved` 或 `deprecated`（不允許 `draft` / `in-review` 殘留）
- [ ] `deprecated` 的 ADR 都有 `related` 指向取代者

## 5. 設計階段（40_design/）

- [ ] `tech_spec.md` `status: approved`
- [ ] `schema/`、`pipeline/`、`prompts/` 內容與 ADR 一致
- [ ] 任何設計變更都有對應 ADR

## 6. 測試規畫階段（45_test_plan/）

- [ ] `test_strategy.md` `status: approved`
- [ ] `fixtures.md` 邊界 case 清單完整
- [ ] `acceptance_tests/` 內每條 acceptance 條件都有 `passing` 狀態的測試

## 7. 實作階段（50_implementation/）

- [ ] 所有 acceptance test 通過（`passing`）
- [ ] 覆蓋率達 `test_strategy.md` §2 設定的目標
- [ ] CI 全綠
- [ ] `README.md` 快速開始可重現

## 8. 實驗階段（60_experiments/）

- [ ] 所有 EXP `status` 為 `approved` 或 `archived`
- [ ] 實驗結論若影響決策，已反映在 ADR 或 PRD

## 9. Meta（99_meta/）

- [ ] `conventions.md` `status: approved`
- [ ] `glossary.md` 涵蓋所有文件用到的術語
- [ ] `traceability.md` 全部對齊（PRD 目標 → ADR → EXP → 實作 → 測試）
- [ ] `prompt_log.md` 完整（給 AI 復盤用）

## 10. 對外文件

- [ ] `README.md`（top-level）已替換所有 placeholder
- [ ] `CHANGELOG.md` 已新增結案條目
- [ ] `USAGE.md`（若衍生自 template）已決定保留或刪除

---

## 結案聲明

> 全部勾選後，請在此簽署。

- **結案日期**：<!-- YYYY-MM-DD -->
- **結案負責人**：<!-- name -->
- **下一步**：<!-- 例：進入維運 / 移交給 X 團隊 / 歸檔 -->
