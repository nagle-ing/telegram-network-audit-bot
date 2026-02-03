from core.validators import is_valid_ip
from core.nmap_runner import scan_host
from core.logger import log_action

async def host(update, context):
    if not context.args:
        await update.message.reply_text("Uso: /host IP")
        return

    ip = context.args[0]
    if not is_valid_ip(ip):
        await update.message.reply_text("❌ IP inválida")
        return

    output = scan_host(ip)
    if not output:
        await update.message.reply_text("❌ Error ejecutando nmap")
        return

    ports = [l for l in output.split("\n") if "/tcp" in l and "open" in l]

    if not ports:
        msg = (
            f"📍 {ip}\n"
            "✅ No se detectaron servicios abiertos.\n"
            "Posible firewall o host endurecido."
        )
        log_action(update.effective_user.username, "HOST", ip, "SIN SERVICIOS")
    else:
        msg = f"📍 Servicios en {ip}:\n\n" + "\n".join(ports)
        log_action(update.effective_user.username, "HOST", ip, "SERVICIOS DETECTADOS")

    await update.message.reply_text(msg)
