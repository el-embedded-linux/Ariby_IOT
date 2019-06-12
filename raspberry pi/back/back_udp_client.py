import socket

back_udp_client_socket = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

def sendToFront(data):
    size = len(data)
    print(data)
    #stream = struct.pack(">L", size)+data
    back_udp_client_socket.sendto( data.encode('utf-8') , ('192.168.100.1',8082) )
