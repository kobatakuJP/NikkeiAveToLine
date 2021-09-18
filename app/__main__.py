from datetime import datetime as dt
import sys
import os
from dotenv import load_dotenv
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

load_dotenv()


def getLatestValue():
    my_share = share.Share(os.getenv("TARGET_STOCK_NAME"))
    symbol_data = None
    try:
        symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                              2,
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


def printing(data):
    if data is None:
        return
    timestamps = data["timestamp"]
    open = data["open"]
    print('timestapms len=' + str(len(timestamps)))
    print('open len=' + str(len(open)))
    for i in range(len(timestamps)):
        time = dt.fromtimestamp(
            timestamps[i]/1000).strftime('%Y/%m/%d %H:%M:%S')
        print(time + ":" + str(open[i]))
    vals = ['open', 'close', 'high', 'low', 'adj_close', 'volume']
    for v in vals:
        print(v + '=' + str(data.get(v)))


latest = getLatestValue()
print(latest)
print(dt.fromtimestamp(
            latest["timestamp"]/1000).strftime('%Y/%m/%d %H:%M:%S'))