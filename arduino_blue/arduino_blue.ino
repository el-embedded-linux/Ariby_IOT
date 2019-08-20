#include <MsTimer2.h>
#define CIRCLE 1.946
#define REEDSWITCH 7 //리드스위치 포트
#define SWITCH 6
#define REGISTER A0

float mySpeed = 0;
uint32_t uckTime = 0;
uint32_t ckTime = 0;
uint32_t count = 0;
uint8_t switch_on = 0;

void notify(){
  Serial.print(mySpeed,2);
  Serial.print(",");
  int reg_origin = analogRead(REGISTER) - 101;
  int reg_map = map(reg_origin, 0, 1023, 0, 180);
  Serial.print(reg_map);
  Serial.print(",");
  Serial.println(digitalRead(SWITCH));
}

void setup() {
  Serial.begin(115200);
  pinMode(SWITCH, INPUT_PULLUP);
  pinMode(REEDSWITCH, INPUT);
  MsTimer2::set(50,notify);
  MsTimer2::start();
}

void loop() {
  uint8_t reed_status = digitalRead(REEDSWITCH);
  
  if(reed_status) count++;
  else count = 0;

  if(count==10) {
      uckTime = ckTime;
      ckTime = millis();
      uint32_t cycleTime = (ckTime - uckTime);
      if(cycleTime==0) mySpeed = 0;
      else mySpeed = (CIRCLE/cycleTime) * 3600;
  }

  if(count>200000) mySpeed = 0;
  
}

void noise_clear(){
}
