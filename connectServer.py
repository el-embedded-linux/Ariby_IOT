import socket

server = socket.socket()
server.bind(('192.168.0.5', 8080))
server.listen(1)

client, addr = server.accept()
msg = client.recv(1024)

print(msg)
client.sendall(msg)
print('Data sent to the client.')
client.close()
server.close()
