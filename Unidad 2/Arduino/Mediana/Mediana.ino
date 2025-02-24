//Pre procesar datos
//Normalmente leemos unicamente una vez cada sensor y mandamos 
// la informacion al puerto serial
// esto es incorrecto debido a que pdorian generarse 
// incosistencias en las lecturas , por lo que debe buscarse
//tratar de artinorar esta situacion mediante el preprocesamiento..


// primera aproximacion  de memdias de tendencia central

#include <DHT.h>

#define DHTPIN 2        
#define DHTTYPE DHT11  
int sensor = 2;
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);


}
int lecturas=30; //teorema de limite central
 // por que es el valor mas grande para que entre a la interacion y debe ser mayor al numero que se puede leer
int valor[30];
void loop() {
  // put your main code here, to run repeatedly:
  for(int i =0;i<lecturas; i++){
    valor [i]= dht.readTemperature(DHTPIN);
    delayMicroseconds(100);
  } 
 
  for (int i= 0; i<lecturas;i++){
    for(int j =i+1;j<lecturas-1;j++){
      if(valor[i]<valor[i]){
        int temp =valor[i];
        valor[i]=valor[j];
        valor[j]=temp;
      }
    }
  }//ordenamiento burbuja
  
// ejercicio 1 - moda
  Serial.println(valor[lecturas/2]);
  
 delay(10);
}