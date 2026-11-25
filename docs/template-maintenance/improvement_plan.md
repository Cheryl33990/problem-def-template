---
title: 模板改善進度
status: in-review
updated: 2026-11-25
---

# 模板改善進度

PR #1、#2 已合併。問題釐清、文件流程與 review 基礎已建立。
本輪將程式、專案紀錄與工作指南分區，根目錄只留 README 與 AGENTS 作文字入口；空白範本按需取用，另保存遷移與檢查紀錄。
PR #3 尚未合併，本輪納入其實驗狀態、prompt 契約及追溯欄位修正；不需再套用舊位置的重複修改。
進行中案例 ipas-learning-hub 已完成（見 [pilot](pilot.md) 與[案例研究](../about/case-study-ipas.md)）；回放案例、一週後接手與時間量測仍未做。
公開準備：加入 MIT 授權、README 圖表與案例、證據對照與狀態頁、文件檢查 CI（連結與錨點、frontmatter、已確認須有日期、validation 判定與證據欄位、圖表）、單元測試與 init-smoke，以及 progress 輪替規則。部署不適用。

## 目前階段與前進判斷（2026-11-25）

| 任務／範圍 | 目前階段 | 最小產出／證據 | 未達條件／限制 | 前進判斷 | 下一個動作 |
|---|---|---|---|---|---|
| 降低 AI 變更的重複人工審查 | 審查與交付 | 使用者 2026-11-25 授權第一版方法論與單案試跑。指南、測試策略與審查規則已更新。錨點歷史回放、當版文件與初始化副本驗證通過，見下方紀錄 | 尚無審查工時、再發或程式架構案例的基準。遠端 CI 未跑，合併待負責人決定 | 可送審，單案支持自動攔截這類錯誤 | 下一個實際程式 PR 記錄介入原因與工時，並檢查正常入口與模組責任是否能減少繞路 |
| 納入形式化驗證與 UI 屬性測試的選用方法 | 審查與交付 | 使用者 2026-11-25 授權補入方法論。[測試策略](../workflow/templates/testing/test_strategy.md#property-and-formal-verification)已加入選用條件、限量試跑及合併門檻，[審查規則](../workflow/reference/review.md)與[驗證範本](../workflow/templates/testing/validation/TEMPLATE.md)已同步 | 工具與案例未試跑，人工介入與維護成本待測 | 文件可送審，工具採用待實際案例提供證據 | iPAS 候選起點是驗證引用 ID 規則，出現 UI 時序風險時再評估 Bombadil |
| 同步專案 README 與方法論交付 | 審查與交付 | [英文 README](../../README.md)與[繁中 README](../../README.zh-TW.md)已同步。使用者於 2026-11-25 授權提交、開 PR、合併及刪除工作分支。`origin/main` 已包含 PR #9 的驗證器更新，本輪 PR 集中在方法論與 README | 新 PR 的遠端 CI 與合併結果由 GitHub PR 紀錄追蹤。新增工具的專案試跑仍待執行，部署不適用 | 本機驗證通過，可提交送審 | PR 檢查通過後合併至 `main`，確認結果並移除工作分支 |

本輪驗證基底為 `eb14341` 加目前工作目錄差異。`python tools/validate.py` 檢查 50 份 Markdown，`python -m unittest discover -s tools -p "test_*.py"` 執行 23 項驗證器測試，依 `init-smoke` 模擬的初始化副本檢查 40 份 Markdown，`git diff --check` 通過。AI 自查對照四種方法的例子與證據限制，並參照 [Bombadil 重跑說明](https://antithesishq.github.io/bombadil/browser/4.1-reproducing-violations.html)、[TLA+ 工具](https://lamport.azurewebsites.net/tla/tools.html)、[Lean](https://lean-lang.org/)與 [iPAS 架構](https://github.com/Cheryl33990/ipas-learning-hub#architecture)。結果涵蓋方法論文件與模板的現有檢查，尚無新增工具的執行證據。

## AI 變更品質試跑（2026-11-25）

- 對象是 `eb14341985def89c1cb41da664e4e589b71a013c` 修正過的 `docs/workflow/templates/design/prompts/_example.prompt.md`。將該 commit 及其父版本分別用 `git archive` 解到暫存目錄，在各目錄執行 `python tools/validate.py`。父版本以原檢查執行，退出碼 0，失效錨點漏檢。修正版以含錨點檢查的版本執行，退出碼 0。
- 只把父版本的 `_example.prompt.md` 放回修正版副本，再執行同一指令。退出碼 1，診斷精確列出兩個不存在的 `#ac-01` 和 `#ac-04`。同一檢查能攔住這筆歷史錯誤，也接受修正版本。
- 對 `eb14341` 加本輪工作目錄差異執行 `python tools/validate.py`，50 份 Markdown 通過。`python -m unittest discover -s tools -p "test_*.py"` 執行 23 項驗證器測試，全數通過。依既有 `init-smoke` 流程在暫存副本移除模板維護材料並替換 README，40 份 Markdown 通過。`git diff --check` 通過。
- AI 自查對照指南、測試策略、review 與工作流程的實際 diff，確認新連結可解析、CI 描述與當前工作流程一致。試跑涵蓋文件錨點，人工審查節省工時、誤報率及程式架構效果待以實際 PR 量測。

## 前次階段與前進判斷（2026-11-18）

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
