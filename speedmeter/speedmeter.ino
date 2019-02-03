#include <IRremote.h>
int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
IRsend irsend;
decode_results results;

uint32_t irToLg[10][2] = {
  0xC26BF044, 0x5B0300FF, //채널 UP
  0xE0E006F9, 0x5B0300FF, //채널 UP
  0xC4FFB646, 0x5B03807F, //채널 DOWN
  0xE0E08679, 0x5B03807F, //채널 DOWN
  0xE0E046B9, 0x5B0340BF, //음량 UP
  0x53801EE8, 0x5B0340BF, //음량 UP
  0xE0E0A659, 0x5B03C03F, //음량 DOWN
  0x758C9D82, 0x5B03C03F, //음량 DOWN
  0xE0E016E9, 0x5B0310EF, //셋톱박스 전원
  0x8AF13528, 0x5B0310EF //셋톱박스 전원
  };

 void setup()
 {
   pinMode(4,OUTPUT);
   pinMode(5,OUTPUT);
   pinMode(12,OUTPUT);
   pinMode(13,OUTPUT);
   digitalWrite(13,HIGH);
   digitalWrite(12,LOW);
   digitalWrite(5,LOW);
   digitalWrite(4,LOW);
   Serial.begin(9600);
   irrecv.enableIRIn(); // Start the receiver

 }
 void loop() {
   if (irrecv.decode(&results)) {
     Serial.println(results.value, HEX);
     irrecv.resume(); // Receive the next value
     for(int i=0; i<10; i++){
      if(results.value==irToLg[i][0]){
        Serial.print("convert : ");
        Serial.println(irToLg[i][1], HEX);
        for (int a = 0; a < 1; a++) {
          irsend.sendNEC(irToLg[i][1], 32); // Sony TV power code
          Serial.print("out");
          delay(40);
        }
        irrecv.enableIRIn();
        break;
       }
     }
   }
 }
