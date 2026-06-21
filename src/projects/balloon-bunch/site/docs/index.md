# Balloon Bunch Wifiman — Scripts

Python scripts for the Raspberry Pi Pico and Pi Zero used in the Balloon Bunch project — a high-altitude Wi-Fi signal logger carried by helium balloons.

## pico-old.py

Original Pico script without LED debugging. Logs Wi-Fi RSSI to memory, then flushes to flash storage after a set interval (to reduce battery draw and flash wear cycles).

## pico-led.py

Same as `pico-old.py` but adds LED status indicators:

| LED Pattern | Meaning |
|---|---|
| Fast blink (0.2s) | Booting / starting |
| Solid on | Wi-Fi connected |
| Short blink every second | Logging RSSI |
| Rapid blink (5×) | Finished logging |

## zero.py

Script for the Raspberry Pi Zero. Hosts a web dashboard on port 5000 showing the current Wi-Fi database and previously saved scans.
