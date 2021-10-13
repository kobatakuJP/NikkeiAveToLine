import os
import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError


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


def get_yesterday_close():
    """ 
    昨日（厳密には市場開いてる直近の一個前の営業日）の終値を取得  
    @return {timestamp: int, close: float}
    """
    my_share = share.Share(os.getenv("TARGET_STOCK_NAME"))
    symbol_data = None
    try:
        symbol_data = my_share.get_historical(share.PERIOD_TYPE_WEEK,
                                              1,
                                              share.FREQUENCY_TYPE_DAY,
                                              1)
    except YahooFinanceError as e:
        print(e.message)
        sys.exit(1)

    if symbol_data is None:
        return None

    timestamps = symbol_data.get("timestamp", [])
    closes = symbol_data.get("close", [])
    is_touch = False
    for i in reversed(range(len(timestamps))):
        # 昨日なので、一個前を取る
        if closes is not None and closes[i] is not None:
            if is_touch:
                return {"timestamp": timestamps[i], "close": closes[i]}
            else:
                is_touch = True
    return None
