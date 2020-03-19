//Librerías utilizadas
#include <ArduinoJson.h>
#include <HCSR04.h> //by Martin Sosic
#include <OneWire.h>  //by Jim Studt and others..
#include <DallasTemperature.h> //by Miles Burton and others
#include <Wire.h>
#include "SparkFunBME280.h"
BME280 mySensorA; //Uses default I2C address 0x77

#define TRIG_PIN 8
#define ECHO_PIN 7
#define TEMP_PIN 10
OneWire  ds(TEMP_PIN);

UltraSonicDistanceSensor distanceSensor(TRIG_PIN, ECHO_PIN);

void setup (){
  Serial.begin(9600); 
  
  Wire.begin();
  DallasTemperature sensors(&ds);
  mySensorA.setI2CAddress(0x77);

  if(mySensorA.beginI2C() == false) Serial.println("Sensor A connect failed");
}
void loop(){
    DynamicJsonBuffer jBuffer; // permite crear un objeto json (distancia)
    JsonObject& distancia = jBuffer.createObject(); //creo el objeto distancia
    float temp; 
    int distance;
    String cad;
    // dentro del objeto distancia tengo la variable idsensor que será fija, y el 
    // valor de la lectura del sensor.
    distancia["idsensor"].set("1"); 
    distancia["valor"].set(Fdistance());
    distancia.printTo(Serial); 
    
    Serial.println();
    delay(200);

    // repito el mismo proceso para añadir el objeto temperatura.
    JsonObject& temperatura = jBuffer.createObject();
    temperatura["idsensor"].set("2");
    temperatura["valor"].set(Ftemp());
    temperatura.printTo(Serial);
    Serial.println();   
    delay(2000);
}
double Fdistance(){
  int d = distanceSensor.measureDistanceCm() ;
  return d;
}
float Ftemp(){
  float f = -127; //En caso de error aparecerá el -127
  /*
  sensors.requestTemperatures();  
  delay (100);
  f = sensors.getTempCByIndex(0);*/
  f = mySensorA.readFloatHumidity();
  return f;  
}