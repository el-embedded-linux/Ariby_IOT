#!/usr/bin/env python
import sys, time
from bledevice import scanble, BLEDevice
import threading
import random

class SpeedMeter():
    isStoped = True
    callback = None
    address = "address"
    #initializer
    def __init__(self):
        try :
            f = open("bledevice.cfg","r")
            self.address = f.read()
            f.close()
        except:
            pass

    def setAddress(self, address):
        try :
            f = open("bledevice.cfg","w")
            f.write(address)
            f.close()
            self.address = address
        except:
            pass

    #thread start
    def start(self):
        if self.isStoped:
            t = threading.Thread(target=self.run, args=())
            t.start()
        else:
            print("SpeedMeter 쓰레드는 한개만 생성 할 수 있습니다.")

    def run(self):
        hm10 = None
        while hm10 == None:
            try:
                hm10 = BLEDevice(self.address)
            except:
                pass

        while True:
            vh=hm10.getvaluehandle(b'dfb1')
            data = hm10.notify()
            if data is not None and self.func is not None:
                self.func(data)
            time.sleep(1)

            if self.isStoped:
                break

    #BLE디바이스 없는 상태에서 테스트를 진행하기위해 랜덤한 스피드값을 출력하는 쓰레드입니다.
    def start_b(self):
        if self.isStoped:
            t = threading.Thread(target=self.run_b, args=())
            t.start()
        else:
            print("SpeedMeter 쓰레드는 한개만 생성 할 수 있습니다.")

    def run_b(self):
        self.isStoped = False
        while True:
            speed = random.randrange(0,30)
            self.func(str(speed))
            time.sleep(random.randrange(1,2))

            if self.isStoped:
                break

    def stop(self):
        self.isStoped = True

speedmeter = SpeedMeter()
speedmeter.start()

speedmeter.setAddress("noooooo")
