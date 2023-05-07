import machine
import ssd1306
import netwoark
import urequests as requests
import json
import time


# Initialize the I2C bus
print("Setting up display...")
try:
    # Define the RST pin
    oled_rst_pin = machine.Pin(21, machine.Pin.OUT)
    # Reset the OLED
    oled_rst_pin.value(0)   # Set RST pin low
    oled_rst_pin.value(1)   # Set RST pin high
    i2c = machine.SoftI2C(sda=machine.Pin(17), scl=machine.Pin(18))
    # Initialize the OLED display object
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
except:
    print("Error setting up display")
    machine.reset()

# Set all pixels off
oled.fill(0)
oled.show()
oled.text("Test Display", 0, 10)
oled.show()
time.sleep(5)
oled.fill(0)
oled.show()

# Set up the network connection
print("Setting up Wifi...")
wifi_ssid = "Sean's iPhone"
wifi_password = ''
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
try:
    if not wifi.isconnected():
        # print('Connecting to Wi-Fi')
        wifi.connect(wifi_ssid, wifi_password)
        while not wifi.isconnected():
            continue
except:
    machine.reset()

# Print out the IP address assigned to the device by the DHCP server
# print('Device IP address:', wifi.ifconfig()[0])

# Send GET request and parse response
print("Sending joke request...")
try :
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    data = json.loads(response.text)
except:
    print("Uh oh...")
    machine.reset()

# Display joke setup for 5 seconds, then punchline for 5 seconds, then repeat
while True:
    try:
        # Display joke setup
        oled.fill(0)
        lines = [data['setup'][i:i+16] for i in range(0, len(data['setup']), 16)]
        for i, line in enumerate(lines):
            oled.text(line, 0, i*10)
        oled.show()
        time.sleep(5)
        
        # Display punchline
        oled.fill(0)
        lines = [data['punchline'][i:i+16] for i in range(0, len(data['punchline']), 16)]
        for i, line in enumerate(lines):
            oled.text(line, 0, i*10)
        oled.show()
        time.sleep(5)
    except:
        print("An error occurred")
        machine.reset()
        