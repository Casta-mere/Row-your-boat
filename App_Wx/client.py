import socket

address=("10.97.19.117",8888)
for i in range(50):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(address)
    s.send(b"Hello")

