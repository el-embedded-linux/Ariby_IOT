import RPi.GPIO as GPIO
import threading
import time

class BackLedCntroller():

    #LED 포트 번호
    LED_LEFT = 21
    LED_RIGHT = 20
    LED_BREAK = 16

    #LED 상태 변수
    led_left_on = False
    led_right_on = False
    led_emergency_on = False
    led_night_on = False
    led_break_on = False

    #깜빡임 간격
    BLINKTIME = 0.5

    def __init__(self):
        threading.Thread.__init__(self)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_LEFT, GPIO.OUT)
        GPIO.setup(self.LED_RIGHT, GPIO.OUT)
        GPIO.setup(self.LED_BREAK, GPIO.OUT)

    #브레이크 제어
    def break_on(self):
        led_break_on = True
        GPIO.output(self.LED_BREAK, GPIO.HIGH)

    def break_off(self):
        led_break_on = False
        GPIO.output(self.LED_BREAK, GPIO.LOW)

    #브레이크 제어
    def break_night_on(self):
        self.turn_off(self.LED_LEFT)
        t = threading.Thread(target=self.break_night_thread, args=())
        t.start()

    def break_night_off(self):
        led_night_on = False



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


    #비상등 제어
    def emergency_on(self):
        self.turn_off(self.LED_LEFT)
        self.turn_off(self.LED_RIGHT)
        t = threading.Thread(target=self.emergency_on_thread, args=())
        t.start()

    def emergency_off(self):
        self.led_emergency_on = False

    def emergency_on_thread(self):
        self.led_emergency_on = True
        while True:
            GPIO.output(self.LED_RIGHT, GPIO.HIGH)
            GPIO.output(self.LED_LEFT, GPIO.HIGH)
            time.sleep(self.BLINKTIME)
            GPIO.output(self.LED_RIGHT, GPIO.LOW)
            GPIO.output(self.LED_LEFT, GPIO.LOW)
            time.sleep(self.BLINKTIME)

            if self.led_emergency_on == False:
                GPIO.output(self.LED_RIGHT, GPIO.LOW)
                GPIO.output(self.LED_LEFT, GPIO.LOW)
                break

    def break_night_thread(self):
        self.led_night_on = True
        while True:
            GPIO.output(self.LED_BREAK, GPIO.LOW)
            time.sleep(0.05)
            GPIO.output(self.LED_BREAK, GPIO.HIGH)
            time.sleep(0.05)
            while led_break_on == True:
                pass
            if led_night_on == False:
                break


backLedCntroller = BackLedCntroller()

if __name__ == "__main__"
    while True:
        text = input()
        if text == "ron":
            backLedCntroller.turn_on(backLedCntroller.LED_RIGHT)
        if text == "lon":
            backLedCntroller.turn_on(backLedCntroller.LED_LEFT)
        if text == "roff":
            backLedCntroller.turn_off(backLedCntroller.LED_RIGHT)
        if text == "loff":
            backLedCntroller.turn_off(backLedCntroller.LED_LEFT)
        if text == "breakon":
            backLedCntroller.break_on()
        if text == "breakoff":
            backLedCntroller.break_off()
        if text == "emeron":
            backLedCntroller.emergency_on()
        if text == "emeroff":
            backLedCntroller.emergency_off()
