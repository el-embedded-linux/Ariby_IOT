#handsoff.py
import RPi.GPIO as GPIO
from time import sleep
import threading

class handsoff(threading.Thread):
    isStoped = False
    handle = None #핸들 포트번호
    handon = None #콜백함수
    handoff = None
    alarmTimer = 0
    ALARMMAX = 10 #알람이 울리는 시간
    isAlarm = False #현재 알람이 울리고 있는지 flag변수

    #initializer
    def __init__(self, handon, handoff):
        threading.Thread.__init__(self)
        self.handle = 21 #RIGHT
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.handle,GPIO.IN)
        self.handon = handon
        self.handoff = handoff

    def run(self):
        while True:
            sum = 0
            for i in range(0,50):
                sum += GPIO.input(self.handle)
                sleep(0.01)
            print(sum)
            if sum>20: #touch
                self.alarmTimer = 0
                if self.isAlarm == True:
                    self.isAlarm = False
                    self.handoff()
            else:
                pass #no touch
                self.alarmTimer += 1

            if (self.alarmTimer > self.ALARMMAX) and self.isAlarm==False:
                self.handon()
                self.isAlarm = True

            if self.isStoped:
                break

    def stop(self):
        self.isStoped = True
