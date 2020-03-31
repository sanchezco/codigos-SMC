//Codido modificaco para generar valores falsos de temperatura y distancia.
// utilizado para comprobar que se mandan bien los datos sin necesidad de conectar sensores

//Librerías utilizadas
#include <ArduinoJson.h>
#include <HCSR04.h> //by Martin Sosic
#include <OneWire.h>  //by Jim Studt and others..
#include <DallasTemperature.h> //by Miles Burton and others

#define TRIG_PIN 8
#define ECHO_PIN 7
#define TEMP_PIN 10
OneWire  ds(TEMP_PIN);
DallasTemperature sensors(&ds);
UltraSonicDistanceSensor distanceSensor(TRIG_PIN, ECHO_PIN);

void setup (){
  Serial.begin(9600);
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
//CAMBIO
    //Serial.print('?'); // porque quiero que me detecte la ? para para el codigo, por lo tanto no valdria si lo mando po usb
    Serial.println();

    delay(200);

    // repito el mismo proceso para añadir el objeto temperatura.
    JsonObject& temperatura = jBuffer.createObject();
    temperatura["idsensor"].set("2");
    temperatura["valor"].set(Ftemp());
    temperatura.printTo(Serial);
    //Serial.print('?');
    Serial.println();
    delay(2000);
}
double Fdistance(){
  int d = distanceSensor.measureDistanceCm() ;
  d = 20;
  return d;
}
float Ftemp(){
  float f = -127; //En caso de error aparecerá el -127
  sensors.requestTemperatures();
  delay (100);
  f = sensors.getTempCByIndex(0);
  f = 30;
  return f;
}
