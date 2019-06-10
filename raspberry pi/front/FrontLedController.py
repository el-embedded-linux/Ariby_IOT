import RPi.GPIO as GPIO
import threading
import time
from front_udp_client import *


class BackLedCntroller():

    #LED 포트 번호
    LED_LEFT = 25
    LED_RIGHT = 18

    SWITCH_LEFT = 23
    SWITCH_RIGHT = 24

    #LED 상태 변수
    led_left_on = False
    led_right_on = False
    led_emergency_on = False
    led_night_on = False
    led_break_on = False

    #깜빡임 간격
    BLINKTIME = 0.5

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_LEFT, GPIO.OUT)
        GPIO.setup(self.LED_RIGHT, GPIO.OUT)
        GPIO.setup(self.SWITCH_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.SWITCH_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.SWITCH_LEFT, GPIO.BOTH, callback=self.select_led, bouncetime=400)
        GPIO.add_event_detect(self.SWITCH_RIGHT, GPIO.BOTH, callback=self.select_led, bouncetime=400)


    def select_led(self, pin):
        print("************************************************")
        if GPIO.input(self.SWITCH_LEFT)==True:
            self.turn_on(self.LED_RIGHT)
            self.turn_off(self.LED_LEFT)
            sendToBack("led_right_on")
            sendToBack("led_left_off")
        elif GPIO.input(self.SWITCH_RIGHT)==True:
            self.turn_on(self.LED_LEFT)
            self.turn_off(self.LED_RIGHT)
            sendToBack("led_left_on")
            sendToBack("led_right_off")
        else:
            self.turn_off(self.LED_LEFT)
            self.turn_off(self.LED_RIGHT)
            sendToBack("led_left_off")
            sendToBack("led_right_off")


    #깜빡이 제어
    def turn_on(self, oriental):
        if oriental == self.LED_RIGHT:
            self.turn_off(self.LED_LEFT)
            t = threading.Thread(target=self.turn_on_thread, args=(self.LED_RIGHT,"right"))
            t.start()
        if oriental == self.LED_LEFT:
            self.turn_off(self.LED_RIGHT)
            t = threading.Thread(target=self.turn_on_thread, args=(self.LED_LEFT,"left"))
            t.start()

    def turn_off(self, oriental):
        if oriental == self.LED_RIGHT:
            self.led_right_on = False
        if oriental == self.LED_LEFT:
            self.led_left_on = False

    def turn_on_thread(self, led_gpio_port,turn):

        if led_gpio_port==self.LED_LEFT:
            self.led_left_on = True
        elif led_gpio_port==self.LED_RIGHT:
            self.led_right_on = True

        while True:
            GPIO.output(led_gpio_port, GPIO.HIGH)
            time.sleep(self.BLINKTIME)
            GPIO.output(led_gpio_port, GPIO.LOW)
            time.sleep(self.BLINKTIME)
            if led_gpio_port==self.LED_LEFT and self.led_left_on==False:
                GPIO.output(led_gpio_port, GPIO.LOW)
                break
            elif led_gpio_port==self.LED_RIGHT and self.led_right_on==False:
                GPIO.output(led_gpio_port, GPIO.LOW)
                break




backLedCntroller = BackLedCntroller()

if __name__ == "__main__":
    while True:
        pass
