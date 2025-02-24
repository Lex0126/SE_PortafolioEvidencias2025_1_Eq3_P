int pots [4]={A0,A1,A2,A3};
int vals [4];

void setup(){

Serial.begin(9600);
Serial.setTimeout(100);

}
void loop(){
for (int i=0; i<4; i++){
vals[i] = analogRead(pots[i]);
delayMicroseconds(1000);
}
String c;

c= String(vals[0])+"-"+
	 String(vals[1])+"-"+
	 String(vals[2])+"-"+
	 String(vals[3]);

Serial.println(c);

delay(1000);

}

