from datetime import datetime as dt
from datetime import timezone as tz
from datetime import timedelta as td

if __name__ == "__main__":
    from .get_value.main import get_latest_close
    latest = get_latest_close()
    if latest is not None:
        print(latest)
        from .send_notification.main import send_notification
        send_notification(dt.fromtimestamp(
            latest["timestamp"]/1000, tz=tz(td(hours=9))), latest["close"])
    else:
        print("no data")
