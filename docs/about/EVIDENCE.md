---
title: 證據對照
status: in-review
updated: 2026-11-18
---

# 證據對照

本模板的每個主張、規則寫在哪裡、怎麼確保被執行，以及真實案例中的證據。

這是文件與流程模板，大部分規則靠 AI 讀 [AGENTS.md](../../AGENTS.md) 後遵守，不是程式強制。能用程式檢查的部分（連結、frontmatter、圖表）由 [`tools/validate.py`](../../tools/validate.py) 在 CI 執行，兩者在下表分開標示。

## 主張與證據

| 主張 | 規則來源 | 執行方式 | 真實案例證據（ipas-learning-hub @ `5891f4c`） |
|---|---|---|---|
| 從一句困擾開始，不需要先寫 PRD | [guide](../workflow/guide.md) §2、[workflow](../workflow/reference/workflow.md)「從模糊目標開始」 | AI 遵守 AGENTS §2 | brief 保存使用者原話，先探索兩輪才定 AC（[案例](case-study-ipas.md)） |
| AI 草案、使用者沉默都不算已確認 | AGENTS §2、workflow「定義成熟度」 | AI 遵守；review 清單檢查 | brief 逐項標「暫定；AI 提案」「已確認；使用者 2026-11-16」 |
| 沒有基準就不編造數字門檻 | AGENTS §2、guide §2 | AI 遵守 | 探索二寫「樣本太小，不足以下結論」，沒有先定準確率門檻 |
| 結果不好時回到探索，不修改判準 | guide 階段表、[review](../workflow/reference/review.md) 清單「沒有偷偷改 AC」 | AI 遵守；PR 審查 | v1 三法各 5/8 → 未命中診斷 → 另建 v2，原 v1 保留 |
| 測試結果要對應被測版本，歷史 passing 不算現在 | AGENTS §4、[PR 範本](../../.github/pull_request_template.md) | PR 範本欄位；人工審查 | 每份 validation 紀錄 commit、索引雜湊、prompt 雜湊 |
| 可合併、可部署、已驗收、已結案分開 | guide 階段表、AGENTS §4 | AI 遵守 | progress 分開寫「CI 通過」「已合併」「品質驗收尚未完成」 |
| AI 自查不冒充真人批准 | AGENTS §4、review | AI 遵守 | 人工抽樣寫明「判讀者是作者本人，非獨立第三方」 |
| 文件按需要建立，範本不是待辦 | AGENTS §3、[範本庫](../workflow/templates/README.md) | AI 遵守 | 21 個 PR 只用到 5 類文件（[案例](case-study-ipas.md#實際用到哪些範本)） |
| 文件之間的相對連結都有效 | [conventions](../workflow/reference/conventions.md) | **程式**：`validate.py` links | CI |
| 每份文件都有 title、status、updated | conventions | **程式**：`validate.py` frontmatter | CI |
| README 圖表與產生程式一致 | 本頁 | **程式**：`validate.py` diagrams | CI |

## 怎麼重跑

```sh
python tools/validate.py          # 連結、frontmatter、圖表；只需 Python 3.9+，沒有第三方套件
python tools/render_diagrams.py   # 修改圖表後重新產生 SVG
```

## 已知限制

- 只有一個真實案例，而且是單人＋AI，沒有對照組。
- 規則是否被遵守主要靠 AI 與人工審查，沒有像 hook 一樣的強制機制。
- 連結檢查不檢查段落錨點與外部網址。
