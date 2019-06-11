import RPi.GPIO as GPIO
import threading
import time
from BackLedCntroller import *

class ReceiveLight():
    light = 4
    cnt = 0
    isStoped = True
    state = None

    def __init__(self, rc_time):
        GPIO.setwarnings(False)
        threading.Thread.__init__(self)
        GPIO.setmode(GPIO.BCM)

    #thread start
    def start(self):
        if self.isStoped:
            t = threading.Thread(target = self.run, args = ())
            t.start()
        else:
            print("Create one light Thread")

    def run(self):
        self.isStoped = False
        while True:
            time.sleep(0.1)
            rc_time()

#use sensor
def rc_time():
    ReceiveLight.cnt = 0
    GPIO.setup(ReceiveLight.light, GPIO.OUT)
    GPIO.output(ReceiveLight.light, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(ReceiveLight.light, GPIO.IN)

    while(GPIO.input(ReceiveLight.light) == GPIO.LOW):
        ReceiveLight.cnt += 1

        if ReceiveLight.cnt >= 1024:
            if ReceiveLight.state != 'night':
                ReceiveLight.state = 'night'
                isNight()
        else:
            if ReceiveLight.state != 'day':
                ReceiveLight.state = 'day'
                isDay()

    return ReceiveLight.cnt


#낮밤 구별
def isDay():
    print("day.")
    backLedCntroller.break_night_off()
def isNight():
    print("night.")
    backLedCntroller.break_night_on()

lg = ReceiveLight(rc_time)
lg.start()
