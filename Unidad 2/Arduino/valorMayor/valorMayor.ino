//Pre procesar datos
//Normalmente leemos unicamente una vez cada sensor y mandamos 
// la informacion al puerto serial
// esto es incorrecto debido a que pdorian generarse 
// incosistencias en las lecturas , por lo que debe buscarse
//tratar de artinorar esta situacion mediante el preprocesamiento..


// primera aproximacion  de memdias de tendencia central


int sensor = A0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);


}
int lecturas=30; //teorema de limite central
int valorMayor = -1; // por que es el valor mas grande para que entre a la interacion y debe ser mayor al numero que se puede leer
int valor[30];
void loop() {
  // put your main code here, to run repeatedly:
  for(int i =0;i<lecturas; i++){
    valor [i]= analogRead(sensor);
    delayMicroseconds(100);
  } 
  valorMayor = -1;
  for(int i =0; i<lecturas ; i++){
    if(valor[i]>valorMayor){
      valorMayor = valor[i];
    }
  }
  

  Serial.println(valorMayor);
  
 delay(10);
}