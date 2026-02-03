async def start(update, context):
    await update.message.reply_text(
        "🤖 *Bot de Auditoría de Red*\n\n"
        "Este bot permite escanear redes locales y auditar "
        "hosts para identificar servicios expuestos.\n\n"
        "📌 *Comandos disponibles:*\n\n"
        "🔹 /scan\n"
        "Escanea la red local y muestra los hosts activos.\n\n"
        "🔹 /scanfull\n"
        "Escanea la red y muestra los puertos abiertos por cada IP.\n\n"
        "🔹 /host IP\n"
        "Muestra los servicios abiertos de una IP específica.\n"
        "Ejemplo: /host 192.168.1.10\n\n"
        "🔹 /audit IP\n"
        "Realiza una auditoría básica con riesgos y recomendaciones.\n\n"
        "🔹 /audit IP txt\n"
        "Realiza la auditoría y guarda un reporte en un archivo TXT.\n\n"
        "⚠️ *Uso responsable*: solo escanea redes propias o autorizadas."
    )
