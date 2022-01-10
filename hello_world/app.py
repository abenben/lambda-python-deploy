"""アプリテスト1"""
import json
import requests
import slackweb

# 環境変数取得
# channel = os.environ.get("CHANNEL_LIST").split(",")
channel = "https://hooks.slack.com/services/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"  # STAR
channel = "https://hooks.slack.com/services/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"  # テスト用


def post_slack(channel, msg):
    """SLack通知

    Slackのチャンネルに通知する.
    :param channel:Slackのチャンネル
    :param msg:Slackへの出力
    """
    slack = slackweb.Slack(url=channel)
    slack.notify(attachments=[{"color": "info", "text": msg}])


def lambda_handler(event, context):
    """ラムダを実行

    ラムダ関数を実行する.
    :param event:
    :param context:
    :return:
    """
    try:
        post_slack(channel, "TEST")

    except requests.RequestException as e:
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "SLack通知"}),
    }
