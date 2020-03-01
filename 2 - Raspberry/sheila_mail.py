#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import mysql.connector
import json

#Importo librería para mandar el mail
import os
arduino = serial.Serial('/dev/ttyACM0', 9600)


def cad_proc(cad):
    print ("\n\nInicio------------------------------------------------>" + cad)
    try:
      
        json_decoded = json.loads(cad)

        sensor = json_decoded['idsensor']
        data = json_decoded['data']
        
        print("sensor:" + str(sensor))    
        print("data:" + str(data))
        
        
        if int(sensor) ==2 and float(data) >=28: 
            
            send_mysql(str(sensor),str(data),"1")
            os.system('echo \"Alarma en el sensor de temperatura-->se han superado 28 Grados\" | mail -s \"Alarma\" c.sanchezcorte@gmail.com')
           
            
        elif int(sensor) ==1 and int(data) >= 20:
        
            send_mysql(str(sensor),str(data),"1")
            os.system('echo \"Alarma en el sensor de Distancia-->Caja manipulada\" | mail -s \"Alarma\" c.sanchezcorte@gmail.com')
        elif int(sensor) ==2 and int(value) == -127:
        
            send_mysql(str(sensor),str(data),"0","1")
            
        else:
           
            send_mysql(str(sensor),str(data))
              
    except:
        print("ERROR FOUND")

def send_mysql(sensor_,data_,alarm_="0",error_="0"): #Por defecto me va aponer la alarma a cero a no ser que envie otro dato como en el caso de aumento de temperatura.
    cnx = mysql.connector.connect(user='carlos', password='1234',
                              host='10.100.18.122',
                              database='iot')
    cursor = cnx.cursor()
    query = "Insert into data (idsensor,data,alarma,error) VALUES (" + sensor_  + "," + data_ + ","+ alarm_ +","+ error_ +");"
    print(query)
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


while True:
    line = arduino.readline()
    cad_proc(line)
arduino.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)
