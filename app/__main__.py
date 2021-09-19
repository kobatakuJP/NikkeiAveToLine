from datetime import datetime as dt
import sys
import os
from dotenv import load_dotenv
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

load_dotenv()
line_bot_api = LineBotApi(os.getenv("LINEBOT_ACCESS_TOKEN"))


def get_latest_close():
    """ 
    最も最近の指数(単位時間の終値)のみ取得する  
    @return {timestamp: int, close: float}
    """
    my_share = share.Share(os.getenv("TARGET_STOCK_NAME"))
    symbol_data = None
    try:
        symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                              1,
                                              share.FREQUENCY_TYPE_MINUTE,
                                              1)
    except YahooFinanceError as e:
        print(e.message)
        sys.exit(1)

    if symbol_data is None:
        return None

    timestamps = symbol_data.get("timestamp", [])
    closes = symbol_data.get("close", [])
    for i in reversed(range(len(timestamps))):
        if closes is not None:
            return {"timestamp": timestamps[i], "close": closes[i]}
    return None


def send_line_bot(s):
    line_bot_api.broadcast(TextSendMessage(text=s))


if __name__ == "__main__":
    latest = get_latest_close()
    if latest is not None:
        print(latest)
        send_line_bot(dt.fromtimestamp(
            latest["timestamp"]/1000).strftime('%Y/%m/%d %H:%M') + "ごろ: " + str(latest["close"]))
