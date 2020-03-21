/***************************************************************************
Código del sensor BME280 
Lectura de temperatura, presión, altitud y humedad en formato Json
 ***************************************************************************/
#include <ArduinoJson.h>

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)
Adafruit_BME280 bme; // protocolo I2C

void setup() {
    Serial.begin(9600);
    while(!Serial);    // time to get serial running

    unsigned status;
    
    // default settings
    status = bme.begin();  
    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
        Serial.print("SensorID was: 0x"); Serial.println(bme.sensorID(),16);
        Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
        Serial.print("   ID of 0x56-0x58 represents a BMP 280,\n");
        Serial.print("        ID of 0x60 represents a BME 280.\n");
        Serial.print("        ID of 0x61 represents a BME 680.\n");
        while (1) delay(10);
    }
}

void loop() { 
    DynamicJsonBuffer jBuffer; // permite crear un objeto json (distancia)

    JsonObject& temperatura = jBuffer.createObject(); // Unidades en grados centígrados
    temperatura["idsensor"].set("0");
    temperatura["valor"].set(bme.readTemperature());
    temperatura.printTo(Serial);
    Serial.println();
    delay(1000);

    JsonObject& presion = jBuffer.createObject(); // Unidades en hPa
    presion["idsensor"].set("1");
    presion["valor"].set(bme.readPressure() / 100.0F);
    presion.printTo(Serial);
    Serial.println();
    delay(1000);

    JsonObject& altitud = jBuffer.createObject(); // Unidades en m
    altitud["idsensor"].set("2");
    altitud["valor"].set(bme.readAltitude(SEALEVELPRESSURE_HPA));
    altitud.printTo(Serial);
    Serial.println();
    delay(1000);

    JsonObject& humedad = jBuffer.createObject();
    humedad["idsensor"].set("3");
    humedad["valor"].set(bme.readHumidity());
    humedad.printTo(Serial);
    Serial.println();
    delay(2000);
}
