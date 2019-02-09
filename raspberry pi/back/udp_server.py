import socket
import struct
import cv2
import pickle

sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
sock.bind( ('127.0.0.1',8080) )
count = 0

while True:
    data , addr = sock.recvfrom(65535)

    frame=pickle.loads(data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow('ImageWindow',frame)

    if cv2.waitKey(1) == 27:
        break  # esc to quit
    print(count)
    count=count+1