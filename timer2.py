import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

start_time = time.ticks_ms()
interval = 1000
led_state = 0

while True:
    if time.ticks_ms() -  start_time >= interval:
        start_time = time.ticks_ms()
        if (led_state == 1):
            led_state = 0
        else:
            led_state = 1
        led.value(led_state)
