import time
import threading
import random
import re, time
import pexpect
from config import *


class BLEDevice:
    def __init__(self, addr=None):
        self.services = {}
        self.characteristics = {}
        if addr is not None:
            self.connect(addr)
            self.getcharacteristics()

    def connect(self, addr):
        print("connecting...{"+addr+"}")
        # Run gatttool interactively.
        self.gatt = pexpect.spawn("gatttool -b " + addr + " -I")
        self.gatt.expect('\[LE\]>', timeout=10)
        self.gatt.sendline('connect')
        self.gatt.expect('Connection successful.*\[LE\]>', timeout=5)
        print("Successfully connected!")

    def getservices(self):
        pass

    def getcharacteristics(self):
        self.gatt.sendline('characteristics')
        time.sleep(0.2)
        ch_pat='handle: (\S+), char properties: (\S+), char value handle: (\S+), uuid: (\S+)'
        #self.gatt.expect('\[LE\]>')
        while True:
            try:
                self.gatt.expect(ch_pat, timeout=2)
                ch_tuple = self.gatt.match.groups()
                uuid = ch_tuple[3][4:8]
                self.characteristics[uuid]=ch_tuple
                #print ch_tuple
            except pexpect.TIMEOUT:
                break
        print("got all characteristics.")

    def gethandle(self, uuid):
        ch = self.characteristics[uuid]
        return int(ch[0],16)

    def getvaluehandle(self, uuid):
        ch = self.characteristics[uuid]
        return int(ch[2],16)

    def writecmd(self, handle, value):
        cmd = "char-write-cmd 0x%04x %s" % (handle, value)
        #cmd = "char-write-cmd 0x%02x %s" % (handle, value.encode('hex'))
        self.gatt.sendline(cmd)

    def notify(self):
        while True:
            try:
                num = self.gatt.expect('Notification handle = .*? \r', timeout=4)
            except pexpect.TIMEOUT:
                break
            if num == 0:
                hxstr = self.gatt.after.split()[3:]
                handle = int(float.fromhex('0x0025'))
                #print "Received: ", hxstr[2:]
                return "".join(chr(int(x,16)) for x in hxstr[2:])
        return None


class SpeedMeter():
    isStoped = True
    callback = None
    address = "address"
    isConnected = False

    #initializer
    def __init__(self):
        self.address =config.get("BLE_ADDR")
        self.start()

    #BLE디바이스 주소를 재설정하고 쓰레드를 다시 시작한다
    def setAddress(self, address):
        self.address =config.set("BLE_ADDR",address)
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
                    vh=hm10.getvaluehandle(b'dfb1')
                    self.isConnected = True
                except:
                    self.isConnected = False

                if self.isStoped:
                    self.isConnected = False
                    break

            #데이터 수신 실패하면 연결부터 다시
            try:
                data = hm10.notify()

            except:
                self.isConnected = False
                hm10 = None
            print(data)
            if data != None and self.callback != None:
                self.callback(data)
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
