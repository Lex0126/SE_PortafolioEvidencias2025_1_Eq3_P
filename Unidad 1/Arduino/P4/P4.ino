int actuador=12;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(actuador,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

digitalWrite(actuador,1);
delay(1000);
digitalWrite(actuador,0);
delay(1000);
}
