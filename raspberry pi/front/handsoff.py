import RPi.GPIO as GPIO
from time import sleep
import threading

class handtouchcheck(threading.Thread):
    time_stack = 0
    overtime = 5
    handon = None
    handoff = None

    
    ledPin = None

    touchR = None
    touchL = None
    
    checkLED = False
    isStopped = False




    def __init__(self, handon, handoff):    
        threading.Thread.__init__(self)
        self.touchR = 23
        self.touchL = 21
        self.ledPin = 27
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.touchR,GPIO.IN)
        GPIO.setup(self.touchL,GPIO.IN)
        GPIO.setup(self.ledPin,GPIO.OUT)
        GPIO.output(self.ledPin, False)

        self.handon = handon
        self.handoff = handoff


    def run(self):
        while True:
            sumR = 0
            sumL = 0

            for i in range(0,50):
                sumR += GPIO.input(self.touchR)
                sumL += GPIO.input(self.touchL)
                sleep(0.01)
            
            print('L:',sumL, '---R:',sumR)
        
            if sumR < 20 and sumL < 20 :
               self.time_stack = self.time_stack + 1

            else :
                GPIO.output(self.ledPin, False)

                if self.checkLED == True :
                    self.handoff()
                    self.checkLED = False

                self.time_stack = 0
            
            ########


            if self.time_stack >= self.overtime :
                GPIO.output(self.ledPin, True)
                self.checkLED = True
                self.handon() 



            if self.isStopped:
                break
        



