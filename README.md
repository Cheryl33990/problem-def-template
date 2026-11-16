---
title: problem-def-template
status: in-review
updated: 2026-11-16
---

# problem-def-template

協助你從自然語言描述的困擾開始，逐步釐清問題、範圍與成功條件，再進行實作、驗證與 review。

**先讀 [使用指南](docs/workflow/guide.md)。** 不需先知道怎麼寫 PRD，也不需先安裝程式。AI 的共同入口為 [AGENTS.md](AGENTS.md)。

## 專案配置

```text
.
├── README.md
├── AGENTS.md
├── .github/                    PR 格式與專案自己的 CI
├── src/                        程式碼（目前只有空目錄標記）
├── tests/                      可執行測試（目前只有空目錄標記）
└── docs/
    ├── project/
    │   ├── brief.md            問題、範圍、AC；開始時可未知
    │   └── progress.md         當前進度、路徑對照與下一步
    ├── workflow/
    │   ├── guide.md            唯一使用入口
    │   ├── reference/          需要時查閱的詳細規則
    │   ├── templates/          按需複製的空白範本
    │   └── examples/           教學示例
    └── template-maintenance/   模板自身的歷史與維護資料
```

只有兩份專案紀錄預先建立：[brief](docs/project/brief.md)、[progress](docs/project/progress.md)。其他文件依實際問題建立；範本庫不是專案待辦，不用逐一填完。
既有專案保留原本 app、packages、src、tests 等框架慣例，以 progress 記實際路徑。

模板目前提供文件與 PR 格式，沒有應用程式、測試執行器或 CI。真實可用性仍待案例驗證。
模板維護者查看 [維護入口](docs/template-maintenance/README.md)；衍生專案可按使用指南移除這一區。
