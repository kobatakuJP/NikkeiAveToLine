import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

def send_notification(str):
    send_line_bot(str)

def send_line_bot(s):
    line_bot_api = LineBotApi(os.getenv("LINEBOT_ACCESS_TOKEN"))
    line_bot_api.broadcast(TextSendMessage(text=s))
