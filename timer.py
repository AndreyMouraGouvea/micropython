import machine

led = machine.Pin(2, machine.Pin.OUT)
reboot = machine.Pin(0, machine.Pin.IN)
'''
def handle_interrupt(pin):
    led.value(not led.value())

reboot.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)
'''

time0 = machine.Timer(0)

time0.init(period=2000, mode=machine.Timer.PERIODIC, callback=lambda t: led.value(not led.value()))
#timer.ONE_SHOT

