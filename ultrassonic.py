import machine
import time
import hcsr04
import neopixel

rgb = neopixel.NeoPixel(machine.Pin(21), 64)
led = machine.Pin(2, machine.Pin.OUT)
i = 64
n = i

red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)

#clear LED

def clear():
  for i in range(n):
    rgb[i] = (0, 0, 0)
    rgb.write()

clear()

#set LED color

def set_color(r, g, b):
  for i in range(n):
    rgb[i] = (r, g, b)
  rgb.write()

set_color(255,0,0) #red

#ultrassonic 

ultrassonic = hcsr04.HCSR04(
    trigger_pin=25,
    echo_pin=33,
    echo_timeout_us=1000000)

start_time = time.ticks_ms()
interval = 1000

while True:
    distance = ultrassonic.distance_cm()
    if time.ticks_ms() -  start_time >= interval:
        start_time = time.ticks_ms()
        if (distance >= 50): # >= 800
            led.on()
            set_color(0,255,0) #green
            print('Distance:',distance,'cm - Free Flow')
        elif (distance >= 20): # >= 100 && <= 50 
            set_color(255,255,0) #yellow
            print('Distance:',distance,'cm - Caution Flow')
            led.off()
        elif (distance <= 10): # <= 50
            set_color(255,0,0) #red
            print('Distance:',distance,'cm - Stopped Flow')
        else:
            print('Nothing to do')
            clear()
    

