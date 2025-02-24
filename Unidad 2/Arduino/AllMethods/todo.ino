int sensor []= {A0,A1,A2,A3,A4,A5};
void setup() {
  Serial.begin(9600);
}

const int totLecturas = 30;
int valor1[totLecturas];
int valor2[totLecturas];
int valor3[totLecturas];
int valor4[totLecturas];
int valor5[totLecturas];
int valor6[totLecturas];

void loop() {
  for (int i = 0; i < totLecturas; i++) {
    valor1[i] = analogRead(sensor[0]);
    valor2[i] = analogRead(sensor[1]);
    valor3[i] = analogRead(sensor[2]);
    valor4[i] = analogRead(sensor[3]);
    valor5[i] = analogRead(sensor[4]);
    valor6[i] = analogRead(sensor[5]);

    delayMicroseconds(100);
  }

 

  int prom = calcularPromedio(valor6, totLecturas);
  int valorMenor = calcularValorMenor(valor2, totLecturas);
  int valorMayor = calcularValorMayor(valor3, totLecturas);
  int mediana = calcularMediana(valor5, totLecturas);
  int moda = calcularModa(valor4, totLecturas);
  int normal =leerNormal(valor1);

  Serial.println(String(prom)+"-"+String(valorMenor)+"-"+String(valorMayor)+"-"+String(mediana)+"-"+String(moda)+"-"+String(normal));

  
}

int calcularPromedio(int arr[], int tam) {
  int suma = 0;
  for (int i = 0; i < tam; i++) {
    suma += arr[i];
  }
  return suma / tam;
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

int calcularValorMayor(int arr[], int tam) {
  int mayor = -1;
  for (int i = 0; i < tam; i++) {
    if (arr[i] > mayor) {
      mayor = arr[i];
    }
  }
  return mayor;
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

int calcularModa(int arr[], int tam){
  int maxRepeticiones = 0;
  int moda = -1;

  for (int i = 0; i < tam; i++) {
    int contador = 0;
    for (int j = 0; j < tam; j++) {
      if (arr[i] == arr[j]) {
        contador++;
      }
    }
    if (contador > maxRepeticiones) {
      maxRepeticiones = contador;
      moda = arr[i];
    }
  }

  return moda;
}

int leerNormal(int arr[]){
  return arr[0];
}
