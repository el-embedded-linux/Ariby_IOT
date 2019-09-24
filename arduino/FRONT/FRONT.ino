#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3);

#define BLINK_INTERVAL 300

// ---- PACKET INFO ---- //
#define START_PCK 0xFF
#define END_PCK 0xFE

#define PIN_LEFT_LED A0
#define PIN_RIGHT_LED A1
#define PIN_ROCKER_SWITCH_RIGHT 8
#define PIN_ROCKER_SWITCH_LEFT 11
#define PIN_PUSH_BUTTON_RIGHT 9
#define PIN_PUSH_BUTTON_LEFT 10
#define PIN_BREAK_SWITCH 12

uint8_t break_status = 0;
uint8_t rocker_switch_right = 0;
uint8_t rocker_switch_left = 0;
uint8_t push_button_right = 0;
uint8_t push_button_left = 0;

uint8_t rx_count = 0;
uint8_t speedHigh = 0;
uint8_t speedLow = 0;
uint8_t speedCheckSum = 0;
uint16_t mySpeed = 0;

void back_packet_write(){
  if(rx_count==0){
      uint8_t back_packet[] = {START_PCK, break_status, rocker_switch_left, rocker_switch_right, 0x00, END_PCK};
      back_packet[4] = back_packet[1]+back_packet[2]+back_packet[3];
      for(int i=0; i<6; i++){
        mySerial.write(back_packet[i]);
      }
  }

}

void packet_read(){
  uint8_t now_packet = 0;
  if(mySerial.available()){
    now_packet = mySerial.read();
    //Serial.println(now_packet,HEX);
    if(now_packet == START_PCK) rx_count = 1;
    else{
      switch(rx_count){
        case 2:
          speedHigh = now_packet;
          break;
        case 3:
          speedLow = now_packet;
          break;
        case 4:
          speedCheckSum = now_packet;
          break;
        case 5:
          if(now_packet==0xFE){
            if(speedCheckSum == speedHigh+speedLow){
              uint16_t tmpMySpeed = ((uint16_t)speedHigh<<8) + (uint16_t)speedLow;
              if(tmpMySpeed<4000) mySpeed = tmpMySpeed;
              rx_count=0;
            }
          }
          break;
        default: break;
      }
    }

    if(rx_count>0) rx_count++;
  }
}

void get_switch(){
  break_status = digitalRead(PIN_BREAK_SWITCH);
  rocker_switch_left = !digitalRead(PIN_ROCKER_SWITCH_LEFT);
  rocker_switch_right = !digitalRead(PIN_ROCKER_SWITCH_RIGHT);
  push_button_left = !digitalRead(PIN_PUSH_BUTTON_LEFT);
  push_button_right = !digitalRead(PIN_PUSH_BUTTON_RIGHT);
  //Serial.print(break_status);
  //Serial.print(rocker_switch_left);
  //Serial.print(rocker_switch_right);
  //Serial.print(push_button_left);
  //Serial.println(push_button_right);
}

void setup() {
  pinMode(PIN_LEFT_LED,OUTPUT);
  pinMode(PIN_RIGHT_LED,OUTPUT);
  
  pinMode(PIN_ROCKER_SWITCH_RIGHT,INPUT_PULLUP);
  pinMode(PIN_ROCKER_SWITCH_LEFT,INPUT_PULLUP);
  pinMode(PIN_PUSH_BUTTON_RIGHT,INPUT_PULLUP);
  pinMode(PIN_PUSH_BUTTON_LEFT,INPUT_PULLUP);
  pinMode(PIN_BREAK_SWITCH,INPUT_PULLUP);
  
  mySerial.begin(115200);
  Serial.begin(115200);
  
  digitalWrite(PIN_LEFT_LED,LOW);
  digitalWrite(PIN_RIGHT_LED,LOW);
  delay(300);
  digitalWrite(PIN_LEFT_LED,HIGH);
  digitalWrite(PIN_RIGHT_LED,HIGH);
  delay(300);
  digitalWrite(PIN_LEFT_LED,LOW);
  digitalWrite(PIN_RIGHT_LED,LOW);
  delay(300);
  digitalWrite(PIN_LEFT_LED,HIGH);
  digitalWrite(PIN_RIGHT_LED,HIGH);
}

void(*resetFunc) (void)=0;

void loop() {
  get_switch();
  packet_read();
  back_packet_write();
  //mySerial.write('A');
  Serial.print((float)mySpeed/100);
  Serial.print(",");
  uint16_t registerValue = analogRead(A7);
  registerValue = registerValue-130;
  registerValue = map(registerValue, 0, 1024, 0, 300);
  Serial.print(registerValue);
  Serial.print(",");
  Serial.println(push_button_left);
  delay(10);
}
