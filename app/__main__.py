from datetime import datetime as dt
from datetime import timezone as tz
from datetime import timedelta as td

if __name__ == "__main__":
    def is_today(datetime):
        return datetime.strftime('%Y%m%d') == dt.now(tz(td(hours=9))).strftime('%Y%m%d')

    def create_str(timestamp: dt, close: float):
        from .get_value.main import get_yesterday_close
        yest = get_yesterday_close()
        yest_close = yest.get("close", 0)
        lines = [
            timestamp.strftime('%Y/%m/%d %H:%M') + "ごろ:",
            str('{:.2f}'.format(close))
        ]
        if yest_close > 0:
            sa = close - yest_close
            lines.append("前終値比:" + str('{:.2f}'.format(sa)) +
                         "(" + str('{:.2f}'.format(sa / yest_close * 100)) + "%)")
        return "\n".join(lines)
    from .get_value.main import get_latest_close
    latest = get_latest_close()
    if latest is not None:
        print(latest)
        datetime = dt.fromtimestamp(
            latest["timestamp"]/1000, tz=tz(td(hours=9)))
        if is_today(datetime):
            from .send_notification.main import send_notification
            send_notification(create_str(datetime, latest["close"]))
        else:
            print("not today")
    else:
        print("no data")
