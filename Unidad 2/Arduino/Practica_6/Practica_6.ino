#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

const int ledPin = 13;
int ledState = LOW;

const int numLecturas = 30;
int temperaturas[numLecturas];

unsigned long previousMillis = 0;
const long interval = 500;

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(ledPin, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    int count = 0;
    while (count < numLecturas) {
      float temp = dht.readTemperature();
      if (!isnan(temp)) {
        temperaturas[count] = (int)temp;
        count++;
      }
    }

    int mediana = calcularMediana(temperaturas, numLecturas);
    Serial.println(mediana);

    if (Serial.available() > 0) {
      char incomingByte = Serial.read();
      if (incomingByte == '1') {
        digitalWrite(ledPin, HIGH);
        ledState = HIGH;
        Serial.println("LED Prendido");
      } 
      else if (incomingByte == '0') {
        digitalWrite(ledPin, LOW);
        ledState = LOW;
        Serial.println("LED Apagado");
      }
    }
  }
}

int calcularMediana(int arr[], int tam) {
  for (int i = 0; i < tam - 1; i++) {
    for (int j = i + 1; j < tam; j++) {
      if (arr[j] < arr[i]) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr[tam / 2];
}
