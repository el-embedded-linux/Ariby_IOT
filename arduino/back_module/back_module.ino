#include <MsTimer2.h>

// ---- PACKET INFO ---- //
#define START_PCK 0xFF
#define END_PCK 0xFE

// ---- PIN ---- //
#define RIGHT_LED A0
#define LEFT_LED A1
#define BREAK_LED A2

/***************************************/


uint8_t packet[] = {START_PCK, 0x00, 0x00, 0x00, 0x00, END_PCK};
uint8_t now_packet = 0;
uint8_t rx_count = 0;
uint8_t break_on=0, right_on=0, left_on=0;
uint8_t tmp_break_on=0, tmp_right_on=0, tmp_left_on=0;
volatile uint8_t led_status = 0;

void packet_read(){
  if(Serial.available()){
    now_packet = Serial.read();
    if(now_packet == START_PCK) rx_count = 1;
    else if(now_packet == END_PCK) rx_count = 0;
    else{
      switch(rx_count){
        case 2: //break
          tmp_break_on = now_packet;
          break;
        case 3: //right
          tmp_right_on = now_packet;
          break;
        case 4: //left
          tmp_left_on = now_packet;
          break;
        case 5:
          if(tmp_break_on + tmp_right_on + tmp_left_on == now_packet){
            break_on = tmp_break_on;
            digitalWrite(BREAK_LED,break_on);
            right_on = tmp_right_on;
            left_on = tmp_left_on;
            blink_start();
          }
         break; //checkSum
      }
    }

    if(rx_count>0) rx_count++;
  }
}

void packet_write(){
  for(int i=0; i<6; i++){
    Serial.write(packet[i]);
  }
}

void light_set(){

}

void blinking(){
  if(left_on==1 && right_on==0){
    digitalWrite(RIGHT_LED,HIGH);
    digitalWrite(LEFT_LED,led_status);
    led_status = !led_status;
  }
  else if(left_on==0 && right_on==1){
    digitalWrite(RIGHT_LED,led_status);
    digitalWrite(LEFT_LED,HIGH);
    led_status = !led_status;
  }
  else if(left_on==1 && right_on==1){
    digitalWrite(RIGHT_LED,led_status);
    digitalWrite(LEFT_LED,led_status);
    led_status = !led_status;
  }
  else{
    digitalWrite(RIGHT_LED,HIGH);
    digitalWrite(LEFT_LED,HIGH);
  }
}

void blink_start(){
  MsTimer2::stop();
  led_status = 0;

  Serial.write(led_status);
  digitalWrite(RIGHT_LED,HIGH);
  digitalWrite(LEFT_LED,HIGH);
  MsTimer2::start();
}

void setup(){
  Serial.begin(115200);
  MsTimer2::set(300, blinking);
  pinMode(BREAK_LED,OUTPUT);
  pinMode(RIGHT_LED,OUTPUT);
  pinMode(LEFT_LED,OUTPUT);
  digitalWrite(BREAK_LED,LOW);
  digitalWrite(RIGHT_LED,HIGH);
  digitalWrite(LEFT_LED,HIGH);
  delay(2000);
  digitalWrite(BREAK_LED,HIGH);
  digitalWrite(RIGHT_LED,LOW);
  digitalWrite(LEFT_LED,LOW);
  delay(300);
  digitalWrite(RIGHT_LED,HIGH);
  digitalWrite(LEFT_LED,HIGH);
  delay(300);
  digitalWrite(RIGHT_LED,LOW);
  digitalWrite(LEFT_LED,LOW);
  delay(300);
  digitalWrite(RIGHT_LED,HIGH);
  digitalWrite(LEFT_LED,HIGH);
  delay(300);
  digitalWrite(RIGHT_LED,LOW);
  digitalWrite(LEFT_LED,LOW);
  delay(300);
  digitalWrite(RIGHT_LED,HIGH);
  digitalWrite(LEFT_LED,HIGH);
  Serial.println("START");
}

void loop(){
  packet_read();
  //packet_write();
}
