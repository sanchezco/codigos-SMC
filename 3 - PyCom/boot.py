# boot.py -- run on boot-up

import pycom
import time
import machine
from network import WLAN


wlan = WLAN ()
wlan.antenna(WLAN.INT_ANT) # antena que uso, la interna
wlan.init(mode=WLAN.STA) # modo de funcionamiento, estacion. Ahora mismo estaria como router

# configuration below MUST match your home router setings
wlan.ifconfig(config=('192.168.2.161','255.255.255.0','192.168.2.1','8.8.8.8')) #configuracion de red
wlan.connect('DeepWAVES_modem4G_01', auth=(WLAN.WPA2, 'deepwavesmodem4G'), timeout=5000) # red wifi que uso y su contraseña

while not wlan.isconnected (): #chequea si nos conectamos a la red wifi, sino lo deja al minimo
    #save power while waiting
    machine.idle()

pycom.heartbeat(False)
pycom.rgbled(0x007f00)
time.sleep(2)
pycom.rgbled(0x000000)
time.sleep(1)
pycom.heartbeat(True)