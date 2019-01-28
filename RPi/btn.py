import RPi.GPIO as GPIO
from time import sleep

LED = 12
Btn = 6
cnt = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Btn, GPIO.IN)

try:
	while True:
		if GPIO.input(Btn) == 0:
			cnt += 1
			if cnt % 2 == 0:
				GPIO.output(LED, True)
			else:
				GPIO.output(LED, False)
				cnt = 1
		else:
			sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
