'''
import machine
import time
led = machine.Pin(2, machine.Pin.OUT)

counter = 0

while (counter < 5):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(1)
    counter += 1
print("complete")
'''


import machine
import time

led = machine.Pin(2, machine.Pin.OUT) # internal led

def blink_led_ntimes(num, t_on, t_off, msg):
    counter = 0
    
    while (counter < num):
        led.on()
        time.sleep(t_on)
        led.off()
        time.sleep(t_off)
        counter += 1
    print(msg)
    
# RUN => in the terminal, blink_led_ntimes(5,0.5,0.5, 'is done')


import machine


led = machine.Pin(2, machine.Pin.OUT)
reboot = machine.Pin(0, machine.Pin.IN)

while True:
    if (sw.value() == 0):
        led.on()
    else:
        led.off()

