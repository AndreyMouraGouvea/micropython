'''
- connect private network

import network

wifi = network.WLAN(network.AP_IF)
wifi.active(True)

wifi.config(essid = 'wifiname',password = '*******', authmode=network.AUTH_WPA_WPA2_PSK)

print(wifi.ifconfig())

'''

'''
- connect open network

import network

wifi = network.WLAN(network.AP_IF)
wifi.active(True)

wifi.config(essid = 'wifiname')

print(wifi.ifconfig())

'''


''' 
- get networks near by

import network

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

networks = wifi.scan()

print(networks)
'''

''' 
- connecting wifi with timeout
import network
import time

timeout = 0

wifi = network.WLAN(network.STA_IF)

#restarting WiFi
wifi.active(False)
time.sleep(0.5)
wifi.active(True)

wifi.connect('wifiname','*****')

if not wifi.isconnected():
    print('Connecting...')
    while(not wifi.isconnected() and timeout < 5):
        print (5 - timeout)
        timeout = timeout + 1
        time.sleep(1)
        
if (wifi.isconnected()):
    print('Connected')
else:
    print('Time Out')
'''

'''
- connect to website
- help('modules')
import network
import time
import urequests

timeout = 0

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

networks = wifi.scan()

print(networks)

wifi.connect('wifi_name','***')

if not wifi.isconnected():
    print('Connecting...')
    while (not wifi.isconnected() and timeout < 5):
        print(5 -  timeout)
        timeout = timeout + 1
        time.sleep(1)

if(wifi.isconnected()):
    print('Connected')
    req = urequests.get('https://')
    print(req.status_code)
    print(req.text)
else:
    print('Time Out')
    print('Not Connected')

'''

'''
- BLYNK IOT PROJECT


import network
import urequests
import time
from machine import Pin

button_status = 0
button_flag = 0
status = 0

button = Pin(0,Pin.IN)

def connect_wifi():
    wifi = newtwork.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.disconnect()
    wifi.connect('wifi_name','password')
    if not wifi.isconnected():
        print('Connecting')
        timeout = 0
        while (not wifi.isconnected() and timeout < 5):
            print(5 - timeout)
            timeout = timeout + 1
            time.sleep(1)
        if(wifi.isconnected()):
            print('Connected')
        else:
            print('Not connected')
            
def buttons_irq(pin):
    global button_status
    global button_flag
    button_status = not button_status
    button_flag = 1
    
button.irq(trigger=Pin.IRQ_FALLING, handler=buttons_irq)

connect_wifi()

while True:
    if (button_status == True and button_flag == 1):
        req = urequests.get('blynk link')
        button_flag = 0
        Status = req.status_code
        if(Status = 200):
            print('Request successful')
            print('Light Off')
            req.close()
    elif (button_status == False and button_flag == 1):
        req = urequests.get('blynk link')
        button_flag = 0
        Status = req.status_code
        if (Status == 200):
            print('Request successful')
            print('Light On')
            req.close()
'''
