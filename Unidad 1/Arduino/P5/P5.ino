
int pinpwm = 12;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i =0 ; i<255; i++){
    analogWrite(pinpwm,i);
    delayMicroseconds(10000);
  }
  delay(10);
  for (int i =255; i>0; i--){
    analogWrite(pinpwm,i);
    delayMicroseconds(10000);

  }
  delay(1000);

}
