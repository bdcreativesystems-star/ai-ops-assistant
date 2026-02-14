from datetime import datetime

def log(message):
    with open("logs/activity.log", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")
