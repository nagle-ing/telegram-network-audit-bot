SERVICE_RISKS = {
    "ssh": ("MEDIO", "Acceso remoto", "Usar llaves y deshabilitar root"),
    "http": ("MEDIO", "Servidor web", "Usar HTTPS y actualizar"),
    "https": ("BAJO", "Servidor web seguro", "Verificar certificados"),
    "ftp": ("ALTO", "Servicio inseguro", "Deshabilitar FTP"),
    "smb": ("ALTO", "Compartición Windows", "Restringir acceso"),
    "mysql": ("ALTO", "Base de datos expuesta", "No exponer a Internet"),
    "rdp": ("ALTO", "Escritorio remoto", "Usar VPN"),
    "telnet": ("CRÍTICO", "Servicio inseguro", "Deshabilitar inmediatamente")
}
