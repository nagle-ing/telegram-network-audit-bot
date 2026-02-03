import subprocess
import re

async def scan(update, context):
    try:
        result = subprocess.run(["ip", "route"], capture_output=True, text=True)
        net = re.search(r"(\d+\.\d+\.\d+\.0/\d+)", result.stdout)
        if not net:
            raise Exception
        network = net.group(1)
    except:
        await update.message.reply_text("❌ No se pudo detectar la red.")
        return

    await update.message.reply_text(f"📡 Escaneando {network}")
    result = subprocess.run(["nmap", "-sn", network], capture_output=True, text=True)

    hosts = [
        l.replace("Nmap scan report for ", "")
        for l in result.stdout.split("\n")
        if "Nmap scan report for" in l
    ]

    if not hosts:
        await update.message.reply_text("⚠️ No se detectaron hosts activos.")
        return

    msg = "📡 Hosts activos:\n"
    for h in hosts:
        msg += f"✅ {h}\n"

    await update.message.reply_text(msg)
