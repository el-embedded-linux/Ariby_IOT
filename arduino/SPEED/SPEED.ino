#include <MsTimer2.h>
#define CIRCLE 1.946
#define REEDSWITCH A3 //리드스위치 포트

uint16_t mySpeed = 0;
uint16_t beforeSpeed = 1;
uint32_t uckTime = 0;
uint32_t ckTime = 0;
uint32_t count = 0;

void setup() {
  Serial.begin(115200);
  pinMode(REEDSWITCH, INPUT);
  delay(2000);
  MsTimer2::set(300, send2front);
  MsTimer2::start();
}

void loop() {
  uint8_t reed_status = !digitalRead(REEDSWITCH);
  
  if(reed_status) count++;
  else count = 0;

  if(count==10) {
      uckTime = ckTime;
      ckTime = millis();
      uint32_t cycleTime = (ckTime - uckTime);
      if(cycleTime==0 || uckTime==0) mySpeed = 0;
      else mySpeed = (((float)CIRCLE/cycleTime)*3600*100);
  }

  if(count>2000) mySpeed = 0;

  beforeSpeed=mySpeed;
  

  //Serial.println(mySpeed);
  delay(1);
}

void send2front(){
  uint8_t high = (mySpeed>>8);
  uint8_t low = mySpeed;
  uint8_t checkSum = high+low;
  if(high==0xFF || high==0xFE) high=0xFD;
  if(low==0xFF || low==0xFE) low=0xFD;
  if(checkSum==0xFF || checkSum==0xFE) checkSum=0xFD;
  Serial.write(0xFF);
  Serial.write(high);
  Serial.write(low);
  Serial.write(checkSum);
  Serial.write(0xFE);
  //Serial.println(mySpeed);
}
