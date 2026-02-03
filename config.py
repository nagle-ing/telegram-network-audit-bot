import os
import os
from dotenv import load_dotenv

load_dotenv()  # carga variables desde .env

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("❌ TELEGRAM_BOT_TOKEN no está definido")

LOGS_DIR = "logs"
LOG_FILE = f"{LOGS_DIR}/audit.log"

REPORTS_DIR = "reports"
