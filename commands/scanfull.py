import subprocess
import re
from core.nmap_runner import scan_host

def get_network():
    try:
        result = subprocess.run(["ip", "route"], capture_output=True, text=True)
        match = re.search(r"(\d+\.\d+\.\d+\.0/\d+)", result.stdout)
        return match.group(1) if match else None
    except:
        return None

async def scanfull(update, context):
    network = get_network()
    if not network:
        await update.message.reply_text("❌ No se pudo detectar la red.")
        return

    await update.message.reply_text(f"📡 Escaneo completo de red: {network}\nEsto puede tardar unos minutos...")

    try:
        result = subprocess.run(
            ["nmap", "-sV", network],
            capture_output=True,
            text=True,
            timeout=300
        )
    except:
        await update.message.reply_text("❌ Error ejecutando nmap.")
        return

    hosts = {}
    current_ip = None

    for line in result.stdout.split("\n"):
        if "Nmap scan report for" in line:
            current_ip = line.replace("Nmap scan report for ", "").strip()
            hosts[current_ip] = []
        elif current_ip and "/tcp" in line and "open" in line:
            hosts[current_ip].append(line.strip())

    if not hosts:
        await update.message.reply_text("⚠️ No se detectaron hosts activos.")
        return

    msg = f"📡 *Resultados del escaneo completo*\n\n"

    for ip, services in hosts.items():
        msg += f"🖥️ {ip}\n"
        if services:
            for s in services:
                msg += f"  • {s}\n"
        else:
            msg += "  • Sin servicios abiertos\n"
        msg += "\n"

    await update.message.reply_text(msg)
