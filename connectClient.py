import socket


ip = '192.168.0.5'
port = 8080

client = socket.socket()
client.connect((ip, port))

client.send(b'connected server')
msg = client.recv(1024)
print(msg)
client.close()
