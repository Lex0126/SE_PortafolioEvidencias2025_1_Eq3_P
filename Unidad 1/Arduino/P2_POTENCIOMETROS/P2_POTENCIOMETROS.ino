int sensores[]={A0,A1,A2,A3};
int actuadores []={8,9,11,12};
int i;


void setup() {
  Serial.begin(9600);
Serial.setTimeout(100);
  // put your setup code here, to run once:
  for (i =0; i<4; i++){
    pinMode(actuadores[i],OUTPUT);

  }

}
int valor;
void loop() {
  // put your main code here, to run repeatedly:
  for(i=0;i<4;i++){
   
    digitalWrite(sensores[i],valor);

    valor = valor/512;
    valor = analogRead(sensores[i]);
  }
   
  
  Serial.println(valor);

  delay(1000);

}
