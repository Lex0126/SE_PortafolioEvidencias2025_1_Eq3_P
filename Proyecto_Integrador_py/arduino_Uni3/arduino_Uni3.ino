const int rele1 = 2;
const int rele2 = 3;
const int sensorLDR = A0;

void setup() {
  Serial.begin(9600);
  pinMode(rele1, OUTPUT);
  pinMode(rele2, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char pedido = Serial.read();
    if (pedido == '1') {
      int valorLDR = analogRead(sensorLDR);
      Serial.println(valorLDR);
    } else if (pedido == '0' || pedido == '1' || pedido == '3') {
      controlarFocos(pedido);
    }
  }
} 

void controlarFocos(char cmd) {
  switch (cmd) {
    case '0':  // Apaga todo
      digitalWrite(rele1, HIGH);
      digitalWrite(rele2, HIGH);
      break;
    case '1':  // Solo foco 1
      digitalWrite(rele1, LOW);
      digitalWrite(rele2, HIGH);
      break;
    case '3':  // Ambos focos
      digitalWrite(rele1, LOW);
      digitalWrite(rele2, LOW);
      break;
  }
}




