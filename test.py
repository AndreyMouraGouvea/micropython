import machine
import time

LED = machine.Pin(2,machine.Pin.OUT)
BOOT = machine.Pin(0,machine.Pin.IN)

while True:
    BOOT_status = BOOT.value()
    if(BOOT_status == False):
        LED.value(1)
    else:
        LED.value(0)
    