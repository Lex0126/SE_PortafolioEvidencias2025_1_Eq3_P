int actuadores[4] = {8, 9, 11, 12};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 4; i++) {
    pinMode(actuadores[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    int v = Serial.parseInt(); 
    if (v >= 0 && v < 4) { 
      digitalWrite(actuadores[v], 1);
      delay(1000);
      digitalWrite(actuadores[v], 0);
    } else {
      Serial.println("Numero no valido"); 
    }
  }
}