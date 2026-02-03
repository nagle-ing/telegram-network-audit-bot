from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN
from commands.scanfull import scanfull
from commands.start import start
from commands.scan import scan
from commands.host import host
from commands.audit import audit

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("scan", scan))
app.add_handler(CommandHandler("scanfull", scanfull))
app.add_handler(CommandHandler("host", host))
app.add_handler(CommandHandler("audit", audit))

print("🤖 Bot de auditoría corriendo...")
app.run_polling()
