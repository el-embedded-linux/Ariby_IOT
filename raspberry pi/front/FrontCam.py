import threading
from picamera import PiCamera
from datetime import datetime
import time
import os
class FrontCam():
    isStoped = True
    #initializer
    def __init__(self):
        try:
            self.camera = PiCamera()
        except:
            print("[FrontCam]전방 카메라 녹화를 시작하지 못했습니다.")
            return
        self.camera.resolution = (1920, 1080)
        #self.camera.framerate = 30
        t = threading.Thread(target=self.run, args=())
        t.start()

    def run(self):
        now = datetime.now()
        filename = now.strftime('%y%m%d_%H%M%S')
        self.camera.start_recording('Movie/recording.h264')
        print("[FrontCam]전방 카메라 녹화를 시작합니다.")
        self.isStoped = False
        while True:
            if self.isStoped: #flag check
                break

        self.camera.stop_recording()
        self.camera.close()
        os.system('avconv -r 30 -i '+'Movie/recording.h264'+' -vcodec copy '+'Movie/'+filename+'.mp4')
        print("[FrontCam]전방 카메라 녹화를 종료합니다.")

    def stop(self):
        self.isStoped = True
