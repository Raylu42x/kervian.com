import network
import time
import os

# ---------------- CONFIG ----------------
SSID = "YOUR_WIFI_SSID"
PASSWORD = "YOUR_WIFI_PASSWORD"
LOG_INTERVAL = 1          # seconds
RUN_TIME = 90 * 60        # 1.5 hours in seconds
MAX_LOG_ENTRIES = RUN_TIME // LOG_INTERVAL
LOG_FILE = "wifi_log.csv"
# ----------------------------------------

# ---------------- CONNECT TO WIFI ----------------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
while not wlan.isconnected():
    time.sleep(0.1)

print("Connected! IP:", wlan.ifconfig()[0])

# ---------------- INITIALIZE MEMORY LOG ----------------
rssi_log = []

start_time = time.time()
print("Logging RSSI every second for 1.5 hours...")

# ---------------- MAIN LOOP ----------------
while time.time() - start_time < RUN_TIME:
    rssi = wlan.status('rssi')
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    rssi_log.append((timestamp, rssi))
    
    # Optional: print current RSSI to serial
    print(timestamp, rssi, "dBm")
    
    time.sleep(LOG_INTERVAL)

# ---------------- SAVE TO FILE AFTER RUN ----------------
print("Logging complete. Saving to CSV...")

with open(LOG_FILE, "w") as f:
    f.write("timestamp,rssi\n")
    for timestamp, rssi in rssi_log:
        f.write(f"{timestamp},{rssi}\n")

print(f"Saved {len(rssi_log)} entries to {LOG_FILE}")
