---
name: trade_coach
description: Mental coach and logger for trading. Facilitates reflective journaling and emotion tracking.
input:
  action: (required) Action to perform: 'log', 'reflect'
  symbol: (optional) Trading symbol (e.g., 7203)
  pnl: (optional) Profit and Loss (+/- amount)
---

# Trade Journal Coach

株式投資（デモトレード）における「メンタル管理」と「振り返り（ジャーナリング）」を支援するスキルです。
技術的な分析よりも、意思決定のプロセスや心理状態の記録に重点を置きます。

## Capabilities

### 1. Trade Logging (トレード記録)
トレード直後の「鮮度の高い感情」と「Entry/Exitの理由」をヒアリングし、Obsidianの日誌ファイル（`05_日誌/YYYY-MM-DD.md`）の `### 💰 株式投資トレーニング` セクションに直接追記します。
- **Usage**: `log` アクションを使用。

### 2. Reflection (振り返り・壁打ち)
負けトレードや「イラッとした時」に、冷静さを取り戻すためのコーチングを行います。
- **Usage**: `reflect` アクションを使用。
- **Features**: アンガーマネジメント的な問いかけ、次回の改善点の抽出。

## Instructions

1.  **Log Process**:
    - ユーザーに `scripts/trade_logger.py` 経由で質問を投げかけます。
    - Q1: 銘柄と損益は？
    - Q2: エントリーの根拠（Setup）は？
    - Q3: 感情（Fear/Greed/FOMO）の影響はあったか？
    - この回答を日誌に書き込みます。

2.  **Reflect Process**:
    - `resources/mental_check_prompt.md` を使用し、「なぜルールを破ったのか？」等を深掘りします。
    - 最後に「明日のための誓い（Next Action）」を言わせます。

## Dependencies
- python3
