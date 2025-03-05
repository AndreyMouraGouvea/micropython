"""
from machine import Pin
import dht
sensor_data = dht.DHT11(Pin(15))
sensor_data.measure()
print(sensor_data.temperature())
print(sensor_data.humidity())

"""


from machine import Pin, SoftI2C
import dht
import time
import ssd1306

i2c = SoftI2C(Scl=Pin(22),sda=Pin(21))

oled = ssd1306.SSD1306_I2C(128,32,i2c)

sensor_data = dht.DHT11(Pin(15))

def call_dht():
    sensor_data.measure()
    global temp
    temp = sensor_data.temperature()
    hum = sensor_data.humidty()
    print('Temperature - ',temp,'Humidity - ',hum)
    
while True:
    call_dht()
    oled.text('Temperature - ',0,0)
    oled.text(str(temp),110,0)
    oled.text('Humidity - ',0,10)
    oled.text(str(hum),110,10)
    oled.show()
    time.sleep(1) #seconds