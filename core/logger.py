import datetime
from config import LOG_FILE

def log_action(user, command, target, result):
    with open(LOG_FILE, "a") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{now} | {user} | {command} | {target} | {result}\n")
