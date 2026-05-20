---
title: 變更紀錄
status: approved
updated: 2026-05-20
---

# Changelog

本文件採 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/) 格式，
版本號遵循 [Semantic Versioning](https://semver.org/lang/zh-TW/)。

## [Unreleased]

## [0.1.0] - 2026-05-20

### Added
- Template 初版發布：問題定義 → 探索 → 決策 → 設計 → 實作 SOP 的完整文件骨架
- 13 個資料夾（10_problem / 20_discovery / 30_decisions / 40_design / 50_implementation / 60_experiments / 99_meta 及子目錄）
- 兩份範本：[30_decisions/TEMPLATE.md](30_decisions/TEMPLATE.md)（ADR）、[60_experiments/EXP_TEMPLATE/](60_experiments/EXP_TEMPLATE/)（實驗三件組）
- 一份探索筆記範本：[20_discovery/NN_template.md](20_discovery/NN_template.md)
- Frontmatter 規範：3 必填欄（title / status / updated）+ 3 選填欄（owner / tags / related）；status 五值（draft / in-review / approved / archived / deprecated）
- [USAGE.md](USAGE.md) — 衍生新專案後的初始化清單
- [CLAUDE.md](CLAUDE.md) — 給 AI session 的工作規則（含「動手前必讀」與「禁止事項」）

### Notes
- 所有骨架檔的 TODO 都明確標示「該填什麼 / 參考哪裡 / 完成後改 status」，方便人機接手。
