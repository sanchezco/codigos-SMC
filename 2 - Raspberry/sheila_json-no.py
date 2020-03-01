#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial # librería interactuar puerto serie
import mysql.connector # libreria MySQL server
import json # librería para decodificar json

arduino = serial.Serial('/dev/ttyACM0', 9600) #puerto de conexión con arduinos

def cad_proc(cad):
    print ("\n\nInicio------------------------------------------------>" + cad)
    try:

        json_decoded = json.loads(cad # Devuelve un objeto de una cadena que represente json

        sensor = json_decoded['idsensor']
        value = json_decoded['valor']
        
        if int(sensor) ==2 and float(value) >=26: #Defino el rango de mis datos no deseados.Si hay una alarma inserto un 1
            send_mysql(str(sensor),str(value),"1") # Manda a la base de datos el idsensor, su dato y la alarma.
            
        elif int(sensor) ==1 and int(value)>= 20:      
            send_mysql(str(sensor),str(value),"1").
            
        else:# Si no hay una alarma inserto solo dos valores
            send_mysql(str(sensor),str(value))# Manda a la base de datos el idsensor y el dato.
        
        print("sensor:" + str(sensor)) 
        print("value:" + str(value))
        

        
    except:# Si hay un error muestro por pantalla el mensaje y continuo sin que se rompa el código.
        print("ERROR FOUND")

def send_mysql(sensor_,value_,alarm_="0"): # Credenciales de mi base de datos, para saber donde llevo la información.
    cnx = mysql.connector.connect(user='carlos', password='1234',
                              host='10.100.18.122',
                              database='iot')
    cursor = cnx.cursor()#interactua con MySQL server
    query = "Insert into data (idsensor,data,alarma) VALUES (" + sensor_  + "," + value_ + ","+ alarm_ +");"
    print(query)
    
    cursor.execute(query) # Ejecuta la query
    cnx.commit()          # Manda un commit a MySQL server, necesario después de cada query
    cursor.close()        # Desconecto el cursor
    cnx.close()           # Desconecto de mi base de datos


while True:
    line = arduino.readline() # lee el puerto serie de arduino
    cad_proc(line)            # Ejecuto la función cad_proc con la informacion del puerto serie
arduino.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)
