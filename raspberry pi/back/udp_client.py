import socket
import cv2
import struct
import pickle
import zlib

sock = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

def sendToFront(data):
    size = len(data)
    #print(size)
    #stream = struct.pack(">L", size)+data
    sock.sendto( data , ('192.168.100.1',8080) )
