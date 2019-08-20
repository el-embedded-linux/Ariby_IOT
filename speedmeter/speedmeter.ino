#include <MsTimer2.h>
#define CIRCLE 1.946
#define REEDSWITCH 2 //리드스위치 포트

float mySpeed = 0;
float beforeSpeed = 1;
uint32_t uckTime = 0;
uint32_t ckTime = 0;
uint32_t count = 0;

void setup() {
  Serial.begin(115200);
  pinMode(REEDSWITCH, INPUT);
}

void loop() {
  uint8_t reed_status = digitalRead(REEDSWITCH);
  
  if(reed_status) count++;
  else count = 0;

  if(count==10) {
    
      uckTime = ckTime;
      ckTime = millis();
      uint32_t cycleTime = (ckTime - uckTime);
      if(cycleTime==0 || uckTime==0) mySpeed = 0;
      else mySpeed = (CIRCLE/cycleTime) * 3600;
  }

  if(count>200000) mySpeed = 0;

  if(mySpeed!=beforeSpeed){
    beforeSpeed=mySpeed;
    Serial.print(mySpeed,2);  
  }
  if(beforeSpeed==0&&count%20000==0&&count!=0){
    Serial.print("0.00");
  }
}
