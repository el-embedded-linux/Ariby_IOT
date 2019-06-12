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
    SWITCH_EMER = 27

    #LED 상태 변수
    led_left_on = False
    led_right_on = False
    led_emergency_on = False
    led_night_on = False
    led_break_on = False
    Emer_on = False;
    #깜빡임 간격
    BLINKTIME = 0.5

    dis = "off"
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_LEFT, GPIO.OUT)
        GPIO.setup(self.LED_RIGHT, GPIO.OUT)
        GPIO.setup(self.SWITCH_EMER, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.SWITCH_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.SWITCH_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.SWITCH_EMER, GPIO.RISING, callback=self.emer, bouncetime=400)
        select_led_t = threading.Thread(target=self.select_led)
        select_led_t.start()


    def emer(self, pin):
        if self.Emer_on:
            self.Emer_on = False
            sendToBack("emergency_off")
        else:
            self.Emer_on = True
            sendToBack("emergency_on")

    def select_led(self):
        while True:
            if self.Emer_on==True and self.dis != "emer":
                self.dis = "emer"
                self.emer_LED_on()
            elif GPIO.input(self.SWITCH_LEFT)==True and self.dis != "left" and self.Emer_on==False:

                self.dis = "left"
                self.turn_on(self.LED_RIGHT)
                self.turn_off(self.LED_LEFT)
                sendToBack("led_right_on")

            elif GPIO.input(self.SWITCH_RIGHT)==True and self.dis != "right" and self.Emer_on==False:

                self.dis = "right"
                self.turn_on(self.LED_LEFT)
                self.turn_off(self.LED_RIGHT)
                sendToBack("led_left_on")
            elif GPIO.input(self.SWITCH_RIGHT)==False and GPIO.input(self.SWITCH_LEFT)==False and self.dis != "off" and self.Emer_on==False:

                self.dis = "off"
                self.turn_off(self.LED_LEFT)
                self.turn_off(self.LED_RIGHT)
                sendToBack("led_left_off")
                sendToBack("led_right_off")
            time.sleep(0.1)


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


    def emer_LED_on(self):
            t = threading.Thread(target=self.emer_on_thread)
            t.start()

    def emer_on_thread(self):
        while True:
            GPIO.output(self.LED_LEFT, GPIO.HIGH)
            GPIO.output(self.LED_RIGHT, GPIO.HIGH)
            time.sleep(self.BLINKTIME)
            GPIO.output(self.LED_LEFT, GPIO.LOW)
            GPIO.output(self.LED_RIGHT, GPIO.LOW)
            time.sleep(self.BLINKTIME)
            if self.Emer_on == False:
                GPIO.output(self.LED_LEFT, GPIO.LOW)
                GPIO.output(self.LED_RIGHT, GPIO.LOW)
                break
    def turn_on_thread(self, led_gpio_port,turn):

        if led_gpio_port==self.LED_LEFT:
            self.led_left_on = True
        elif led_gpio_port==self.LED_RIGHT:
            self.led_right_on = True

        while True:
            while self.Emer_on:
                pass
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
