import os
from datetime import datetime as dt
from linebot import LineBotApi
from linebot.models import TextSendMessage


def send_notification(timestamp: dt, value: float):
    send_line_bot(timestamp.strftime('%Y/%m/%d %H:%M') + "ごろ: " + str(value))


def send_line_bot(s):
    notifi_func = get_notification_function()
    notifi_func(TextSendMessage(text=s))


def get_notification_function():
    if (os.getenv("DEBUG") == "true"):
        print("debug")
        return lambda mes: LineBotApi(os.getenv("LINEBOT_ACCESS_TOKEN")).push_message(os.getenv("MY_LINE_ID"), mes)
    else:
        return prd_notification_function


def prd_notification_function(mes):
    """
    broadcastとマルチキャストを行う
    """
    line_bot_api = LineBotApi(os.getenv("LINEBOT_ACCESS_TOKEN"))
    line_bot_api.broadcast(mes)
    for id in os.getenv("MULTI_CAST_LINE_IDS", "").split(":"):
        if id != "" and id is not None:
            line_bot_api.push_message(id, mes)
