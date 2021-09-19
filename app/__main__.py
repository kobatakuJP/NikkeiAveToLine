from datetime import datetime as dt
import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi(os.getenv("LINEBOT_ACCESS_TOKEN"))

def send_line_bot(s):
    line_bot_api.broadcast(TextSendMessage(text=s))

if __name__ == "__main__":
    from .get_value.main import get_latest_close
    latest = get_latest_close()
    if latest is not None:
        print(latest)
        send_line_bot(dt.fromtimestamp(
            latest["timestamp"]/1000).strftime('%Y/%m/%d %H:%M') + "ごろ: " + str(latest["close"]))
