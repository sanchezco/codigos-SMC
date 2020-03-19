# Mejora del código que introduce las alarmas cuando el valor es mejor a 20cm
# o superior a 80ºC

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial # librería interactuar puerto serie
import mysql.connector # libreria MySQL server
import json # librería para decodificar json

arduino = serial.Serial('/dev/ttyACM0', 9600) #puerto de conexión con arduinos

def cad_proc(cad):
    print ("\n\nInicio------------------------------------------------>" + cad)
    try:
        json_decoded = json.loads(cad) # Devuelve un objeto de una cadena que represente json

        sensor = json_decoded['idsensor']
        value = json_decoded['valor']

        print("sensor:" + str(sensor))
        print("value:" + str(value))

        send_mysql(str(sensor),str(value)) # Manda a la base de datos el sensor id y su dato.

    except:
        print("ERROR FOUND")

def send_mysql(sensor_,value_): # Credenciales de mi base de datos, para saber donde llevo la información.
    cnx = mysql.connector.connect(user='carlos', password='1234',
                              host='10.100.18.122',
                              database='iot')
    cursor = cnx.cursor() #interactua con MySQL server

    if ((int(sensor_) == 1) and (int(value_) < 20)):
        query = "Insert into data (idsensor,data,alarma) VALUES (" + sensor_  + "," + value_ + "," + "1" + ");"
    elif ((int(sensor_) == 2) and (float(value_) > 80)):
        query = "Insert into data (idsensor,data,alarma) VALUES (" + sensor_  + "," + value_ + "," + "1" + ");"
    else:
        query = "Insert into data (idsensor,data) VALUES (" + sensor_  + "," + value_ + ");"

    print(query)
    cursor.execute(query) # Ejecuta la query
    cnx.commit()          # Manda un commit a MySQL server, necesario después de cada query
    cursor.close()        # Desconecto el cursor
    cnx.close()           # Desconecto de mi base de datos

    print("------------------------------------------------")

while True:
    line = arduino.readline() # lee el puerto serie de arduino
    cad_proc(line)            # Ejecuto la función cad_proc con la informacion del puerto serie

arduino.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)
