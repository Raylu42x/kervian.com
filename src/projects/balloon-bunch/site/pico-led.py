import network
import time
from machine import Pin

# ---------------- CONFIG ----------------
SSID = "Bibliotheca"
PASSWORD = "ilikebooks"
LOG_INTERVAL = 1          # seconds
RUN_TIME = 45 * 60        # 1.5 hours
LOG_FILE = "wifi_log.csv"
# ----------------------------------------

# Pico W LED
led = Pin("LED", Pin.OUT)

def blink(times, delay=0.2):
    for _ in range(times):
        led.on()
        time.sleep(delay)
        led.off()
        time.sleep(delay)

# ---------------- BOOT INDICATOR ----------------
blink(10, 0.1)  # fast blink = starting

# ---------------- CONNECT TO WIFI ----------------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

timeout = 20  # seconds
start = time.time()

while not wlan.isconnected():
    if time.time() - start > timeout:
        # ERROR: Wi-Fi failed
        while True:
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
    time.sleep(0.1)

# Wi-Fi connected
led.on()
print("Connected! IP:", wlan.ifconfig()[0])

# ---------------- INITIALIZE MEMORY LOG ----------------
rssi_log = []
start_time = time.time()
print("Logging RSSI...")

# ---------------- MAIN LOOP ----------------
while time.time() - start_time < RUN_TIME:
    rssi = wlan.status('rssi')
    elapsed = int(time.time() - start_time)

    # Store elapsed seconds + RSSI (RAM safe)
    rssi_log.append((elapsed, rssi))

    # Debug output
    print(elapsed, "s:", rssi, "dBm")

    # LED heartbeat (short blink)
    led.off()
    time.sleep(0.05)
    led.on()

    time.sleep(LOG_INTERVAL)

# ---------------- FINISHED LOGGING ----------------
led.off()
blink(5, 0.1)  # finished indicator

# ---------------- SAVE TO FILE ----------------
print("Saving CSV...")

with open(LOG_FILE, "w") as f:
    f.write("seconds,rssi\n")
    for t, r in rssi_log:
        f.write(f"{t},{r}\n")

print("Saved", len(rssi_log), "entries")

# ---------------- IDLE ----------------
# Slow blink = done, safe to power off
while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(2)
