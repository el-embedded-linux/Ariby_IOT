import RPi.GPIO as GPIO
import time
import threading


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(21, GPIO.IN)
GPIO.output(23, False)


time_stack = int (0)

try :

    while True : 

        if time_stack < 3 :
            if GPIO.input(21) :
                print("5V")
                GPIO.output(23, False)
                time_stack = 0
                time.sleep(1)

            else :
                print("0V")
                time_stack = time_stack + 1
                time.sleep(1)

        


        elif time_stack >= 3 :
            GPIO.output(23, True)
            time_stack = time_stack - 1


    time.sleep(1)

    
except KeyboardInterrupt : 
    GPIO.cleanup()

