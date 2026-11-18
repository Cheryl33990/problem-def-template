---
title: 模板改善進度
status: in-review
updated: 2026-11-18
---

# 模板改善進度

PR #1、#2 已合併。問題釐清、文件流程與 review 基礎已建立。
本輪將程式、專案紀錄與工作指南分區，根目錄只留 README 與 AGENTS 作文字入口；空白範本按需取用，另保存遷移與檢查紀錄。
PR #3 尚未合併，本輪納入其實驗狀態、prompt 契約及追溯欄位修正；不需再套用舊位置的重複修改。
進行中案例 ipas-learning-hub 已完成（見 [pilot](pilot.md) 與[案例研究](../about/case-study-ipas.md)）；回放案例、一週後接手與時間量測仍未做。
公開準備：加入 MIT 授權、README 圖表與案例、證據對照與狀態頁、文件檢查 CI（連結與錨點、frontmatter、已確認須有日期、validation 判定與證據欄位、圖表）、單元測試與 init-smoke，以及 progress 輪替規則。部署不適用。

## 目前階段與前進判斷（2026-11-18）

本輪模板維護進度記在此處；docs/project 的 brief、progress 保留為衍生專案起點。

| 任務／範圍 | 目前階段 | 最小產出／證據 | 未達條件／限制 | 前進判斷 | 下一個動作 |
|---|---|---|---|---|---|
| 檢查擴充及圖文一致性；使用者 2026-11-18 授權 | 審查與交付 | feat/validate-compliance；原有變更已保留；23 項測試、50 份文件檢查與 40 份初始化副本檢查通過，見下方紀錄 | 瀏覽器目視與遠端 CI 尚未驗證；負責人尚未驗收／合併 | 可送 Draft PR；不代表真人批准、驗收或結案 | AI 提交與推送並於 PR 記精確被測 commit；負責人決定合併 |

測法先定：保留方框配置，以兩行檢查說明容納新增項目；檢查 SVG 文字邊界與兩語系對等。初始化只在暫存副本移除模板材料。成功條件依本輪使用者指示，不變更既有檢查契約或歷史 CHANGELOG；合併由負責人決定。

## 本輪結果與 AI review（2026-11-18）

- 被測版本：基底 `9d2f6b75d250ac22d68a5d0ed41702073f649bf0` 加本輪工作目錄差異；提交後的重驗結果與精確 commit 記於 Draft PR。
- `python -m unittest discover -s tools -p "test_*.py"`：23 tests，OK；`python tools/validate.py`：50 份 Markdown 的 links、frontmatter、anchors、maturity、validation records 及 diagrams 全為 ok。
- 初始化：用 `git ls-files` 複製目前追蹤檔案到系統暫存目錄，只在副本刪除 docs/about、docs/template-maintenance、tools/render_diagrams.py、README.zh-TW.md；README 換成僅連 AGENTS 與 guide 的最小內容。副本執行 `python tools/validate.py`：40 份 Markdown 全為 ok。此時 diagrams 依設計略過，不能解讀成已驗證刪除後的圖表。
- `python tools/render_diagrams.py`：重產 16 檔，只有四版 framework-map 內容改變；XML 解析與產生器比對皆通過。四版各 11 段列內文字依產生器字寬估算及座標檢查均在方框內；方框位置、尺寸與整體結構不變。此為靜態估算，不等於瀏覽器字型量測。
- 全域搜尋僅留下 CHANGELOG「公開準備」的歷史描述及 AGENTS 複製範本說明的非檢查清單匹配；歷史條目未改。兩版 README 的檢查表、驗證段落及 alt 意義對等。`git diff --check` 通過。

| 嚴重度 | 位置／觸發情境與影響 | 處理與驗證 |
|---|---|---|
| 低 | render_diagrams.py、兩版 README、improvement_plan：舊清單漏列新增檢查，使讀者低估 CI 範圍 | 已同步清單、alt 與 SVG；重產及一致性檢查通過 |
| 低 | framework-map 說明變長可能超出既有方框 | 已在原方框內分為兩行，路徑加入 test_validate.py；靜態邊界檢查通過，目視仍待補 |
| 資訊／證據限制 | Chrome 最小化；Edge 的電腦操作工具無法可靠辨識網址並停止操作 | 四版瀏覽器目視未完成，未宣稱視覺驗證通過 |

AI review 範圍含上一輪完整程式、23 項測試、CI、文件差異及本輪產生器／SVG；未發現其他本輪阻擋交付的問題，結論為可送 Draft PR，非真人批准。簡化 Markdown 解析不代表完整 GitHub 語法相容性，未另做全語法或多 Python 版本測試。已知限制維持：只檢查證據欄位，不驗真偽或 commit 存在；ipas-learning-hub `0435c35` 的 2 列日期及 13 份舊格式紀錄問題沿用 EVIDENCE 記錄，本輪未重跑該案例。

回復方式：由負責人另建 revert commit 撤回本輪變更；不 reset 或改寫歷史。部署不適用；尚未合併、驗收或結案。
