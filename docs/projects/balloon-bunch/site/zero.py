#!/usr/bin/env python3
import subprocess
import time
import csv
from flask import Flask, render_template_string

# ---------- CONFIG ----------
INTERFACE = "wlan0"
LOG_FILE = "wifi_log.csv"
LOG_INTERVAL = 1  # seconds
# ----------------------------

# Function to get Wi-Fi signal
def get_signal(interface=INTERFACE):
    result = subprocess.run(["iwconfig", interface], capture_output=True, text=True)
    for line in result.stdout.split("\n"):
        if "Signal level=" in line:
            dbm = int(line.split("Signal level=")[1].split(" ")[0])
            return dbm
    return None

# Function to append to CSV
def log_signal():
    signal = get_signal()
    if signal is not None:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, signal])

# Initialize CSV with headers if it doesn't exist
try:
    with open(LOG_FILE, "r") as f:
        pass
except FileNotFoundError:
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "signal_dBm"])

# Flask web server
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Wi-Fi Signal Monitor</title>
<meta http-equiv="refresh" content="5">
<style>
body { font-family: Arial; text-align:center; padding:50px; background:#f0f0f0;}
h1 { color:#333; }
.signal { font-size:3em; color:#007700; }
table { margin:auto; border-collapse: collapse; }
td, th { border:1px solid #999; padding:5px 10px; }
</style>
</head>
<body>
<h1>Current Wi-Fi Signal</h1>
<p class="signal">{{ current_signal }} dBm</p>

<h2>Recent Measurements</h2>
<table>
<tr><th>Time</th><th>Signal (dBm)</th></tr>
{% for row in recent_data %}
<tr><td>{{ row[0] }}</td><td>{{ row[1] }}</td></tr>
{% endfor %}
</table>
</body>
</html>
"""

@app.route("/")
def index():
    # Get current signal
    current_signal = get_signal()
    # Load last 20 measurements from CSV
    recent_data = []
    try:
        with open(LOG_FILE, "r") as f:
            reader = list(csv.reader(f))
            # skip header
            for row in reader[-20:]:
                recent_data.append(row)
    except:
        pass
    return render_template_string(HTML, current_signal=current_signal, recent_data=recent_data)

if __name__ == "__main__":
    from threading import Thread

    # Thread to log signal every second
    def logger_thread():
        while True:
            log_signal()
            time.sleep(LOG_INTERVAL)

    t = Thread(target=logger_thread, daemon=True)
    t.start()

    # Run Flask web server
    app.run(host="0.0.0.0", port=5000)
