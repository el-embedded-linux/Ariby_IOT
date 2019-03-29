import RPi.GPIO as GPIO
import time
import threading

class handcheck(threading.Thread) :
    time_stack = 0      ## 누적시간
    overtime = 3          ## 제한시간 3초
    touchHand = None       ## 터치센서 핀번호
 
    ledPinNumber = None ## LED 핀번호
    checkLED = False       ## LED on(True),off(False) 확인

    isStopped = False     ## handoff 끝내기


    def __init__(self, handon, handoff):
        threading.Thread.__init__(self)
        self.touchHand = 21           ## 터치센서 
        self.ledPinNumber = 23     ## LED 핀번호
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.touchHand, GPIO.IN)         ## 터치센서 on
        GPIO.setup(self.ledPinNumber, GPIO.OUT) ## LED 출력설정
        GPIO.output(self.ledPinNumber, GPIO.LOW)

        self.handon = handon
        self.handoff = handoff

    def run(self):
        while True:
            print(GPIO.input(self.touchHand))
            
            self.time_stack = self.time_stack + 1 ## 손을 떼었을 경우 누적시간 누적
                 
            if GPIO.input(self.touchHand) == True:                      ## 손을 다시 붙혔을 경우 누적시간 초기화
                self.time_stack = 0 
                self.checkLED = False
                GPIO.output(self.ledPinNumber, GPIO.LOW) ## 소등
                
            elif self.time_stack >= self.overtime: ## 누적시간 초 이상
                   GPIO.output(self.ledPinNumber, GPIO.HIGH) ## 점등
                   self.checkLED = True
                   self.handon()
                
        
            time.sleep(1)   
                    
            if self.isStopped:
                break

def _on():
    pass

def _off():
    pass


handtouch = handcheck(_on, _off)
handtouch.start()

