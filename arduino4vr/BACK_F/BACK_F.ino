#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3);

void setup(){
  Serial.begin(115200);
  mySerial.begin(115200);

}

void loop(){
    if (mySerial.available()){
      uint8_t words = mySerial.read();
      Serial.write(words);
    }
}
