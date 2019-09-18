void setup(){
  pinMode(A0,OUTPUT);
  delay(1000);
  digitalWrite(A0,LOW);
  delay(1000);
  digitalWrite(A0,HIGH);
  
  pinMode(A0,INPUT);

}

void loop(){
}
