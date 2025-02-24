
int sensor =A0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}
int v;
void loop() {
  // put your main code here, to run repeatedly:
  v=analogRead(sensor);
  Serial.println("Valor="+String(v));
  delay(500);

}
