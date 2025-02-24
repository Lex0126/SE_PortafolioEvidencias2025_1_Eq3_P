#include <DHT.h>

#define DHTPIN 2        // Pin donde está conectado el sensor DHT
#define DHTTYPE DHT11   // Tipo de sensor DHT

DHT dht(DHTPIN, DHTTYPE);

const int ledPin = 13;  // Pin para el LED
int ledState = LOW;     

void setup() {
  Serial.begin(9600);  
  dht.begin();        
  pinMode(ledPin, OUTPUT);  
}

void loop() {
  // Leer temperatura
  float temp = dht.readTemperature();
  if (isnan(temp)) {
    Serial.println("Error al leer el sensor DHT");
  } else {
    Serial.print("Temperatura: ");
    Serial.println(temp);
  }

  // Verificar si hay datos enviados desde Python
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();  // Leer el valor recibido

    // Si recibimos '1' de Python, encender el LED
    if (incomingByte == '1') {
      digitalWrite(ledPin, HIGH);  // Encender LED
      ledState = HIGH;
      Serial.println("LED Prendido");
    } 
    // Si recibimos '0' de Python, apagar el LED
    else if (incomingByte == '0') {
      digitalWrite(ledPin, LOW);   // Apagar LED
      ledState = LOW;
      Serial.println("LED Apagado");
    }
  }

  delay(500);  // Esperar 1 segundo antes de la siguiente lectura
}


