# main.py -- put your code here!

from network import LoRa
import socket
import time
from machine import UART

#Importamos de la libreria machine la funcion UART para establecer la conexion
uart = UART(1, 9600, timeout_chars=2000, pins=('P11', 'P10'))
#P11 (Tx UART LoPy) --> receptor Arduino Rx

#Se crea el objeto LoRa
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
#Se crea el objeto socket, la comunicación se realiza por socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
#Hasta que no se establezca la conexión no pasa nada
s.setblocking(True)
print('Conectado a LoRa')

while True:
    #print('Waiting for UART data')
    uartread = uart.read(256)
    print('leido')

    if uartread != None:
        print ('no esta vacio')
        s.send(uartread)
        print(uartread)
    time.sleep(1)
