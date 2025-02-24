int actuador = 11;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(actuador,OUTPUT);

}
int v;
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    v=Serial.readString().toInt();
    if(v ==0 || v==1){
      digitalWrite(actuador,v);

    }else{
      Serial.println("Valor no valido");
    }
    
  }
  delay(100);

}
