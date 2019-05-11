import threading
from picamera import PiCamera
from datetime import datetime
import time
import os
class FrontCam():
    isStoped = True

    #initializer
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1280, 720)
        self.camera.framerate = 24
        t = threading.Thread(target=self.run, args=())
        t.start()

    def run(self):
        now = datetime.now()
        filename = now.strftime('%y%m%d_%H%M%S')
        self.camera.start_recording('Movie/recording.h264')
        print("start front camera recording")
        self.isStoped = False
        while True:
            if self.isStoped: #flag check
                break

        self.camera.stop_recording()
        self.camera.close()
        os.system('avconv -r 25 -i '+'Movie/recording.h264'+' -vcodec copy '+'Movie/'+filename+'.mp4')
        print("stop front camera recording")

    def stop(self):
        self.isStoped = True
