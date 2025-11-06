# 📡 Análisis de Redes WiFi con Raspberry Pi Pico 2W

Práctica desarrollada como parte del curso de **Comunicaciones Digitales** en la **Universidad Militar Nueva Granada**, con el objetivo de analizar el funcionamiento de la conectividad **WiFi** en sistemas embebidos utilizando la **Raspberry Pi Pico 2W** y el lenguaje **MicroPython**.

---

## 🧠 Objetivo

Analizar el comportamiento de las redes WiFi mediante la Raspberry Pi Pico 2W, comprendiendo la estructura de canales, la intensidad de señal (RSSI), la configuración de puntos de acceso y la adquisición de datos analógicos en un entorno IoT.

---

## ⚙️ Contenido del proyecto

| Archivo | Descripción |
|----------|--------------|
| `mac_wifi.py` | Obtiene la dirección MAC del módulo WiFi del Pico 2W. |
| `scanner_wifi.py` | Escanea las redes WiFi disponibles y muestra su canal, RSSI, BSSID y SSID. |
| `APWifipico.py` | Configura la Pico W como **punto de acceso (AP)** y servidor web local. |
| `index.html` | Interfaz web para el control del LED y visualización del valor ADC. |
| `promdistances.py` | Script para medir el **RSSI en función de la distancia**, guardar promedios en `rssi.csv` y analizar el alcance. |
| `rssi.csv` | Archivo de salida con los valores de distancia y RSSI promedio. |

---

## 🔌 Requisitos

- **Hardware:**
  - Raspberry Pi Pico 2W
  - Cable micro-USB
  - PC con Thonny o rshell
  - Fuente de voltaje variable (para probar ADC)
  - Dispositivo móvil o PC para conexión WiFi

- **Software:**
  - MicroPython (firmware actualizado)
  - Thonny IDE
  - WiFi Analyzer (Android/iOS)
  - Excel / Python / GNUPlot para graficar RSSI vs distancia

---

