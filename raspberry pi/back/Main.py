from TcpClient import *
from BackLedCntroller import *

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

while True:
    pass
