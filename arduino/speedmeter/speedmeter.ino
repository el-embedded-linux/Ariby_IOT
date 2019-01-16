//TODO 블루투스 페어링, 타이어 크기별 속도 계산

#define CIRCLE 1.946
#define READSWITCH 5 //리드스위치 포트

float mySpeed = 0;

void setup() {
  Serial.begin(9600);
  pinMode(READSWITCH, INPUT);
}

void loop() {
  if(mySpeed == 0)
    noise_clear();
  while(!digitalRead(READSWITCH));
  uint32_t uckTime = millis();
  while(digitalRead(READSWITCH)){
    if((millis() - uckTime) > 2000) break;
  }
  uint32_t ckTime = millis();
  uint32_t cycleTime = (ckTime - uckTime);
  if(cycleTime>2000) mySpeed = 0;
  else mySpeed = (CIRCLE / cycleTime) * 3600;
  Serial.println(mySpeed);
}

void noise_clear(){
  while(!digitalRead(READSWITCH));
  while(digitalRead(READSWITCH));
}
