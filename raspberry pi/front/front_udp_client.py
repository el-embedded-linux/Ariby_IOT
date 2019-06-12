import socket

front_udp_client_socket = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

def sendToBack(data):
    size = len(data)
    print(data)
    #stream = struct.pack(">L", size)+data
<<<<<<< HEAD
    front_udp_client_socket.sendto( data.encode('utf-8') , ('192.168.100.2',8081) )
=======
    front_udp_client_socket.sendto( data.encode('utf-8') , ('223.194.169.182',8081) )
>>>>>>> 8b2043927710181e4a8a383241b61ee11f5b54b7
