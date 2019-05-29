import RPi.GPIO as GPIO
import time
import threading

class BreakCheck(threading.Thread):
	left_break = None ## 왼쪽 브레이크
	right_break = None ## 오른쪽 브레이크
	isStopped = False ## 브레이크체크 끝내기
	
	time_Stack = 0
	
	
	def __init__(self, left_b, right_b) :
		threading.Thread.__init__(self)
		self.left_break = 23
		self.right_break = 24
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.left_break, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(self.right_break, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
		
		self.left_b = left_b
		self.right_b = right_b
	
	def run(self):
		while True :
			#print(self.time_Stack)
			#print(GPIO.input(self.left_break), "    |    ", GPIO.input(self.right_break))
			if (self.time_Stack > 2) :
				if GPIO.input(self.left_break) == False or GPIO.input(self.right_break) == False :
					print ("Break!!")
					self.time_Stack = 0
				
			
			time.sleep(0.1)
			self.time_Stack += 1
			
			if self.isStopped:
				break
				
				
def left_b():
	pass
	
def right_b():
	pass
	
BreakCheck = BreakCheck(left_b, right_b)
BreakCheck.start()
	
