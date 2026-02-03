import os
from core.validators import is_valid_ip
from core.nmap_runner import scan_host
from core.risks import SERVICE_RISKS
from core.logger import log_action
from config import REPORTS_DIR

async def audit(update, context):
    if not context.args:
        await update.message.reply_text("Uso: /audit IP [txt]")
        return

    ip = context.args[0]
    export_txt = len(context.args) > 1 and context.args[1] == "txt"

    if not is_valid_ip(ip):
        await update.message.reply_text("❌ IP inválida")
        return

    output = scan_host(ip)

    if output.startswith("ERROR"):
        await update.message.reply_text(
            "❌ Error al ejecutar nmap.\n\n"
            f"Detalle técnico:\n{output}"
        )
        log_action(update.effective_user.username, "AUDIT", ip, "ERROR NMAP")
        return

    msg = f"📋 Auditoría {ip}\n\n"
    report = msg
    found = False

    for line in output.split("\n"):
        if "/tcp" in line and "open" in line:
            found = True
            parts = line.split()
            port = parts[0]
            service = parts[2].lower()

            level, risk, rec = SERVICE_RISKS.get(
                service,
                ("DESCONOCIDO", "Servicio no identificado", "Revisión manual")
            )

            block = (
                f"Puerto: {port}\n"
                f"Servicio: {service.upper()}\n"
                f"Riesgo: {level} - {risk}\n"
                f"Recomendación: {rec}\n\n"
            )

            msg += block
            report += block

    if not found:
        msg += "✅ No se detectaron servicios abiertos."
        report += "No se detectaron servicios abiertos."
        log_action(update.effective_user.username, "AUDIT", ip, "SIN SERVICIOS")
    else:
        log_action(update.effective_user.username, "AUDIT", ip, "SERVICIOS DETECTADOS")

    if export_txt:
        os.makedirs(REPORTS_DIR, exist_ok=True)
        filename = f"{REPORTS_DIR}/audit_{ip}.txt"
        with open(filename, "w") as f:
            f.write(report)
        msg += f"\n\n📄 Reporte guardado en {filename}"

    await update.message.reply_text(msg)
