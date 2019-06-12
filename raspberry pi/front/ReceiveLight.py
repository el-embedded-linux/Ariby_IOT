import RPi.GPIO as GPIO
import threading
import time

class ReceiveLight():
    light = 25
    cnt = 0

    def __init__(self, rc_time):
        GPIO.setmode(GPIO.BCM)
        time = rc_time(self.light)

    def run(self):
        while True:
            print(rc_time(self.light))

def rc_time(light):
    GPIO.setup(ReceiveLight.light, GPIO.OUT)
    GPIO.setup(ReceiveLight.light, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(ReceiveLight.light, GPIO.IN)

    while(GPIO.input(ReceiveLight.light) == GPIO.LOW):

        ReceiveLight.cnt += 1
        
    return ReceiveLight.cnt

lg = ReceiveLight(rc_time)
lg.run()

