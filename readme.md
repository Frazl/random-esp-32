# Overview

- Install the CP210 driver by going to drivers/cp210 and right clicking silabser.inf and clicking install.
 - This makes the ESP32-S3 chip appear as a communications device (COMS5 for me) in device manager.
- pip install the requirements
- plug in the device USB-C to USB-A (into PC)
- run the erase script
- run the firmware script 


## Links 

- https://heltec.org/project/wifi-kit-32-v3/
 - Schematics: https://resource.heltec.cn/download/WiFi_Kit_32_V3/HTIT-WiFi%20kit32_V3(Rev1.1).pdf
    - Most accurate = https://resource.heltec.cn/download/WiFi_Kit_32_V3/HTIT-WB32_V3_Schematic_Diagram.pdf
- https://docs.micropython.org/en/latest/esp8266/tutorial/index.html#esp8266-tutorial
 - https://docs.micropython.org/en/latest/esp32/tutorial/intro.html