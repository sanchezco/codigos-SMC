#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import mysql.connector
import json

arduino = serial.Serial('/dev/ttyACM0', 9600)
#  #1:68#2:21.50@

def cad_proc(cad):
    print ("\n\nInicio------------------------------------------------>" + cad)
    try:
        ##y = json.dumps(cad)
        json_decoded = json.loads(cad)
        ##print(y)
        #for x in json_loaded:
    
        

        sensor = json_decoded['idsensor']
        value = json_decoded['valor']
        
        #print("sensor:" + str(sensor))    
        #print("value:" + str(value))
        
        if int(sensor) ==2 and float(value) >=26: #Estaba comparando un string con un número float por eso había que ponerlo en int y en float.
            
            send_mysql(str(sensor),str(value),"1")
            
        elif int(sensor) ==1 and int(value)>= 20:
        
            send_mysql(str(sensor),str(value),"1")
            
        else:
            send_mysql(str(sensor),str(value))
        
        print("sensor:" + str(sensor)) 
        print("value:" + str(value))
        

        
    except:
        print("ERROR FOUND")

def send_mysql(sensor_,value_,alarm_="0"): #Por defecto me va aponer la alarma a cero a no ser que envie otro dato como en el caso de aumento de temperatura.
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
