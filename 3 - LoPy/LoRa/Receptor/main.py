# main.py -- put your code here!

from network import LoRa
import socket
import time

#Se crea el objeto LoRa
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
#Se crea el objeto socket, la comunicación se realiza por socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
#Hasta que no se establezca la conexión no pasa nada
s.setblocking(True)
print('Conectado a LoRa')

while True:
    
    #print('Waiting for LoRa data...')
    loraread = s.recv(256)

    if loraread != None:
        #print ('n---> Printing data...')
        print(loraread)
        
    time.sleep(1)
