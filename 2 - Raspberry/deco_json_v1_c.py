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

        print (json_decoded ['idsensor'])
        print (json_decoded ['valor'])


        sensor = json_decoded['idsensor']
        value = json_decoded['valor']
        #print("A")
        print("sensor:" + str(sensor))
        #print("B")
        print("value:" + str(value))
        #print("C")
        send_mysql(str(sensor),str(value))
    except:
        print("ERROR FOUND")

def send_mysql(sensor_,value_):
    cnx = mysql.connector.connect(user='carlos', password='1234',
                              host='10.100.18.122',
                              database='iot')
    cursor = cnx.cursor()
    query = "Insert into data (idsensor,data) VALUES (" + sensor_  + "," + value_ + ");"
    print(query)
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


while True:
    line = arduino.readline()
    cad_proc(line)
arduino.close() #Finalizamos la comunicacionarduino = serial.Serial('/dev/ttyACM0', 9600)
