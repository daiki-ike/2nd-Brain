# Kindle分析ツール (KindleAnalyzer) 使用マニュアル

## 📍 ツール概要
PC画面上のKindleを「撮影＆OCR」してデータ化したり、Kindle Paperwhiteの「ハイライト」を一括で取り込んだりするためのツールです。
法的リスク（DRM解除）を回避し、Windows操作の自動化によって実現しています。

**設置場所**: `99_Sbox\KindleAnalyzer`

---

## 🛠️ 事前準備 (初回のみ)

### 1. 必要なアプリのインストール
このツールは文字認識に **Tesseract-OCR** を使用します。
1.  [配布サイト](https://github.com/UB-Mannheim/tesseract/wiki) から `tesseract-ocr-w64-setup...exe` をDL＆インストール。
2.  ※インストール時に「Additional Script Data」で **Japanese** にチェックを入れること。

### 2. 環境構築
ターミナルで以下を実行し、必要なライブラリを入れます。
```powershell
cd c:\Users\daiki\Product\2nd-Brain\2nd-Brain\99_Sbox\KindleAnalyzer
pip install -r requirements.txt
```

---

## 🚀 使い方は2パターン

ツールを起動すると、モード選択画面になります。
```powershell
python main.py
```

### [1] PC画面分析 (Screen Analysis)
PC版Kindleアプリで開いているページを、自動でめくりながら撮影＆テキスト化します。図解が多い本に便利です。

1.  Kindleアプリで本を開く。
2.  ツールで `1` を選択。
3.  マウスで「範囲の左上」→ Enter、「範囲の右下」→ Enter と指示。
4.  ページ数を入力。
5.  Kindleウィンドウをクリックして待機（5秒後に開始）。
    *   **結果**: `output` フォルダに画像とテキストが保存されます。

### [2] ハイライト取込 (Import Highlights)
Paperwhiteで引いたハイライトを、Obsidianに一括取込します。

1.  Kindle PaperwhiteをUSBケーブルでPCに接続。
2.  ツールで `2` を選択。
3.  Kindleドライブ内の `Documents\My Clippings.txt` をツール画面にドラッグ＆ドロップ。
4.  Enterを押すと、**自動的にObsidianの `03_知識ベース/Source/Kindle` に保存されます**。

---

## ⚠️ 注意点
*   **私的利用のみ**: 生成されたファイルは自分自身の分析・学習目的にのみ使用してください。
*   **停止方法**: 自動撮影中に止めたいときは、ターミナルで `Ctrl+C` を押してください。
