import socket

front_udp_client_socket = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

def sendToBack(data):
    size = len(data)
    print(data)
    #stream = struct.pack(">L", size)+data
    front_udp_client_socket.sendto( data.encode('utf-8') , ('223.194.169.182',8081) )
