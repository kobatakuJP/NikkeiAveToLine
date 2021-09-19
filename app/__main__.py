from datetime import datetime as dt

if __name__ == "__main__":
    from .get_value.main import get_latest_close
    latest = get_latest_close()
    if latest is not None:
        print(latest)
        from .send_notification.main import send_notification
        send_notification(dt.fromtimestamp(
            latest["timestamp"]/1000), latest["close"])
