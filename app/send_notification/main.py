import os
from datetime import datetime as dt
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError


def send_notification(timestamp: dt, value: float):
    send_line_bot(timestamp.strftime('%Y/%m/%d %H:%M') + "ごろ: " + str(value))


def send_line_bot(s):
    notifi_func = get_notification_function()
    notifi_func(TextSendMessage(text=s))


def get_notification_function():
    line_bot_api = LineBotApi(os.getenv("LINEBOT_ACCESS_TOKEN"))
    if (os.getenv("DEBUG") is None):
        return line_bot_api.broadcast
    else:
        print("debug")
        return lambda mes: line_bot_api.push_message(os.getenv("MY_LINE_ID"), mes)
