import RPi.GPIO as GPIO
import threading
from time import sleep

def callback():
    print('callback')

class blinking(threading.Thread):
    LED_Left = None
    LED_Rigt = None
    btn_Left = None
    btn_Rigt = None
    
    def blink_Left(self, LED):
        self.func()
        GPIO.output(self.LED_Left, True)
        sleep(0.5)
        GPIO.output(self.LED_Left, False)
        sleep(0.5)

    def blink_Rigt(self, LED):
        self.func()
        GPIO.output(self.LED_Rigt, True)
        sleep(0.5)
        GPIO.output(self.LED_Rigt, False)
        sleep(0.5)

    def flashOut(self):
        GPIO.output(self.LED_Left, False)
        GPIO.output(self.LED_Rigt, False)

    def __init__(self, func):
        
        threading.Thread.__init__(self)
        self.func = func
        self.LED_Left = 27
        self.LED_Rigt = 22
        self.btn_Left = 21
        self.btn_Rigt = 20

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.LED_Left, GPIO.OUT)
        GPIO.setup(self.LED_Rigt, GPIO.OUT)

        GPIO.setup(self.btn_Left, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self.btn_Rigt, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        self.flashOut()
    
    def run(self):
        GPIO.add_event_detect(self.btn_Left, GPIO.RISING, callback = self.blink_Left, bouncetime = 500)
        GPIO.add_event_detect(self.btn_Rigt, GPIO.RISING, callback = self.blink_Rigt, bouncetime = 500)
