import RPi.GPIO as GPIO
from time import sleep
import threading

class handtouchcheck(threading.Thread):
    time_stack = 0
    handon_R = None
    handon_L = None
    handoff_R = None
    handoff_L = None

    touchR = None
    touchL = None
    
    checkLED = False
    isStopped = False

    right_check = None
    left_check = None



    def __init__(self, handon_R, handon_L, handoff_R, handoff_L):    
        threading.Thread.__init__(self)
        self.touchR = 20
        self.touchL = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.touchR,GPIO.IN)
        GPIO.setup(self.touchL,GPIO.IN)

        self.handon_R = handon_R
        self.handon_L = handon_L
        self.handoff_R = handoff_R
        self.handoff_L = handoff_L


    def run(self):
        while True:
            sumR = 0
            sumL = 0

            for i in range(0,50):
                sumR += GPIO.input(self.touchR)
                sumL += GPIO.input(self.touchL)
                sleep(0.01)
            
            print('R:',sumR, '---L:',sumL)
            

            if self.isStopped:
                break




