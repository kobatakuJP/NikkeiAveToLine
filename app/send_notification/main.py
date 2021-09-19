import os
from datetime import datetime as dt
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

def send_notification(timestamp: dt, value: float):
    send_line_bot(timestamp.strftime('%Y/%m/%d %H:%M') + "ごろ: " + str(value))

def send_line_bot(s):
    line_bot_api = LineBotApi(os.getenv("LINEBOT_ACCESS_TOKEN"))
    line_bot_api.broadcast(TextSendMessage(text=s))
