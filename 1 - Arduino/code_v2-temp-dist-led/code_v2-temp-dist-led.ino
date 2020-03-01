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

int pinLed = 13;

void setup (){
  Serial.begin(9600); 
  pinMode(pinLed, OUTPUT);
  sensors.begin();

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
    delay(500);

    // repito el mismo proceso para añadir el objeto temperatura.
    JsonObject& temperatura = jBuffer.createObject();
    temperatura["idsensor"].set("2");
    temperatura["valor"].set(Ftemp());
    temperatura.printTo(Serial);
    Serial.println();   
    delay(3000);

//    if (Fdistance()<20){
//      alarma();
//    } else { 
//      digitalWrite(pinLed,LOW);
//    }    
//    readserial();
//
//    delay(3000);
}
double Fdistance(){
  int d = distanceSensor.measureDistanceCm() ;
  return d;
}
float Ftemp(){
  float f = -127; //En caso de error aparecerá el -127
  sensors.requestTemperatures();  
  delay (100);
  f = sensors.getTempCByIndex(0);
  return f;  
}

char readserial(){
  if (Serial.available()) { //Si está disponible el puerto serie
      char c_ = Serial.read(); //Guardamos la lectura en una variable char
      if (c_ == 'H') { //Si es una 'H', enciendo el LED
         digitalWrite(pinLed, HIGH);
      } else if (c_ == 'L') { //Si es una 'L', apago el LED
         digitalWrite(pinLed, LOW);
      }
   }
}

//char alarma(){ // si recibe un dato fuera de rango parpadea
//      digitalWrite(pinLed,HIGH);  
//      delay(200);
//      digitalWrite(pinLed,LOW);  
//      delay(200);
//      digitalWrite(pinLed,HIGH);
//}
