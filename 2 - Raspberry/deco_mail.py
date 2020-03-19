# Se añade la notificación por correo de las alarmas

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import mysql.connector
import json
import os

arduino = serial.Serial('/dev/ttyACM0', 9600)

def cad_proc(cad):
    print ("\n\nInicio------------------------------------------------>" + cad)
    try:

        json_decoded = json.loads(cad)
        sensor = json_decoded['idsensor']
        value = json_decoded['valor']

        if int(sensor) ==2 and float(value) >=20:
            os.system('echo \"Alarma en el sensor de temperatura--> Temperatura superior a 20 Grados\" | mail -s \"Alarma\" c.sanchezcorte@gmail.com')
            send_mysql(str(sensor),str(value),"1")

        elif int(sensor) ==1 and int(value)>= 10:
            os.system('echo \"Alarma en el sensor de distancia--> Distancia menor a 10 cm \" | mail -s \"Alarma\" c.sanchezcorte@gmail.com')
            send_mysql(str(sensor),str(value),"1")

        else:
            send_mysql(str(sensor),str(value))

        print("sensor:" + str(sensor))
        print("value:" + str(value))

    except:
        print("ERROR FOUND")


def send_mysql(sensor_,value_,alarm_="0"):
    cnx = mysql.connector.connect(user='carlos', password='1234',
                              host='10.100.18.122',
                              database='iot')
    cursor = cnx.cursor()
    query = "Insert into data (idsensor,data,alarma) VALUES (" + sensor_  + "," + value_ + ","+ alarm_ +");"
    print(query)
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


while True:
    line = arduino.readline()
    cad_proc(line)
arduino.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)
