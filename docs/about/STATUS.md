---
title: 目前狀態
status: in-review
updated: 2026-11-27
---

# 目前狀態

- 階段：已公開（2026-11-18）；ipas-learning-hub 同日公開。2026-11-25 PR #10 加入程式變更的正常入口與模組責任規則，以及屬性測試、UI 探索、模型檢查、形式化證明的選用條件（[測試策略](../workflow/templates/testing/test_strategy.md#property-and-formal-verification)）；這些工具尚無專案試跑證據
- 授權：[MIT](../../LICENSE)
- 定位：從模糊需求開始、以證據推進的 AI 協作開發方法論與文件模板
- 驗證：`python tools/validate.py`（連結與錨點、frontmatter、確認日期、validation 證據欄位、圖表）與其單元測試，另有模擬衍生專案初始化的 `init-smoke`；CI 在每個 PR 與 main 執行
- 真實案例：1 個，[ipas-learning-hub](case-study-ipas.md)（單人＋AI；案例證據固定在 `5891f4c` 的 21 個 PR，專案之後持續開發）
- 已知限制：沒有多人團隊或其他領域的案例；規則主要靠 AI 遵守與人工審查，不是程式強制

## 公開檢查清單

| 項目 | 狀態 |
|---|---|
| MIT LICENSE | 已加入 |
| README 定位、圖表、案例與證據連結 | 已完成：英文（README.md）與繁體中文（README.zh-TW.md）兩版，圖表也各有兩種語言（PR #6） |
| 文件檢查 CI | 已完成：PR #6 的 GitHub Actions `validate` 通過 |
| ipas-learning-hub 轉為 public | 已完成：案例研究連到 `5891f4c` 的頁面可正常開啟（2026-11-18 抽查回應 200） |
| ipas-learning-hub 的 AGENTS.md 把本模板寫成「私人」 | 已完成：ipas `aaa7e87` 已改為「公開」 |
| GitHub description 與 topics 更新為目前定位 | 已完成：2026-11-18 經作者同意更新 description，topics 為 agents-md、ai-assisted-development、claude-code、documentation-template、methodology、spec-driven-development |
| 機敏資料掃描（個人路徑、email、密鑰） | 已完成：2026-11-18 以 git grep 掃描追蹤檔案，無命中（只有範本中談 LLM「tokens」長度的一行）；屬於樣式比對，不取代人工檢查 |
