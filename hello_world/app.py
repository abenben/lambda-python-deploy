import json
import requests
import slackweb
import os

# 環境変数取得
# channel_list = os.environ.get("CHANNEL_LIST").split(",")
# channel_list = ["https://hooks.slack.com/services/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"] # STAR
channel_list = ["https://hooks.slack.com/services/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"] # テスト用


def post_slack(channel, msg):
    """
    SLackへの通知
    :param channel:Slackのチャンネル
    :param msg:Slackへの出力
    """
    slack = slackweb.Slack(url=channel)
    slack.notify(attachments=[{"color": "info", "text": msg}])


def lambda_handler(event, context):
    try:
        ip = requests.get("http://checkip.amazonaws.com/")
        for channel in channel_list:
            try:
                post_slack(channel, "TEST")
            except Exception as e:
                post_slack(channel, "TEST")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.text.replace("\n", "")
        }),
    }
