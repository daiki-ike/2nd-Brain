ユーザー名
tsubox
ドメイン名
@69tsubox.onmicrosoft.com
パスワード
p6NUdLVY

ユーザー名
seisaku
ドメイン名
@69tsubox.onmicrosoft.com
パスワード
 Y^520485879528ad 

privacy@
PW：Test0351172425


**「365併用で社内POPとも送受信するための2手順」を、運用メモとしてそのまま貼れる形でまとめます。**

---

## ① 既存メールを Microsoft 365（Exchange）へ転送する手順

（例：privacy@tsu-box.com を 365 で使う）

### 目的

- MXは変更せず
    
- **既存サーバーで受信 → 365へ転送** して使う
    

### 手順（既存メールサーバー側）

1. 既存メールサーバーの管理画面にログイン
    
2. 対象アドレス：
    
    `privacy@tsu-box.com`
    
3. 設定内容：
    
    - 転送（Forward）を有効化
        
    - **転送先：**
        
        `privacy@＜テナント名＞.onmicrosoft.com`
        
        （例：privacy@69tsubox.onmicrosoft.com）
        
4. 初期テスト時は
    
    - **「転送＋サーバーにも保存」** を推奨
        
5. Gmail 等から privacy@ に送信し、
    
    - **Outlook（365）で受信できることを確認**
        

### 注意点

- 転送先を **privacy@tsu-box.com にすると転送ループになる（NG）**
    
- onmicrosoft.com は **内部用の実体アドレス**（対外的には使わない）
    

---

## ② Exchange に「同じ社内メール」を Mail Contact 登録する手順

（例：daiki@tsu-box.com に返信できるようにする）

### 目的

- **365（Exchange）から、既存POP運用の社内アドレスへ送信可能にする**
    

### 手順（Exchange 管理センター）

1. 管理センターにログイン  
    [https://admin.exchange.microsoft.com](https://admin.exchange.microsoft.com)
    
2. 左メニュー  
    **［受信者］→［連絡先］**
    
3. **［＋ 連絡先を追加］** をクリック
    
4. 以下を入力
    
    - 表示名
        
        `池田 大希（POP）`
        
    - エイリアス
        
        `daiki`
        
    - 外部電子メール アドレス
        
        `daiki@tsu-box.com`
        
5. 確認 → 作成
    

### 結果

- Exchange は
    
    - daiki@tsu-box.com を  
        **「外部宛の正しい配送先」** と認識
        
- privacy@（365）→ daiki@（既存POP）  
    → **エラーなく送信可能**
    

### 注意点

- 人が増えるたびに **Mail Contact を追加する必要あり**
    
- 少人数・限定用途向けの回避策
    

---

## 運用上の整理（重要）

- privacy@tsu-box.com
    
    - 受信：既存 → 転送 → 365
        
    - 送信：
        
        - 社外：そのままOK
            
        - 社内（POP）：Mail Contact 登録済みならOK
            
- MX変更：**不要**
    
- 全社365移行：**不要**
    

---

### 一文まとめ（貼り用）

> **「MXは変えず、既存サーバーで転送＋ExchangeにMail Contact登録することで、  
> 一部ユーザーのみ365を使いながら社内POPとも送受信できる」**


