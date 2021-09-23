from datetime import datetime as dt
from datetime import timezone as tz
from datetime import timedelta as td

if __name__ == "__main__":
    def is_today(datetime):
        return datetime.strftime('%Y%m%d') == dt.now(tz(td(hours=9))).strftime('%Y%m%d')
    from .get_value.main import get_latest_close
    latest = get_latest_close()
    if latest is not None:
        print(latest)
        datetime = dt.fromtimestamp(
            latest["timestamp"]/1000, tz=tz(td(hours=9)))
        if is_today(datetime):
            from .send_notification.main import send_notification
            send_notification(datetime, latest["close"])
        else:
            print("not today")
    else:
        print("no data")
