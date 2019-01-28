import RPi.GPIO as GPIO
from time import sleep

LED_Right = 24
LED_Left = 23

Swt_Right = 22
Swt_Left = 17
Swt_Mid = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_Right, GPIO.OUT)
GPIO.setup(LED_Left, GPIO.OUT)

GPIO.setup(Swt_Right, GPIO.IN)
GPIO.setup(Swt_Left, GPIO.IN)
GPIO.setup(Swt_Mid, GPIO.IN)

try:
	while True:
		if GPIO.input(Swt_Right) == 0:
			GPIO.output(LED_Right, True)
			GPIO.output(LED_Left, False)
		elif GPIO.input(Swt_Left) == 0:
			GPIO.output(LED_Right, False)
			GPIO.output(LED_Left, True)
		else:
			GPIO.output(LED_Right, False)
			GPIO.output(LED_Left, False)

except KeyboardInterrupt:
	GPIO.cleanup()
