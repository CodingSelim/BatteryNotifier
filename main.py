import psutil
import time
from plyer import notification

def check_battery():
    battery = psutil.sensors_battery()
    if battery is None:
        print("No battery information available.")
        return
    percent = battery.percent
    plugged = battery.power_plugged

    if percent <= 20 and not plugged:
        notification.notify(
            title="Low Battery",
            message=f"Battery is at {percent}%. Please plug in your charger.",
            timeout=10
        )
    elif percent >= 95 and plugged:
        notification.notify(
            title="Battery Full",
            message=f"Battery is at {percent}%. You can unplug your charger.",
            timeout=10
        )

def start_monitoring():
    while True:
        check_battery()
        time.sleep(60)

if __name__ == "__main__":
    print("Battery monitor started...")
    start_monitoring()
