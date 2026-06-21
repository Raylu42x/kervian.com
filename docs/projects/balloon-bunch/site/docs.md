# This folder is where the scripts for the wifiman project is

## pico-old
this is the script made for the pico but it is an old version that doesnt have led debugging. it still uses memory for storage than flashes it to flash storage after the set time to not waste battery or flash cycles.

## pico-led
this is the same version as the old one but it includes led debugging:
LED pattern:Meaning
Fast blink (0.2s):booting / starting
Solid:ON Wi-Fi connected
Short blink every second:Logging RSSI
Rapid blink (5×):Finished logging

## zero
this programs if for the zero. it hosts a website on port 5000 that shows current db and the last ones that are saved to the file.
