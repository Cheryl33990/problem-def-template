---
title: Definition of Done 檢查清單
status: draft
updated: 2026-11-16
tags: [closure, dod, checklist]
# related: [acceptance] 
---

# Definition of Done 檢查清單

> **範本庫文件**：需要時才複製到專案紀錄區。本檔連結供瀏覽範本；複製後須改為實際專案文件，未建立的依賴標待建立或連到 brief。做法見 [使用指南](../../guide.md)。

本清單把 [docs/project/problem/acceptance.md](../problem/acceptance.md) §4「結案閘門」展開為**逐項可勾選**的檢查表。
**適用項目全部勾選**、完成復盤後才能宣告結案。小型專案可以用 brief 與 progress 中的對應紀錄滿足下列條件；不為勾選清單而新增文件。未建立且不需要的專用文件可註明 N/A 與理由。

> 規則：每項勾選後填「驗證方式」欄（誰、何時、怎麼確認）。空白勾選等於沒勾。不適用項目填 N/A、理由與確認人；不可空白略過。未通過的 AC 須列為未完成，或先經 PRD 修訂移出本次範圍，不可直接視為通過。

---

## 1. 問題定義階段（docs/project/problem/）

- [ ] brief 或 PRD 的本次範圍與成功標準已確認，影響結案的待確認事項已處理 — 驗證：<!-- TODO -->
- [ ] `stakeholders.md` `status: approved`，角色清單完整 — 驗證：<!-- TODO -->
- [ ] `non_goals.md` `status: approved`，與 PRD §5 一致 — 驗證：<!-- TODO -->
- [ ] `acceptance.md` `status: approved`，每條 PRD §4 指標都有對應驗收條件 — 驗證：<!-- TODO -->

## 2. 探索階段（docs/project/discovery/）

- [ ] 所有已使用的探索筆記已審閱（不含未使用範本） — 驗證：<!-- TODO -->
- [ ] 探索結論已記錄；影響重大決策者已反映在 ADR — 驗證：<!-- TODO -->

## 3. 方法選擇階段（docs/project/approach/）

- [ ] `options.md` 列出至少 2 個候選方法（若只有 1 個合理方法可豁免，但須於 ADR 註明）
- [ ] `tradeoffs.md` `status: approved`
- [ ] 被否決方案的「為什麼不選」已寫進對應 ADR

## 4. 決策階段（docs/project/decisions/）

- [ ] 所有重大決策都有 ADR
- [ ] 所有 ADR `status` 為 `approved` 或 `deprecated`（不允許 `draft` / `in-review` 殘留）
- [ ] `deprecated` 的 ADR 都有 `related` 指向取代者

## 5. 設計階段（docs/project/design/）

- [ ] `tech_spec.md` `status: approved`
- [ ] `schema/`、`pipeline/`、`prompts/` 內容與 ADR 一致
- [ ] 重大設計變更有對應 ADR，其餘變更記於 progress

## 6. 測試規畫階段（docs/project/testing/）

- [ ] `test_strategy.md` `status: approved`
- [ ] `fixtures.md` 邊界 case 清單完整
- [ ] `acceptance_tests/` 內每條 acceptance 條件都有 `passing` 狀態的測試

## 7. 實作階段（src/）

- [ ] 所有 acceptance test 通過（`passing`）
- [ ] 若有設定覆蓋率目標，實測結果達到目標
- [ ] 已設定的必要自動檢查通過；未設定 CI 時記錄實際執行的驗證與限制
- [ ] `README.md` 快速開始可重現

## 8. 實驗階段（docs/project/experiments/）

- [ ] 所有 EXP `status` 為 `approved` 或 `archived`
- [ ] 實驗結論若影響決策，已反映在 ADR 或 PRD

## 9. Meta（docs/project/meta/）

- [ ] 實際專案遵循已確認的工作與文件規則
- [ ] 關鍵術語已於 brief 或 glossary 定義
- [ ] 成功標準能追溯至適用的決策、實作與測試證據；簡單專案可在 progress 記錄
- [ ] 需要重現的重要提示詞已記錄；一般對話不要求留存

## 10. 對外文件

- [ ] `README.md`（top-level）已替換所有 placeholder
- [ ] 專案 progress 或專案自己的 CHANGELOG 已記錄結案；不寫入模板維護歷史
- [ ] 模板維護資料已移除或明確區分；專案保留 docs/workflow/guide.md 作使用入口

---

## 11. 復盤與最終結案

- [ ] 上述適用項目已完成，已記錄驗收結果與未解風險
- [ ] 復盤已記於 progress 或 retrospective；改善事項有負責人與下一步

## 結案聲明

> 全部勾選後，請在此簽署。

- **結案日期**：<!-- YYYY-MM-DD -->
- **結案負責人**：<!-- name -->
- **下一步**：<!-- 例：進入維運 / 移交給 X 團隊 / 歸檔 -->
