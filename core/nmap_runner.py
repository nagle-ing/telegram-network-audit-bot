import subprocess

def scan_host(ip):
    try:
        result = subprocess.run(
            ["nmap", "-Pn", "--open", "-p", "1-1024", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=90
        )

        # Si nmap devolvió algo útil, lo usamos
        if result.stdout.strip():
            return result.stdout

        # Si no hay stdout, devolvemos el error para debug
        return f"ERROR: {result.stderr}"

    except subprocess.TimeoutExpired:
        return "ERROR: Tiempo de escaneo excedido"
    except Exception as e:
        return f"ERROR: {str(e)}"
