#include <DHT.h>

#define DHTPIN 7        
#define DHTTYPE DHT11   // Tipo de sensor DHT
#define INTERVALO 300 // Intervalo de tiempo en milisegundos (5 minutos)

DHT dht(DHTPIN, DHTTYPE);

unsigned long previousMillis = 0; // Variable para almacenar el último tiempo de lectura
const int lec = 24;

void setup() {
    Serial.begin(9600);
    dht.begin();
}

void loop() {
    unsigned long currentMillis = millis(); // Obtener el tiempo actual

    // Verificar si ha pasado el intervalo de tiempo
    if (currentMillis - previousMillis >= INTERVALO) {
        previousMillis = currentMillis; // Actualizar el ultimo tiempo de lectura

        int temperatura = dht.readTemperature();

        int valormenor = calcularValorMenor(temperatura,lec);   
        
        if (isnan(temperatura)) {
            Serial.println("Error");
        } else {
            Serial.println(temperatura);
        }
    }
}

int calcularValorMenor(int arr[], int tam) {
  int menor = 1024;
  for (int i = 0; i < tam; i++) {
    if (arr[i] < menor) {
      menor = arr[i];
    }
  }
  return menor;
}
