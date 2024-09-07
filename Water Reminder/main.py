from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title='Please drink water Now!',
            message='Please drink water for your own safety',
           app_icon='D:\\Python Projects\\Water Reminder\\icon.ico',# Replace with the path to your PNG file
            timeout=10
        )
        time.sleep(60*60)
