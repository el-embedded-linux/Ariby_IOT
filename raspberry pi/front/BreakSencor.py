import RPi.GPIO as GPIO
import time
from front_udp_client import *

class BreakCheck():
	left_break = 21 ## 왼쪽 브레이크
	right_break = 20 ## 오른쪽 브레이크
	BREAK_VCC = 16 ## 브래이크 VCC
	isStopped = False ## 브레이크체크 끝내기

	time_Stack = 0

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.BREAK_VCC, GPIO.OUT)
		GPIO.setup(self.left_break, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(self.right_break, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
		GPIO.add_event_detect(self.left_break, GPIO.BOTH, callback=self.break_run, bouncetime=20)
		GPIO.add_event_detect(self.right_break, GPIO.BOTH, callback=self.break_run, bouncetime=20)
		GPIO.output(self.BREAK_VCC, GPIO.HIGH)

	def break_run(self,pin):
		if GPIO.input(self.left_break)==False or GPIO.input(self.right_break)==False:
			sendToBack("break_on")
		elif GPIO.input(self.left_break)==True and GPIO.input(self.right_break)==True:
			sendToBack("break_off")



BreakCheck = BreakCheck()
