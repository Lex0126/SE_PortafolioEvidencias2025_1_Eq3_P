#include <DHT.h>

#define DHTPIN 2        // Pin donde esta conectado el sensor DHT11
#define DHTTYPE DHT11   // Tipo de sensor DHT
#define INTERVALO 300000 // Intervalo de tiempo en milisegundos (5 minutos)

DHT dht(DHTPIN, DHTTYPE);

unsigned long previousMillis = 0; 
  
void setup() {
    Serial.begin(9600);
    dht.begin();
}

void loop() {
    unsigned long currentMillis = millis(); // Obtener el tiempo actual

    // Verificar si ha pasado el intervalo de tiempo
    if (currentMillis - previousMillis >= INTERVALO) {
        previousMillis = currentMillis; 

        float temperatura = dht.readTemperature();
        
        if (isnan(temperatura)) {
            Serial.println("Error");
        } else {
            Serial.println(temperatura);
        }
    }
}