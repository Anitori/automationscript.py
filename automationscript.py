import schedule
import time
import subprocess

def run_script():
    subprocess.run(["python3", "NOMBRE DE TU SCRIPT"])  # Reemplaza con la ruta completa si es necesario

# Programa la ejecución cada 30 minutos
schedule.every(30).minutes.do(run_script)

print("Ejecutando el script cada 30 minutos. Presiona Ctrl+C para detener.")

while True:
    schedule.run_pending()
    time.sleep(1)
