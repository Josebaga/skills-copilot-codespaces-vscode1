#Analisis pc version 2
import os
import psutil
import subprocess
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

def obtener_procesos_en_ejecucion():
    procesos = []
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'username', 'memory_info']):
        try:
            procesos.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procesos

def obtener_procesos_sospechosos(procesos, palabras_clave, hashes_maliciosos):
    sospechosos = []
    for proc in procesos:
        nombre = proc.get('name', '').lower()
        exe = str(proc.get('exe', '')).lower()
        if any(p in nombre or p in exe for p in palabras_clave):
            sospechosos.append(proc)
        else:
            try:
                hash_proc = subprocess.getoutput(f'certutil -hashfile "{exe}" SHA256').splitlines()[1].strip()
                if hash_proc in hashes_maliciosos:
                    sospechosos.append(proc)
            except:
                continue
    return sospechosos

def obtener_conexiones_red():
    conexiones = []
    for conn in psutil.net_connections(kind='inet'):
        try:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
            conexiones.append(f"{conn.type} {laddr} -> {raddr} (PID: {conn.pid})")
        except:
            continue
    return conexiones

def cargar_hashes_maliciosos():
    try:
        with open("recursos/hashes_maliciosos.txt", "r") as f:
            return {line.strip() for line in f}
    except FileNotFoundError:
        print("⚠️ Archivo de hashes maliciosos no encontrado.")
        return set()

def generar_pdf(ruta, nombre_archivo, titulo, contenido):
    archivo_pdf = os.path.join(ruta, nombre_archivo)
    c = canvas.Canvas(archivo_pdf, pagesize=A4)
    ancho, alto = A4
    y = alto - 2*cm

    c.setFont("Helvetica-Bold", 16)
    c.drawString(2*cm, y, titulo)
    y -= 1*cm

    c.setFont("Helvetica", 10)
    c.drawString(2*cm, y, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y -= 1.5*cm

    for linea in contenido:
        if y < 2*cm:
            c.showPage()
            y = alto - 2*cm
            c.setFont("Helvetica", 10)
        c.drawString(2*cm, y, linea[:100])  # recorta líneas largas
        y -= 0.5*cm

    c.save()
    print(f"✅ PDF generado: {archivo_pdf}")

def main():
    ruta_salida = r"C:\Users\Joseba\Desktop\analisis forense rafa"
    os.makedirs(ruta_salida, exist_ok=True)

    palabras_clave = ['keylogger', 'bitcoin', 'miner', 'ransom', 'botnet', 'trojan']
    hashes_maliciosos = cargar_hashes_maliciosos()

    procesos = obtener_procesos_en_ejecucion()
    sospechosos = obtener_procesos_sospechosos(procesos, palabras_clave, hashes_maliciosos)
    conexiones = obtener_conexiones_red()

    # Generar contenido técnico
    contenido_tecnico = ["🔧 PROCESOS EN EJECUCIÓN"]
    for p in procesos:
        contenido_tecnico.append(f"PID: {p['pid']} | Nombre: {p['name']} | Usuario: {p.get('username', '')} | RAM: {p.get('memory_info').rss // 1024} KB")
    contenido_tecnico.append("\n🚨 PROCESOS SOSPECHOSOS:")
    if sospechosos:
        for p in sospechosos:
            contenido_tecnico.append(f"[!] PID: {p['pid']} | Nombre: {p['name']} | Ruta: {p.get('exe', '')}")
    else:
        contenido_tecnico.append("No se detectaron procesos sospechosos.")

    contenido_tecnico.append("\n🌐 CONEXIONES DE RED:")
    contenido_tecnico.extend(conexiones)

    generar_pdf(ruta_salida, "informe_tecnico.pdf", "Informe Forense Técnico", contenido_tecnico)

    # Generar contenido ejecutivo
    contenido_ejecutivo = ["📋 RESUMEN EJECUTIVO"]
    contenido_ejecutivo.append(f"Total procesos: {len(procesos)}")
    contenido_ejecutivo.append(f"Procesos sospechosos: {len(sospechosos)}")
    contenido_ejecutivo.append(f"Conexiones activas: {len(conexiones)}")

    if sospechosos:
        contenido_ejecutivo.append("⚠️ Se recomienda investigar los procesos sospechosos.")
    else:
        contenido_ejecutivo.append("✔️ No se detectaron amenazas en procesos.")

    if len(conexiones) > 50:
        contenido_ejecutivo.append("⚠️ Actividad de red elevada.")
    else:
        contenido_ejecutivo.append("✔️ Actividad de red dentro de lo esperado.")

    generar_pdf(ruta_salida, "informe_ejecutivo.pdf", "Informe Forense Ejecutivo", contenido_ejecutivo)

if __name__ == "__main__":
    main()