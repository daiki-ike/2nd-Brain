---
name: resale_strategist
description: Strategic assistant for resale business. Calculates profits, logs research data, and provides market insights.
input:
  action: (required) Action to perform: 'calc', 'log', 'analyze'
  price: (optional) Purchase price for calculation
  name: (optional) Product name for logging
---

# Resale Strategist

物販ビジネス（せどり・リユース）における「参謀」として、利益計算、リサーチログの記録、市場分析を支援するスキルです。
感情に流されず、数字に基づいた意思決定（GO/NO-GO）をサポートします。

## Capabilities

### 1. Profit Calculation (利益計算)
仕入れ値と想定売値を入力すると、FBA手数料や送料を考慮した純利益と損益分岐点を即座に計算します。
- **Usage**: `calc` アクションを使用。

### 2. Research Logging (リサーチログ)
リサーチした商品の情報を記録し、Obsidianのデータベース（`00_システム/03_Resale/Research_Log.md` 等）に追記します。
- **Usage**: `log` アクションを使用。
- **Fields**: 商品名, 仕入値, 想定売値, 理由, 画像URL(あれば)

### 3. Market Analysis (相場分析)
(Future) Keepaの波形や市場トレンドに基づいたアドバイスを提供します。

## Instructions

1.  **Calc Process**:
    - ユーザーから「仕入値」と「想定売値」を聞き出します。
    - `scripts/profit_calculator.py` を実行して数値を算出します。
    - 「利益率 XX% です。GOですか？」と判定を促します。

2.  **Log Process**:
    - ユーザーに「商品名」「価格」「リサーチ理由」をヒアリングします。
    - `resources/research_logger_template.md` を読み込み、フォーマットを整えて追記します。

## Dependencies
- python3
