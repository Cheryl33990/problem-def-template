---
title: 25_approach 候選方法
status: draft
updated: 2026-05-20
tags: [approach, overview]
---

# 25_approach/

本資料夾收錄**候選方法比較**。SOP 的中介階段——介於 `20_discovery/`（已知事實）
與 `30_decisions/`（已下決定）之間，用來把「為什麼選 A 不選 B、C」的過程留下來。

> 沒有這層，ADR 容易看起來「一拍腦袋就決定」；有這層，ADR 的 Decision 可以直接引用本資料夾的對比結果。

## 內容

| 檔案 | 用途 |
|---|---|
| [options.md](options.md) | 候選方法清單：每個方法的核心想法、優點、限制、不確定性 |
| [tradeoffs.md](tradeoffs.md) | 跨方法對比矩陣：用一致的維度評分 |

## 何時使用本資料夾

- 當有「不只一種合理做法」時，**先**把候選方法寫進 `options.md`、對比寫進 `tradeoffs.md`，**再**進 `30_decisions/` 開 ADR
- 當問題只有單一明顯做法時，可以跳過本資料夾，直接在 ADR 的「Alternatives Considered」段帶過
- 規則：ADR 的 Decision 若引用本資料夾，本資料夾的 status 應為 `approved`

## 與其他資料夾的關係

- 上游：`20_discovery/` 的探索筆記提供「現況」與「資料樣態」
- 下游：`30_decisions/` 的 ADR 引用本資料夾的對比結果作為決策依據
- 平行：`60_experiments/` 可被用來驗證某個候選方法是否真的可行

## 寫作原則

<!-- TODO: 此處填本資料夾的寫作慣例
     建議內容：
       - 候選方法至少列 2 個（只有 1 個就不是「選擇」了）
       - 每個方法用同一套評估維度，避免被優劣偏見影響
       - 「為什麼否決」要誠實，不要為了讓最終選擇看起來合理而美化
     完成後將 status 從 draft 改為 in-review -->
