import machine
import usocket as socket
import time
import network

timeout = 0

wifi = network.WLAN(network.STA_IF)

wifi.active(False)
time.sleep(0.5)
wifi.active(True)

wifi.connect('','')

if not wifi.isconnected():
    print('Connecting...')
    while (not wifi.isconnected() and timeout < 5):
        print(5 - timeout)
        timeout = timeout + 1
        time.sleep(1)
        
if(wifi.isconnected()):
    print('Connected...')
    print('Network config:', wifi.ifconfig())
    
# HTML doc

html='''<!DOCTYPE html>
<html>
<center><h2>ESP32 WEBSERVER </h2></center>
<form>
<center>
<h3> LED </h3>
<button name="LED" value='ON' type='submit'> ON </button>
<button name="LED" value='OFF' type='submit'> OFF </button>
</center>
'''

# Output Pin Declaration
LED = machine.Pin(2, machine.Pin.OUT)
LED.value(0)

#Initialising Socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # internet socket TCP protocol

HOST = '' #empty means it will allow all IP address to connect
Port = 80
s.bind((Host,Port))

s.listen(5)

#main loop

while True:
    connection_socket, address=s.accept() #storing conn_socket and address from new request
    print('Got a connection from ', adress)
    request = connection_socket.recv(1024) #storing response coming from client
    print('Content ', request)
    request = str(request) #converting bytes to string
    #comparing and finding position of word in String
    LED_ON = request.find('/?LED=ON')
    LED_OFF = request.find('/LED=OFF')
    
    if(LED_ON==6):
        LED
        
        #ep 05 - home automation using Socket Programming in Micropython
    


