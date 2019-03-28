import RPi.GPIO as GPIO
from time import sleep
import threading

class handtouchcheck(threading.Thread):
    time_stack = 0
    overtime = 5
    handon = None
    handoff = None

    
    ledPin = None

    touchHand = None
    
    checkLED = False
    isStopped = False


  
    def __init__(self, handon, handoff):    
        threading.Thread.__init__(self)
        self.touchHand = 21
        self.ledPin = 27
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.touchHand,GPIO.IN)
        GPIO.setup(self.ledPin,GPIO.OUT)
        GPIO.output(self.ledPin, False)

        self.handon = handon
        self.handoff = handoff

		def run(self):
			while True :
				print(GPIO.input(21))
			for i in range(0,100):
				sleep(0.01)

	        	if GPIO.OUT == True :
					self.time_stack = self.time_stack + 1

				else :
					GPIO.output(self.ledPin, False)

				if self.checkLED == True :
					self.handoff()
					self.checkLED = False
					self.time_stack = 0

				if self.time_stack >= self.overtime :
					GPIO.output(self.ledPin, True)
					self.checkLED = True
					self.handon() 

				if self.isStopped:
					break

def _on():
    #print("on")
    pass
def _off():
    #print("off")
    pass

handtouch = handtouchcheck(_on,_off)
handtouch.start()
