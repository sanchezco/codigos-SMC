# main.py -- put your code here!
import socket
import time
from machine import UART

uart = UART(1, 9600, timeout_chars=200, pins=('P11', 'P10'))
#10 transmisor y 11 receptor
s = socket.socket()
s.connect(('192.168.2.244',5201)) # puerto al que me conecto

while True:
    print('Waiting for UART data')
    uartread = uart.read(256)

    if uartread != None:
        s.send(uartread)
    time.sleep(1)

