int sensor = 10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(sensor,INPUT);

}
int v;
void loop() {
  // put your main code here, to run repeatedly:
  v = digitalRead(sensor);
  Serial.println(v);
  delay(1000);

}
