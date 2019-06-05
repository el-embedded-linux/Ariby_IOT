from TcpClient import *
from BackLedCntroller import *
from ReceiveLight import *

def getMessage(text):
    print(text)
    if text == "led_right_on":
        backLedCntroller.turn_on(backLedCntroller.LED_RIGHT)
    if text == "led_left_on":
        backLedCntroller.turn_on(backLedCntroller.LED_LEFT)
    if text == "led_right_off":
        backLedCntroller.turn_off(backLedCntroller.LED_RIGHT)
    if text == "led_left_off":
        backLedCntroller.turn_off(backLedCntroller.LED_LEFT)
    if text == "break_on":
        backLedCntroller.break_on()
    if text == "break_off":
        backLedCntroller.break_off()
    if text == "emergency_on":
        backLedCntroller.emergency_on()
    if text == "emergency_off":
        backLedCntroller.emergency_off()

tcpClient.setCallback(getMessage)

# TODO ReceiveLight에 아래 두 함수를 콜백으로 등록 조도센서에 따라 밤낮이 바뀔때 on/ off 함수가 실행되도록 변경
# backLedCntroller.break_night_on()
# backLedCntroller.break_night_off()

while True:
    pass
