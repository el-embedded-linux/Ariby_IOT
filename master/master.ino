#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX


void setup()  
{
  pinMode(2, INPUT_PULLUP);
  Serial.begin(115200);
  mySerial.begin(115200);
}

void loop() // run over and over
{
  int dyValue = analogRead(A1);
  int dyMap = map(dyValue, 0, 1023, 0, 180);

  int swValue = digitalRead(2);

  Serial.print(",");
  Serial.print(dyMap);
  Serial.print(",");
  Serial.println(swValue);
  
  delay(50);
}
