
int sensor = A0;
int actuador =12;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}
int v;
void loop() {
  // put your main code here, to run repeatedly:
  v=analogRead(sensor);
  v= map(v,0,1023,0,255);
  analogWrite(actuador,v);
  delay(100);

}
