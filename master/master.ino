#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX
uint16_t rotate = 0;

void setup()  
{
  Serial.begin(115200);
  mySerial.begin(115200);
}

void loop() // run over and over
{
  uint16_t rotate_temp = analogRead(A0);
  
  if(rotate_temp!=rotate) {
    rotate = rotate_temp;
    Serial.print("S");
    Serial.print("rotation=");
    Serial.print(rotate);
    Serial.print("E");
  }
  while (mySerial.available()){
    Serial.write(mySerial.read());
  }
  delay(50);
}
