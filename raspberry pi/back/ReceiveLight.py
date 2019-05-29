import RPi.GPIO as GPIO
import threading
import time

class ReceiveLight():
    light = 25
    led = 21
    cnt = 0
    isStoped = True
    state = None

    def __init__(self, rc_time):
        GPIO.setwarnings(False)
        threading.Thread.__init__(self)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led, GPIO.OUT)

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

        if ReceiveLight.cnt >= 150: 
            shade_on()
            if ReceiveLight.state != 'night':
                ReceiveLight.state = 'night'
                isNight()
        else:
            shade_off()
            if ReceiveLight.state != 'day':
                ReceiveLight.state = 'day'
                isDay()

    return ReceiveLight.cnt

#shade
def shade_on():
    GPIO.output(ReceiveLight.led, GPIO.HIGH)
def shade_off():
    GPIO.output(ReceiveLight.led, GPIO.LOW)

#낮밤 구별
def isDay():
    print("낮입니다.")
def isNight():
    print("밤입니다.")

lg = ReceiveLight(rc_time)
lg.start()
