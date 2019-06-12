import RPi.GPIO as GPIO
import threading
import time

class TurnSignal():
    isStoped = True
    btn_Left = 21
    btn_Right = 20
    btn_Emer = 5
    direction = None
    push_state = None

    def __init__(self, left_func, middle_func, right_func, emer_func):
        threading.Thread.__init__(self)
        self.emer_func = emer_func
        self.left_func = left_func
        self.right_func = right_func
        self.middle_func = middle_func
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.btn_Left, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self.btn_Right, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self.btn_Emer, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    #thread start
    def start(self):
        if self.isStoped:
            t = threading.Thread(target=self.run, args=())
            t.start()
        else:
            print("blink 쓰레드는 한개만 생성 할 수 있습니다.")

    def run(self):
        self.isStoped = False
        while True:
            time.sleep(0.1)
            if GPIO.input(self.btn_Emer):
                if self.direction != "Emer":
                    self.direction = "Emer"
                    self.emer_func()
            else:
                if GPIO.input(self.btn_Left):
                    if self.direction != "Left":
                        self.direction = "Left"
                        self.left_func()
                elif GPIO.input(self.btn_Right):
                    if self.direction != "Right":
                       self.direction = "Right"
                       self.right_func()
                else:
                    if self.direction != None:
                       self.direction = None
                       self.middle_func()


            if self.isStoped: #flag check
                break

    def stop(self):
        self.isStoped = True


###HOW TO USE###
def blink_emer():
    print('!! 비상 !!')
    
    GPIO.setup(TurnSignal.btn_Left, GPIO.IN)
    GPIO.setup(TurnSignal.btn_Right, GPIO.IN)
    GPIO.setup(TurnSignal.btn_Left, GPIO.OUT)
    GPIO.setup(TurnSignal.btn_Right, GPIO.OUT)
   
    if TurnSignal.push_state != "push" :
        TurnSignal.push_state = "push"
        while True :
            GPIO.output(TurnSignal.btn_Left, GPIO.HIGH)
            GPIO.output(TurnSignal.btn_Right, GPIO.HIGH)

            time.sleep(0.3)
            if GPIO.input(TurnSignal.btn_Emer) == 1 :
                GPIO.output(TurnSignal.btn_Left, GPIO.LOW)
                GPIO.output(TurnSignal.btn_Right, GPIO.LOW)
                TurnSignal.push_state = "nope"
                break

def blink_left():
    print('왼쪽 <---')
    
    GPIO.setup(TurnSignal.btn_Left, GPIO.IN)
    GPIO.setup(TurnSignal.btn_Right, GPIO.IN)
    GPIO.setup(TurnSignal.btn_Left, GPIO.OUT)
    GPIO.setup(TurnSignal.btn_Right, GPIO.OUT)

    GPIO.output(TurnSignal.btn_Left, GPIO.LOW)
    GPIO.output(TurnSignal.btn_Right, GPIO.LOW)

    while TurnSignal.btn_Left == 1 :
        GPIO.output(TurnSignal.btn_Left, GPIO.HIGH)

def blink_middle():
    print('--- 중간 ---')
    
#    GPIO.setup(TurnSignal.btn_Left, GPIO.IN)
#   GPIO.setup(TurnSignal.btn_Right, GPIO.IN)
#   GPIO.setup(TurnSignal.btn_Left, GPIO.OUT)
#   GPIO.setup(TurnSignal.btn_Right, GPIO.OUT)

#   GPIO.output(TurnSignal.btn_Left, GPIO.LOW)
#   GPIO.output(TurnSignal.btn_Right, GPIO.LOW)

def blink_right():
    print('---> 오른쪽')
    
    GPIO.setup(TurnSignal.btn_Left, GPIO.IN)
    GPIO.setup(TurnSignal.btn_Right, GPIO.IN)
    GPIO.setup(TurnSignal.btn_Left, GPIO.OUT)
    GPIO.setup(TurnSignal.btn_Right, GPIO.OUT)

    GPIO.output(TurnSignal.btn_Left, GPIO.LOW)
    GPIO.output(TurnSignal.btn_Right, GPIO.LOW)

    while TurnSignal.btn_Right == 1 :
        GPIO.output(TurnSignal.btn_Right, GPIO.HIGH)

turn = TurnSignal(blink_left, blink_middle, blink_right, blink_emer)
turn.start()
