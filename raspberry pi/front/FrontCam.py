import threading
from picamera import PiCamera

class FrontCam():
    isStoped = False

    #initializer
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (1280, 720)
        self.camera.framerate = 24

    #thread start
    def start(self):
        t = threading.Thread(target=self.run, args=())
        t.start()

    def run(self):
        #TODO 파일명 날짜-시간으로 변경

        self.camera.start_recording('/home/pi/video.h264')
        self.isStoped = False
        print("start front camera recording")

        while True:
            if self.isStoped: #flag check
                break

        self.camera.stop_recording()
        print("stop front camera recording")
        #TODO 완료된 파일 확장자 변경

    def stop(self):
        self.isStoped = True
