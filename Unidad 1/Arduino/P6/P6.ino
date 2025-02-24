long v;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  v=millis();
  Serial.println(v);
  delay(1000);

}
