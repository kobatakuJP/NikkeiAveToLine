# quandl.ApiConfig.api_key = os.getenv("QUANDL_TOKEN")
# # data = quandl.get_table('MER/F1',qopts={"columns":["compnumber", "ticker"]}, paginate=True)
# data = quandl.get_table('MER/F1',paginate=True)

from datetime import datetime as dt

import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
my_share = share.Share('^N225')
symbol_data = None
try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                          10,
                                          share.FREQUENCY_TYPE_MINUTE,
                                          5)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

# print(symbol_data)

def printing(data):
    timestamps = data["timestamp"]
    open = data["open"]
    print('timestapms len=' + str(len(timestamps)))
    print('open len=' + str(len(open)))
    for i in range(len(timestamps)):
        time = dt.fromtimestamp(timestamps[i]/1000).strftime('%Y/%m/%d %H:%M:%S')
        print(time + ":" + str(open[i]))

printing(symbol_data)