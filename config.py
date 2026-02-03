import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("❌ TELEGRAM_BOT_TOKEN no está definido")

LOGS_DIR = "logs"
LOG_FILE = f"{LOGS_DIR}/audit.log"

REPORTS_DIR = "reports"
