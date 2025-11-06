import network
import time
import os

# ======= CONFIGURACIÓN ==========
SSID = "Dylan :D"        # Cambia por el SSID de tu teléfono o router
PASSWORD = "uno2tres"
DISTANCIAS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # metros
MEDIDAS_POR_PUNTO = 10
ARCHIVO = "rssi.csv"

# ======= CONECTAR A WIFI =======
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print("Conectando a WiFi...")
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("\nConectado:", wlan.ifconfig())

# ======= CREAR ARCHIVO CSV =======
if ARCHIVO in os.listdir():
    os.remove(ARCHIVO)

with open(ARCHIVO, "w") as f:
    f.write("Distancia_m,RSSI_dBm\n")

# ======= MEDICIONES ==========
for d in DISTANCIAS:
    print(f"\n=== Midiendo en {d} m ===")
    rssi_vals = []
    for i in range(MEDIDAS_POR_PUNTO):
        # wlan.status('rssi') devuelve RSSI en dBm
        rssi = wlan.status('rssi')
        print(f"  Medida {i+1}: {rssi} dBm")
        rssi_vals.append(rssi)
        time.sleep(1)

    promedio = sum(rssi_vals) / len(rssi_vals)
    print(f"Promedio RSSI en {d} m: {promedio:.2f} dBm")

    with open(ARCHIVO, "a") as f:
        f.write(f"{d},{promedio:.2f}\n")

print("\nMediciones completas. Archivo guardado como", ARCHIVO)
