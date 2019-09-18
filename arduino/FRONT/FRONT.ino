#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3);

#define BLINK_INTERVAL 300

// ---- PACKET INFO ---- //
#define START_PCK 0xFF
#define END_PCK 0xFE

#define PIN_BLUNO_POWER 4
#define PIN_LEFT_LED 7
#define PIN_RIGHT_LED 8
#define PIN_ROCKER_SWITCH_RIGHT 12
#define PIN_ROCKER_SWITCH_LEFT 11
#define PIN_PUSH_BUTTON_RIGHT 10
#define PIN_PUSH_BUTTON_LEFT 9
#define PIN_BREAK_SWITCH 6
#define PIN_REGISTER A0

uint8_t break_status = 0;
uint8_t rocker_switch_right = 0;
uint8_t rocker_switch_left = 0;
uint8_t push_button_right = 0;
uint8_t push_button_left = 0;

void back_packet_write(){
  uint8_t back_packet[] = {START_PCK, break_status, rocker_switch_left, rocker_switch_right, 0x00, END_PCK};
  back_packet[4] = back_packet[1]+back_packet[2]+back_packet[3];
  for(int i=0; i<6; i++){
    mySerial.write(back_packet[i]);
  }
}

void get_switch(){
  break_status = digitalRead(PIN_BREAK_SWITCH);
  rocker_switch_left = !digitalRead(PIN_ROCKER_SWITCH_LEFT);
  rocker_switch_right = !digitalRead(PIN_ROCKER_SWITCH_RIGHT);
}

void setup() {
  pinMode(PIN_LEFT_LED,OUTPUT);
  pinMode(PIN_RIGHT_LED,OUTPUT);
  pinMode(PIN_BLUNO_POWER,OUTPUT);
  
  pinMode(PIN_ROCKER_SWITCH_RIGHT,INPUT_PULLUP);
  pinMode(PIN_ROCKER_SWITCH_LEFT,INPUT_PULLUP);
  pinMode(PIN_PUSH_BUTTON_RIGHT,INPUT_PULLUP);
  pinMode(PIN_PUSH_BUTTON_LEFT,INPUT_PULLUP);
  pinMode(PIN_BREAK_SWITCH,INPUT_PULLUP);
  
  mySerial.begin(115200);
  
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
  
  digitalWrite(PIN_BLUNO_POWER,HIGH);
}

void(*resetFunc) (void)=0;

void loop() {
  get_switch();
  back_packet_write();
}
