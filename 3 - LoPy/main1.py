# main.py -- put your code here!

import socket
import time

s = socket.socket()
s.connect(('192.168.2.244',5100)) # puerto al que me conecto

while True:
    s.send("Hello Word 2")
    time.sleep(2)