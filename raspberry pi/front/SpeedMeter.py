#!/usr/bin/env python
import sys, time
from bledevice import scanble, BLEDevice
import threading

def speedmeter(address,func):
    hm10 = BLEDevice(address)
    while True:
        vh=hm10.getvaluehandle(b'dfb1')
        data = hm10.notify()
        if data is not None:
            func(data)
        time.sleep(1)

def speedmeterStart(address,func):
    t = threading.Thread(target=speedmeter, args=(address, func))
    t.start()
