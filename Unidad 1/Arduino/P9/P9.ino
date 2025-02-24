int actuadores [4] = {12,11,9,8};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for(int i = 0;i<4;i++){

    pinMode(actuadores[i],OUTPUT);
  }

}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0; i<4;i++){
    digitalWrite(actuadores[i],1);
    delay(100);
    digitalWrite(actuadores[i],0);
    delay(100);
  }
  delay(100);

}
