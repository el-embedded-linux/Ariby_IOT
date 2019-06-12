import socket
import cv2
import struct
import pickle
import zlib

sock = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
img_counter = 0
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 70]

def sendToFront(frame):
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)
    #print(size)
    #stream = struct.pack(">L", size)+data
    sock.sendto( data , ('192.168.100.1',8080) )
