# Slack API メッセージ送信（Python）

このプロジェクトは、`slack_sdk` を使って Slack の `#general` チャンネルへメッセージを送信するサンプルです。  
実行時にターミナルで入力したメッセージを投稿します。

## 1. 事前準備

- Python 3 が使えること
- Slack App の Bot Token（`xoxb-...`）を取得済みであること
- Bot が投稿先チャンネル（この例では `#general`）に追加されていること

## 2. インストール

プロジェクトフォルダで、以下を実行してください。

```bash
python3 -m pip install -r requirements.txt
```

## 3. 環境変数（.env）設定

`.env.example` をコピーして `.env` を作成します。

```bash
cp .env.example .env
```

`.env` を開いて、以下のように Bot Token を設定します。

```env
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
```

## 4. 実行方法

```bash
python3 send_message.py
```

実行すると、ターミナルでメッセージ入力を求められます。

```text
送信するメッセージを入力してください:
```

入力して Enter を押すと、`#general` に投稿されます。

## 5. ファイル構成

- `send_message.py`: Slack へメッセージ送信するメインスクリプト
- `requirements.txt`: 必要ライブラリ一覧
- `.env.example`: 環境変数テンプレート
- `.gitignore`: `.env` などを Git 管理対象から除外

## 6. よくあるエラーと対処

- `ModuleNotFoundError: No module named 'dotenv'`
  - 原因: `python-dotenv` 未インストール
  - 対処: `python3 -m pip install -r requirements.txt`

- `送信失敗: not_in_channel`
  - 原因: Bot が `#general` に参加していない
  - 対処: Slack 上で Bot をチャンネルに招待する

- `送信失敗: invalid_auth` / `送信失敗: account_inactive`
  - 原因: Token が不正または無効
  - 対処: `.env` の `SLACK_BOT_TOKEN` を見直す

## 7. 補足

- Token のような秘密情報は `.env` に入れ、Git にはコミットしないでください。
- 投稿先チャンネルを変更したい場合は、`send_message.py` の `channel_name` を変更してください。
