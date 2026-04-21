import os

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def main() -> None:
    # .env ファイルを読み込み、環境変数を使えるようにする
    load_dotenv()

    # Slack Bot Token を環境変数から取得する
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        raise ValueError("SLACK_BOT_TOKEN が .env に設定されていません。")

    # Slack API を呼び出すためのクライアントを作成する
    client = WebClient(token=token)
    channel_name = "#general"

    # ターミナルで送信したいメッセージを受け取る
    message = input("送信するメッセージを入力してください: ").strip()
    if not message:
        raise ValueError("メッセージが空です。文字を入力して再実行してください。")

    try:
        # chat_postMessage で指定チャンネルに投稿する
        response = client.chat_postMessage(
            channel=channel_name,
            text=message,
        )
        print(f"送信成功: channel={channel_name}, ts={response['ts']}")
    except SlackApiError as e:
        # 失敗時は Slack 側のエラー内容を表示する
        print(f"送信失敗: {e.response['error']}")


if __name__ == "__main__":
    main()
