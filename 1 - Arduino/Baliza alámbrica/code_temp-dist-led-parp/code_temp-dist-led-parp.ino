// codigo completo con sensor de temperatura, distancia, y alarma que enciende el pinLed
// si la distancia es menor que 20 salta la alarma

//Librerías utilizadas
#include <ArduinoJson.h>
#include <HCSR04.h> //by Martin Sosic
#include <OneWire.h>  //by Jim Studt and others
#include <DallasTemperature.h> //by Miles Burton and others

#define TRIG_PIN 8
#define ECHO_PIN 7
#define TEMP_PIN 10
OneWire  ds(TEMP_PIN);
DallasTemperature sensors(&ds);
UltraSonicDistanceSensor distanceSensor(TRIG_PIN, ECHO_PIN);

int pinLed = 13;

void setup (){
  Serial.begin(9600);
  pinMode(pinLed, OUTPUT);
  sensors.begin();
}
void loop(){
    DynamicJsonBuffer jBuffer;           // Permite crear un objeto json (distancia)
    JsonObject& distancia = jBuffer.createObject(); //Creo el objeto distancia
    float temp;
    int distance;

    distancia["idsensor"].set("1");      // Dentro del objeto distancia, sensorid tendrá el identificador '1'
    distancia["valor"].set(Fdistance()); // Valor de lectura del sensor
    distancia.printTo(Serial);
    Serial.println();
    delay(300);

    JsonObject& temperatura = jBuffer.createObject(); // creo el objeto temperatura
    temperatura["idsensor"].set("2");    // Dentro del objeto temperatura, sensorid tendrá el identificador '2'
    temperatura["valor"].set(Ftemp());   // Valor de lectura del sensor
    temperatura.printTo(Serial);
    Serial.println();
    delay(300);

    if (Fdistance()<20){                 // Si el dato está fuera del rango deseado salta la alarma 3seg.
      alarma();
    } else {
      digitalWrite(pinLed,LOW);
    }
    delay(3000);
}

double Fdistance(){
  int d = distanceSensor.measureDistanceCm() ;
  return d;
}
float Ftemp(){
  float f = -127;                        //En caso de error aparecerá el -127
  sensors.requestTemperatures();
  delay (100);
  f = sensors.getTempCByIndex(0);
  return f;
}

char alarma(){                           // Si recibe un dato fuera de rango parpadea
      digitalWrite(pinLed,HIGH);
      delay(200);
      digitalWrite(pinLed,LOW);
      delay(200);
      digitalWrite(pinLed,HIGH);
}
