import time
from bledevice import BLEDevice
import threading
import random

class SpeedMeter():
    isStoped = True
    callback = None
    address = "address"
    isConnected = False

    #initializer
    def __init__(self):
        try :
            f = open("bledevice.cfg","r")
            self.address = f.read()
            f.close()
        except:
            pass
        self.start()

    #BLE디바이스 주소를 재설정하고 쓰레드를 다시 시작한다
    def setAddress(self, address):
        try :
            f = open("bledevice.cfg","w")
            f.write(address)
            f.close()
            self.address = address
        except:
            pass
        self.stop()
        self.start()

    #thread start
    def start(self):
        if self.isStoped:
            t = threading.Thread(target=self.run, args=())
            t.start()
        else:
            print("SpeedMeter 쓰레드는 한개만 생성 할 수 있습니다.")

    def run(self):
        self.isStoped = False
        hm10 = None
        while True:
            #연결에 성공할때까지 반복
            while hm10 == None:
                try:
                    hm10 = BLEDevice(self.address)
                    self.isConnected = True
                except:
                    self.isConnected = False

                if self.isStoped:
                    self.isConnected = False
                    break

            #데이터 수신 실패하면 연결부터 다시
            try:
                vh=hm10.getvaluehandle(b'dfb1')
                data = hm10.notify()
                if data is not None and self.callback is not None:
                    self.callback(data)
                time.sleep(1)
            except:
                self.isConnected = False
                hm10 = None

            if self.isStoped:
                self.isConnected = False
                break

    #BLE디바이스 없는 상태에서 테스트를 진행하기위해 랜덤한 스피드값을 출력하는 쓰레드입니다.
    def start_b(self):
        self.isStoped = True
        time.sleep(1)
        t = threading.Thread(target=self.run_b, args=())
        t.start()

    def run_b(self):
        self.isStoped = False
        while True:
            speed = random.randrange(0,30)
            self.callback(str(speed))
            time.sleep(random.randrange(1,2))

            if self.isStoped:
                break

    def stop(self):
        self.isStoped = True

speedmeter = SpeedMeter()
