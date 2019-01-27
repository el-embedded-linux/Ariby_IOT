import cv2
import threading
from PyQt5.QtGui import *
import socket
import sys
import pickle
import numpy as np
import struct ## new
import zlib

class frontCamera(threading.Thread):
    isStoped = False
    cap = None #카메라
    func = None #콜백함수

    #initializer
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func

        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print('Socket created')

        self.socket.bind(('',8485))
        print('Socket bind complete')
        self.socket.listen(10)
        print('Socket now listening')

    def run(self):
        print('__front camera start__')
        conn,addr=self.socket.accept()
        data = b''
        payload_size = struct.calcsize(">L")
        while True:
            while len(data) < payload_size:
                print("Recv: {}".format(len(data)))
                data += conn.recv(4096)

            print("Done Recv: {}".format(len(data)))
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack(">L", packed_msg_size)[0]
            print("msg_size: {}".format(msg_size))
            while len(data) < msg_size:
                data += conn.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]

            frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            iamges = cv2.imdecode(frame, cv2.IMREAD_COLOR)

            iamges = cv2.cvtColor(iamges, cv2.COLOR_BGR2RGB) #convert BGR to RGB
            image = cv2.resize(iamges, dsize=(800, 480), interpolation=cv2.INTER_AREA) #frame resize
            image = QImage(image, image.shape[1], image.shape[0], image.shape[1] * 3,QImage.Format_RGB888) #create QIamge
            pix = QPixmap(image) #create QPixmap
            self.func(pix) #call func

            if self.isStoped: #flag check
                break

        self.isStoped = False
        print('__front camera stop__')

    def stop(self):
        self.isStoped = True
