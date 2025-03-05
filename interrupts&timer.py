from machine import Timer, Pin

led = Pin(2,Pin.OUT)
button = Pin(0,Pin.IN)

def buttons_irq(pin):
    print("Triggered")

timer = Timer(0)

#lambda - define a function

timer.init(period=1000, mode=Timer.PERIODIC, callback = lambda t: led.value(not led.value()))

#irq - interrupt request
button.irq(trigger=Pin.IRQ_FALLING, handler=buttons_irq)