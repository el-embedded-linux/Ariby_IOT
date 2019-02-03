import RPi.GPIO as GPIO
import threading
from time import sleep

def blink(led):
    GPIO.output(led, True)
    sleep(0.5)
    GPIO.output(led, False)
    sleep(0.5)

def my_callback1(btn):
    t1 = threading.Thread(target=blink, args=(LED_Left,))
    t1.start()

def my_callback2(btn):
    t2 = threading.Thread(target=blink, args=(LED_Rigt,))
    t2.start()

GPIO.setwarnings(False)

LED_Left = 27
LED_Rigt = 22
btn_Left = 23
btn_Rigt = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_Left, GPIO.OUT)
GPIO.setup(LED_Rigt, GPIO.OUT)

GPIO.setup(btn_Left, GPIO.IN)
GPIO.setup(btn_Rigt, GPIO.IN)

GPIO.add_event_detect(btn_Left, GPIO.RISING, callback = my_callback1, bouncetime = 500)
GPIO.add_event_detect(btn_Rigt, GPIO.RISING, callback = my_callback2, bouncetime = 500)

GPIO.output(LED_Left, False)
GPIO.output(LED_Rigt, False)

try:
    while True:
        pass

except KeyboardInterrupt:
	GPIO.cleanup()
