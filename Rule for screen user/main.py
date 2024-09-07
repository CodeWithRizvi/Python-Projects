import time
from plyer import notification
import pyttsx3

def remind_20_20_20():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Notification details
    title = "20-20-20 Rule Reminder"
    message = "Look at something 20 feet away for 20 seconds."

    # Notify and say reminder
    notification.notify(
        title=title,
        message=message,
        app_icon='D:\\Python Projects\\Rule for Screen\\Eyes.ico',
        timeout=20  # Duration the notification stays on the screen
    )
    
    # Speak the reminder
    engine.say("Muhammad Abdullah Rizvi .Look at something 20 feet away for 20 seconds.")
    engine.runAndWait()

def start_reminder():
    while True:
        remind_20_20_20()
        time.sleep(15*60)  # Wait for 20 minutes

#Uncomment the line below to start the reminder
start_reminder()