import RPi.GPIO as GPIO
import threading

class blinking():
    isStoped = True
    btn_Left = 21
    btn_Right = 20
    direction = None

    def __init__(self, left_func, middle_func, right_func):
        threading.Thread.__init__(self)
        self.left_func = left_func
        self.right_func = right_func
        self.middle_func = middle_func
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.btn_Left, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self.btn_Right, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

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
def blink_left():
    print('왼쪽 <---')
def blink_middle():
    print('--- 중간 ---')
def blink_right():
    print('---> 오른쪽')

b = blinking(blink_left, blink_middle, blink_right)
b.start()
while True:
    pass
